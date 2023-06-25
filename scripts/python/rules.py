import language_tool_python as lt
import tokenize          
import re
import sys
import spacy
sys.path.append('..')
from patterns import AUTO_GEN_PATTERNS, HACK_PATTERNS
#from corenlp import StanfordCoreNLP
from stanfordcorenlp import StanfordCoreNLP
from pycorenlp import StanfordCoreNLP
# grammar checker is global because it is too costly to open/close all the time P1 is invoked
LANG_TOOL = lt.LanguageTool('en-US')

def tokenize_text(text) -> str:
    """Tokenize dromedaryCase or CamelCase or underscore_case words within a text.
    
    :param text: the text to be split
    :returns: a version of the text that has all words tokenized.
    """
    regex = '.+?(?:(?<=[a-z])(?=[A-Z])|(?<=[A-Z])(?=[A-Z][a-z])|$)'
    matches = re.finditer(regex, text.replace("_"," "))
    return " ".join([m.group(0) for m in matches])

def rule_p1(comment: str) -> bool:
    #print(comment)
    """
    Check if the comment contains a grammar mistake.
    
    :param comment: source code comment to be inspected
    :returns: true if a grammar issue was found.
    """
    tokenized_comment = tokenize_text(comment)
    # checks the tokenized version
    matches = LANG_TOOL.check(tokenized_comment)
    #if (len(matches)>0): 
        #print(matches)
    return len(matches) > 0


def rule_p2(comment: str) ->bool:
    """
    Check if the comment is too short.
    
    :param comment: source code comment to be inspected
    :returns: true if the comment is too short.
    """
    tokenized_comment = tokenize_text(comment)
    splitted_tokenize_comment=tokenized_comment.split(" ")
    if len(splitted_tokenize_comment)<3:
        #print("Too short")
        return True
    return False


def rule_p3(comment:str) ->bool:
    
    
    """
    Check if the comment is incomplete.
    
    :param comment: source code comment to be inspected
    :returns: true if the comment is incomplete.
    """
    # Download stanford-corenlp-4.5.4.zip from https://stanfordnlp.github.io/CoreNLP/index.html
    # Start corenlp server using: java -mx4g -cp "<path_to_the_extracted_zip_folder>/*" edu.stanford.nlp.pipeline.StanfordCoreNLPServer -port 9000 -timeout 15000
    # Create a StanfordCoreNLP object
    # nlp = StanfordCoreNLP('http://localhost:9000')
    # print("nlppp")
    # #nlp=StanfordCoreNLP('http://localhost:9000',9000)
    # #nlp.close()
    # output = nlp.annotate(comment, properties={'annotators': 'parse', 'outputFormat': 'json'})
    # print(output)
    # parse_tree = eval(output)["sentences"][0]["parse"]

    # # Check if the top-level constituent under ROOT is a FRAG
    # if parse_tree.startswith('(ROOT (FRAG'):
    #     print("Incomplete")
    #     return True
    # return False

    # Perform parsing and get constituency parse trees
    #result = nlp.annotate(comment, properties={'annotators': 'tokenize,ssplit,pos,parse', 'outputFormat': 'json'})
    
    # # Iterate over sentences
    # for sentence in result['sentences']:
    #     parse_tree = sentence['parse']
    #     root_constituent = parse_tree['root']['child'][0]
    #     if root_constituent['value'] == 'FRAG':
    #         print("Incomplete sentence")
    #         nlp.close()
    #         return True
    # nlp.close()
    #return False

    # Check if the top-level constituent is FRAG
    
    
    # python -m spacy download en_core_web_sm
    # https://stackoverflow.com/questions/72858984/mkl-service-package-failed-to-import-therefore-intelr-mkl-initialization-ensu
    

    nlp = spacy.load("en_core_web_sm")
    #text = "This is a complete sentence. Partial sentence without a verb. Another complete sentence."
    doc = nlp(comment)
    partial_sentences = []
    for sentence in doc.sents:
        if len(sentence) > 1 and not any(token.dep_ == 'ROOT' for token in sentence):
            partial_sentences.append(sentence.text.strip())
    if len(partial_sentences)>=1:
        return True
    return False
    
    
    

def rule_p4(comment:str) ->bool:
    """
    Check if the comment is Self-Admitted Technical Debt.
    
    :param comment: source code comment to be inspected
    :returns: true if the comment is Self-Admitted Technical Debt.
    """
    tokenized_comment = tokenize_text(comment).lower()
    lower_case_hack_patterns = [item.lower() for item in HACK_PATTERNS]
    found = any(pattern in tokenized_comment for pattern in lower_case_hack_patterns)
    if found:
        print("self-admitted technical debt")
    return found

