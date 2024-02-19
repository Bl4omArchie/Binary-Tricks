def get_length(num):
    length = 0
    while num:
        length += 1
        num >>= 1
    return length
