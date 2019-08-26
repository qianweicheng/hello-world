#include "ccallp.h"
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char** argv)  
{
    int a = ccallp(argc, argv);
    printf("Result is: %d\n", a);
    printf("====================\n");
    int b = pcallc("abc", argv);
    printf("Result2 is: %d\n", b);
    return 0;
}   
