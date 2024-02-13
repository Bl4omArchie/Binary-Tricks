import time

def mine_bit_length(a):
    compt=0
    while (a>0):
        compt += 1
        a>>=1
    return compt

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


def define_bit(num, n, x):
    #define the x bits to 0 or 1
    #ex: 0b1010 -> 0b1010 | (1 << 2) = 0b1110
    return num | (x << n-1)


def concatenation(a, b):
    #Concaténer le nombre binaire b avec a
    #ex: 0b1010 et 0b1111 donne 0b11111010
    return a | (b << 4)


"""
#Effacement du 5e bit (le met à 0)
n = 0b11011 & ~(1 << 4);  

#Inversion du 2e bit
n = 0b1111 ^ (1 << 1);
"""


if __name__ == "__main__":
    a = 0b11000101101110011100
    b = 0b10111010101100101110

    start = time.time()
    mine_bit_count(a)
    print (f"{(time.time()-start):.10f}")

    start = time.time()
    a.bit_count()
    print (f"{(time.time()-start):.10f}")