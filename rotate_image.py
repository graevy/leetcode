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


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        bounds = n - 1
        # base_x = 0
        # base_y = 0
        # number of concentric squares to rotate. if n%2, ignore middle
        # y,x refer to literal coordinate axes
        for y in range(n >> 1):
            # side length of current square
            for x in range(y, bounds-y + 1):
                # store top right
                # top left -> top right
                cache_1 = matrix[x][bounds-y]
                matrix[x][bounds-y] = matrix[y][x]

                # store bottom right
                # top right -> bottom right
                cache_2 = matrix[bounds-y][bounds-x]
                matrix[bounds-y][bounds-x] = cache_1

                # store bottom left
                # bottom right -> bottom left
                cache_1 = matrix[bounds-x][y]
                matrix[bounds-y][bounds-x] = cache_2

                # bottom left -> top left
                matrix[y][x] = cache_1


from timing import batch

data = [[1,2],[3,4]]
classifiers = [[4,1],[2,3]]

batch(fns=[Solution().rotate], data=data, classifiers=classifiers)