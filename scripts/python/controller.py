from tqdm import tqdm
from utils import get_data, process_concode_dataset, write_result
from rules import rule_p1,rule_p2,rule_p5,rule_p4,rule_p3

TARGET_DATASET = "../../datasets/CONCODE/concode_test.json"
RESULT_FOLDER  = "../../results/"
MAX_NUMBER_OF_HEURISTICS = 6


def apply_rules(data: object) -> None:
    """
    Executes the heuristics on the JSON data passed as inout.
    
    :param data: the prompt dataset
    """

    nl_docs = []
    write_path = RESULT_FOLDER
    if "CONCODE" in TARGET_DATASET:
        nl_docs = process_concode_dataset(data)
        write_path += "CONCODE_heuristic_results.json"
        
    assert nl_docs != []
    results = []
    #nl_docs=nl_docs[1:20]
    # Open the file in write mode
    # file_path = 'processed_file.txt'
    # file = open(file_path, 'w')

# Write content to the file
    # file.writelines([str(item) + '\n' for item in nl_docs])
    #file.write("This is a sample text.")

# Close the file
    # file.close()
    file_path = 'test_file.txt'
    with open(file_path, 'r') as file:
    # Read all lines from the file and store them in a list
        nl_docs_temp = file.readlines()
    for nl in tqdm(nl_docs_temp):
        print(nl)
        result = {"nl": nl, "Heuristic": ""}
        applied_heuristics = [False for _ in range(0, MAX_NUMBER_OF_HEURISTICS)]
        if rule_p1(nl):
            applied_heuristics[0] = True
        if rule_p2(nl):
            applied_heuristics[1] = True
        if rule_p3(nl):
            applied_heuristics[2]=True
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
    data = get_data(path=TARGET_DATASET, jsonl=True)
    apply_rules(data)


if __name__ == "__main__":
    main()
