import java.io.*;
import java.lang.*;
import java.util.*;
import java.math.*;


class FilterBySubstring {
    /**
     * Filter an input list of strings only for ones that contain given substring
     * >>> filter_by_substring([], 'a')
     * []
     * >>> filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a')
     * ['abc', 'bacd', 'array']
     *
     */
    public static List<Object> filterBySubstring(List<Object> strings, String substring) {
