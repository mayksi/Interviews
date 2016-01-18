'''
Write a method to compute number of ways for choosing 'k' objects from 'n' objects
(Question ends here)

# Key Ideas:

1) Binomial Coefficient => n!/((n-k)!*k!)
    -- Although the final answer may fit well within an integer range, the individual values of the terms may overflow
2) Next we should conside Pascal's Triangle to see how we can use it to compute 'k choose n'
   In Pascal's Triangle every digit is sum of two digits directly above it
   (https://en.wikipedia.org/wiki/Pascal%27s_triangle)
                                        1
                                    1       1
                                1       2       1
                            1       3       3       1
                        1       4       6       4       1
                    1       5       10      10      5       1
3) Recurrence relationship for calculating 'k choose n'
   Think about 'n'th object being in 'k' objects chosen from 'n' objects. Then there are two cases:
   i) If the nth object is present in k objects, then the number of ways this subset can formed is ('k-1' choose 'n-1')
   ii) If the nth object is NOT present in k objects, then the number of ways this subset can be formed is ('k' choose 'n-1')

   Hence, (k choose n) = (k-1 choose n-1) + (k choose n-1)

   Base Condition:
   1) Left Term => 0 choose (n-k) = 1 or 1 choose (n-k) = n - k, since there is exactly 1 way to choose 0 out of (n-k) objects i.e. empty set
   2) k choose k = 1, since there is exactly 1 way to choose k out of k objects i.e. all the objects
'''

def findBinomialCoefficient(N, K):
    '''
    '''
    # initialization
    lookupTable = []
    for i in range(0, N+1):
        lookupTable.append([1])

    for n in range(1, N+1):
        k = 1
        while k < n and k <= K:
            lookupTable[n].append(lookupTable[n-1][k-1]+lookupTable[n-1][k])
            k += 1
        if k == n and k <= K:
           lookupTable[n].append(1) # for n == k

    # print table
    return lookupTable[-1][-1]


print findBinomialCoefficient(5, 3)
print findBinomialCoefficient(5, 4)