"""

we can use A* to find the shortest path through a simple array of numbers, 
where the cost of moving to a position is equal to the number at that position.
In this case, the heuristic could be the difference in indices (position)
 between the current position and the target.

"""







import time
import torch
import random
from queue import PriorityQueue

def heuristic(a, b):
    return abs(b - a)

def cost_to_move(array, current, next):
    return array[next]

def get_neighbours(array, current):
    neighbors = []
    if current - 1 >= 0:
        neighbours.append(current, 0)
    if current + 1 < len(array):
        neighbours.append(current, 1)
    return neighbors


def astar_search(array, start, target):
    open_set = PriorityQueue()
    open_set.put((0, start))
    came_from = {}
    cost_so_far = {}
    came_from[start] = None
    cost_so_far[start] = 0


    while not open_set.empty():
        _, current = open_set.get()



    if current == target:
        break



array = [1, 3, 1, 1, 4, 1, 1, 1, 1, 2]
start = 0
target = len(array) - 1

path, cost = astar_search(array, start, target)
print(f"Path: {path}, cost: {cost}")




    
