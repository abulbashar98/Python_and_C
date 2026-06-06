#include <stdio.h>
#include <stdarg.h>

// 1️⃣ Basic of variadic functions

// Variadic function to add numbers
int getsum(int n, ...){
    
    int sum = 0;
    
    // Declaring a va_list pointer to
    // argument args
    va_list args;
    
    // Initializing argument to the
    // args pointer
    va_start(args, n);

    for(int i = 0; i < n; i++){

        // Accessing current variable
        // and pointing to next one
        sum += va_arg(args, int);
    }
    // Ending list of argument args traversal
    va_end(args);

    return sum;
}



int main(void){
    
    // Calling same function with
    // variable number of arguments
    printf("Sum of 5 elements(1,2,3,4,5): %d\n", getsum(5,1,2,3,4,5));
    printf("Sum of these 3 elements(20,30,55): %d", getsum(3, 20,30,55));


    return 0;
}