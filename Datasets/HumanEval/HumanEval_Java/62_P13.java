import java.io.*;
import java.lang.*;
import java.util.*;
import java.math.*;


class Derivative {
    /**
     * xs represent coefficients of a polynomial.
     * xs[0] + xs[1] * x + xs[2] * x^2 + ....
     *  Return derivative of this polynomial in the same form.
     * >>> derivative([3, 1, 2, 4, 5])
     * [1, 4, 12, 20]
     * >>> derivative([1, 2, 3])
     * [2, 6]
     * @param xs a list of integers representing coefficients of a polynomial
     * @return a list with derivatives of the polynomial.
     */
    public static List<Object> derivative(List<Integer> xs) {
