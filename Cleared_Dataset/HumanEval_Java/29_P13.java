import java.io.*;
import java.lang.*;
import java.util.*;
import java.math.*;


class FilterByPrefix {
    /**
     * Filter an input list of strings only for ones that start with a given prefix.
     * >>> filter_by_prefix([], 'a')
     * []
     * >>> filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a')
     * ['abc', 'array']
     * @param strings an input list of strings
     * @param prefix a given prefix
     * @return the input list filtered for ones that start with the given prefix.
     */
    public static List<Object> filterByPrefix(List<Object> strings, String prefix) {
