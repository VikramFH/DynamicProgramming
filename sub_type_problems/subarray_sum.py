def subarray_sum_brute(array_list,queries):
    #time/space complexity of o(m*n)
    sum_array=[]

    for start,end in queries:
        sum_array.append(sum(array_list[start:end]))

    return sum_array

def prefix_sum_subarray(array_list,queries):

    prefix_list = [0]*len(array_list)

    for i in range(len(array_list)):
        if i==0:
            prefix_list[i] = array_list[i]
        else:
            prefix_list[i] = prefix_list[i-1] + array_list[i]

    result = []
    for start,end in queries:
        result_per_element = prefix_list[end] - prefix_list[start]
        result.append(result_per_element)


    return result 
