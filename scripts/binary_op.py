from util import *
import random

# -------------  BINARY ADDITION -------------

#First version of this algo I've done
def add_bin_v1(a, b):
    res, ret= 0, -1

    while (ret != 0):
        res = a ^ b
        ret = (a&b)<<1
        a, b = res, ret
    return res


def add_bin_opti_v2(a, b):
    while (b):
        a ^= b
        b = ((a^b) & b)<<1
    return a


def add_bin_opti_v3(a, b):
    while (b):
        a ^= b
        b = (~a & b)<<1
    return a



# -------------  BINARY SUBSTRACTION  -------------

def sub_binary_v1(a, b):
    res, ret = 0, -1

    while (ret):
        res = a ^ b
        ret = ((a^b) & b) << 1
        a, b = res, ret
    return a

def sub_binary_v1_recur(a, b):
    if (b == 0): return a
    else:  return sub_binary_v1_recur(a ^b, ((a^b) & b) << 1)


def sub_binary_opti_v2(a, b):
    while (b):
        a = a ^ b
        b = (a & b) << 1
    return a


# -------------  BINARY MULTIPLICATION  -------------

def karatsuba_opti_v2(x, y):
    if x < 10 and y < 10:
        return x*y

    n = max(get_bit_length(x), get_bit_length(y))
    m = (n + 1) >> 1

    x_H = x >> m
    x_L = x & ((1 << m)-1)

    y_H = y >> m
    y_L = y & ((1 << m)-1)

    a = karatsuba_opti_v2(x_H, y_H)
    d = karatsuba_opti_v2(x_L, y_L)
    e = karatsuba_opti_v2((x_H + x_L), (y_H + y_L)) - a - d

    return (a << (m << 1)) + ((e << m) + d)


def mult_bin_opti_v1(a, b):
    res = 0
    while b:
        if b & 1:
            res += a
        a <<= 1
        b >>= 1

    return res


# -------------  BINARY EXPONENTIATION  -------------

def exp_bin(a, exp):
    res = 1

    while (exp > 0):
        if (exp&1):
            res = res*a
        a = a*a
        exp >>= 1
    return res


if __name__ == "__main__":
    a = random.randint(pow(2, 254), pow(2, 255))
    b = random.randint(pow(2, 128), pow(2, 129))

    print (a-b == add_bin_v1(a, b))
    print (a-b == add_bin_opti_v2(a, b))
    print (a-b == add_bin_opti_v3(a, b))

    print (a-b == sub_binary_v1(a, b))
    print (a-b == sub_binary_v1_recur(a, b))
    print (a-b == sub_binary_opti_v2(a, b))

    print (a*b == karatsuba_opti_v2(a, b))
    print (a*b == mult_bin_opti_v1(a, b))