import numpy as np
import matplotlib.pyplot as plt
import heapq


def heuristic(a, b):
    return abs(b[0] - a[0]) + abs(b[1] - a[1])


def a_star_algorithm(start, goal, graph):
    neighbours = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    close_set = set()
    came_from = {}
    gscore = {start: 0}
    fscore = {start: heuristic(start, goal)}
    open_heap = []

    heapq.heappush(open_heap, (fscore[start], start))
    path = []
    all_nodes = []
    while open_heap:
        current = heapq.heappop(open_heap)[1]
        # print(current)
        all_nodes.append(current)


        if current == goal:
            while current in came_from:
                path.append(current)
                current = came_from[current]
            return path, all_nodes


        close_set.add(current)
        for i, j in neighbours:
            neighbour = current[0] + i, current[1] + j
            tentative_g_score = gscore[current] + heuristic(current, neighbour)
            if 0 <= neighbour[0] < graph.shape[0]:
                if 0 <= neighbour[1] < graph.shape[1]:
                    if graph[neighbour[0]][neighbour[1]] == 1:
                        continue

                else:
                    continue

            else:
                continue

            if neighbour in close_set and tentative_g_score >= gscore.get(neighbour, 0):
                continue


            if tentative_g_score < gscore.get(neighbour, 0) or neighbour not in [i[1] for i in open_heap]:
                came_from[neighbour] = current
                gscore[neighbour] = tentative_g_score
                fscore[neighbour] = tentative_g_score + heuristic(neighbour, goal)
                heapq.heappush(open_heap, (fscore[neighbour], neighbour))
            
    
    return path, all_nodes


def draw_path(graph, path, all_nodes):
    plt.imshow(graph, cmap='Greys', origin='lower')

    # All nodes considered by the algorithm are marked in blue
    all_nodes = np.array(all_nodes)
    plt.scatter(all_nodes[:, 1], all_nodes[:, 0], color='blue')

    # The final path is marked in red
    path = np.array(path)
    plt.plot(path[:, 1], path[:, 0], color='red')
    plt.show()





nmap = np.array([
    [0, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0],
])

# no obstacles in this one
# just for testing

# nmap = np.array([
#     [0, 1, 0, 0, 0],
#     [0, 0, 0, 0, 0],
#     [0, 0, 1, 0, 0],
#     [0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0]
# ])



# print(nmap)

path, all_nodes = a_star_algorithm((0, 0), (0, 5), nmap)

# print(path)

# print(all_nodes)

# print(path)

# comment this out to show the path taken
# refer to the output and construct a more complex maze
# draw_path(nmap, path, all_nodes)


# core concepts in understanding the algorithm

"""
1. The (0, 1), (0, -1), (-1, 0), (0, 1) are directions in the grid. they represent up, down, left and right
respectively

2. neighbour = current[0] + j, current[1] + j is computing the coordinates of the neighbouring cell 
in the grid based on the current cell

3. the conditional statements 



"""

# exercises start here

# 1. basic grid manipulation

# create a 5 x 5 grid with numpy and set the value of the cell at (2, 3) to 1.


import numpy as np

grid = np.zeros((5, 5))
grid[2][3] = 1
# print(grid)


# 2. neighbour calculation

# given a cells coordinates, write a function to compute and return the coordinates of its neighbours

# this is for a four connected grid. also know as the manhattan distance

def neighbour_calculation(cell):
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    neighbours = [(cell[0] + i, cell[1] + j) for i, j in directions]
    return neighbours


print(neighbour_calculation((2, 2)))

# now we calculate it for a 8 connected grid. this is to introduce the diagonals as well.
# consider a 3 x 3 grid

def neighbour_calculation_8(cell):
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
    neighbours = [(cell[0] + i, cell[1] + j) for i, j in directions]
    return neighbours



print(neighbour_calculation_8((2, 2)))

# 3. boundary checking

# given a grid and a cell's coordinates , write a function to check if the cell is within the grid's neighbours

def is_within_bounds(grid, cell):
    return 0 <= cell[0] < grid.shape[0] and 0 <= cell[1] < grid.shape[1]


print(is_within_bounds(grid, (2,2)))

# check the grid again to see why this is false
print(is_within_bounds(grid, (3, 5)))



# 4. cell type checking

# given a grid and a cell's coordinates , write a function to check if the cell is a wall or not
# (you can represent a wall by the value of 1)

def is_wall(grid, cell):
    return grid[cell[0]][cell[1]] == 1


# this is from the numpy grid at the start of the exercise

# check whether a wall or a "1" is there at the position below
print(is_wall(grid, (0, 1)))

# this is from the numpy grid at the start of the exercise
print(is_wall(grid, (2, 3)))


# 5.Moving on a grid