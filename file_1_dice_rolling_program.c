#include <stdio.h>
#include <stdlib.h>
#include <time.h>

const char* dice_art[7][5] = {
    {NULL},
    //1
    {"┌─────────┐",
     "│         │",
     "│    ●    │",
     "│         │",
     "└─────────┘"},
     //2
    {"┌─────────┐",
     "│ ●       │",
     "│         │",
     "│       ● │",
     "└─────────┘"},
      //3
    {"┌─────────┐",
     "│ ●       │",
     "│    ●    │",
     "│       ● │",
     "└─────────┘"},
     //4
    {"┌─────────┐",
     "│ ●     ● │",
     "│         │",
     "│ ●     ● │",
     "└─────────┘"},
     //5
    {"┌─────────┐",
     "│ ●     ● │",
     "│    ●    │",
     "│ ●     ● │",
     "└─────────┘"},
    //6
    {"┌─────────┐",
     "│ ●     ● │",
     "│ ●     ● │",
     "│ ●     ● │",
     "└─────────┘"}
    };

    

int main(void){
    
    int dice[6]= {0,0,0,0,0,0};
    int total = 0;
    int num_of_rolls;
    

    srand(time(NULL));

    printf("Enter the number of rolls: ");
    scanf("%d", &num_of_rolls);

    for(int i = 0; i < num_of_rolls;i++){
        dice[i] = (rand() % 6) + 1;
        printf("%d\n", dice[i]);
    }

    printf("Number of rolls: %d", num_of_rolls);

    int dice_length = sizeof(dice) / sizeof(dice[0]);
    // printf("Dice Length: %d", dice_length);

    for(int line = 0; line < 5; line++){
        for(int die = 0; die < dice_length; die++){
            // printf("%s",dice_art[dice[die]][line]);
        }
        printf("\n");
    }

    for(int j = 0; j < dice_length; j++){
        total += dice[j];
    }
    
    printf("Your total is: %d", total);
    return 0;
}

