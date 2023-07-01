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


// for reference
// origin is at the top left

//     0   1   2   3   4   <- x-coordinate (position[1])
// 0 | a | b | c | d | e |
// 1 | f | g | h | i | j |
// 2 | k | l | m | n | o |
// 3 | p | q | r | s | t |
// 4 | u | v | w | x | y |
// ^
// |
// y-coordinate (position[0])


void initialize_grid()
{
    position[0] = size/ 2;
    position[1] = size/ 2;

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

void move_right()
{
    if(position[1] < size - 1)
    {
        // ensure we are not on the right edge of the grid
        // make current cell empty
        strcpy(grid[position[0]][position[1]], empty);

        // move to the right
        position[1] += 1;

        // mark new cell as pos
        strcpy(grid[position[0]][position[1]], pos);
    }
    else {
        printf("Cant move right from here\n");
    }
}


void move_left()
{
    if(position[1] > 0)
    {
        strcpy(grid[position[0]][position[1]], empty);

        position[1] -= 1;

        strcpy(grid[position[0]][position[1]], pos);
    }
    else {
        printf("canot move left from here\n");
    }
}







int main()
{
    printf("create the grid here\n");
    srand(time(NULL));
    initialize_grid();
    print_grid();

    // printf("move right\n");
    // move_right();
    // print_grid();

    printf("move left\n");
    move_left();
    print_grid();

    return 0;
}