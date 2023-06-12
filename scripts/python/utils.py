import json
from tqdm import tqdm
import re
def get_data(path: str, jsonl = False) -> object:
    """
    Parse data from a JSON or JSONL file.
    :param path: absolute/relative path to the file to be parsed.
    :param jsonl: indicates whether it is a JSONL format (defaults to False)
    :returns: the parsed JSON data.
    """
    if jsonl:
        data = []
        with open(path, 'r') as f:
            for line in f:
                data.append(json.loads(line))
        return data
    else:
        with open(path, 'r') as f:
            data = json.load(f)
        return data
    
def process_concode_dataset(data: list) -> list:
    """
    Parses the CONCODE's dataset format.

    :param data: loaded data list
    :returns: a new list containing just the natural language descriptions
    """
    nl_docs = []
    for d in tqdm(data):
        nl_docs.append(d['nl'])
    return nl_docs

def process_human_eval_dataset(data: list) -> list:
    nl_docs = []
    for d in tqdm(data):
        # print(d)
        # print("here")
        temp_nl_docs = d['prompt']
        # print(temp_nl_docs)
        start_index = temp_nl_docs.find(r'"""')
        if start_index == -1:
            start_index = temp_nl_docs.find(r"'''")
        start_index += 3

        end_index = temp_nl_docs.rfind(r'"""')
        if end_index == -1:
            end_index = temp_nl_docs.rfind(r"'''")
        nl_docs.append(temp_nl_docs[start_index:end_index])
        # nl_docs.append(re.search(r'\"\"\"(.+?)\"\"\"', temp_nl_docs, re.DOTALL).group(1))
        print(nl_docs[-1])
    return nl_docs





def write_result(filepath: str, data: object) -> None:
    """
    Saves the results into a JSON file.
    
    :param filepath: absolute/relative filepath to a JSON file where the data shall be saved.
    :param data: results to be saved
    """
    with open(filepath, 'w') as f:
        json.dump(data, f)
    
    