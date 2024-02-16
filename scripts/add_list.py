
"""
Algo add_list:

a = [0b1010, 0b0000, 0b1011]
b = [0b1111, 0b1100, 0b0001]
c = [0b1001, 0b1101, 0b1100]

This algorithm read the array from left to right. For each element you only can store N bits.
First, we anticipate if the result of the addition will lead to a carry. If so, this bit will be add to the next operation.

"""

def check_carry(a: int, b: int, bits):
    c = 0

    for _ in range(bits):
        c = a&1 and b&1
        a >>= 1
        b >>= 1
    return c

def add_bin(a, b, c, mask):
    b += c
    while (b):
        a ^= b
        b = (((a^b) & b)<<1) & mask
    return a

def add_two_list(a: list, b: list):
    c = 0
    bits = 4
    mask = 0b1111
    result = []

    for i in range(max(len(a), len(b))):
        result.append(add_bin(a[i], b[i], c, mask))
        c = check_carry(a[i], b[i], bits)

    return result


if __name__ == "__main__":
    a = [0b1010, 0b0000, 0b1011]
    b = [0b1111, 0b1100, 0b0001]

    print (add_two_list(a, b))