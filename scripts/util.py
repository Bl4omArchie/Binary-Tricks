#Count the number of bits
def get_bit_length(num):
    length = 0
    while num:
        length += 1
        num >>= 1
    return length


#Count the number of bits equal to 1
def bit_count(a):
    compt=0
    while (a):
        compt += a&1
        a>>=1
    return compt
