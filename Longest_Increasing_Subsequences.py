
def longest_increasing_subsequences(numbers):

        longest_subsequences_at = []

        for number in numbers:
            new_seq = [number]
            for seq in longest_subsequences_at:
                if seq[-1]<number:
                    if len(seq)+1<len(new_seq):
                        new_seq = seq + new_seq

            longest_subsequences_at.append(new_seq)

        return max(longest_subsequences_at,key=len)

#optimized nlogn using bisect_left


import bisect
def optimizedLIS(nums):

    sub = [nums[0]]

    for num in nums:
        if sub[-1]<num:
            sub.append(num)
        else:
            index_to_sort = bisect.bisect_left(sub,num)
            sub[index_to_sort] = num

    return len(sub)


