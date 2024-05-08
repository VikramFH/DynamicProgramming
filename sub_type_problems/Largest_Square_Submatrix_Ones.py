
#Matrix = [[0 1 1 0 1],
# [1 0 0 1 0],
# [1 1 1 1 0],
# [0 1 1 1 1],
# [1 1 1 1 0]]


def find_largest_square_on5(matrix):

    if not matrix:
        return 0

    def find_squares_of_ones(top,left,size):
        for row in range(top,top+size):
            for col in range(left,left+size):
                if matrix[row][col]==0:
                    return False
        return True

    number_of_rows = len(matrix)
    number_of_cols = len(matrix[0])
    largest = 0

    for top in range(number_of_rows):
        for left in range(number_of_cols):
            #Make sure we do not pass the edges of the matrix.
            max_size = min(number_of_rows - top,number_of_cols - left)
            for size in range(size,max_size+1):
                if find_squares_of_ones(top,left,size):
                    largest = max(largest,size*size)

    return largest

# Suppose we find  a large square then we need to check if (s+1)x(s+1) contains three overlapping sxs squares

#To check,if it is (s+1)x(s+1) square is filled with ones,its sufficient to:
# a) Check if the bottom right corner contains one.
# b) Check if the sxs square one row above is filled with ones?
# c) Check if the sxs square one column left is filled with ones?
# d) Check if the sxs square one row above and one column to the left is filled with ones.

#If the squares of the rows above and the columns to the left have already been checked, we can check  the
# (s+1)X(s+1) in O(1) time.

#We still have to decide how to handle special cases when the checks are failing?

# *Bottom right corner contains a zero,we cannot form a square filled with ones.
# *If one or more of three smalled neighboring squares are not of the same size.
# *The first pointer is also applicable for top left value.

# Lets Refine this procedure:
# We iterate over the matrix elements row by row and column by column
# If the current cell contains a zero, no square can be formed for that row and column
# If the current cell contains a 1:
        # *We read the size s1 of the largest square with bottom right corner above the cell
        # *We read the size s2 of the largest square with bottom right corner to the left of the cell
        # *We read the size of s3 the largest square with bottom right corner above to and left of the cell.
        # *We compute the size of the largest square filled with ones that has the bottom-right corner in the cell
        # min(s1,s2,s3).



def find_largest_square(matrix):

    number_of_rows =len(matrix)
    number_of_cols = len(matrix[0])

    reference_size_matrix = [[0]*len(rows) for rows in number_of_rows]
    largest = 0
    for row in number_of_rows:
        for col in number_of_cols:
            if matrix[row][col]==0:
                continue
            size_from_above = reference_size_matrix[row][col-1] if col>0 else 0
            size_from_left = reference_size_matrix[row-1][col] if row>0 else 0
            size_above_left = reference_size_matrix[row-1][col-1] if row>0 and col>0 else 0
            reference_size_matrix[row][col]=1+min(size_from_above,size_from_left,size_above_left)
            largest = max(largest,reference_size_matrix[row][col])

    return largest*largest

