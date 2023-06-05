import json
from tqdm import tqdm

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

def write_result(filepath: str, data: object) -> None:
    """
    Saves the results into a JSON file.
    
    :param filepath: absolute/relative filepath to a JSON file where the data shall be saved.
    :param data: results to be saved
    """
    with open(filepath, 'w') as f:
        json.dump(data, f)
    
    