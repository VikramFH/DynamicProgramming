import collections


def largest_rectangle_skyline(array_heights):
#This is an o(n3) soln because there two for loops and min height at each step.
    if not array_heights:
        return 0

    num_builidings=len(array_heights)

    largest = 0

    for left in range(num_builidings):
        for right in range(left,num_builidings):
            min_height = min(array_heights[left:right+1])
            area = min_height * len(array_heights[left:right+1])
            largest = max(area,largest)

    return largest

def largest_rectangle_skyline_dp(array_heights):

    if not array_heights:
        return 0

    num_buildings = len(array_heights)
    largest = 0
    for left in range(num_buildings):
        height = array_heights[left]
        for right in range(left,num_buildings):
            width = right - left + 1
            height = min(height,array_heights[right])
            area = width * height
            largest = max(largest,area)

    return largest

def lrs_dp_stacking(skyline):
    #pad 0s on the skyline, to avoid cleanup with left_candidates at
    # the end of each iteration.

    skyline = skyline + [0]
    num_buildings = len(skyline)
    candidate = collections.namedtuple('candidates',['index','height'])

    left_candidates=[]
    largest_area=0

    for right in range(num_buildings):
        height = skyline[right]
        #left pointer of the next candidate to be created
        next_left = right

        while left_candidates and left_candidates[-1].height >= height:
            # update area
            # We remove the rectangle starting left and ending at right-1. It has height left_candidates[-1].height
            left = left_candidates[-1].index
            width = right - left
            area = width*left_candidates[-1].height
            largest_area = max(area,largest_area)
            #Possible next candidate  by trimming down the building.
            next_left = left
            del left_candidates[-1]
        left_candidates.append(candidate(index=next_left,height=height))

    return largest_area

