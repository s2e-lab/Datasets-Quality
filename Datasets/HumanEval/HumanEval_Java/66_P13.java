import java.io.*;
import java.lang.*;
import java.util.*;
import java.math.*;


class Digitsum {
    /**
     * Task
     * Write a function that takes a string as input and returns the sum of the upper characters only'
     * ASCII codes.

     * Examples:
     *     digitSum("") => 0
     *     digitSum("abAB") => 131
     *     digitSum("abcCd") => 67
     *     digitSum("helloE") => 69
     *     digitSum("woArBld") => 131
     *     digitSum("aAaaaXa") => 153
     * 
     * @param s an input string
     * @return the sum of the upper characters only of s
     *
     */
    public static int digitsum(String s) {
