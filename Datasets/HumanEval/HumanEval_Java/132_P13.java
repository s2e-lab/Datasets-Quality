import java.io.*;
import java.lang.*;
import java.util.*;
import java.math.*;


class IsNested {
    /**
     * * Create a function that takes a string as input which contains only square brackets.
     * The function should return True if and only if there is a valid subsequence of brackets 
     * where at least one bracket in the subsequence is nested.

     * is_nested('[[]]') ➞ True
     * is_nested('[]]]]]]][[[[[]') ➞ False
     * is_nested('[][]') ➞ False
     * is_nested('[]') ➞ False
     * is_nested('[[][]]') ➞ True
     * is_nested('[[]][[') ➞ True
     * @param string an input string which contains only square brackets
     * @return true if and only if there is a valid subsequence of brackets in string
     * where at least one bracket in the subsequence is nested, false otherwise

     *
     */
    public static Boolean isNested(String string) {
