import java.io.*;
import java.lang.*;
import java.util.*;
import java.math.*;


class Bf {
    /**
     * * There are eight planets in our solar system: the closerst to the Sun 
     * is Mercury, the next one is Venus, then Earth, Mars, Jupiter, Saturn, 
     * Uranus, Neptune.
     * Write a function that takes two planet names as strings planet1 and planet2. 
     * The function should return a tuple containing all planets whose orbits are 
     * located between the orbit of planet1 and the orbit of planet2, sorted by 
     * the proximity to the sun. 
     * The function should return an empty tuple if planet1 or planet2
     * are not correct planet names. 
     * Examples
     * bf("Jupiter", "Neptune") ==> ("Saturn", "Uranus")
     * bf("Earth", "Mercury") ==> ("Venus")
     * bf("Mercury", "Uranus") ==> ("Venus", "Earth", "Mars", "Jupiter", "Saturn")
     *
     */
    public static List<String> bf(String planet1, String planet2) {