def rule_p5(comment:str) ->bool:
    """
    Check if the comment is automatically generated code/comment.
    
    :param comment: source code comment to be inspected
    :returns: true if the comment is automatically generated.
    """
    tokenized_comment = tokenize_text(comment).lower()
    lower_case_auto_gen_patterns = [item.lower() for item in AUTO_GEN_PATTERNS]
    found = any(pattern in tokenized_comment for pattern in lower_case_auto_gen_patterns)
    if found:
        print("auto generated")
    return found

def  rule_p7(comment:str) ->bool:
    """
    Check if the comment is not using standard JavaDoc (Java) or docstring (Python)
    """
    # start_pattern = ["#", "//", "/"", "'"]
    # if comment[0] in start_pattern:
    #     standard_java_pattern = r"/\*\*(.*?)\*/"
    #     standard_python_multi_pattern = r'(?:"""|\'\'\')(.*?)(?:"""|\'\'\')'
    #     standard_python_single_pattern = r'(#.*?\n)'
    #     patterns = [standard_java_pattern, standard_python_multi_pattern, standard_python_single_pattern]
    #     for pattern in patterns:
    #         if re.findall(pattern, comment, re.DOTALL):
    #             return True 
    # else:
    #     return False
    if comment.startswith('#'):
        print("here in")
        return True
    elif comment.startswith('/*'):
        standard_java_pattern = r"/\*\*(.*?)\*/"
        if re.findall(standard_java_pattern,comment,re.DOTALL):
            return False
        else:
            print("here in")
            return True
    else:
        return False



def rule_p9(comment:str) ->bool:
    """
    Check if the comment is URL Link or reference.
    
    :param comment: source code comment to be inspected
    :returns: true if the comment contains URL.
    """
    # tokenized_comment = tokenize_text(comment).lower()
    # print(len(comment))
    # print(comment)
    # pattern = "^https?:\\/\\/(?:www\\.)?[-a-zA-Z0-9@:%._\\+~#=]{1,256}\\.[a-zA-Z0-9()]{1,6}\\b(?:[-a-zA-Z0-9()@:%_\\+.~#?&\\/=]*)$"
    protocol_pattern = r'\b((?:https?|ftp):\/\/[^\s/$.?#].[^\s]*)\b'
    # non_protocol_pattern = "[-a-zA-Z0-9@:%._\\+~#=]{1,256}\\.[a-zA-Z0-9()]{1,6}\\b(?:[-a-zA-Z0-9()@:%_\\+.~#?&\\/=]*)"
    comments = re.findall(protocol_pattern, comment, re.DOTALL)
    # print(comments)
    # comments.extend(re.findall(non_protocol_pattern, comment, re.DOTALL))
    # print(comments)
    
    if(len(comments) > 0):
        # print(comments)
        return True
    return False

def rule_p10(comment:str) ->bool:
    """
    Check if the comment is HTML Tags.
    
    :param comment: source code comment to be inspected
    :returns: true if the comment contains HTML Tags.
    """
    
    pattern = r"<[^>]+>"

    comments = re.findall(pattern, comment, re.DOTALL)

    # print(comments)
    
    if(len(comments) > 0):
        #print(comments)
        return True
    return False

def rule_p11(comment:str) ->bool:
    """
    Check if the comment is JavaDoc Tags.
    
    :param comment: source code comment to be inspected
    :returns: true if the comment contains JavaDoc Tags.
    """
    
    pattern = r"\{@link\s+([\w.#\s$]+)\}"
    tags = re.findall(pattern, comment, re.DOTALL)
    if(len(tags) > 0):
     
        return True
    return False


def rule_p12(comment:str) ->bool:
    """
    Check if the comment Interrogation.
    
    :param comment: source code comment to be inspected
    :returns: true if the comment contains Interrogation.
    """
    


    nlp = spacy.load("en_core_web_sm")

    python_comment = """
    This function calculates the sum of two numbers.
    What are the parameters of this function?
    How does this function handle errors?
    """

    doc = nlp(comment)

    question_sentences = [
        sentence.text.strip()
        for sentence in doc.sents
        if sentence.text.strip().endswith('?')
    ]

    # for question_sentence in question_sentences:
    #     print(question_sentence)
    if len(question_sentences)>0:
        return True
    return False
    
