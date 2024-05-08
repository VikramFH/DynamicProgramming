
#coins = [1,2,5]
#amount = 10

def make_change(amount,coins):

    if not amount:
        return []

    if amount<0:
        return None

    optimal=None
    for coin in coins:
        partial = make_change(amount-coin,coins)
        if partial is None:
            continue
        candidate = partial+[coin]
        if optimal is None or len(candidate)<len(optimal):
            optimal = candidate

    return optimal



from functools import lru_cache
def make_change_lru(amount,coins):

    @lru_cache(maxsize=None)
    def helper(amount):
        if amount<0:
            return None
        if not amount:
            return []

        optimal_candidate = None

        for coin in coins:
            partial_candidate = make_change(amount - coin,coins)
            if partial_candidate is None:
                continue
            candidate = partial_candidate+[coin]
            if optimal_candidate is None or len(candidate)<len(optimal_candidate):
                optimal_candidate=candidate
        return optimal_candidate

    return helper(amount)

def make_change_bp(amount,coins):

    solutions = [None]*amount
    solutions[0] = []

    paid = 0
    while paid<amount:
        if solutions[paid] is not None:
            for coin in coins:
                next_paid = paid + coin
                if next_paid > amount:
                     continue

                if (solutions[next_paid] is not None or len(solutions[next_paid])>len(solutions[paid])+1):
                    solutions[next_paid]=solutions[paid]+[coin]
        paid = paid + 1
    return solutions[paid]


import collections

def make_coin_change(amount,coins):

    solutions = {0:[]}
    amounts_to_be_handled = collections.deque([0])

    while amounts_to_be_handled:
        paid = amounts_to_be_handled.popleft()
        solution = solutions[paid]

        if solution==amount:
            return solution

        for coin in coins:
            next_paid = paid + coin
            if next_paid > amount:
                continue
            if next_paid not in solutions:
                solutions[next_paid]=solution +[coin]
                amounts_to_be_handled.append(next_paid)

    return None








