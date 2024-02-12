def add_bin_opti(a, b):
    while (b):
        a ^= b
        b = (~a & b)<<1
    return a

def add_bin_2(a, b):
    while (b):
        a ^= b
        b = ((a^b) & b)<<1
    return a

#First version of this algo I've done
def add_bin_3(a, b):
    ret=-1

    while (ret != 0):
        res = a ^ b
        ret = (a&b)<<1
        a, b = res, ret
    return res