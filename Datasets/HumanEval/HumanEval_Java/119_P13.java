import java.io.*;
import java.lang.*;
import java.util.*;
import java.math.*;


class MatchParens {
    /**
     * * You are given a list of two strings, both strings consist of open
     * parentheses '(' or close parentheses ')' only.
     * Your job is to check if it is possible to concatenate the two strings in
     * some order, that the resulting string will be good.
     * A string S is considered to be good if and only if all parentheses in S
     * are balanced. For example: the string '(())()' is good, while the string
     * '())' is not.
     * Return 'Yes' if there's a way to make a good string, and return 'No' otherwise.

     * Examples:
     * match_parens(['()(', ')']) == 'Yes'
     * match_parens([')', ')']) == 'No'
     * @param lst list of two strings, both strings consist of open parentheses '(' or close parentheses ')' only
     * @return 'Yes' if it is possible to concatenate the two strings of lst in some order, that the resulting string will be good,
     * 'No' otherwise.
     */
    public static String matchParens(List<String> lst) {
