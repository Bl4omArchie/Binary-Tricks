# Binary Tricks 


## Binary matrice
For this first binary trick, I'm trying to implement matrice operation only with numbers in base 2. 
### Introduction
The point of this implementation is to represent the matrix into a single value which is a large base2 number.
This is the struct that represent my matrix: 
```c
struct BinaryMatrice {
    int value;
    int bit_size;
    int column;
    int row;
};
```
The **value** contains the rows and columns from MSB to LSB:
```
M = 01  10  10  11
    01  11  00  10 

value_M  = 0110101101110010
```
The **bit_size** represent the numbers of bits you have for each numbers. With the below example, bit_size = 2.

Finally, **row** and **column** are the dimension of the matrix.

### Operations

To perform operations, I have to find mask to extract specific bits from my value. 
Let's add the matrice a and b together onto the c matrix:
```c
struct BinaryMatrice a = {.value=0b0110101101110010, .bit_size=2, .row=2, .column=4};
struct BinaryMatrice b = {.value=0b1110110111000011, .bit_size=2, .row=2, .column=4};
struct BinaryMatrice c = {};
```****