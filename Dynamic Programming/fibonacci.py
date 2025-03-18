def fib(self, n):
        """
        :type n: int
        :rtype: int
        """

        # # Solving the question using dynamic programming
        # dp = [0] * (n + 1)
        # def helper(n):
        #     if n <= 1:
        #         return n
        #     if dp[n] != 0:
        #         return dp[n]
        #     dp[n] = helper(n - 1) + helper(n - 2)
        #     return dp[n]
        # return helper(n)

        # Solving the question using recursio O(1) space

        prev = 1
        prev_two = 0
        solution = 1
        for i in range(2,n+1):
                solution = prev + prev_two
                prev_two = prev
                prev = solution
        return solution
                


fib(5)