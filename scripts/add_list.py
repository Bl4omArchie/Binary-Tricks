
"""
Algo add_list:

a = [0b1010, 0b0000, 0b1011]
b = [0b1111, 0b1100, 0b0001]
c = [0b1001, 0b1101, 0b1100]

This algorithm read the array from left to right. For each element you only can store N bits.
First, we anticipate if the result of the addition will lead to a carry. If so, this bit will be add to the next operation.

"""

def add_bin(a, b, c):
    b += c
    while (b):
        a ^= b
        b = ((a^b) & b)<<1
    return a

def add_two_list(a: list, b: list):
    i = 0
    result = []

    while (a | b):
        c = check_carry(a[0], b[0])
        result.append(add_bin(a[0], b[0], c))

        i += 1


def check_carry(a: int, b: int):
    pass 

if __name__ == "__main__":
    a = [0b1010, 0b0000, 0b1011]
    b = [0b1111, 0b1100, 0b0001]

    add_two_list(a, b)