import java.io.*;
import java.lang.*;
import java.util.*;
import java.math.*;


class TotalMatch {
    /**
     * * Write a function that accepts two lists of strings and returns the list that has 
     * total number of chars in the all strings of the list less than the other list.

     * if the two lists have the same number of chars, return the first list.

     * Examples
     * total_match([], []) ➞ []
     * total_match(['hi', 'admin'], ['hI', 'Hi']) ➞ ['hI', 'Hi']
     * total_match(['hi', 'admin'], ['hi', 'hi', 'admin', 'project']) ➞ ['hi', 'admin']
     * total_match(['hi', 'admin'], ['hI', 'hi', 'hi']) ➞ ['hI', 'hi', 'hi']
     * total_match(['4'], ['1', '2', '3', '4', '5']) ➞ ['4']
     *
     */
    public static List<String> totalMatch(List<String> lst1, List<String> lst2) {
