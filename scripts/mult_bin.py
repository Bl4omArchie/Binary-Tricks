import random

def get_length(num):
    length = 0
    while num:
        length += 1
        num >>= 1
    return length

def karatsuba(x, y):
    if x < 10 and y < 10:
        return x*y

    n = max(get_length(x), get_length(y))
    m = (n + 1) >> 1

    x_H = x >> m
    x_L = x & ((1 << m)-1)

    y_H = y >> m
    y_L = y & ((1 << m)-1)

    a = karatsuba(x_H, y_H)
    d = karatsuba(x_L, y_L)
    e = karatsuba((x_H + x_L), (y_H + y_L)) - a - d

    return (a << (m << 1)) + ((e << m) + d)


def mult_bin(a, b):
    res = 0
    while b:
        if b & 1:
            res += a
        a <<= 1
        b >>= 1

    return res


if __name__ == "__main__":
    a = random.randint(pow(2, 1023), pow(2, 2024))
    b = random.randint(pow(2, 1023), pow(2, 1024))

    print (a*b == karatsuba(a, b))
    print (a*b == mult_bin(a, b))

    print (mult_bin(10, 5))