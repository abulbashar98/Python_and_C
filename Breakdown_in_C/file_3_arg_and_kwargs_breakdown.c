#include <stdio.h>

typedef struct{
    char street[20];
    char state[20];
    char zip[20];
    char poBox[20];
    char city[20];
    char apt[20];
}Address;

void shipping_label(char *args[],int count, Address *addr){
    
    for(int i = 0; i < count; i++){
        printf("%s ", args[i]);
    };
    printf("\n");

    if(addr->apt[0] != '\0' && addr->poBox[0] != '\0'){
        printf("Street:%s Apartment:%s poBox:%s", addr->street, addr->apt,addr->poBox);
    }

    else if(addr->apt[0] != '\0'){
        printf("%s %s", addr->street, addr->apt);
    }

    else if(addr->poBox[0] != '\0'){
        printf("%s %s", addr->street, addr->poBox);
    }
    printf("\n");

    printf("State:%s Zip:%s City:%s", addr->state, addr->zip, addr->city);

}


int main(void){
    
    char *names[] = {"Mr", "Spongebob", "Squarepants", "III"};
    
    Address addr = {
        .street = "123fakestreet",
        .state = "Michigan",
        .zip = "10601",
        .poBox = "101",
        .city = "Detroit",
        .apt = "3A1"
    };

    shipping_label(names, 4, &addr);


    return 0;
}