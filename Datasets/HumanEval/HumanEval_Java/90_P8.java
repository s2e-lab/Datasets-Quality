import java.io.*;
import java.lang.*;
import java.util.*;
import java.math.*;


class NextSmallest {
    /**
     * * You are given a list of integers.
     * Write a function next_smallest() that returns the 2nd smallest element of the list.
     * Return null if there is no such element.
     * 
     * next_smallest([1, 2, 3, 4, 5]) == 2
     * next_smallest([5, 1, 4, 3, 2]) == 2
     * next_smallest([]) == None
     * next_smallest([1, 1]) == None
     *
     */
    public static Integer nextSmallest(List<Integer> lst) {
