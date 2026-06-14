/*  1️⃣ Basic of variadic functions

#include <stdio.h>
#include <stdarg.h>



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
*/

// 2️⃣ Another example of variadic function-> va_list,va_start,va_arg,va_end and ellipsis with first parameter of character pointer pointing types of arguments in a string.

#include <stdio.h>
#include <stdarg.h>

// Variadic function receive a character pointer as 1st argument, that describes the types of argument we receive in ellipsis
int print(const char* types, ...){
    
    
    va_list list;

    va_start(list, types);



    for(int i = 0; types[i] != '\0';i++){
        
        
        if(types[i] == 'i'){
            int v = va_arg(list,int);
            printf("Integer: %d\n", v);
        }  
        else{
            double v = va_arg(list,double);
            printf("Float: %.2f\n", v);
        }
    }
    
    va_end(list);
    return 0;
}


int main(void){
    
    print("iddidi",8,8.4,4.4,5,3.14159,7);
    return 0;
}