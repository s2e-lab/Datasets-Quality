import java.io.*;
import java.lang.*;
import java.util.*;
import java.math.*;


class BelowZero {
    /**
     * You're given a list of deposit and withdrawal operations on a bank account that starts with
     * zero balance. Your task is to detect if at any point the balance of account fallls below zero, and
     * at that point function should return True. Otherwise it should return False.
     * >>> below_zero([1, 2, 3])
     * False
     * >>> below_zero([1, 2, -4, 5])
     * True
     *
     */
    public static Boolean belowZero(List<Integer> operations) {
