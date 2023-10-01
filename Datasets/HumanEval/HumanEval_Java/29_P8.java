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
     *
     */
    public static List<String> filterByPrefix(List<String> strings, String prefix) {
