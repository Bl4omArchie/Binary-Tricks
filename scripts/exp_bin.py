import random

def exp_bin(a, exp):
    res = 1

    while (exp > 0):
        if (exp&1):
            res = res*a
        a = a*a
        exp >>= 1
    return res


if __name__ == "__main__":
    a = random.randint(pow(2, 1023), pow(2, 1024))
    b = 65537
    m = random.randint(pow(2, 1023), pow(2, 1024))

    print (exp_bin(2, 3))