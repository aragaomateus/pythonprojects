# from array import *
# matrix = [[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],
# 		   [1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],
# 		   [1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],
# 		   [1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],
#            [1,2,3,4,5,6,7,8,9]]

# for i in matrix: 
#     for x in i:   
#         print(x, end = " ")
#     print()

import numpy as np


arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])

newarr = arr.reshape(2, 2, -1)

print(newarr)