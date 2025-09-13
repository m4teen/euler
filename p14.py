def collatz(n):
    """
    Compute the starting number under a given limit that produces the longest Collatz chain.

    According to the Collatz (3n + 1) problem, define a sequence for any positive integer n:
        • If n is even, next term = n / 2.
        • If n is odd, next term = 3n + 1.
    The sequence terminates once it reaches 1 (though intermediate values may exceed the starting bound).

    Parameters:
        limit (int): The exclusive upper bound for starting numbers (i.e. consider all starting n with 1 ≤ n < limit).

    Returns:
        int: The number < limit that produces the longest Collatz chain.
             If multiple starting numbers produce chains of the same maximal length, returns the smallest such starting number.

    Preconditions:
        • limit ≥ 1.
        • All arithmetic fits within integer range (or uses a type that can handle large intermediate values).
        • It is assumed (though not proved) that every starting number’s Collatz sequence terminates at 1.

    Behaviour / Approach:
        • For each integer n from 1 up to limit−1, generate its Collatz sequence, counting the number of terms until 1 (inclusive).
        • Maintain the maximum chain length seen so far, and the corresponding starting number.
        • Optimisations may include caching previously computed chain lengths (memoisation) to avoid redundant computation.

    Complexity:
        Time: O(n × [average cost to compute one chain]). 
        Space: O(n).
    """
    chains = {}

    for i in range(n-1,1,-1):
        chain = [i]
        startnum = i
        while i != 1:
            if i % 2 == 0:
                i = i//2 
                if i in chains:
                    chain.extend(chains[i])
                    break
                else:
                    chain.append(i)
            else:
                i = 3*i + 1
                if i in chains:
                    chain.extend(chains[i])
                    break
                else:
                    chain.append(i)
        
        chains[startnum] = chain

    maxl = 0
    answer = None
    for key, value in chains.items():
        if len(value) > maxl:
            maxl = len(value)
            answer = key

    return answer


        