import java.io.*;
import java.lang.*;
import java.util.*;
import java.math.*;


class HowManyTimes {
    /**
     * Find how many times a given substring can be found in the original string. Count overlaping cases.
     * >>> how_many_times('', 'a')
     * 0
     * >>> how_many_times('aaa', 'a')
     * 3
     * >>> how_many_times('aaaa', 'aa')
     * 3
     * @param string an input string
     * @param substring a substring to search for in the given string
     * @return the number of times the substring can be found in the input string
     */
    public static int howManyTimes(String string, String substring) {
