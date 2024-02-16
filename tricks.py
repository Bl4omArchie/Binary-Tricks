import time

#Count the number of bits
def mine_bit_length(a):
    compt=0
    while (a>0):
        compt += 1
        a>>=1
    return compt

#Count the number of bits equal to 1
def mine_bit_count(a):
    compt=0
    while (a>0):
        compt += a&1
        a>>=1
    return compt


def power_of_2(exp):
    return 1 << exp

def divide_by_power_of_2(num, exp):
    return num >> exp

def modulo_power_of_2(num, exp):
    return num & (power_of_2(exp) - 1)

def concatenation(a, b):
    #Concaténer le nombre binaire b avec a
    #ex: 0b1010 et 0b1111 donne 0b11111010
    return a | (b << 4)


def define_bit(n, x):
    # sets the x-th bit in the number n
    #ex: 0b1010 -> 0b1010 | (1 << 2) = 0b1110
    return n | (1 << x)

def flips_bit(n, x):
    #flips the x-th bit in the number n
    return n ^ (1 << x)

def erase_bit(n, x):
    # erase the x-th bit of the binary number n
    return n & ~(1 << x)


if __name__ == "__main__":
    a = 0b11000101101110011100
    b = 0b10111010101100101110

    start = time.time()
    mine_bit_count(a)
    print (f"{(time.time()-start):.10f}")

    start = time.time()
    a.bit_count()
    print (f"{(time.time()-start):.10f}")