import json
from tqdm import tqdm

def get_data(path, jsonl = False):
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
    
def process_concode_dataset(data):
    nl_docs = []
    for d in tqdm(data):
        nl_docs.append(d['nl'])
    return nl_docs

def write_result(path, data):
    with open(path, 'w') as f:
        json.dump(data, f)
    
    