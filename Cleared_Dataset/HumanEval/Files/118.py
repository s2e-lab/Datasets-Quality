
def get_closest_vowel(word) -> str:
    """
    You are given a word. Your task is to find the closest vowel that stands between 
    two consonants from the right side of the word (case sensitive).
 
    Vowels in the beginning and ending don't count. Return an empty string if you didn't
    ind any vowel that met the above condition. 
    You may assume that the given string contains English letters only.
    >>> get_closest_vowel("yogurt")
    'u'
    >>> get_closest_vowel("FULL")
    'U'
    >>> get_closest_vowel("quick")
    ''
    >>> get_closest_vowel("ab")
    ''
    """