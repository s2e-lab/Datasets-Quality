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
        text = d['prompt']
        comment=find_python_comment(text)
        nl_docs.append(comment)
    return nl_docs

def process_human_eval_plus_dataset(data: list) -> list:
    nl_docs = []
    for d in tqdm(data):
        text = d['prompt']
        comment=find_python_comment(text)
        nl_docs.append(comment)
    return nl_docs
    
def process_mbxp_python_dataset(data: list) -> list:
    nl_docs = []
    for d in tqdm(data):
        text = d['prompt']
        comment=find_python_comment(text)
        nl_docs.append(comment)
    return nl_docs

def process_mbxp_humaneval_python_dataset(data: list) -> list:
    nl_docs = []
    for d in tqdm(data):
        text = d['prompt']
        comment=find_python_comment(text)
        nl_docs.append(comment)
    return nl_docs

def process_mbxp_java_dataset(data: list) -> list:
    nl_docs = []
    for d in tqdm(data):
        text = d['prompt']
        comment=find_java_comment(text)
        nl_docs.append(comment)
    return nl_docs

def process_mbxp_humaneval_java_dataset(data: list) -> list:
    nl_docs = []
    for d in tqdm(data):
        text = d['prompt']
        comment=find_java_comment(text)
        nl_docs.append(comment)
    return nl_docs

def process_mbxp_mathqa_java_dataset(data: list) -> list:
    nl_docs = []
    for d in tqdm(data):
        text = d['prompt']
        comment=find_java_comment(text)
        nl_docs.append(comment)
    return nl_docs

def process_mbxp_mathqa_python_dataset(data: list) -> list:
    nl_docs = []
    for d in tqdm(data):
        text = d['prompt']
        comment=find_python_comment(text)
        nl_docs.append(comment)
    return nl_docs
    
def process_odex_en_dataset(data: list) -> list:
    nl_docs = []
    for d in tqdm(data):
        text = d['intent']
        comment=find_python_comment_sigQ(text)
        nl_docs.append(comment)
    return nl_docs
def process_pandasNumpyEval_numpy_dataset(data: list) -> list:
    nl_docs = []
    for d in tqdm(data):
        text = d['prompt']
        comment=find_python_comment_hash(text)
        print(comment)
        nl_docs.append(comment)
    return nl_docs

def process_pandasNumpyEval_pandas_dataset(data: list) -> list:
    nl_docs = []
    for d in tqdm(data):
        text = d['prompt']
        comment=find_python_comment_hash(text)
        print(comment)
        print(comment)
        nl_docs.append(comment)
    return nl_docs
def process_CoderEval_python_dataset(data: list) -> list:
    nl_docs = []
    for d in tqdm(data):
        text = d['test_name']
        comment=find_python_comment_sigQ(text)
        print(comment)
        print(comment)
        nl_docs.append(comment)
    return nl_docs

def find_python_comment_hash(text):
    
    start_index = text.find(r'#')
    start_index += 2
    end_index = text.rfind(r'\n')

    return text[start_index:end_index]



def find_python_comment_sigQ(text):
    
    start_index = text.find(r'"')
    start_index += 1
    end_index = text.rfind(r'"')

    return text[start_index:end_index]


def find_python_comment(text):
    start_index = text.find(r'"""')
    if start_index == -1:
            start_index = text.find(r"'''")
    start_index += 3

    end_index = text.rfind(r'"""')
    if end_index == -1:
        end_index = text.rfind(r"'''")
    return text[start_index:end_index]


def find_java_comment(text):
    start_index = text.find(r'/*')
    start_index += 3
    end_index = text.rfind(r'*/')
    
    return text[start_index:end_index]

    



def write_result(filepath: str, data: object) -> None:
    """
    Saves the results into a JSON file.
    
    :param filepath: absolute/relative filepath to a JSON file where the data shall be saved.
    :param data: results to be saved
    """
    with open(filepath, 'w') as f:
        json.dump(data, f)
    
    