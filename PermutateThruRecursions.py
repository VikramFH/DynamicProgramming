
arr = ['a','b','c']

#Permutatuins:

def factorial(n):

    if n==0:
        return 1

    if dp[n]!=-1:
        return dp[n]

    dp[n] = n * factorial(n-1)

    return dp[n]

def permutate(arr,l,r):

    if l==r:
        print(arr)
    else:
        for i in range(l,r+1):
            arr[l],arr[i] = arr[i],arr[l]
            permutate(arr,l+1,r)
            arr[l],arr[i] = arr[i],arr[l]

if __name__=="__main__":
    arr = ['a','b','c', 'd']
    print(permutate(arr,0,len(arr)-1))