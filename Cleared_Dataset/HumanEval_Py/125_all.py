from typing import List

def split_words(txt: str) -> List[str]:
    """
    Given a string of words, return a list of words split on whitespace, if no whitespaces exists in the text you
    should split on commas ',' if no commas exist you should return the number of lower-case letters with odd order in the
    alphabet, ord('a') = 0, ord('b') = 1, ... ord('z') = 25
    
    args:
        txt: string of words

    returns:
        list of words split on whitespace, if no whitespaces exists in the text you
        should split on commas ',' if no commas exists you should return the number of lower-case letters with odd order in the
        alphabet, ord('a') = 0, ord('b') = 1, ... ord('z') = 25

    examples:
    split_words("Hello world!") ➞ ["Hello", "world!"]
    split_words("Hello,world!") ➞ ["Hello", "world!"]
    split_words("abcdef") == 3 
    """
