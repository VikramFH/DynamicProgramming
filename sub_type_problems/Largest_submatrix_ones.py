import collections


def BruteLargestRectangleMatrix(mat):
    #this is probably with a time complexity of n6

    num_rows = len(mat)
    num_cols = len(mat[0]) -1

    def find_rectangles_as_ones(top,bottom,left,right):
        for row in range(top,bottom+1):
            for col in range(left,right+1):
                if mat[row][col]==0:
                    return False
        return True

    largest_area = 0
    for top in range(len(mat)):
        for bottom in range(top,len(mat)):
            for left in range(0,len(mat[0])):
                for right in range(0,len(mat[0])):
                    if find_rectangles_as_ones(top,bottom,left,right):
                        width = right - left + 1
                        height = bottom - top + 1
                        area = width*height
                        largest_area = max(area,largest_area)

    return largest_area

def on3(matrix):

    num_of_rows = len(matrix)
    num_of_cols = len(matrix[0])
    col_heights = [[0]*num_of_cols]
    largest = 0

    for row in num_of_rows:
        for col in num_of_cols:
            if matrix[row][col]==0:
                col_heights[col]=0
            else:
                col_heights=col_heights+1

    for col in col_heights:
        height = col_heights[col]

        #find the left most edge
        left = col
        while left-1>=1 and col[left-1]>=height:
            left = left - 1

        right = col
        while right+1>=1 and col[right+1]>=height:
            right = right + 1


        width = right - left + 1
        area = width*height
        largest = max(area,largest)

    return largest

def find_largest_area_skyline(skyline):

    left_candidates = []
    skyline = skyline + [0]
    num_buildings=len(skyline)
    candidates = collections.namedtuple('candidates',['index','height'])

    for right in range(num_buildings):
        height = skyline[right]
        next_left = right
        while left_candidates and left_candidates[-1].height >=height:
            left = left_candidates[-1].index
            width  = right - left
            area = width * left_candidates[-1].height
            largest = max(area,largest)
            next_left = left
        left_candidates.append('candidates',index=next_left,height=height)

    return largest






def dp_with_stack(matrix):

    num_rows = len(matrix)
    num_cols = len(matrix[0])
    col_heights=[[0]*num_cols]
    largest = 0

    for row in range(num_rows):
        for col in range(num_cols):
            if matrix[row][col]==0
                col_heights = 0
            else:
                col_heights=col_heights+1

    area = find_largest_rectangle_skyline(heights)
    largest = max(largest,area)

    return largest


