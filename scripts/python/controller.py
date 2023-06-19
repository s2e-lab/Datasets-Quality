from tqdm import tqdm
#from utils import get_data, process_concode_dataset, process_human_eval_dataset, process_mbxp_python_dataset, process_mbxp_java_dataset, process_mbxp_humaneval_java_dataset, process_mbxp_humaneval_python_dataset, process_mbxp_mathqa_python_dataset, process_mbxp_mathqa_java_dataset, process_odex_en_dataset, write_result
from utils import *
#from utils import process_pandasNumpyEval_numpy_dataset,process_pandasNumpyEval_pandas_dataset,process_CoderEval_python_dataset
from rules import rule_p1,rule_p2,rule_p5,rule_p4,rule_p3

TARGET_DATASET = [{"Source_Path":"../../datasets/CONCODE/concode_test.json", "Output_Path":"CONCODE_heuristic_results.json","jsonl":True},
                  {"Source_Path":"../../datasets/HumanEval/human-eval-v2-20210705.jsonl", "Output_Path":"HumanEval_heuristic_results.json","jsonl":True},
                  {"Source_Path":"../../datasets/mbxp/mbpp_release_v1.jsonl", "Output_Path":"mbxp_python_heuristic_results.json","jsonl":True},
                  {"Source_Path":"../../datasets/mbxp/mbjp_release_v1.jsonl", "Output_Path":"mbxp_java_heuristic_results.json","jsonl":True},
                  {"Source_Path":"../../datasets/mbxp_humaneval/HumanEval.jsonl", "Output_Path":"mbxp_humaneval_python_heuristic_results.json","jsonl":True},
                  {"Source_Path":"../../datasets/mbxp_humaneval/HumanEval_java_v1.1.jsonl", "Output_Path":"mbxp_humaneval_java_heuristic_results.json","jsonl":True},
                  {"Source_Path":"../../datasets/mbxp_mathqa/mathqa-test-python_v1.jsonl", "Output_Path":"mbxp_mathqa_python_heuristic_results.json","jsonl":True},
                  {"Source_Path":"../../datasets/mbxp_mathqa/mathqa-test-java_v1.jsonl", "Output_Path":"mbxp_mathqa_java_heuristic_results.json","jsonl":True},
                  {"Source_Path":"../../datasets/ODEX/en_test.jsonl", "Output_Path":"odex_en_heuristic_results.json","jsonl":True},
                  {"Source_Path":"../../datasets/pandasNumpyEval/offical_numpy.jsonl", "Output_Path":"pandasNumpyEval_numpy_heuristic_results.json","jsonl":True},
                  {"Source_Path":"../../datasets/pandasNumpyEval/offical_pandas.jsonl", "Output_Path":"pandasNumpyEval_pandas_heuristic_results.json","jsonl":True},
                  {"Source_Path":"../../datasets/CoderEval/CoderEval4Python.json", "Output_Path":"CoderEval4Python__heuristic.json","jsonl":False},
                  {"Source_Path":"../../datasets/MCoNaLa/test/flores101/es_test_to_en.json", "Output_Path":"MCoNaLa_es_test_to_en__heuristic.json","jsonl":False},
                  {"Source_Path":"../../datasets/MCoNaLa/test/flores101/ja_test_to_en.json", "Output_Path":"MCoNaLa_ja_test_to_en__heuristic.json","jsonl":False},
                  {"Source_Path":"../../datasets/MCoNaLa/test/flores101/ru_test_to_en.json", "Output_Path":"MCoNaLa_ru_test_to_en__heuristic.json","jsonl":False},
                  {"Source_Path":"../../datasets/TorchDataEval/real_beatnum_eval_v3_human_labelled.jsonl", "Output_Path":"real_beatnum_eval_v3_human_labelled_heuristic.json","jsonl":True},
                  {"Source_Path":"../../datasets/TorchDataEval/real_monkey_eval_v3_human_labelled.jsonl", "Output_Path":"real_monkey_eval_v3_human_labelled_heuristic.json","jsonl":True},
                  {"Source_Path":"../../datasets/TorchDataEval/real_torchdata_eval_v3_human_labelled.jsonl", "Output_Path":"real_torchdata_eval_v3_human_labelled_heuristic.json","jsonl":True},
                  {"Source_Path":"../../datasets/TorchDataEval/real_torchdata_eval_v3_human_labelled_make_sense.jsonl", "Output_Path":"real_torchdata_eval_v3_human_labelled_make_sense_heuristic.json","jsonl":True},
                  {"Source_Path":"../../datasets/CodeComplex/extend_data.jsonl", "Output_Path":"CodeComplex_extend_data_heuristic.json","jsonl":True},
                  {"Source_Path":"../../datasets/CodeComplex/new_data.jsonl", "Output_Path":"CodeComplex_new_data_heuristic.json","jsonl":True},
                  {"Source_Path":"../../datasets/HumanEval-Infilling/HumanEval-MultiLineInfilling.jsonl", "Output_Path":"HumanEval-MultiLineInfilling_heuristic.json","jsonl":True},
                  {"Source_Path":"../../datasets/JigsawDataset/PandasEval1.json", "Output_Path":"JigsawDataset_pandas_eval1_heuristic.json","jsonl":False},
                  {"Source_Path":"../../datasets/JigsawDataset/PandasEval2.json", "Output_Path":"JigsawDataset_pandas_eval2_heuristic.json","jsonl":False},
                  {"Source_Path":"../../datasets/MBPP/sanitized-mbpp.json", "Output_Path":"sanitized-mbpp_heuristic.json","jsonl":False}]

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
    elif "HumanEval-Infilling" in current_dataset["Source_Path"]:
        #print("hereeein")
        nl_docs = process_HumanEval_Infilling_MultiLineInfilling_dataset(data)
        write_path += current_dataset["Output_Path"]
    elif "HumanEval" in current_dataset["Source_Path"]:
        nl_docs = process_human_eval_dataset(data)
        write_path += current_dataset["Output_Path"]
    elif "mbxp" in current_dataset["Source_Path"] and "mbpp" in current_dataset["Source_Path"]:
        nl_docs = process_mbxp_python_dataset(data)
        write_path += current_dataset["Output_Path"]
    elif "mbxp" in current_dataset["Source_Path"] and "mbjp" in current_dataset["Source_Path"]:
        nl_docs = process_mbxp_java_dataset(data)
        write_path += current_dataset["Output_Path"]
    elif "mbxp_humaneval" in current_dataset["Source_Path"] and not "java" in current_dataset["Source_Path"]:
        nl_docs = process_mbxp_humaneval_python_dataset(data)
        write_path += current_dataset["Output_Path"]
    elif "mbxp_humaneval" in current_dataset["Source_Path"] and "java" in current_dataset["Source_Path"]:
        nl_docs = process_mbxp_humaneval_java_dataset(data)
        write_path += current_dataset["Output_Path"]
    elif "mbxp_mathqa" in current_dataset["Source_Path"] and "python" in current_dataset["Source_Path"]:
        nl_docs = process_mbxp_mathqa_python_dataset(data)
        write_path += current_dataset["Output_Path"]
    elif "mbxp_mathqa" in current_dataset["Source_Path"] and "java" in current_dataset["Source_Path"]:
        nl_docs = process_mbxp_mathqa_java_dataset(data)
        write_path += current_dataset["Output_Path"]
    elif "ODEX" in current_dataset["Source_Path"] and "en" in current_dataset["Source_Path"]:
        nl_docs = process_odex_en_dataset(data)
        write_path += current_dataset["Output_Path"]
    elif "pandasNumpyEval" in current_dataset["Source_Path"] and "numpy" in current_dataset["Source_Path"]:
        nl_docs = process_pandasNumpyEval_numpy_dataset(data)
        write_path += current_dataset["Output_Path"]
    elif "pandasNumpyEval" in current_dataset["Source_Path"] and "pandas" in current_dataset["Source_Path"]:
        nl_docs = process_pandasNumpyEval_pandas_dataset(data)
        write_path += current_dataset["Output_Path"]
    elif "CoderEval" in current_dataset["Source_Path"] and "Python" in current_dataset["Source_Path"]:
        nl_docs = process_CoderEval_python_dataset(data)
        write_path += current_dataset["Output_Path"]
    elif "MCoNaLa" in current_dataset["Source_Path"] and "es_test_to_en" in current_dataset["Source_Path"]:
        nl_docs = process_MCoNaLa_es_test_to_en_dataset(data)
        write_path += current_dataset["Output_Path"]
    elif "MCoNaLa" in current_dataset["Source_Path"] and "ja_test_to_en" in current_dataset["Source_Path"]:
        nl_docs = process_MCoNaLa_ja_test_to_en_dataset(data)
        write_path += current_dataset["Output_Path"]
    elif "MCoNaLa" in current_dataset["Source_Path"] and "ru_test_to_en" in current_dataset["Source_Path"]:
        nl_docs = process_MCoNaLa_ru_test_to_en_dataset(data)
        write_path += current_dataset["Output_Path"]
    elif "TorchDataEval" in current_dataset["Source_Path"] and "beatnum" in current_dataset["Source_Path"]:
        nl_docs = process_torch_data_beatnum_eval_v3_dataset(data)
        write_path += current_dataset["Output_Path"]
    elif "TorchDataEval" in current_dataset["Source_Path"] and "monkey" in current_dataset["Source_Path"]:
        nl_docs = process_torch_data_monkey_eval_v3_dataset(data)
        write_path += current_dataset["Output_Path"]
    elif "TorchDataEval" in current_dataset["Source_Path"] and "torchdata" in current_dataset["Source_Path"]:
        nl_docs = process_torch_data_torchdata_eval_v3_dataset(data)
        write_path += current_dataset["Output_Path"]
    elif "TorchDataEval" in current_dataset["Source_Path"] and "make_sense" in current_dataset["Source_Path"]:
        nl_docs = process_torch_data_makesense_eval_v3_dataset(data)
        write_path += current_dataset["Output_Path"]
    elif "CodeComplex" in current_dataset["Source_Path"] and "extend_data" in current_dataset["Source_Path"]:
        nl_docs = process_CodeComplex_extend_data_dataset(data)
        write_path += current_dataset["Output_Path"]
    elif "CodeComplex" in current_dataset["Source_Path"] and "new_data" in current_dataset["Source_Path"]:
        nl_docs = process_CodeComplex_new_data_dataset(data)
        write_path += current_dataset["Output_Path"]
    elif "JigsawDataset" in current_dataset["Source_Path"] and "PandasEval1" in current_dataset["Source_Path"]:
        nl_docs = process_Jigsaw_PandasEval1_dataset(data)
        write_path += current_dataset["Output_Path"]
    elif "JigsawDataset" in current_dataset["Source_Path"] and "PandasEval2" in current_dataset["Source_Path"]:
        nl_docs = process_Jigsaw_PandasEval2_dataset(data)
        write_path += current_dataset["Output_Path"]
    elif "MBPP" in current_dataset["Source_Path"] and "sanitized-mbpp" in current_dataset["Source_Path"]:
        nl_docs = process_sanitized_mbpp_dataset(data)
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
    TARGET_DATASET.reverse()
    for current_dataset in TARGET_DATASET:
        #print(current_dataset["Source_Path"])
        
        data = get_data(path=current_dataset["Source_Path"], jsonl=current_dataset["jsonl"])
        
        apply_rules(current_dataset,data)



if __name__ == "__main__":
    main()
