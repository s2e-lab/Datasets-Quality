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
    #print(path)
    if jsonl:
        data = []
        with open(path, 'r') as f:
            for line in f:
                data.append(json.loads(line))
        return data
    else:
        # with open(path,'r',encoding="utf8") as f:
        with open(path,'r') as f:
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
        #print(comment)
        nl_docs.extend(comment)
    return nl_docs

def process_human_eval_plus_dataset(data: list) -> list:
    nl_docs = []
    for d in tqdm(data):
        text = d['prompt']
        comment=find_python_comment(text)
        nl_docs.extend(comment)
    return nl_docs
    
def process_mbxp_python_dataset(data: list) -> list:
    nl_docs = []
    for d in tqdm(data):
        text = d['prompt']
        comment=find_python_comment(text)
        nl_docs.extend(comment)
    return nl_docs

def process_mbxp_humaneval_python_dataset(data: list) -> list:
    nl_docs = []
    for d in tqdm(data):
        text = d['prompt']
        comment=find_python_comment(text)
        nl_docs.extend(comment)
    return nl_docs

def process_mbxp_java_dataset(data: list) -> list:
    nl_docs = []
    for d in tqdm(data):
        text = d['prompt']
        comment=find_java_comment(text)
        nl_docs.extend(comment)
    return nl_docs

def process_mbxp_humaneval_java_dataset(data: list) -> list:
    nl_docs = []
    for d in tqdm(data):
        text = d['prompt']
        comment=find_java_comment(text)
        nl_docs.extend(comment)
    return nl_docs

def process_mbxp_mathqa_java_dataset(data: list) -> list:
    nl_docs = []
    for d in tqdm(data):
        text = d['prompt']
        comment=find_java_comment(text)
        nl_docs.extend(comment)
    return nl_docs

def process_mbxp_mathqa_python_dataset(data: list) -> list:
    nl_docs = []
    for d in tqdm(data):
        text = d['prompt']
        comment=find_python_comment(text)
        nl_docs.extend(comment)
    return nl_docs
    
def process_odex_en_dataset(data: list) -> list:
    nl_docs = []
    for d in tqdm(data):
        text = d['intent']
        comment=text
        nl_docs.append(comment)
    return nl_docs
def process_pandasNumpyEval_numpy_dataset(data: list) -> list:
    nl_docs = []
    for d in tqdm(data):
        text = d['prompt']
        comment=find_python_comment(text)
        
        nl_docs.extend(comment)
    return nl_docs

def process_pandasNumpyEval_pandas_dataset(data: list) -> list:
    nl_docs = []
    for d in tqdm(data):
        text = d['prompt']
        comment=find_python_comment(text)
        
        nl_docs.extend(comment)
    return nl_docs
def process_CoderEval_python_dataset(data: list) -> list:
    nl_docs = []
    data=data["RECORDS"]
    for d in tqdm(data):
        text = d["human_label"]
        comment=text
        nl_docs.append(comment)
    return nl_docs

def process_MCoNaLa_ru_test_to_en_dataset(data: list) -> list:
    nl_docs = []
    
    for d in tqdm(data):
        text = d["intent"]
        nl_docs.extend(text)
    return nl_docs

def process_MCoNaLa_ja_test_to_en_dataset(data: list) -> list:
    nl_docs = []
    
    for d in tqdm(data):
        text = d["intent"]
        nl_docs.extend(text)
    return nl_docs

def process_MCoNaLa_es_test_to_en_dataset(data: list) -> list:
    nl_docs = []
    for d in tqdm(data):
        text = d["intent"]
        nl_docs.extend(text)
    return nl_docs

def process_torch_data_beatnum_eval_v3_dataset(data: list) -> list:
    nl_docs = []
    
    for d in tqdm(data):
        text = d["prompt"]
        comment=find_python_comment(text)
        nl_docs.extend(comment)
    return nl_docs

def process_torch_data_beatnum_eval_v3_dataset(data: list) -> list:
    nl_docs = []
    
    for d in tqdm(data):
        text = d["prompt"]
        comment=find_python_comment(text)
        nl_docs.extend(comment)
    return nl_docs

