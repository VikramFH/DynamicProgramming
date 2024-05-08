# GPT Q:
# You are given an array of positive integers where each integer represents the height of a vertical line on a graph.
# Write a function to compute the maximum area of water that can be contained between these lines.
#
# Example:
#
# Input: [1,8,6,2,5,4,8,3,7]
# Output: 49

#1..8...6..2...5...4..8..3

# We have to look at left and right
# We might have to start fresh whenever the height reduces
# We need to have a largest area to track and always have a max to estimate between the current iteration
# and the past largest

import collections


def brute_force_on2(containers):
    num_of_containers = len(containers)
    largest = 0

    for left in range(num_of_containers):
        for right in range(left,num_of_containers):
            width = right - left
            height = min(containers[left],containers[right])
            area = width*height
            largest = max(largest,area)

    return largest

def optimal(containers):

    start = 0
    end = len(containers) - 1
    largest_area = 0

    while start<end:
        height = min(containers[start],containers[end])
        width = end - start
        area = height * width
        largest_area = max(largest_area,area)

        if containers[start]<containers[end]:
            start = start + 1
        else:
            end = end - 1

    return largest_area





























