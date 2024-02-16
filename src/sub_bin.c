#include <stdio.h>
#include <stdlib.h>
#include <sys/time.h>


int sub_bin_nopti(int a, int b) {
    int res=0;
    int ret=-1;

    while (ret) {
        res = a ^ b;
        ret = ((a^b) & b) << 1;
        a = res;
        b = ret;
    }
    return a;
}

int sub_bin_opti(int a, int b) {
    while (b) {
        a = a ^ b;
        b = (a & b) << 1;
    }
    return a;
}

int main() {
    int a = 0xffaabcb;
    int b = 0xafbcffff;
    struct timeval tv_start, tv_end;

    gettimeofday(&tv_start, NULL);
    sub_bin_opti(a, b);
    gettimeofday(&tv_end, NULL);

    double mtime = (tv_end.tv_sec - tv_start.tv_sec) * 1000000.0 + (tv_end.tv_usec - tv_start.tv_usec) / 1000000.0; // in ms
    printf ("%f\n", mtime);

    
    gettimeofday(&tv_start, NULL);
    sub_bin_nopti(a, b);
    gettimeofday(&tv_end, NULL);

    mtime = (tv_end.tv_sec - tv_start.tv_sec) * 1000000.0 + (tv_end.tv_usec - tv_start.tv_usec) / 1000000.0; // in ms
    printf ("%f\n", mtime);
    
}