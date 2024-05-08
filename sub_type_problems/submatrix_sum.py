#There is a matrix

MATRIX_EXAMPLE = [[1,2,3,4,5],
                  [6,7,8,9,10],
                  [11,12,13,14,15],
                  [16,17,18,19,20],
                  [21,22,23,24,25]]

QUERIES_EXAMPLE = [(0,0,2,2),(1,2,3,5)]

#top,left,bottom,right

#matrix formed by [top,bottom) and [left,right)

def submatrix_brute_force(matrix,queries):
    result = []
    for top,left,bottom,right in queries:
        rectangle_sum=0
        for row in matrix[top:bottom]:
            rectangle_sum=rectangle_sum+sum(row[left:right])
        result.append(rectangle_sum)

    return result

def rectangle_sum(matrix,queries):

    num_rows = len(matrix)
    num_cols = len(matrix[0])

    prefix_sums = [[0]*num_cols+1 for _ in range(num_rows+1)]

    for i in range(num_rows):
        for j in range(num_cols):
            prefix_sums[i+1][j+1] += matrix[i][j]

    for i in range(num_rows):
        for j in range(num_cols):
            prefix_sums[i+1][j+1] += prefix_sums[i+1][j]


    for i in range(num_rows):
        for j in range(num_cols):
            prefix_sums[i+1][j+1] += prefix_sums[i][j+1]

    result = []

    for top,bottom,left,right in queries:
        bottom = max(bottom,top)
        right = max(right,left)

        rectangle_sum = (prefix_sums[bottom][right] -
                         prefix_sums[bottom][left] -
                         prefix_sums[top][right] +
                         prefix_sums[bottom][left])

        result.append(rectangle_sum)

    return result


