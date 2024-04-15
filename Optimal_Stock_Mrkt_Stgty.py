#Top Down Approach

def max_profit(daily_price):
    @lru_cache(maxsize=None)
    def get_best_profit(day,have_stock):
        """
        Returns the best profit that can be obtained by the end of the day
        at the end of the day:
        if have_stock is true, the trader must own the stock.
        if have_stock is false,the trader must have sold the stock
        """

        if day<0:
            if not have_stock:
                #Initial state have no stock or profit
                return 0
            else:
                #We are not allowed to have initial stock.
                #Add a very large penalty to eliminate this option.
                return -float('inf')

        price = daily_price[day]
        if have_stock:
            strategy_buy = get_best_profit(day - 1,False) - price
            strategy_hold = get_best_profit(day - 1,True)
            return max(strategy_hold,strategy_buy)
        else:
            #We can reach this state by selling or avoiding.
            strategy_sell = get_best_profit(day - 1,True) + price
            strategy_avoid = get_best_profit(day - 1,False)
            return max(strategy_sell,strategy_avoid)

    last_day = len(daily_price) - 1
    no_stock = False
    return get_best_profit(last_day,no_stock)

## Bottom Up Approach

Class BottomUp:
    def __init__():
        pass

    def max_profit(daily_price):
        #Initital State: Start from a reference cash amount
        #It can be of any value
        #We use 0 and our cash to go below 0 if we use that to buy an expensive stock
        cash_not_owning_share = 0
        #High penalty for owning a stock initially
        #ensure this option is never chosen
        cash_owning_share = -float('inf')

        for price in daily_price:
            # Transitions to the current day  owning stock:
            strategy_buy = cash_not_owning_share - price
            strategy_hold = cash_owning_share
            #Tranisitions to the current_day owning the stoch
            strategic_sell =  cash_owning_share + price
            strategic_avoid = cash_not_owning_share
            #compute the new_states
            cash_owning_share = max(strategy_buy,strategy_hold)
            cash_not_owning_share = max(strategic_avoid,strategic_sell)

        #The profit is the final amount since we start from a ref of 0
        return cash_not_owning_share
        #Space Complexity is o(1) and time complexity is 0(n)

Class _withBudget:
    def __init__(self):
        pass

    def max_daily_profit(self,daily_price,budget):

        #Basically there are two states one with cash_with_shares and cash_wihout_shares

        cash_without_shares = budget
        cash_with_shares = -float('inf')

        for price in daily_price :
            buy = cash_without_shares - price
            sell = cash_with_shares + price
            hold = cash_with_shares
            avoid = cash_without_shares

            cash_with_shares = max(hold,buy)
            if cash_with_shares < 0:
                cash_with_shares  = -float('inf')

            cash_without_shares = max(avoid,sell)

        return cash_without_shares - budgets

Class TXLimits:

    def __init__(self):
        pass

    def maxdailyprofits(self,daily_price,tx_limits):

        cash_with_shares= [-float('inf')]*(tx_limits+1)
        cash_without_shares = [-float('inf')]*(tx_limits+1)

        cash_without_shares[0]=0

        for price in daily_price:
            cash_without_shares_next = [-float('inf')]*(tx_limits+1)
            cash_with_shares_next = [-float('inf')]*(tx_limits+1)
            for prev_count in range(tx_limits):
                buy = cash_without_shares_next[prev_count] - price
                sell = cash_with_shares_next[prev_count] + price
                avoid = cash_without_shares_next[prev_count]
                hold  = cash_with_shares[prev_count]

                if prev_count <tx_limits:
                    cash_without_shares_next[prev_count +1]=max(cash_without_shares[prev_count+1],sell)

                cash_without_shares_next[prev_count]=max(cash_without_shares_next[prev_count],avoid)
                cash_with_shares_next[prev_count] =max(cash_with_shares_next[prev_count],hold,buy)
            cash_with_shares = cash_with_shares_next
            cash_without_shares = cash_without_shares_next

        return max(cash_without_shares)
