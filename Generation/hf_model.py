import json
from tqdm import tqdm

import torch
from transformers import AutoModelForCausalLM, AutoTokenizer


dataset = ['Java', 'Py']
temperatures = [ 0.2, 0.8]
token_size_limits = [512]

NUMBER_OF_RESPONSES = 20

def model_response(prompt, temperature=0.8, max_length=128):
    prompt_text = prompt["prompt"]+'\n'
    inputs = tokenizer(prompt_text, return_tensors="pt").to('cuda')
    x = inputs['input_ids']
    x = x.expand(NUMBER_OF_RESPONSES, -1)
    generated_token = model.generate(
        x,
        temperature=temperature,
        max_length=max_length,
        do_sample=True,
    )
    prompt["output"] =[]
    for i in range(NUMBER_OF_RESPONSES):
        prompt["output"].append({})
        output = generated_token[i].cpu().squeeze()
        prompt["output"][i]["text"] = tokenizer.decode(output)

    return prompt

for item in dataset:
    # if 'Java' in item:
    #     model_name = "Salesforce/codegen25-7b-mulit"
    # else:
    #     model_name = "Salesforce/codegen25-7b-mono"

    model_name = "WizardLM/WizardCoder-1B-V1.0"

    dtype = torch.float16

    model = AutoModelForCausalLM.from_pretrained(model_name, trust_remote_code=True,torch_dtype=dtype,device_map="auto")
    tokenizer = AutoTokenizer.from_pretrained(model_name, trust_remote_code=True, torch_dtype=dtype,device_map="auto")

    with open(f'./HumanEval_{item}.jsonl') as f:
        data = [json.loads(line) for line in f.readlines()]
    print(f'Loaded {len(data)} prompts from {item} dataset')

    for temp in temperatures:
        for token_limit in token_size_limits:
            new_data = []
            print(f'Processing temperature {temp} and token limit {token_limit}')
            for item in tqdm(data):
                updated_item = model_response(item, temp, token_limit)
                new_data.append(updated_item)

                # Save to a JSON file with a filename indicating the parameters
            filename = f'./Output/WizardCoder_Output_{item}_{temp}.json'
            with open(filename, "w") as f:
                    json.dump(new_data, f, indent=4)
                    print(f'Saved to {filename}')