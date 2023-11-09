import java.io.*;
import java.lang.*;
import java.util.*;
import java.math.*;


class RollingMax {
    /**
     * From a given list of integers, generate a list of rolling maximum element found until given moment
     * in the sequence.
     * >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
     * [1, 2, 3, 3, 3, 4, 4]
     * @param numbers a list of integers
     * @return a list of rolling maximum element found until given moment
     * in the input sequence.
     */
    public static List<Object> rollingMax(List<Object> numbers) {
