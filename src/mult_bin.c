#include <stdio.h>
#include <stdlib.h>

int get_length(int num) {
    int length = 0;
    while (num != 0) {
        length++;
        num >>= 1;
    }
    return length;
}

int karatsuba(int x, int y) {
    if (x < 10 && y < 10) {
        return x * y;
    }

    int n = get_length(x > y ? x : y);
    int m = (n + 1) >> 1;

    int x_H = x >> m;
    int x_L = x - (x_H << m);

    int y_H = y >> m;
    int y_L = y - (y_H << m);

    int a = karatsuba(x_H, y_H);
    int d = karatsuba(x_L, y_L);
    int e = karatsuba(x_H + x_L, y_H + y_L) - a - d;

    return (a << (m << 1)) + (e << m) + d;
}

int mult_bin(int a, int b) {
    int res = 0;
    while (b) {
        if (b & 1)
            res += a;
        a <<= 1;
        b >>= 1;
    }
    return res;
}



int main() {
    printf ("%d \n", mult_bin(10, 15));
    printf ("%d \n", karatsuba(10, 15));
    return 1;
}
