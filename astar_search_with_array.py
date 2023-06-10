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

def 