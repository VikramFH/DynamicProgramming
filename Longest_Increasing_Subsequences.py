def increasing_longest_subsequnce(numbers):

    if not numbers:
        return 0

    longest_subsequence_at = []

    for number in numbers:
        best_seq = [number]
        for seq in longest_subsequence_at:
            if seq[-1]<number:
                if len(seq)+1>len(best_seq):
                    best_seq = seq + [number]
        longest_subsequence_at.append(best_seq)

    return max(longest_subsequence_at,keys=len)