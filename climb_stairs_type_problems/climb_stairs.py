
def top_down(number_of_stairs):

    if number_of_stairs<=1:
        return 1

    using_1_step = top_down(number_of_stairs-1)
    using_2_step = top_down(number_of_stairs-2)
    total_steps = using_2_step+using_1_step

    return total_steps

def bottom_down(n):

    #this is an o(n) in time complexity and space complexity

    # define an array with each index being total number of way to climb the ith stair..

    number_of_stairs = [0]*len(n)

    #climb the 0th stair
    number_of_stairs[0]=0
    number_of_stairs[1]=1

    for i in range(2,n+1):
        number_of_stairs_1_step = number_of_stairs[i-1]
        number_of_stairs_2_step = number_of_stairs[i-2]
        number_of_stairs[i] =  number_of_stairs_1_step + number_of_stairs_2_step

    return number_of_stairs[n]

def bottom_down_optimized(n):
    #This is the same solution but with o(1) space
    #This removes the need for storing the index

    if n<=1:
        return 1

    num_paths_prev = 1
    num_paths_current = 1

    for i in range(2,n+1):
        num_paths_1_step = num_paths_current
        num_paths_2_step = num_paths_prev
        num_paths_prev = num_paths_current
        current_path = num_paths_1_step + num_paths_2_step

    return current_path

