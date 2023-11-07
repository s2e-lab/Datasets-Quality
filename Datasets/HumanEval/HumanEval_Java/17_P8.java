import java.io.*;
import java.lang.*;
import java.util.*;
import java.math.*;


class ParseMusic {
    /**
     * Input to this function is a string representing musical notes in a special ASCII format.
     * Your task is to parse this string and return list of integers corresponding to how many beats does each
     * not last.

     * Here is a legend:
     * 'o' - whole note, lasts four beats
     * 'o|' - half note, lasts two beats
     * '.|' - quater note, lasts one beat

     * >>> parse_music('o o| .| o| o| .| .| .| .| o o')
     * [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
     * >>> parse_music('o o| .| o')
     * [4, 2, 1, 4]

     */
    public static List<Integer> parseMusic(String musicString) {
