from tqdm import tqdm
from utils import get_data, process_concode_dataset, write_result
from rules import rule_p1

TARGET_DATASET = [{"Source_Path":"../../datasets/CONCODE/concode_test.json", "Output_Path":"CONCODE_heuristic_results.json"}]
RESULT_FOLDER  = "../../results/"
MAX_NUMBER_OF_HEURISTICS = 6


def apply_rules(data: object) -> None:
    """
    Executes the heuristics on the JSON data passed as inout.
    
    :param data: the prompt dataset
    """

    nl_docs = []
    write_path = RESULT_FOLDER
    if "CONCODE" in TARGET_DATASET[0]["Source_Path"]:
        nl_docs = process_concode_dataset(data)
        write_path += TARGET_DATASET[0]["Output_Path"]
        
    assert nl_docs != []
    results = []

    for nl in tqdm(nl_docs):
        result = {"nl": nl, "Heuristic": ""}
        applied_heuristics = [False for _ in range(0, MAX_NUMBER_OF_HEURISTICS)]
        if rule_p1(nl):
            applied_heuristics[0] = True

        result["Heuristic"] = [
            f"H{i + 1}"
            for i in range(0, MAX_NUMBER_OF_HEURISTICS)
            if applied_heuristics[i]
        ]

        results.append(result)
    write_result(write_path, results)


def main():
    data = get_data(path=TARGET_DATASET[0]["Source_Path"], jsonl=True)
    apply_rules(data)


if __name__ == "__main__":
    main()
