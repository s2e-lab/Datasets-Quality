import java.io.*;
import java.lang.*;
import java.util.*;
import java.math.*;


class AllPrefixes {
    /**
     * Return list of all prefixes from shortest to longest of the input string
     * >>> all_prefixes('abc')
     * ['a', 'ab', 'abc']
     * >>> all_prefixes('abcd')
     * ['a', 'ab', 'abc','abcd']
     */
    public static List<String> allPrefixes(String string) {
