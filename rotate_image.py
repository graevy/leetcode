# You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

# You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

 

# Example 1:

# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [[7,4,1],[8,5,2],[9,6,3]]

# Example 2:

# Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
# Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]

 

# Constraints:

#     n == matrix.length == matrix[i].length
#     1 <= n <= 20
#     -1000 <= matrix[i][j] <= 1000


# so this is a really stupid solution. rotate the array by concentric squares
# basically, rotate a 4-item sliding window. start with the corners. coordinates are given by:
#  _________________
# |     |     |     |
# | x,y |     |x,n-y|
# |_____|_____|_____|
# |     |FREE |     |
# |     |SPACE|     |
# |_____|_____|_____|
# | n-x,|     | n-x,|
# |  y  |     | n-y |
# |_____|_____|_____|
#
# where x,y refer to matrix coordinates, and n refers to array indexing bounds.
# after rotating the corners, rotate the window n times
# the center doesn't need to get rotated for odd n;
# the number of concentric squares is len(matrix) >> 1
class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix) - 1

        for y in range(len(matrix) >> 1):
            # side length of current square (shrinking each loop)
            for x in range(y, n-y):
                # store top right
                cache_1 = matrix[x][n-y]

                # top left -> top right
                matrix[x][n-y] = matrix[y][x]

                # store bottom right
                cache_2 = matrix[n-y][n-x]

                # top right -> bottom right
                matrix[n-y][n-x] = cache_1

                # store bottom left
                cache_1 = matrix[n-x][y]

                # bottom right -> bottom left
                matrix[n-x][y] = cache_2

                # bottom left -> top left
                matrix[y][x] = cache_1

        return matrix


from timing import batch
import numpy as np


data = [[[1,2],[3,4]], [[1,2,3],[4,5,6],[7,8,9]], [[1]], [[]],
    [[1,2,3,4,5,6],[7,8,9,10,11,12],[13,14,15,16,17,18],
    [19,20,21,22,23,24],[25,26,27,28,29,30],[31,32,33,34,35,36]]
]
# this classification doesn't work for the empty matrix but i just ignore it
classifiers = [[[elem for elem in line] for line in np.rot90(point, k=-1)] for point in data]

batch(fns=[Solution().rotate], data=data, classifiers=classifiers)