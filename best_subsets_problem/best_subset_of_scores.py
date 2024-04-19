def best_subset_of_score(scores,rank):

    #example : scores [85,92,78,95,88]

    #score_bottom and score_top

    if rank>=len(scores):
        return sum(scores)

    score_bottom = rank
    score_top = 0
    candidates_score = sum(scores[0:score_bottom])
    best_candidates_score = candidates_score

    while score_top <= rank:
        score_bottom = score_bottom - 1
        score_top = score_top+1
        candidates_score = candidates_score - scores[score_bottom]
        candidates_score = candidates_score + scores[-score_top]
        best_candidates = max(candidates_score,best_candidates)

    return best_candidates



