import java.io.*;
import java.lang.*;
import java.util.*;
import java.math.*;


class IsBored {
    /**
     * * You'll be given a string of words, and your task is to count the number
     * of boredoms. A boredom is a sentence that starts with the word "I".
     * Sentences are delimited by '.', '?' or '!'.
   
     * For example:
     * >>> is_bored("Hello world")
     * 0
     * >>> is_bored("The sky is blue. The sun is shining. I love this weather")
     * 1
     * @param s an input string
     * @return the count of boredoms
     */
    public static int isBored(String s) {
