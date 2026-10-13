class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        post_0 = []

        for idx, x in enumerate(matrix):
            row_z = False

            for idy, y in enumerate(x):
                if y == 0:
                    post_0.append(idy)
                    row_z = True

            if row_z:
                for col in range(len(x)):
                    matrix[idx][col] = 0

        for idy in post_0:
            for row in range(len(matrix)):
                matrix[row][idy] = 0
