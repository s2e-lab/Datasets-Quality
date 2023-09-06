from typing import List

def parse_music(music_string: str) -> List[int]:
    """ 
    Input to this function is a string representing musical notes in a special ASCII format.
    Your task is to parse this string and return a list of integers corresponding to how many beats each does
    not last.
    Here is a legend:
    'o' - whole note, lasts four beats
    'o|' - half note, lasts two beats
    '.|' - quarter note, lasts one beat
    >>> parse_music('o o| .| o| o| .| .| .| .| o o')
    [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
    >>> parse_music('o o| .| o| o| .| .| .| .| o o | .')
    [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4, 1]
    """
