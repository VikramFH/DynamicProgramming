# There are variables step {1,3,5}
# What are the different ways to climb stairs

def calculate_number_of_paths(n,variable_steps):

    number_of_paths = [0]*len(n+1)
    number_of_paths[0] = 1

    for i in range(1,n+1):
        for step in variable_steps:
            if i - step>=0:
                number_of_paths[i]=number_of_paths[i]+number_of_paths[i-step]

    return number_of_paths[n]
