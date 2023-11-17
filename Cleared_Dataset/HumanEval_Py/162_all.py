
def string_to_md5(text: str) -> str:
    """
    Given a string 'text', return its md5 hash equivalent string.
    If 'text' is an empty string, return None.

    args:
        text: string
    
    returns:
        md5 hash equivalent string of 'text'

    examples:
    >>> string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
    >>> string_to_md5('test string') == '6f8db599de986fab7a21625b7916589c'
    """
