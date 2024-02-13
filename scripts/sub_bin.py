import random


def sub_binary_1(a, b):
    res, ret = 0, -1

    while (ret):
        res = a ^ b
        ret = ((a^b) & b) << 1
        a, b = res, ret
    return a

def sub_binary_1_recur(a, b):
    if (b == 0): return a
    else:  return sub_binary_1_recur(a ^b, ((a^b) & b) << 1)


def sub_binary_2(a, b):
    while (b):
        a = a ^ b
        b = (a & b) << 1
    return a


if __name__ == "__main__":
    a = random.randint(pow(2, 254), pow(2, 255))
    b = random.randint(pow(2, 128), pow(2, 129))

    print (a-b == sub_binary_1(a, b))
    print (a-b == sub_binary_1_recur(a, b))
    print (a-b == sub_binary_2(a, b))