
def reverse_delete(s,c) -> tuple:
    """
    Task
    We are given two strings, s, and c, and you have to delete all the characters in s that are equal to any character in c
    then check if the result string is palindrome.
    A string is called a palindrome if it reads the same backward as forward.
    You should return a tuple containing the result string and True/False for the check.

    >>> reverse_delete("abcde", "ae")
    ('bcd', False)
    >>> reverse_delete("abcdef", "b")
    ('acdef', False)
    >>> reverse_delete("abcdedcba", "ab")
    ('cdedc', True)
    """
