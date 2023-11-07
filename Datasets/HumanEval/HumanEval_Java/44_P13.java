import java.io.*;
import java.lang.*;
import java.util.*;
import java.math.*;


class ChangeBase {
    /**
     * Change numerical base of input number x to base.
     * return string representation after the conversion.
     * base numbers are less than 10.
     * >>> change_base(8, 3)
     * '22'
     * >>> change_base(8, 2)
     * '1000'
     * >>> change_base(7, 2)
     * '111'
     * @param x an input integer
     * @param base an integer representing a numerical base
     * @return string representation after converting the numerical base of x to base
     *
     */
    public static String changeBase(int x, int base) {
