import java.io.*;
import java.lang.*;
import java.util.*;
import java.math.*;


class RescaleToUnit {
    /**
     * Given list of numbers (of at least two elements), apply a linear transform to that list,
     * such that the smallest number will become 0 and the largest will become 1
     * >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
     * [0.0, 0.25, 0.5, 0.75, 1.0]
     * @param numbers a list of floating point numbers
     * @return the list after applying a linear transform
     * such that the smallest number will become 0 and the largest will become 1
     *
     */
    public static List<Double> rescaleToUnit(List<Double> numbers) {
