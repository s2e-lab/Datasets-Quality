import java.io.*;
import java.lang.*;
import java.util.*;
import java.math.*;


class CheckIfLastCharIsALetter {
    /**
     * * Create a function that returns True if the last character
     * of a given string is an alphabetical character and is not
     * a part of a word, and False otherwise.
     * Note: "word" is a group of characters separated by space.

     * Examples:
     * check_if_last_char_is_a_letter("apple pie") ➞ False
     * check_if_last_char_is_a_letter("apple pi e") ➞ True
     * check_if_last_char_is_a_letter("apple pi e ") ➞ False
     * check_if_last_char_is_a_letter("") ➞ False 
     * @param txt an input string
     * @return true if the last character of txt is an alphabetical character and is not
     * a part of a word, false otherwise
     *
     */
    public static Boolean checkIfLastCharIsALetter(String txt) {
