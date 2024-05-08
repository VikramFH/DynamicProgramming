# There are variables step {1,3,5}
# What are the different ways to climb stairs

def calculate_number_of_paths(n,variable_steps):

    index_at_steps = [0]*len(n+1)
    index_at_steps[0] = 1
    index_at_steps[1] = 1

    for i in range(2,len(index_at_steps)):
        for v in variable_steps:
            if i-v>0:
                index_at_steps[i] += index_at_steps[i-v]

    return index_at_steps[n]
