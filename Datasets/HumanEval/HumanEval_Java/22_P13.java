import java.io.*;
import java.lang.*;
import java.util.*;
import java.math.*;


class FilterIntegers {
    /**
     * Filter given list of any Java values only for integers
     * >>> filter_integers(['a', 3.14, 5])
     * [5]
     * >>> filter_integers([1, 2, 3, 'abc', {}, []])
     * [1, 2, 3]
     * @param values a list any Java values
     * @return the list fitered for only integers
     *
     */
    public static List<Object> filterIntegers(List<Object> values) {
