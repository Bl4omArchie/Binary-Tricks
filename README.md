# Binary operators

Bitwise operators

**&**: The bitwise AND operator compares each bit of its first operand with the corresponding bit of its second operand. If both bits are 1, the corresponding result bit is set to 1. Otherwise, the corresponding result bit is set to 0.


**|**: The bitwise inclusive OR operator compares each bit of its first operand with the corresponding bit of its second operand. If one of the two bits is 1, the corresponding result bit is set to 1. Otherwise, the corresponding result bit is set to 0.


**^**: The bitwise exclusive OR (XOR) operator compares each bit of its first operand with the corresponding bit of its second operand. If one bit is 0 and the other bit is 1, the corresponding result bit is set to 1. Otherwise, the corresponding result bit is set to 0.

 
**~**: The bitwise complement (NOT) operator flips each bit of a number, if a bit is set the operator will clear it, if it is cleared the operator sets it.

**>>**: Shifts a number to the right by removing the last few binary digits of the number. Each shift by one represents an integer division by 2, so a right shift by  $k$  represents an integer division by  $2^k$ .

**<<**: Shifts a number to left by appending zero digits. In similar fashion to a right shift by  $k$ , a left shift by  $k$  represents a multiplication by  $2^k$ .


# Bit manipulation
- Defining a bit: To define a bit at a given position (set it to 1), use the bitwise OR operation ( | ) with an appropriate mask: ```n = n | (1 << position)```.
<br/>

- Erase a bit: To erase a bit at a given position (set to 0), use the AND bitwise operation (&) with the addition of the mask: ```n = n & ~(1 << position)```.
<br/>

- Invert a bit: To invert (toggle) a bit at a given position, use the bitwise XOR operation ( ) with a mask: ```n = n   (1 << position)```.
<br/>

- Extract a bit: To extract the value of a bit at a given position, use the AND bitwise operation with a mask and test if the result is different from zero: ```(n & (1 << position)) != 0```.
<br/>

- Bit rotation: To perform a bit rotation (circular offset), use the offset operations (<< or >>) with the appropriate logical operations.
<br/>

- Detect defined bits: Use AND operations and masks to detect if a specific set of bits is defined: ```(n & mask) == mask```.

- Create masks: Use bitwise operations to create masks that allow you to select, define, or clear specific bits.

# Sources
[Bit manipulation, cp-algorithm](https://cp-algorithms.com/algebra/bit-manipulation.html)