import numpy as np
from tinygrad.tensor import Tensor
import time


t1 = Tensor([1, 2, 3, 4, 5])
na = np.array([1, 2, 3, 4, 5])
t2 = Tensor(na)

# tensors can also be created by using one of the many factory methods
# full = Tensor.full(shape= (2, 3), fill_value=5)
# print(full)
zeros = Tensor.zeros(2, 3)
ones = Tensor.ones(2, 3)


# full_like = Tensor.full_like()
zeros_like = Tensor.zeros_like()
ones_like = Tensor.ones_like()

