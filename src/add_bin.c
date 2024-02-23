#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>
#include <sys/time.h>


int add_bin_opti_1(int a, int b) {
    while (b) {
        a ^= b;
        b = ((a^b) & b)<<1;
    }
    return a;
}


int add_bin_opti_2(int a, int b) {
    while (b) {
        a ^= b;
        b = (~a & b)<<1;
    }
    return a;
}

int add_bin_nopti(int a, int b) {
    int res;
    int ret = -1;

    while (ret != 0) {
        res = a ^ b;
        ret = (a&b)<<1;
        a = res;
        b = ret;
    }
    return res;
}

uint64_t add_bin_mask(uint64_t a, uint64_t b, int mask) {
    while (b) {
        a ^= b;
        b = (((a^b) & b)<<1)&mask;
    }
    return a;
}

int main() {
    uint64_t a = 0b1010;
    uint64_t b = 0b1111;
    int mask = (1 << 4) - 1;

    printf ("%ld\n", add_bin_mask(a, b, mask));

    /*
    struct timeval tv_start, tv_end;
    gettimeofday(&tv_start, NULL);

    add_bin_nopti(a, b);

    gettimeofday(&tv_end, NULL);
    double mtime = (tv_end.tv_sec - tv_start.tv_sec) * 1000000.0 + (tv_end.tv_usec - tv_start.tv_usec) / 1000000.0; // in ms
    printf ("%f\n", mtime);

    
    gettimeofday(&tv_start, NULL);

    add_bin_opti_1(a, b);

    gettimeofday(&tv_end, NULL);
    mtime = (tv_end.tv_sec - tv_start.tv_sec) * 1000000.0 + (tv_end.tv_usec - tv_start.tv_usec) / 1000000.0; // in ms
    printf ("%f\n", mtime);

    gettimeofday(&tv_start, NULL);

    add_bin_opti_2(a, b);

    gettimeofday(&tv_end, NULL);
    mtime = (tv_end.tv_sec - tv_start.tv_sec) * 1000000.0 + (tv_end.tv_usec - tv_start.tv_usec) / 1000000.0; // in ms
    printf ("%f\n", mtime);
    */
}