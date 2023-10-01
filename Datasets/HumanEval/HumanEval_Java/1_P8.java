import java.io.*;
import java.lang.*;
import java.util.*;
import java.math.*;


class SeparateParenGroups {
    /**
     * Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
     * separate those group into separate strings and return the list of those.
     * Separate groups are balanced (each open brace is properly closed) and not nested within each other
     * Ignore any spaces in the input string.
     * >>> separate_paren_groups('( ) (( )) (( )( ))')
     * ['()', '(())', '(()())']
     * >>> separate_paren_groups('(( )) ((( )( )))')
     * ['(())', '((()()))']
     *
     */
    public static List<String> separateParenGroups(String parenString) {
