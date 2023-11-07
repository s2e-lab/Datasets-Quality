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
     * @param strings a list of strings
     * @param substring a substring to search for in the given list of strings
     * @return a list of strings containing only those strings that have the given substring
     */
    public static List<String> filterBySubstring(List<String> strings, String substring) {
