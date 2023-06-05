import language_tool_python as lt
import tokenize          
import re

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
    """
    Check if the comment contains a grammar mistake.
    
    :param comment: source code comment to be inspected
    :returns: true if a grammar issue was found.
    """
    tokenized_comment = tokenize_text(comment)
    # checks the tokenized version
    matches = LANG_TOOL.check(tokenized_comment)
    if (len(matches)>0): print(matches)
    return len(matches) > 0


# def rule_p2()
# def rule_p3()
# def rule_p4()
# def rule_p5()
# def rule_p6()
    