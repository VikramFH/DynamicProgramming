import collections


def expressiosns_with_target_results(numbers,target):

    @lru_cache(maxsize=None)
    def helper(result,index):

        if index == len(numbers):
            if result==target:
                return 1
        return 0

        count_add =  helper(result + numbers[index],index+1)
        count_sub = helper(result - numbers[index], index + 1)
        return count_add + count_sub

    partial_result = numbers[0]
    start_index = 1
    return helper(partial_result,start_index)

def expressiosns_with_target_results(numbers,target):

    @lru_cache(maxsize=None)
    def helper(result,index):

        if index == len(numbers):
            if result==target:
                return 1
        return 0

        count_add = helper(result + numbers[index],index+1)
        count_sub = helper(result - numbers[index], index + 1)
        return count_add + count_sub

    partial_result = numbers[0]
    start_index = 1
    return helper(partial_result,start_index)


def bfs_dp(numbers,target):

    counter_result = collections.Counter({numbers[0]:1})
    index=1
    while index<len(numbers):
        new_counter = collections.Counter()
        for partial_result,count in counter_result.items() :
            new_add = partial_result + numbers[index]
            new_sub = partial_result - numbers[index]
            new_counter[new_add] += count
            new_counter[new_sub] += count
        counter_result = new_counter
        index=index+1
    return counter_result[target]
