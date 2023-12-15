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


if __name__ == "__main__":
    a = 0b11000101101110011100
    b = 0b10111010101100101110

    start = time.time()
    mine_bit_count(a)
    print (f"{(time.time()-start):.10f}")

    start = time.time()
    a.bit_count()
    print (f"{(time.time()-start):.10f}")