from tqdm import tqdm

from utils import get_data, process_concode_dataset, write_result
from heuristics import heuristic_1

TARGET_DATASET = "../../../Datasets/CONCODE/concode_test.json"

MAX_NUMBER_OF_HEURISTICS = 6


def run_heuristic(data):
    nl_docs = []
    write_path = "./Result/"
    if "CONCODE" in TARGET_DATASET:
        nl_docs = process_concode_dataset(data)
        write_path += "CONCODE_heuristic_results.json"
        print(nl_docs[0])
    assert nl_docs != []
    results = []

    for nl in tqdm(nl_docs):
        result = {"nl": nl, "Heuristic": ""}
        applied_heuristics = [False for _ in range(0, MAX_NUMBER_OF_HEURISTICS)]
        if heuristic_1(nl):
            applied_heuristics[0] = True

        result["Heuristic"] = [
            f"H{i + 1}"
            for i in range(0, MAX_NUMBER_OF_HEURISTICS)
            if applied_heuristics[i]
        ]

        results.append(result)
    write_result(write_path, results)


def main():
    data = get_data(path=TARGET_DATASET, jsonl=True)
    run_heuristic(data)


if __name__ == "__main__":
    main()
