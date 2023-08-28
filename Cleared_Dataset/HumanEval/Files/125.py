
def split_words(txt) -> list:
    """
    Given a string of words, return a list of words split on whitespace; if no whitespaces exist in the text, you
    should split on commas ',' if no commas exist, you should return the number of lower-case letters with odd order in the
    alphabet, ord('a') = 0, ord('b') = 1, ... ord('z') = 25    

    >>> split_words("Hello world!")
    ['Hello', 'world!']
    >>> split_words("Hello,world!")
    ['Hello', 'world!']
    >>> split_words("abcdef")
    3
    """
