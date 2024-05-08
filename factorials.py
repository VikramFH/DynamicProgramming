
def factorial(n,dp):

    """

    :param n: number to calc the factorial
    :param dp: list to store subproblems
    :return: factorial result
    """
    if n==0:
        return 1

    if dp[n]!=-1:
        return dp[n]

    dp[n] = n * factorial(n,dp)
    return dp[n]

if __name__=="__main__":
    dp = [-1 for i in range(101)]

