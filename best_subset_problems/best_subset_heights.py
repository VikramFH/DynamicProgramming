def best_subset_height(people,head):

    if len(people)<=head:
        return sum(people)

    starting_range = head
    ending_range = 0
    eligibile_head = sum(people[0:starting_range])
    best_head = eligibile_head

    while ending_range<=head:
        starting_range = starting_range - 1
        ending_range = ending_range + 1
        eligibile_head = eligibile_head - people[starting_range]
        eligibile_head = eligibile_head + people[-ending_range]
        best_head = max(eligibile_head,best_head)

    return best_head