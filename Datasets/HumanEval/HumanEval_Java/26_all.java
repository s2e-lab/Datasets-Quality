import java.io.*;
import java.lang.*;
import java.util.*;
import java.math.*;


class RemoveDuplicates {
    /**
     * From a list of integers, remove all elements that occur more than once.
     * Keep order of elements left the same as in the input.
     * >>> remove_duplicates([1, 2, 3, 2, 4])
     * [1, 3, 4]
     * >>> remove_duplicates([1, 1,1, 2, 2, 4])
     * [4]
     * @param numbers a list of integers
     * @return the input list without the elements that occur more than once
     */
    public static List<Integer> removeDuplicates(List<Integer> numbers) {
