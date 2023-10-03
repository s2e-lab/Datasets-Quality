import java.io.*;
import java.lang.*;
import java.util.*;
import java.math.*;


class DoAlgebra {
    /**
     * * Given two lists operator, and operand. The first list has basic algebra operations, and 
     * the second list is a list of integers. Use the two given lists to build the algebraic  
     * expression and return the evaluation of this expression.

     * The basic algebra operations:
     * Addition ( + ) 
     * Subtraction ( - ) 
     * Multiplication ( * ) 
     * Floor division ( // ) 
     * Exponentiation ( ** ) 

     * Example:
     * operator['+', '*', '-']
     * array = [2, 3, 4, 5]
     * result = 2 + 3 * 4 - 5
     * => result = 9
     * 
     * operator['-', '*']
     * array = [7, 3, 9]
     * result = 7 - 3 * 9
     * => result = -20
     * 
     * @param operator a list of basic algebra operations
     * @param operand a list of integers
     * @return the evaluation of this expression created by the two lists

     * Note:
     *     The length of operator list is equal to the length of operand list minus one.
     *     Operand is a list of of non-negative integers.
     *     Operator list has at least one operator, and operand list has at least two operands.

     *
     */
    public static int doAlgebra(List<String> operator, List<Integer> operand) {
