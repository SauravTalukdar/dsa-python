# Problem: Climbing Stairs
# LeetCode: #70
# Difficulty: Easy
# Time Complexity: O(n) — both approaches
# Space Complexity: O(n) — memo dictionary / steps array
# Approach 1: Memoization (top down) — recursive
# Approach 2: DP Table (bottom up) — iterative, fill array from base cases
# Pattern: Fibonacci — ways(n) = ways(n-1) + ways(n-2)
# Base cases: 1 step = 1 way, 2 steps = 2 ways

class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        def climb(i):
            if i <= 0:
                return 0
            if i == 1:
                return 1
            if i == 2:
                return 2
            if i in memo:        
                return memo[i]
            else:
                memo[i] = climb(i-1) + climb(i-2)
            return memo[i]
        return climb(n)    

class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        steps = [0] * (n+1)
        steps[1] = 1
        steps[2] = 2
        for i in range(3,n+1):
            steps[i] = steps[i-1] + steps[i-2]
        return steps[n]    
                 