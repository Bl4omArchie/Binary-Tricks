#Most opti algo

def add_bin(a, b):
    while (b):
        a ^= b
        b = ((a^b) & b)<<1
    return a


def sub_binary(a, b):
    while (b):
        a = a ^ b
        b = (a & b) << 1
    return a


def mult_bin(a, b):
    res = 0
    while b:
        if b & 1:
            res += a
        a <<= 1
        b >>= 1

    return res