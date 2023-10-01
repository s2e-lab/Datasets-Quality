import java.io.*;
import java.lang.*;
import java.util.*;
import java.math.*;


class FindClosestElements {
    /**
     * From a supplied list of numbers (of length at least two) select and return two that are the closest to each
     * other and return them in order (smaller number, larger number).
     * >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
     * (2.0, 2.2)
     * >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
     * (2.0, 2.0)
     *
     */
    public static List<Double> findClosestElements(List<Double> numbers) {
