#include <stdio.h>

struct BinaryMatrice {
    int value;
    int bit_size;
    int pack_bit_size;
    int column;
    int row;
};

int bin_add(int a, int b) {
    int res, ret = -1;
    while (ret != 0) {
        res = a^b;
        ret = (a&b)<<1;
        a, b = res, ret;
    }
    return res;
}

int add_matrice(struct BinaryMatrice *res, struct BinaryMatrice a, struct BinaryMatrice b) {
    if (a.row != b.row || a.column != b.column || a.bit_size != b.bit_size)
        return -1;
    
    res->row = a.row;
    res->column = a.column;
    int mask = (1<<a.pack_bit_size)-1;

    while (a.value>0) {
        printf ("%d\n", bin_add(a.value&mask, b.value&mask));
        res->value = (bin_add(a.value&mask, b.value&mask) << mask) | res->value;
        a.value>>=a.pack_bit_size;
        b.value>>=b.pack_bit_size;
    }
        
    return 1;
}

int main(){
    /*
                01  10  10  11
                01  11  00  10 
                ---------------
    11 10 11 01| 100 100 101 100
    11 00 00 11| 100 011 000 110

    = 4, 4, 5, 4, 4, 3, 0, 6

    100100101100100011000110 

    101 000 011 100 100 101 100 100

    -----------------------------

    0110101101110010

    0110101101110010
    */
    
    struct BinaryMatrice a = {.value=0b0110101101110010, .pack_bit_size=2, .bit_size=16, .row=2, .column=4};
    struct BinaryMatrice b = {.value=0b1110110111000011, .pack_bit_size=2, .bit_size=16, .row=2, .column=4};
    struct BinaryMatrice c = {};

    add_matrice(&c, a, b);
    printf ("%d", c.value);

    return 1;
}