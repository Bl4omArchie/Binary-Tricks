"""
Algo add_list:

a = [0b1010, 0b0000, 0b1011]
b = [0b1111, 0b1100, 0b0001]
c = [0b1001, 0b1101, 0b1100]

This algorithm read the array from left to right. For each element you only can store N bits.
First, we anticipate if the result of the addition will lead to a carry. If so, this bit will be add to the next operation.

"""

def check_carry(a: int, b: int, BIT_PER_ELEMENT):
    c = 0

    for _ in range(BIT_PER_ELEMENT):
        c = (a & 1) + (b & 1) + c
        c >>= 1
        a >>= 1
        b >>= 1
    return c


def add_bin(a, b, c, mask):
    b += c
    while (b):
        a ^= b
        b = (((a^b) & b)<<1) & mask
    return a


def add_two_list(a: list, b: list, BIT_PER_ELEMENT):
    c = 0
    mask = 0b1111
    result = []

    for i in range(max(len(a), len(b))):
        result.append(add_bin(a[i], b[i], c, mask))
        c = check_carry(a[i], b[i], BIT_PER_ELEMENT)

    return result


def print_real_size(a: list, BIT_PER_ELEMENT):
    i = len(a)-1
    print ("0b", end="")

    while i != -1:
        print (str(bin(a[i]).replace("0b", "")), end="")
        i -= 1


if __name__ == "__main__":
    BIT_PER_ELEMENT = 4

    a = [0b1010, 0b0100, 0b1011]
    b = [0b1111, 0b1100, 0b0001]

    real_size_a = 0b101101001010
    real_size_b = 0b000111001111

    print (bin(real_size_a+real_size_b))
    c = add_two_list(a, b, BIT_PER_ELEMENT)
    print_real_size(c, BIT_PER_ELEMENT)