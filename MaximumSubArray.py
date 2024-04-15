
def calc_max_sub_array(input):

    #I cant sort them
    # This is prefix sum problem
    #create an empty chunk and keep adding element to the empty chunk.
    # if the chunk result is negative then start adding the new element and initate the new element as
    # a chunk again.
    #[1,1,1,-4,5,2]


    best_chunk = -float('inf')
    previous_chunk = -float('inf')

    if input.empty():
        return 0

    for i in input:
        if chunk<0:
            chunk = i
        else:
            chunk = previous_chunk+i
        best_chunk = max(chunk,best_chunk)
        previous_chunk = chunk

    return best_chunk