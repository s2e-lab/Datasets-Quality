import java.io.*;
import java.lang.*;
import java.util.*;
import java.math.*;


class FixSpaces {
    /**
     * * Given a string text, replace all spaces in it with underscores, 
     * and if a string has more than 2 consecutive spaces, 
     * then replace all consecutive spaces with - 
     * 
     * fix_spaces("Example") == "Example"
     * fix_spaces("Example 1") == "Example_1"
     * fix_spaces(" Example 2") == "_Example_2"
     * fix_spaces(" Example   3") == "_Example-3"
     * @param text an input string
     * @return a string formed after replacing all spaces in text with underscores, 
     * and if text has more than 2 consecutive spaces,then after replacing all consecutive spaces with - 
     *
     */
    public static String fixSpaces(String text) {
