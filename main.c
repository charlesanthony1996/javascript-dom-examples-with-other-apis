#include <stdio.h>

int main() {
    int i = 42;
    float f = 3.14159265;
    double d = 2.71828;

    printf("size of int: %d \n", sizeof(int));
    printf("size of float: %d \n", sizeof(float));
    printf("size of float: %d \n", sizeof(double));

    float converted_f = (float) i;
    int converted_i = (float) f;
    int truncated_f = (float) f;

    printf("i as a float: %f\n",(float) i);



    return 0;

}