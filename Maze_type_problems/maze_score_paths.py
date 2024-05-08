

def bottom_up_on2(maze):

    num_of_rows = len(maze)
    num_of_cols = len(maze[0])
    IMPOSSIBLE=-1
    WALL=1
    best_score_cells = [[IMPOSSIBLE]*num_of_cols for _ in range(num_of_rows)]

    for row in range(num_of_rows):
        for col in range(num_of_cols):

            if maze[row][col]==WALL:
                best_score_cells[row][col]=IMPOSSIBLE

            if row=0 and col=0:
                best_score_cells[row][col]=1

            else:
                if row>0:
                    best_from_above = best_score_cells[row-1][col]
                else:
                    best_from_above = IMPOSSIBLE

                if col>0:
                    best_from_left = best_score_cells[row][col-1]
                else:
                    best_from_left = IMPOSSIBLE

                winner_at_cell = max(best_from_above,best_from_left)

                if winner_at_cell!=IMPOSSIBLE:
                    best_score_cells[row][col]=winner_at_cell+maze[row][col]
                else:
                    best_score_cells[row][col]=IMPOSSIBLE

    return best_score_cells[-1][-1]

def bottom_up_linear_space_on2time(maze):

    IMPOSSIBLE=-1
    WALL=1
    num_of_rows=len(maze)
    num_of_cols=len(maze[0])

    best_score_prev_row = [IMPOSSIBLE]*num_of_cols
    best_score_next_row = [IMPOSSIBLE]*num_of_cols

    for row in range(num_of_rows):
        for col in range(num_of_cols):
            if maze[row][col]==WALL:
                best_score_next_row=IMPOSSIBLE

            if row=0 and col=0:
                best_score_next_row[col]=maze[row][col]

            else:
                if row>0:
                    best_from_left = maze[row][col] + best_score_prev_row[col]
                else:
                    best_from_left = IMPOSSIBLE
                if col>0:
                    best_from_top = maze[row][col] + best_score_prev_row[col-1]
                else:
                    best_from_top = IMPOSSIBLE

                winner_at_cell = max(best_from_left,best_from_top)
                if winner_at_cell!=IMPOSSIBLE:
                    best_score_next_row[col]=winner_at_cell
                else:
                    best_score_next_row[col]=IMPOSSIBLE

        best_score_prev_row,best_score_next_row = best_score_next_row,best_score_prev_row

    return best_score_next_row[-1]


