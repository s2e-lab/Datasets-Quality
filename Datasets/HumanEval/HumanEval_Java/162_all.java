import java.io.*;
import java.lang.*;
import java.util.*;
import java.math.*;


class StringToMd5 {
    /**
     * * Given a string 'text', return its md5 hash equivalent string.
     * If 'text' is an empty string, return null.

     * >>> string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
     * >>> string_to_md5('test string') == '6f8db599de986fab7a21625b7916589c'
     * 
     * @param text a given string 
     * @return the md5 hash equivalent string of the given string
     */
    public static String stringToMd5(String text) {
