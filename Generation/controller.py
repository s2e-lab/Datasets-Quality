# %%
import json
from collections import defaultdict
import subprocess
import os

# %%
import re

def remove_comments(code):
    # Remove single-line comments
    code = re.sub(r'#.*', '', code)
    
    # Remove multi-line comments
    code = re.sub(r'(\'\'\'(.|\n)*?\'\'\'|\"\"\"(.|\n)*?\"\"\")', '', code)

    lines = code.split('\n')
    code = ''
    for line in lines:
        if line.strip() != '':
            code += line + '\n'
    
    return code

# %%

with open('./HumanEval_Py_original.jsonl', 'r') as f:
    data = f.readlines()
    original_data = [json.loads(line) for line in data]


# lines = []
mapping = defaultdict(list)
for d in original_data:
    id = d['task_id'].split('/')[1]
    mapping[id].append(d)
#     with open(f'./Original_Files/{id}_.py', 'w') as f:
#         f.write(remove_comments(d['prompt']+'\n'+d['canonical_solution']))
#         prompt_line = len(d['prompt'].split('\n'))
#         canonical_line = len(d['canonical_solution'].split('\n'))
#         total_line = prompt_line + canonical_line
#         without_comments = len(remove_comments(d['prompt']+'\n'+d['canonical_solution']).split('\n'))
#         lines.append([id, prompt_line, canonical_line, total_line, without_comments])

# import pandas as pd
# df = pd.DataFrame(lines, columns=['id', 'prompt', 'canonical', 'total', 'without_comments'])
# df.to_csv('line_count.csv', index=False)


# %%
from execution import check_correctness

# %%
file_name = 'SantaCoder_1B_Output_Py_0.2'
with open(f'./Output/{file_name}.json', 'r') as f:
    data = json.load(f)


# %%
split_tokens = ["\n'''","\n\"\"\"'","if __name__ == '__main__':",'if __name__ == "__main__":']
# split_tokens = ["if __name__ == '__main__':",'if __name__ == "__main__":']

# %%
def clear_generated_code(data):
    data = data.split('<|endoftext|>')[0]   

    for token in split_tokens:
        data = data.split(token)[0]
        
    lines = data.split('\n')
    new_data = ''
    for line in lines:
        if 'def ' in line:
            continue
        if not line.startswith(' '):
            line = '    '+line
        new_data += line+'\n'

    

    return new_data


# %%
def java_clear_generated_code(data):
    data = data.split('<|endoftext|>')[0]   
    data = data.split('public static void main')[0]
    left_bracket = data.count('{')
    right_bracket = data.count('}')
    if left_bracket > right_bracket:
        data += '}'*(left_bracket-right_bracket)
    return data

# %%
def get_Java_compilation_result(path):

    cmd = f'javac {path}'
    # print(cmd)
    p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = p.communicate()
    if err:
        return out, err.decode('utf-8')
    
    path = path.replace('.java', '')
    p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = p.communicate()

    return out, err


# %%
new_data = []
# for file in os.listdir('./Files'):
#     if file.endswith('.class'):
#         os.remove(f'./Files/{file}')
#     if file.endswith('.java'):
#         os.remove(f'./Files/{file}')
for d in data:
    id = d['id']

    original_id = id.split('_')[0]
    original_item = mapping[original_id][0]
    problem ={
        'task_id': id,
        'test': original_item['test'],
        'entry_point': original_item['entry_point'],
        'prompt': d['prompt']+'\n',
    }
    # for i, c in enumerate(d['output']['choices']):
    for i, c in enumerate(d['output']):
        # print(i)
        # completion = clear_generated_code(c['message']['content'])
        # completion = c['message']['content'].split('<|endoftext|>')[0]
        completion = c['text'].split('<|endoftext|>')[0]
        # problem['completion_'+str(i)] = completion
        # with open(f'./Files/{id}_{str(i)}.py', 'w') as f:
        #     # f.write(remove_comments(original_item['prompt']+'\n'+completion))
        #     f.write(remove_comments(completion))

        result = check_correctness(problem, completion, 3.0)

        print(result)
        
        # with open(f'./Files/Main.java', 'w') as f:
        #     f.write(java_clear_generated_code(completion)+'\n'+original_item['test'])
        # out, err = get_Java_compilation_result(f'./Files/Main.java')

        # for file in os.listdir('./Files'):
        #     if file.endswith('.class'):
        #         os.remove(f'./Files/{file}')
        #     if file.endswith('.java'):
        #         os.remove(f'./Files/{file}')



        # result = {}
        # if err:
        #     result['passed'] = False
        #     result['compilation_error'] = str(err)
        # else:
        #     result['passed'] = True
        #     result['compilation_error'] = ''
        #     result['output'] = out.decode('utf-8')
        #print(result)

        problem['result_'+str(i)] = result
    new_data.append(problem)
        # print(problem)
with open(f'./Output/{file_name}_result.jsonl', 'w') as f:
    for d in new_data:
        f.write(json.dumps(d)+'\n')

# %%
