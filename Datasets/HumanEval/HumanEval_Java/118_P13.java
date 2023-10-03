import java.io.*;
import java.lang.*;
import java.util.*;
import java.math.*;


class GetClosestVowel {
    /**
     * You are given a word. Your task is to find the closest vowel that stands between 
     * two consonants from the right side of the word (case sensitive).
     * 
     * Vowels in the beginning and ending doesn't count. Return empty string if you didn't
     * find any vowel met the above condition. 

     * You may assume that the given string contains English letter only.

     * Example:
     * get_closest_vowel("yogurt") ==> "u"
     * get_closest_vowel("FULL") ==> "U"
     * get_closest_vowel("quick") ==> ""
     * get_closest_vowel("ab") ==> ""
     * @param word an input string
     * @return find the closest vowel that stands between two consonants from the right side of word 
     *
     */
    public static String getClosestVowel(String word) {
