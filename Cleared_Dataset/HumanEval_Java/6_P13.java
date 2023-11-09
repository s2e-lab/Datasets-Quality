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
     * @param parenString a string represented by multiple groups for nested parentheses separated by spaces.
     * @return a list of integers where each integer denotes the deepest level of nesting of parentheses of each group in the input
     *
     *
     */
    public static List<Integer> parseNestedParens(String parenString) {
