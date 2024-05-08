def top_down_on2(maze):
    num_of_rows = len(maze)
    num_of_cols = len(maze[0])
    WALL=1

    @lru_cache(maxsize=None)
    def count_number_paths(row,col):

        if col<0 or row<0 or maze[row][col]==WALL:
            return 0:
        if row==0 and col==0:
            return 1

        paths_from_the_left =  coun_number_paths(row,col-1)
        paths_from_the_top =  coun_number_paths(row-1,col)
        total_paths = paths_from_the_left + paths_from_the_top
        return total_paths


    return count_number_paths(num_of_rows-1,num_of_cols-1)


def bottom_up_on2(maze):
    num_of_rows = len(maze)
    num_of_cols = len(maze([0]))
    WALL = 1

    num_of_paths_to_cell =  [[0] * num_of_cols for _ in range(num_of_rows)]

    for row in range(num_of_rows):
        for col in range(num_of_cols):
            if maze[row][col]== 1:
                num_of_paths_to_cell[row][col]=0

            elif row==0 and col==0:
                num_of_paths_to_cell[row][col]=1

            else:
                if row>0:
                    num_from_above = num_of_paths_to_cell[row-1][col]
                else:
                    num_from_above =0
                if col>0:
                    num_from_left = num_of_paths_to_cell[row][col-1]
                else:
                    num_from_left=0
                num_of_paths_to_cell[row][col] = num_from_above + num_from_left


    return num_of_paths_to_cell[-1][-1]
