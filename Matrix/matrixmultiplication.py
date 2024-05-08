
# Simple Matrix Multiplication

#x = [[1,2,3],[4,5,6],[7,8,9]]
#y = [[1,2,1],[4,5,4],[7,8,7]]

def transpose_matrix(y):
        rows = len(y)
        cols = len(y[0])

        transposed = [[0]*cols for _ in range(rows)]

        for i in range(rows):
            for j in range(cols):
                transposed[j][i] = y[i][j]

        return transposed

def matrix_multiplication(x,y):

    new =[[0]*len(y[0]) for _ in range(len(x))]

    for i in range(len(x)):
        for j in range(len(y[0])):
            for k in range(len(y)):
                new[i][j]=new[i][j]+x[i][k]*y[k][j]

    return new



if __name__=="__main__":
    x = [[1,2,3],[4,5,6],[7,8,9]]
    y = [[1,2,1],[4,5,4],[7,8,7]]
    _x = matrix_multiplication(x,y)





