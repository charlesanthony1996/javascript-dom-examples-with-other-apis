import time
import random
import torch

# # define the size of the grid
# size = 5

# # grid layout building parts
# vertical = "|"
# horizontal = "_"
# intersection = "+"


# # creating the grid
# for i in range(size):
#     # print horizaontal lines
#     print(intersection + horizontal*size + intersection)

#     # print vertical lines
#     print((vertical + " "*size)* size + vertical)

# # print the last horizontal line
# print(intersection + horizontal*size + intersection)


# end of drawing a grid
class Grid:
    def __init__(self, size):
        self.size = size
        self.grid = [["  " for _ in range(size)] for _ in range(size)]
        # position of the x
        self.position = [size // 2, size // 2]
        # for the target? why should it be in the init function?
        self.place_target()
        # place X after the target
        self.grid[self.position[0]][self.position[1]] = " X "

        # intialize the cost to zero here
        self.cost = 0



    def print_grid(self):
        for row in self.grid:
            print("|" + "|".join(row) + " | ")
            # seperator line
            print("--" * (self.size * 2 + 1))
        # wait for 1 second to print the next grid
        time.sleep(1)
        print()


    def move_up(self):
        # what does this mean?
        # going up is possible -> there is a top row available
        if self.position[0] > 0:
            self.grid[self.position[0]][self.position[1]] = "  "
            self.position[0] -= 1
            self.grid[self.position[0]][self.position[1]] = " X "
            self.cost += 1

    # diagonal move function towards the top right quadrant
    def move_up_right(self):
        if self.position[0] > 0 and self.position[1] < self.size - 1:
            self.grid[self.position[0]][self.position[1]] = "  "
            self.position[0] -= 1
            self.position[1] += 1
            self.grid[self.position[0]][self.position[1]] = " X "
            self.cost += 1



    def move_left(self):
        # able to go a left
        # draw a 5 x 5 grid on paper and see
        # there is a 1 column on the left for traversal
        if self.position[1] > 0:
            self.grid[self.position[0]][self.position[1]] = "  "
            self.position[1] -= 1
            self.grid[self.position[0]][self.position[1]] = " X "
            self.cost += 1


    def move_up_left(self):
        if self.position[0] > 0 and self.position[1] < self.size - 1:
            self.grid[self.position[0]][self.position[1]] = "  "
            self.position[0] -= 1
            self.position[1] -= 1
            self.grid[self.position[0]][self.position[1]] = " X "
            self.cost += 1


    def move_down(self):
        # able to go down by 1 unit
        # draw a 5 by 5 grid on paper and see
        # there is 1 row at the bottom for the X to go
        if self.position[0] < self.size - 1:
            self.grid[self.position[0]][self.position[1]] = "  "
            self.position[0] += 1
            self.grid[self.position[0]][self.position[1]] = " X "
            self.cost += 1


    def move_down_right(self):
        if self.position[0] > 0 and self.position[1] < self.size - 1:
            self.grid[self.position[0]][self.position[1]] = "  "
            self.position[0] += 1
            self.position[1] -= 1


    def move_right(self):
        if self.position[1] < self.size - 1:
            self.grid[self.position[0]][self.position[1]] = "  "
            self.position[1] += 1
            self.grid[self.position[0]][self.position[1]] = " X "
            self.cost += 1

    def move_down_left(self):
        pass

    def place_target(self):
        while True:
            # generate random row and column indices
            # make sure to import random
            target_row = random.randint(0, self.size - 1)
            target_col = random.randint(0, self.size - 1)

            # if the selected cell is not currently occupied by "X", place the target
            if self.grid[target_row][target_col] == "  ":
                self.grid[target_row][target_col] = " T "
                break


    def print_cost(self):
        print(f"Total cost: {self.cost}")


    def follow_target(self):
        # scan the position of the target here
        target_position = [(i, j) for i in range(self.size) for j in range(self.size) if self.grid[i][j] == " T "][0]

        # move horizontally towards the target
        while self.position[1] != target_position[1]:
            if self.position[1] < target_position[1]:
                self.move_right()
                # self.print_grid()
            else:
                self.move_left()
                # self.print_grid()
            self.print_grid()


        # move vertically towards the target
        while self.position[0] != target_position[0]:
            if self.position[0] < target_position[0]:
                self.move_down()
            else:
                self.move_up()
            self.print_grid()



# # Initializing the grid
grid = Grid(5)

# # printing the grid before the grud
# grid.print_grid()

# # perform the movement operation
# grid.move_up()

# # print the grid after
# grid.print_grid()

# print the left movement operation
# grid.move_left()

# print the grid after
# grid.print_grid()

# print the down movement operation
# grid.move_down()

# print the grid
# grid.print_grid()

# print the right movement operation
# grid.move_right()

# print the grid
# grid.print_grid()


# put a target on the grid
# grid.place_target()


# print the grid
grid.print_grid()

# move the target
# grid.follow_target()


# grid.print_cost()


# print the diagonal movement functions out!
grid.move_up_left()

grid.print_grid()


# adding the cost part to the algorithm? why is it important though?

# basically cost is a measure of the effort thats required for the X

# 1. path optimization -> in more complex scenarios when there are multiple routes to the target?
# this becomes important. maybe increase the grid size? and check this point further down the road

# 2. reward system
# this basically comes under a reinforcement algorithm the cost function can serve as a reward system
# that encourages the AI to find an optimal path

# 3. energy constraints
# if your simulating a real world situation, the x might represent a
# robot that has a finite amount of energy. in such cases minimizing the cost
# would be critical -> very complex scenario!


# remember our basic cost function also resembles the steps taken here, so its a pretty basic system here



