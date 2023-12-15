import time

def add_bin(a, b):
    ret = -1
    while ret != 0:
        res = a^b
        ret = (a&b) << 1
        a, b = res, ret
    return res

def add_bin_recur(a, b):
    res = a^b
    ret = (a&b) << 1

    if ret == 0:
        return res
    else:
        return add_bin_recur(res, ret)
    
def add_bin_gpt(a, b):
    result = 0
    carry = 0
    shift = 0

    while a > 0 or b > 0 or carry > 0:
        bit_a = a & 1
        bit_b = b & 1
        sum_bits = bit_a ^ bit_b ^ carry
        result |= (sum_bits << shift)
        carry = (bit_a & bit_b) | ((bit_a ^ bit_b) & carry)
        a >>= 1
        b >>= 1
        shift += 1

    return result

def mult_bin(a, b):
    res = a
    for _ in range(b):
        res = add_bin(res, res)
    return res

def mult_bin_gpt(a, b):
    result = 0
    shift = 0

    while b > 0:
        if b & 1:
            result += (a << shift)
        a <<= 1
        b >>= 1
        shift += 1

    return result

def div_bin_gpt(a, b):
    q = 0
    r = 0

    for i in range(a.bit_length(), -1, -1):
        r = (r << 1) | ((a >> i) & 1)

        if r >= b:
            r -= b
            q |= (1 << i)  

    return q, r




if __name__ == "__main__":
    a = 0b11000101101110011100
    b = 0b10111010101100101110
    

    start = time.time()
    a.__add__(a)
    print (f"{(time.time()-start):.10f}")

    start = time.time()
    add_bin(a, b)
    print (f"{(time.time()-start):.10f}")