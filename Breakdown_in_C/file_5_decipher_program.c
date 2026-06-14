#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <string.h>


int main(void){
    char chars[] =
    " !\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
    "0123456789"
    "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ";

    int length = strlen(chars);

    char key[length + 1];
    
    strcpy(key,chars);

    // Seed random number generator
    srand(time(NULL));
    
    // shuffle key
    
    // Shuffle key (Fisher yates  shuffleE)
    for(int i = strlen(key) - 1; i >= 0; i-- ){
        
        int j = rand() % (i + 1);
        char temp = key[i];
        key[i] = key[j];
        key[j] = temp;
    }

    printf("%s", key);

    return 0;
}

