# Prefix function. Knuth-Maurice-Pratt algorithm

## Prefix function

Function prefix value from string `s[0, ..., n-1]` is an array of natural numbers `π‎[0, ..., n-1]` where `π‎[i]` is defined as the maximum length of a native prefix that matches the suffix. The value of π [0] is naturally equal to 0, since a string of length 1 does not have its own prefix (its own prefix is ​​a prefix that does not match the entire string).

Consider the following case:

![example_1](https://i.imgur.com/s2tHaEX.png)

    π[0] is 0.
    π[1] = 0 as s[0] != s[1]
    π[2] = 1 as maximum native prefix of length 1 (s[0]) is the same as the suffix (s[2])
    π[3] = 2 as maximum native prefix of length 2 (s[0...1]) is the same as the suffix (s[2...3])
We can notice the following regularity that if the value at the previous step `s[i]` is not equal to `0`, then we can compare the next element `s[i+1]` with the next element of the prefix `p[j+1]` and if the values ​​are equal, then the next value of the array prefix function will be equal to `π[i+1] = π[i] + 1`. Otherwise, subtract one element from the prefix until `s[i+1]` equals `s[p]`, or p equals `0`.

Such algorithm will work in `O(n)`

## KMP algorithm

KMP algorithm is an algorithm for finding all occurrences of a prototype in the source text. The algorithm is based on a prefix function and runs in `O(prototype length + text length)`.

The idea behind the algorithm is that we can calculate the prefix function for the original string relative to the prototype. That is, we can glue the prototype with the original string and pass result to prefix function. Thus, when looping through a part of the original string, the algorithm will compare the characters (suffix) of the original string with the characters (prefix) of the prototype. 

As a result, array from prefix function will contain a part of the values ​​corresponding to the prototype length (these positions will be the ends of the prototype occurrences).

In order for us not to get values ​​in the array greater than the length of the prototype, we need to add a separator between the string and the prototype, which is not included in the alphabet. For example, `p + "#" + s`.

Consider finding prototype prototype `aab` in string `baabcabaabaabab`


![example_2](https://i.imgur.com/FmjqSum.png)

At the output of the prefix function, we will receive the lower array, and in order to find the initial positions of the prototype, we just have to loop through this array, starting from the 4th element (prototype length + separator), and compare its values ​​with the prototype length if the values ​​are equal , then this position is the end of the occurrence (to get the beginning, subtract the length of the prototype from this position).