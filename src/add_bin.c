#include <stdio.h>
#include <stdlib.h>
#include <sys/time.h>

int add_bin_opti(int a, int b) {
    while (b) {
        a ^= b;
        b = (~a & b)<<1;
    }
    return a;
}


int add_bin_2(int a, int b) {
    while (b) {
        a ^= b;
        b = ((a^b) & b)<<1;
    }
    return a;
}

int add_bin_3(int a, int b) {
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

int main() {
    int a = 0xfffaabcb;
    int b = 0xabcffff;

    struct timeval tv_start, tv_end;
    gettimeofday(&tv_start, NULL);

    add_bin_opti(a, b);

    gettimeofday(&tv_end, NULL);
    double mtime = (tv_end.tv_sec - tv_start.tv_sec) * 1000000.0 + (tv_end.tv_usec - tv_start.tv_usec) / 1000000.0; // in ms
    printf ("%f\n", mtime);

    
    gettimeofday(&tv_start, NULL);

    add_bin_2(a, b);

    gettimeofday(&tv_end, NULL);
    mtime = (tv_end.tv_sec - tv_start.tv_sec) * 1000000.0 + (tv_end.tv_usec - tv_start.tv_usec) / 1000000.0; // in ms
    printf ("%f\n", mtime);

    gettimeofday(&tv_start, NULL);

    add_bin_3(a, b);

    gettimeofday(&tv_end, NULL);
    mtime = (tv_end.tv_sec - tv_start.tv_sec) * 1000000.0 + (tv_end.tv_usec - tv_start.tv_usec) / 1000000.0; // in ms
    printf ("%f\n", mtime);
    
}