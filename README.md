# Dimensional analysis

Dimensional analysis is the method of deriving possible equations by analyzing the units of the relevant variables and combining them for the desired output.

## SI-Units

The international system of units measures 7 units from which all other units can be constructed.

Quantity | Unit | Index in vector
---------|------|----------------
Time     | s    | 0
Distance | m    | 1
Mass     | kg   | 2
Current  | A    | 3
Heat     | K    | 4
Amount   | mol  | 5
Luminousity | cd | 6

By ordering this list and interpreting the powers on each unit as a vector in 7-dimensional Unit-Space we can calculate the powers of each variable.

## Dimensional Analysis using Linear Algebra

Once the vectors and the target point are defined a base of the vector space is constructed.

> The vector space is 7 dimensional. If n vectors are supplied 7-n linearly independent vectors have to be constructed from the supplied variables to form a complete base.

Writing the base as a Matrix `B` and the target as the vector `t` we can calculate the coordinates `a` in the base `B`

![B*a = t -> B^(-1) t = a](https://latex.codecogs.com/gif.latex?B\cdot%20\vec%20a%20=%20\vec%20t%20\implies%20\vec%20a%20=%20B^{-1}\cdot%20\vec%20t)
