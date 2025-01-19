class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        row, column = len(matrix), len(matrix[0])
        row0 = False
        for index1, val1 in enumerate(matrix):
            for index2, val2 in enumerate(val1):
                if val2 == 0:
                    # print(index1,index2)
                    matrix[0][index2] = 0
                    if index1 > 0:
                        matrix[index1][0] = 0
                    else:
                        row0 = True
        for i in range(1, row):
            for j in range(1, column):
                if matrix[i][0] == 0:
                    matrix[i][j] = 0
                if matrix[0][j] == 0:
                    matrix[i][j] = 0

        for i in range(row):
            for j in range(column):
                if matrix[0][j] == 0:
                    matrix[i][j] = 0
        if row0 == True:
            for j in range(column):
                matrix[0][j] = 0
        print(matrix)
