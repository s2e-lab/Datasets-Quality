import java.io.*;
import java.lang.*;
import java.util.*;
import java.math.*;


class StringXor {
    /**
     * Input are two strings a and b consisting only of 1s and 0s.
     * Perform binary XOR on these inputs and return result also as a string.
     * >>> string_xor('010', '110')
     * '100'
     * >>> string_xor('0001', '1100')
     * '1101'
     * @param a a string consisting only of 1s and 0s.
     * @param b a string consisting only of 1s and 0s.
     * @return the binary XOR of a and b
     */
    public static String stringXor(String a, String b) {
