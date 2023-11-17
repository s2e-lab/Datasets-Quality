from typing import List


def parse_music(music_string: str) -> List[int]:
    """ Input to this function is a string representing musical notes in a special ASCII format.
    Your task is to parse this string and return list of integers corresponding to how many beats does each
    not last.

    Here is a legend:
    'o' - whole note, lasts four beats
    'o|' - half note, lasts two beats
    '.|' - quarter note, lasts one beat

    args:
        music_string: string representing musical notes in a special ASCII format
    
    returns:
        list of integers corresponding to how many beats does each not last

    examples:
    >>> parse_music('o o| .| o| o| .| .| .| .| o o')
    [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
    >>> parse_music('o| o| o| .| o .| o|')
    [2, 2, 2, 1, 4, 1, 2]
    """
