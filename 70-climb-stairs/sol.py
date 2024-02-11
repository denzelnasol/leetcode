# You are climbing a staircase. It takes n steps to reach the top.

# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

 

# Example 1:

# Input: n = 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps

# n = 38

class Solution:
    def climbStairsDP(self, n: int) -> int:
        
        if n == 0: 
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 2
        
        dp = [0] * (n + 1)
        dp[1] = 1
        dp[2] = 2
        
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
            
        return dp[n]
    
    def climbStairsMap(self, n: int) -> int:

        memo = {}
        memo[1] = 1
        memo[2] = 2
        
        def climb(n):
            if n in memo:
                return memo[n]
            else: 
                memo[n] = climb(n - 1) + climb(n - 2)
                return memo[n]
            
            
        return climb(n)
            
    
sol = Solution()
print(sol.climbStairsDP(100))
print(sol.climbStairsMap(100))