
import inspect
from collections import deque

def stack_depth():
    return len(inspect.getouterframes(inspect.currentframe())) - 1

def make_coin_change(amount,coins):

    print("{indent} stack depth {amount}".format(indent=" "*stack_depth(),amount=amount))

    @lru_cache(maxsize=None)
    def helper(amount):
        if not amount:
            return []

        if amount<0:
            return None

        optimal_solution=None
        for coin in coins:

            partial_solution =  make_coin_change(amount-coin,coins)
            if partial_solution is None:
                continue

            candidate = partial_solution + [coin]

            if optimal_solution is None or len(candidate)<len(optimal_solution):
                optimal_solution=candidate

        return optimal_solution

    return helper(amount)

#Bottom up
def make_change(amount, coins):
    # solutions[k] is the optimal list of coins that add up to k or None if no solution shows up to k.
    solutions = [None] * (amount + 1)
    # initial state: no coins needed to pay for amount 0
    solutions[0] = []
    # starting from amount 0, find ways to pay higher amount to hit the amount to be paid.
    paid = 0

    # Create a table to visualize the solutions
    table = [[' ']*(amount + 1) for _ in range(len(coins) + 2)]
    table[0] = list(range(amount + 1))
    table[1][0] = '0'

    # Example: 10 coins [5, 2, 1]
    while paid < amount:
        if solutions[paid] is not None:
            for coin in coins:
                next_paid = paid + coin
                if next_paid > amount:
                    continue

                if (solutions[next_paid] is None or len(solutions[next_paid]) > (len(solutions[paid]) + 1)):
                    solutions[next_paid] = solutions[paid] + [coin]


        paid = paid + 1

    # Print visualization table

    return solutions[amount]

def simple_coin_change(amount,coins):

    solutions = {0:[]}
    amounts_to_be_paid = deque([0])

    while amounts_to_be_paid:
        paid = amounts_to_be_paid.popleft()
        solution = solutions[paid]

        if amount==paid:
            return solution
        else:
            for coin in coins:
                next_paid = paid+coin
                if next_paid > amount:
                    continue
                if next_paid not in solutions:
                    solutions[next_paid]=solution+[coin]
                    amounts_to_be_paid.append(next_paid)
    return None


if __name__=="__main__":
    amount=10
    coins=[5,2,1]
    print(simple_coin_change(amount,coins))