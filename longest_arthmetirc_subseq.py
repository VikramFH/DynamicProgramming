def longest_arthimetic_subsequence(numbers):

    #edge cases
    if not numbers:
        return 0

    if numbers<=2:
        return 1

    best_global_len = 0
    best_len_step_dict = [{} for _ in numbers]

    for index,element in enumerate(numbers):
        for i in range(index):
            step = element - numbers[i]
            #There are two options either extend an existing seq or create a new seq
            seq_len = 2
            extend_seq_len = 1 + best_len_step_dict[index].get(step,0)
            max_len_at_index = max(seq_len,extend_seq_len)
            best_len_step_dict[i][step]=max_len_at_index
            best_global_len = max(best_global_len,best_len_step_dict[i][step])

    return best_global_len
