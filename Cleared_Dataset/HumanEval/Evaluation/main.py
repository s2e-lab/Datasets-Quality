from argparse import Namespace

from tqdm import tqdm

from data import write_jsonl, read_problems
from evaluation import evaluate_functional_correctness
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

torch.cuda.empty_cache()

# Code Generation Configuration Parameters
MODEL = "Salesforce/codegen-2B-mono"
TEMPERATURE = 1e-5
TOP_P = 1
DO_SAMPLE = False
EARLY_STOPPING = True
TOTAL_OUTPUT = 1
MAX_TOKENS = 512


STOP_TOKENS = "<|endoftext|>"


def setup_model():
    tokenizer = AutoTokenizer.from_pretrained(MODEL, use_fast=False)
    model = AutoModelForCausalLM.from_pretrained(MODEL, device_map="auto")
    print(model.hf_device_map)
    tokenizer.pad_token = tokenizer.eos_token
    model.config.pad_token_id = model.config.eos_token_id
    # model = model.to(device)
    return tokenizer, model


def entry_point(
    problem_file: str,
    sample_file: str,
    k: str = "1,10",
    n_workers: int = 4,
    timeout: float = 3.0,
):
    """
    Evaluates the functional correctness of generated samples, and writes
    results to f"{sample_file}_results.jsonl.gz"
    """
    k = list(map(int, k.split(",")))
    results = evaluate_functional_correctness(
        sample_file, k, n_workers, timeout, problem_file
    )

    return results


def filter_code(completion: str) -> str:
    completion = completion.lstrip("\n")
    return completion.split("\n\n")[0]


def gen_prompt(prompt: str, model) -> str:
    if "starcoder" in model.model_path:
        prompt = "<fim_prefix>" + prompt + "<fim_suffix><fim_middle>"
    else:
        prompt = (
            "Please complete the following Python code without providing any additional tasks such as testing or explanations\n"
            + prompt
        )
    if "starchat" in model.model_path:
        prompt = f"<|system|>\n<|end|>\n<|user|>{prompt}<|end|>\n<|assistant|>"
    return prompt


def count_indent(text: str) -> int:
    count = 0
    for char in text:
        if char == " ":
            count += 1
        else:
            break
    return count


def fix_indents(text: str, multiple: int = 4):
    outputs = []
    for line in text.split("\n"):
        while count_indent(line) % multiple != 0:
            line = " " + line
        outputs.append(line)
    return "\n".join(outputs)


def test_fix_indents():
    text = "   # TODO: Implement separate_paren_groups\nreturn []"
    print(fix_indents(text))


def code_completion(
    prompt,
    tokenizer,
    model,
    temperature=1e-5,
    top_p=1,
    do_sample=False,
    early_stopping=True,
    total_output=1,
    max_tokens=512,
):
    inputs = tokenizer(prompt, return_tensors="pt")
    input_ids = inputs.input_ids.to(model.device)
    attention_mask = inputs.attention_mask.to(model.device)
    outputs = model.generate(
        input_ids=input_ids,
        attention_mask=attention_mask,
        temperature=temperature,
        top_p=top_p,
        do_sample=do_sample,
        early_stopping=early_stopping,
        num_return_sequences=total_output,
        max_length=max_tokens,
    )
    outputs = tokenizer.batch_decode(outputs, skip_special_tokens=True)
    return outputs


def evaluate(tokenizer, model, data_path: str) -> dict:
    dataset = read_problems(data_path)
    n_sample = 100
    best_temperature = {1: 0.1, 10: 0.6, 100: 0.8}
    samples = []
    progress_bar = tqdm(total=len(dataset) * n_sample, desc="Generating samples")
    for task_id in dataset:
        for i in range(n_sample):
            prompt = dataset[task_id]["prompt"]
            # prompt = gen_prompt(prompt, model)
            temperature = best_temperature[n_sample]
            completion = code_completion(
                prompt,
                tokenizer,
                model,
                temperature=temperature,
                top_p=TOP_P,
                do_sample=DO_SAMPLE,
                early_stopping=EARLY_STOPPING,
                total_output=TOTAL_OUTPUT,
                max_tokens=MAX_TOKENS,
            )
            if TOTAL_OUTPUT == 0:
                output_code = completion[0]
            else:
                for i, c in enumerate(completion):
                    output_code = c + "\n"
            output_code = fix_indents(output_code)
            # new_code = output_code.split(prompt)[-1]
            sample = dict(task_id=task_id, completion= output_code)
            if i == 0:
                print("Prompt: ", "-" * 100)
                print(prompt)
                print("Completion: ", "-" * 100)
                print( output_code)
            samples.append(sample)
            progress_bar.update(1)
    progress_bar.close()

    model_name = MODEL.replace("/", "_")
    pred_filename = f"humaneval_{model_name}_predictions.jsonl"
    write_jsonl(pred_filename, samples)
    print("Evaluating...")
    result = entry_point(problem_file=data_path, sample_file=pred_filename)
    return result


# def main():
#     tokenizer, model = setup_model()

#     data_path: str = "../HumanEval_Clear.jsonl"
#     result = evaluate(tokenizer, model, data_path)
#     print(result)
#     return result["pass@1"]


def main():

    data_path: str = "./HumanEval_Clear.jsonl"
    pred_filename: str = "./humaneval_clear_Salesforce_codegen-2B-mono_predictions_cleared.jsonl"

    result = entry_point(problem_file=data_path, sample_file=pred_filename)
    print(result)

"""
p humaneval.py main  --model_name llama --model_path decapoda-research/llama-7b-hf --n_sample 1
{'pass@1': 0.105}

p humaneval.py main  --model_name llama --model_path chavinlo/alpaca-native --n_sample 1
{'pass@1': 0.105}

p humaneval.py main  --model_name llama --model_path eachadea/vicuna-13b --n_sample 1 --load_8bit
{'pass@1': 0.152}

python main.py humaneval --model_name llama --model_path decapoda-research/llama-7b-hf --n_sample 1 --load_8bit
{'pass@1': 0.10365853658536585}

python main.py humaneval --model_name llama --model_path decapoda-research/llama-13b-hf --n_sample 1 --load_8bit
{'pass@1': 0.12804878048780488}

python main.py humaneval --model_name llama --model_path huggyllama/llama-13b --n_sample 1 --load_8bit
{'pass@1': 0.12804878048780488}

python main.py humaneval --model_name causal --model_path Salesforce/codegen-6B-mono --n_sample 1
{'pass@1': 0.27439024390243905}

python main.py humaneval --model_name llama --model_path TheBloke/wizardLM-7B-HF --n_sample 1
{'pass@1': 0.1402439024390244}

python main.py humaneval --model_name seq_to_seq --model_path google/flan-t5-xl --n_sample 1
{'pass@1': 0.0}                                                        

python main.py humaneval --model_name causal --model_path stabilityai/stablelm-tuned-alpha-7b --n_sample 1
{'pass@1': 0.054878048780487805}

python main.py humaneval --model_name llama --model_path TheBloke/OpenAssistant-SFT-7-Llama-30B-HF --load_8bit
{'pass@1': 0.23170731707317074}

python main.py humaneval --model_name causal --model_path ../FlanPaca/export/flan-codegen-3b
{'pass@1': 0.15853658536585366}

python main.py humaneval --model_name llama --model_path huggyllama/llama-30b --load_8bit
{'pass@1': 0.1402439024390244}

python main.py humaneval --model_name causal --model_path facebook/opt-iml-30b --load_8bit --n_sample 1
{'pass@1': 0.09146341463414634}

"""


if __name__ == "__main__":
    main()
