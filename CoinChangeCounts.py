
def coin_change_count(amount,coins):

    @lru_cache(mazsize=None)
    def helper(amount):
        if amount==0:
            return 1
        if amount<0:
            return 0

        num_of_ways = 0
        for coin in coins:
            num_of_ways = num_of_ways+coin_change_count(amount-coin)
        return num_of_ways

    return helper(amount)


def count_ways_to_pay_combinations(amount,coins):

    @lru_cache(maxsize=None)
    def helper(index,amount):

        coin = coins[index]

        if amount==0:
            return 1

        if amount<0 or len(index)==coins:
            return 0
        num_ways=0
        for repeat in range(amount//coin+1):
            payments = repeat*coin
            num_ways =+ helper(index+1,amount-payments)
        
        return num_ways
    index = 0
    return helper(index,amount)