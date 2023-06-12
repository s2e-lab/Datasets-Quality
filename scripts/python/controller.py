from tqdm import tqdm
from utils import get_data, process_concode_dataset, process_human_eval_dataset, process_mbxp_python_dataset, process_mbxp_java_dataset, process_mbxp_humaneval_java_dataset, process_mbxp_humaneval_python_dataset, process_mbxp_mathqa_python_dataset, process_mbxp_mathqa_java_dataset, write_result
from rules import rule_p1,rule_p2,rule_p5,rule_p4,rule_p3

TARGET_DATASET = [{"Source_Path":"../../datasets/CONCODE/concode_test.json", "Output_Path":"CONCODE_heuristic_results.json"},
                  {"Source_Path":"../../datasets/HumanEval/human-eval-v2-20210705.jsonl", "Output_Path":"HumanEval_heuristic_results.json"},
                  {"Source_Path":"../../datasets/mbxp/mbpp_release_v1.jsonl", "Output_Path":"mbxp_python_heuristic_results.json"},
                  {"Source_Path":"../../datasets/mbxp/mbjp_release_v1.jsonl", "Output_Path":"mbxp_java_heuristic_results.json"},
                  {"Source_Path":"../../datasets/mbxp_humaneval/HumanEval.jsonl", "Output_Path":"mbxp_humaneval_python_heuristic_results.json"},
                  {"Source_Path":"../../datasets/mbxp_humaneval/HumanEval_java_v1.1.jsonl", "Output_Path":"mbxp_humaneval_java_heuristic_results.json"},
                  {"Source_Path":"../../datasets/mbxp_mathqa/mathqa-test-python_v1.jsonl", "Output_Path":"mbxp_mathqa_python_heuristic_results.json"},
                  {"Source_Path":"../../datasets/mbxp_mathqa/mathqa-test-java_v1.jsonl", "Output_Path":"mbxp_mathqa_java_heuristic_results.json"}]

RESULT_FOLDER  = "../../results/"
MAX_NUMBER_OF_HEURISTICS = 6

def apply_rules(current_dataset: dict,data: object) -> None:
    """
    Executes the heuristics on the JSON data passed as inout.
    
    :param data: the prompt dataset
    """

    nl_docs = []
    write_path = RESULT_FOLDER
    if "CONCODE" in current_dataset["Source_Path"]:
        nl_docs = process_concode_dataset(data)
        write_path += current_dataset["Output_Path"]
    elif "HumanEval" in current_dataset["Source_Path"]:
        nl_docs = process_human_eval_dataset(data)
        write_path += current_dataset["Output_Path"]
    elif "mbxp" in current_dataset["Source_Path"] and "mbpp" in current_dataset["Source_Path"]:
        nl_docs = process_mbxp_python_dataset(data)
        write_path += current_dataset["Output_Path"]
    elif "mbxp" in current_dataset"Source_Path"] and "mbjp" in current_dataset["Source_Path"]:
        nl_docs = process_mbxp_java_dataset(data)
        write_path += current_dataset["Output_Path"]
    elif "mbxp_humaneval" in current_dataset["Source_Path"] and not "java" in current_dataset["Source_Path"]:
        nl_docs = process_mbxp_humaneval_python_dataset(data)
        write_path += TARGET_DATASET[global_i]["Output_Path"]
    elif "mbxp_humaneval" in current_dataset["Source_Path"] and "java" in current_dataset["Source_Path"]:
        nl_docs = process_mbxp_humaneval_java_dataset(data)
        write_path += current_dataset["Output_Path"]
    elif "mbxp_mathqa" in current_dataset["Source_Path"] and "python" in current_dataset["Source_Path"]:
        nl_docs = process_mbxp_mathqa_python_dataset(data)
        write_path += current_dataset["Output_Path"]
    elif "mbxp_mathqa" in current_dataset["Source_Path"] and "java" in current_dataset["Source_Path"]:
        nl_docs = process_mbxp_mathqa_java_dataset(data)
        write_path += current_dataset["Output_Path"]

    assert nl_docs != []
    results = []

    for nl in tqdm(nl_docs):
        result = {"nl": nl, "Heuristic": ""}
        applied_heuristics = [False for _ in range(0, MAX_NUMBER_OF_HEURISTICS)]
        if rule_p1(nl):
            applied_heuristics[0] = True
        if rule_p2(nl):
            applied_heuristics[1] = True
        # if rule_p3(nl):
        #     applied_heuristics[2]=True
        if rule_p4(nl):
            applied_heuristics[3] = True
        if rule_p5(nl):
            applied_heuristics[4]=True
        
        

        result["Heuristic"] = [
            f"H{i + 1}"
            for i in range(0, MAX_NUMBER_OF_HEURISTICS)
            if applied_heuristics[i]
        ]

        results.append(result)
    write_result(write_path, results)


def main():
    for current_dataset in TARGET_DATASET:
        data = get_data(path=current_dataset["Source_Path"], jsonl=True)
        apply_rules(current_dataset,data)



if __name__ == "__main__":
    main()
