
def check_dict_case(dict) -> bool:
    """
    Given a dictionary, return True if all keys are strings in lower 
    case or all keys are strings in upper case; else, return False.
    The function should return False if the given dictionary is empty.

    >>> check_dict_case({"a":"apple", "b":"banana"})
    True
    >>> check_dict_case({"a":"apple", "A":"banana", "B":"banana"})
    False
    >>> check_dict_case({"a":"apple", 8:"banana", "a":"apple"})
    False
    >>> check_dict_case({"Name":"John", "Age":"36", "City":"Houston"})
    False
    >>> check_dict_case({"STATE":"NC", "ZIP":"12345" })
    True
    """