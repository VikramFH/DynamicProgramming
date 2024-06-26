
def get_pairs(arr,target):

    window_sum = 0
    left = 0
    for right,number in enumerate(arr):
        window_sum = window_sum + arr[right]

        while window_sum > target:
            window_sum=window_sum - arr[left]
            left = left + 1

        if window_sum==target:
            return (left,right)

def find_min_length(arr,target):

    window_sum = 0
    left = 0
    min_length = float('inf')
    for right,number in enumerate(arr):
        window_sum = window_sum + arr[right]

        while window_sum > target:
            window_sum = window_sum - arr[left]
            left = left + 1

        if window_sum==target:
            length = right - left + 1
            min_length = min(min_length,length)

    return min_length




def find_the_shortest_subarray_with_sum(arr,target):

    result = float('inf')
    window_sum = 0
    left = 0
    min_length_upto = [float('inf')]*len(arr)

    for right,num in enumerate(arr):
        min_length_upto[right] = min_length_upto[right-1]
        window_sum = window_sum + arr[right]

        while window_sum > target:
            window_sum = window_sum - arr[left]
            left = left + 1

        if window_sum==target:
            length = right - left + 1
            result = min(result,min_length_upto[left-1]+length)
            min_length_upto[right] = min(length,min_length_upto[right])

    if result == float('inf'):
        return 0

    return result