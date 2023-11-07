import java.io.*;
import java.lang.*;
import java.util.*;
import java.math.*;


class ParseNestedParens {
    /**
     * Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
     * For each of the group, output the deepest level of nesting of parentheses.
     * E.g. (()()) has maximum two levels of nesting while ((())) has three.

     * >>> parse_nested_parens('(()()) ((())) () ((())()())')
     * [2, 3, 1, 3]
     * >>> parse_nested_parens('(()()) (((())))')
     * [2, 4]
     *
     */
    public static List<Integer> parseNestedParens(String parenString) {
