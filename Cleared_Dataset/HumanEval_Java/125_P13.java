import java.io.*;
import java.lang.*;
import java.util.*;
import java.math.*;


class SplitWords {
    /**
     * * Given a string of words, return a list of words split on whitespace, if no whitespaces exists in the text you
     * should split on commas ',' if no commas exists you should return the number of lower-case letters with odd order in the
     * alphabet, ord('a') = 0, ord('b') = 1, ... ord('z') = 25
     * Examples
     * split_words("Hello world!") ➞ ["Hello", "world!"]
     * split_words("Hello,world!") ➞ ["Hello", "world!"]
     * split_words("abcdef") == 3 
     * @param txt a string of words
     * @return a list of words by splitting txt on whitespace.
     * If no whitespace exists, return a list of words by splitting txt on commas ','.
     * If no comma exists, return the number of lower-case letters in txt with odd order in the alphabet.
     */
    public static Object splitWords(String txt) {
