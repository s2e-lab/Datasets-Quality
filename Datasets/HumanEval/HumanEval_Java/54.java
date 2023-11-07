import java.io.*;
import java.lang.*;
import java.util.*;
import java.math.*;


class SameChars {
    /**
     * * Check if two words have the same characters.
     * >>> same_chars('eabcdzzzz', 'dddzzzzzzzddeddabc')
     * True
     * >>> same_chars('abcd', 'dddddddabc')
     * True
     * >>> same_chars('dddddddabc', 'abcd')
     * True
     * >>> same_chars('eabcd', 'dddddddabc')
     * False
     * >>> same_chars('abcd', 'dddddddabce')
     * False
     * >>> same_chars('eabcdzzzz', 'dddzzzzzzzddddabc')
     * False
     *
     */
    public static Boolean sameChars(String s0, String s1) {