def process_torch_data_monkey_eval_v3_dataset(data: list) -> list:
    nl_docs = []
    
    for d in tqdm(data):
        text = d["prompt"]
        comment1=find_python_comment(text)
        comment2=find_python_comment(text)
        nl_docs.extend(comment1)
        nl_docs.extend(comment2)
    return nl_docs

def process_torch_data_torchdata_eval_v3_dataset(data: list) -> list:
    nl_docs = []
    
    for d in tqdm(data):
        text = d["prompt"]
        comment=find_python_comment(text)
        nl_docs.extend(comment)
    return nl_docs

def process_torch_data_makesense_eval_v3_dataset(data: list) -> list:
    nl_docs = []
    
    for d in tqdm(data):
        text = d["prompt"]
        comment=find_python_comment(text)
        nl_docs.extend(comment)
    return nl_docs

def process_CodeComplex_extend_data_dataset(data: list) -> list:
    nl_docs = []
    #print("here")
    for d in tqdm(data):
        text = d["src"]
        comments=find_java_comment(text)
        #print("hereeee")
        #comment2=find_java_comment_singleline(text)
        nl_docs.extend(comments)
        #nl_docs.extend(comment2)
        
    return nl_docs

def process_CodeComplex_new_data_dataset(data: list) -> list:
    nl_docs = []
    data=data[0]
    for d in tqdm(data):
        text = d["src"]
        
        # comment1=find_java_comment_multiline(text)
        # # print("hereee")
        # # print(comment1)
        # comment2=find_java_comment_singleline(text)
        comments=find_java_comment(text)
        # print(comment1)
        # print(comment2)
        nl_docs.extend(comments)
        #nl_docs.extend(comment2)
    return nl_docs



def process_HumanEval_Infilling_MultiLineInfilling_dataset(data: list) -> list:
    nl_docs = []
    
    for d in tqdm(data):
        text = d["prompt"]
        comment=find_python_comment(text)
        nl_docs.extend(comment)

        #print(d)
    return nl_docs

def process_Jigsaw_PandasEval1_dataset(data: list) -> list:
   nl_docs = []
    
   for entry in tqdm(data.values()):
        for set_data in entry['sets'].values():
            for query_data in set_data['queries']:
                nl_docs.append(query_data['query'])
   return nl_docs
def process_Jigsaw_PandasEval2_dataset(data: list) -> list:
    nl_docs = []
    
    for entry in tqdm(data.values()):
        for set_data in entry['sets'].values():
            for query_data in set_data['queries']:
                nl_docs.append(query_data['query'])
        

    return nl_docs

def process_sanitized_mbpp_dataset(data: list) -> list:
    nl_docs = []
    
    for d in tqdm(data):
        text = d["prompt"]
        comment=text
        nl_docs.append(comment)

    return nl_docs



def find_python_comment(text):
    pattern_hash = r'(#.*?\n)'
    comments=(re.findall(pattern_hash, text, re.DOTALL))
    pattern_single_double_quote = r"(['\"]{3}.*?['\"]{3})"
    comments.extend(re.findall(pattern_single_double_quote, text, re.DOTALL))
    return comments


def find_java_comment(text):
    #print(text)
    #print("hereeee")
    pattern_multiline = r"(/\*.*?\*/)"
    comments = re.findall(pattern_multiline, text, re.DOTALL)
    pattern_single_line = r'(//.*?\n)'
    comments.extend(re.findall(pattern_single_line, text, re.DOTALL))
    return comments
    
# def find_java_comment_singleline(text):    
#     pattern = r'//(.*?)\n'
#     comments = re.findall(pattern, text, re.DOTALL)
#     return comments

def write_result(filepath: str, data: object) -> None:
    """
    Saves the results into a JSON file.
    
    :param filepath: absolute/relative filepath to a JSON file where the data shall be saved.
    :param data: results to be saved
    """
    with open(filepath, 'w') as f:
        json.dump(data, f)
    
    