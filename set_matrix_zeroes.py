class Solution:
    def set_zeroes(self, matrix):
        """
        Do not return anything, modify matrix in-place instead.
        """
        ROWS, COLUMNS = len(matrix), len(matrix[0])
        first_row_zero = False
        # iterate through rows and columns
        # if there is 0 in any row and column
        # set zero in the first row in a column where 0 was found
        # if row where 0 was found is other than first row
        # set the first column to 0 in that row
        # in other case just mark that first row should be set to zeroes
        for r in range(ROWS):
            for c in range(COLUMNS):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0
                    if r > 0:
                        matrix[r][0] = 0
                    else:
                        first_row_zero = True

        # iterate through rows and columns but starting from index 1
        # i. e. second row and second column
        # if any of the rows starting from the second
        # have zeroes or any of the columns starting from the second
        # have zeroes, then set those columns to zeroes
        for r in range(1, ROWS):
            for c in range(1, COLUMNS):
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0

        # check if 0 is set in first row in first column
        # if so, go down every row and set 0 in this column
        if matrix[0][0] == 0:
            for r in range(ROWS):
                matrix[r][0] = 0

        # check if the first zero was detected in first row
        # if so, set the whole row to zer0
        if first_row_zero:
            for c in range(COLUMNS):
                matrix[0][c] = 0

        print(matrix)


solution = Solution()
solution.set_zeroes([[1, 0, 1], [1, 1, 1], [1, 1, 1]])
