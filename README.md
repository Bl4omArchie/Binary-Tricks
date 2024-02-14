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

# Binary operators

- logical AND

Truth table:
  
|p |q |R |
|--|-- |--|
| 0| 0| 0|
| 0| 1| 0|
| 1| 0| 0|
| 1| 1| 1|

Representation:
  
| field        | symbol |  
|:--:          | :--:   |
|matematic     | ^      |
|programmation | &      |
|grammar       | and    |
|probabilities | ∩      |

<br/>

- logical OR

Truth table:
  
|p |q |R |
|--|-- |--|
| 0| 0| 0|
| 0| 1| 1|
| 1| 0| 1|
| 1| 1| 1|

Representation:

| field        | symbol |  
|:--:          | :--:   |
|matematic     | <      |
|programmation |  &#124;|
|grammar       | or     |
|probabilities | ∪      |

<br/>

- XOR

Truth table:
  
|p |q |R |
|--|-- |--|
| 0| 0| 0|
| 0| 1| 1|
| 1| 0| 1|
| 1| 1| 0|


Representation

| field        | symbol |  
|:--:          | :--:   |
|matematic     | &oplus |
|programmation | ^      |
|grammar       | exclusif or    |