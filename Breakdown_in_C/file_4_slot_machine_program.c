#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <time.h>

typedef struct{
    
    char row[4];

}Slotrow;



Slotrow spinrow(const char symbols[], size_t size_symbols){

   Slotrow result;
    
   for(int i = 0; i < 3; i++){
        int random_number = (rand() % size_symbols); 
        result.row[i] = (symbols[random_number]);
   }

   result.row[3] = '\0';

//    printf(row);

   return result; 

}

void print_row(Slotrow slot){
    printf("Spinning...\n");
    
    int i = 0;

    while(slot.row[i] != '\0'){
        printf("%c | ", slot.row[i]);
        i++;
    } 

    printf("\n");
 
}

int get_payout(Slotrow slot, int bet){
    printf("***************************\n");
    if(slot.row[0] == slot.row[1] && slot.row[1] == slot.row[2]){
        printf("Congratulations you won!!!\n");
        if(slot.row[1] == 'c'){
            return bet*3;
        }
        else if(slot.row[1] == 'w'){
            return bet*5;
        }
        else if(slot.row[1] == 'b'){
            return bet*10;
        }
        else if(slot.row[1] == 's'){
            return bet*20;
        }        
    }
    printf("You lost this round.\n");
    return 0;
}

char play_again(int balance){

    while(balance > 0){
        char user_response;
        char buffer2[20];
        printf("Do you want to play again? Input(Y/N): ");
        fgets(buffer2, sizeof(buffer2), stdin);
        sscanf(buffer2, " %c", &user_response);
        
        user_response = toupper(user_response);
        // printf("%c",user_response);

        while(1){
            if(user_response == 'Y'){
                break;
            }
            else if(user_response == 'N'){
                break;
            }
            else{
                printf("\n");
                printf("Pleas put (Y/N) as your response: ");
                fgets(buffer2, sizeof(buffer2), stdin);
                sscanf(buffer2, " %c", &user_response);
                user_response = toupper(user_response);
                // printf(" %c",user_response);
            }
            
        }
  
        return user_response;      
    }

}



int main(void){
    
    srand(time(NULL));

    int balance = 100;
    const char symbols[] ={'c','w','b','s'};
    size_t size_symbols = sizeof(symbols)/sizeof(symbols[0]);
    char buffer[50];
    int bet = 0;
    char extra;

     
    
    printf("********************************\n");
    printf("Welcome to C slot machine game\n");
    for(int i =0; i < size_symbols; i++){
        printf(" %c ", symbols[i]);
    }
    printf("\n");
    printf("****************************\n");
    
    while(1){
        
        while(1){
            printf("Enter your bet amount: ");

            if(fgets(buffer, sizeof(buffer), stdin) == NULL){
            return 1;
            }
            // int result = sscanf(buffer, "%d", &bet);
            // printf("sscanf returned %d\n", result);
            // printf("buffer = '%s'\n", buffer);

            if(sscanf(buffer, "%d %c", &bet, &extra) != 1){
            
                printf("Input a valid number\n");
                continue;
            }

            if(bet <= 0){
                printf("Bet amount must be greater than 0.\n");
                continue;
            }
            else if(bet > balance){
                printf("Insufficient funds\n");
                continue;
            }
            else{
                printf("%d\n", bet);
                balance -= bet;
                break;
            }  

        }

        Slotrow slot = spinrow(symbols, size_symbols);
        // printf(slot.row);
        print_row(slot);

        balance += get_payout(slot, bet);

        printf("Your current balance is: %d\n", balance);
        printf("***************************\n");
        char isRunning = play_again(balance);
        // printf("%c", isRunning);
        if(isRunning == 'Y'){
            continue;
        }
        else{
            break;
        }
    }
    

    return 0;
}