#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <string.h>
#include <unistd.h>

#define size 5
#define empty "  "
#define target " T "
#define pos " X "

// declare the grid and the position
char grid[size][size][3];
int position[2];

void print_grid()
{
    for (int i = 0; i < size; i++)
    {
        for (int j= 0; j < size; j++)
        {
            printf("|%3s", grid[i][j]);
        }
        printf("|\n");
        printf("---------------------\n");
    }
    // sleep for a second
    sleep(1);
    printf("\n");
}


void initialize_grid()
{
    position[0] = size/ 2;
    position[1] = size/2;

    // initialize all cells to empty
    for(int i =0; i < size; i++)
    {
        for(int j = 0; j < size; j++)
        {
            strcpy(grid[i][j] , empty);
        }
    }

    // set target to a random position
    int target_row = rand() % size;
    int target_col = rand() % size;

    strcpy(grid[target_row][target_col], target);

    // set x position
    strcpy(grid[position[0]][position[1]], pos);


}


int main()
{
    printf("create the grid here\n");
    srand(time(NULL));
    initialize_grid();
    print_grid();

    return 0;
}