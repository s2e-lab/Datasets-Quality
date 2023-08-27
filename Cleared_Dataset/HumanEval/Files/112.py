
def reverse_delete(s,c):
    """
    Task
    We are given two strings, s, and c, and you have to delete all the characters in s that are equal to any character in c
    then check if the result string is palindrome.
    A string is called a palindrome if it reads the same backward as forward.
    You should return a tuple containing the result string and True/False for the check.
    Example
    For s = "abcde", c = "ae", the result should be ('bcd',False)
    For s = "abcdef", c = "b"  the result should be ('acdef',False)
    For s = "abcdedcba", c = "ab", the result should be ('cdedc',True)
    """
