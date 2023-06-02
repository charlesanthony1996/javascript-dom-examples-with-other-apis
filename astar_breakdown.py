


























# class Grid:
#     def __init__(self, size):
#         self.size = size
#         self.grid = [['   ' for _ in range(size)] for _ in range(size)]
#         self.position = [size // 2, size // 2]  # start at the center
#         self.grid[self.position[0]][self.position[1]] = 'X'

#     # printing the playground grid 
#     def print_grid(self):
#         for row in self.grid:
#             print('|' + '|'.join(row) + '|')
#             print('--' * (self.size*2+1))  # separator line

#     # function to move up the x by a single unit
#     def move_up(self):
#         if self.position[0] > 0:
#             self.grid[self.position[0]][self.position[1]] = '   ' 
#             self.position[0] -= 1  # move up
#             self.grid[self.position[0]][self.position[1]] = ' X ' 



# # Initializing the grid
# grid = Grid(5)

# # printing the grid before the grud
# grid.print_grid()

# # perform the movement operation
# grid.move_up()

# # print the grid after
# grid.print_grid()
