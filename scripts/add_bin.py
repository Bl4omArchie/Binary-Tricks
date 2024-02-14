import random



def add_bin_opti_1(a, b):
    while (b):
        a ^= b
        b = ((a^b) & b)<<1
    return a


def add_bin_opti_2(a, b):
    while (b):
        a ^= b
        b = (~a & b)<<1
    return a

#First version of this algo I've done
def add_bin_3(a, b):
    res, ret= 0, -1

    while (ret != 0):
        res = a ^ b
        ret = (a&b)<<1
        a, b = res, ret
    return res


if __name__ == "__main__":
    a = random.randint(pow(2, 254), pow(2, 255))
    b = random.randint(pow(2, 128), pow(2, 129))

    print (a-b == add_bin_opti_1(a, b))
    print (a-b == add_bin_opti_2(a, b))
    print (a-b == add_bin_3(a, b))