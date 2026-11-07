# Problem: Edit Distance
# LeetCode: #72
# Difficulty: Medium
# Time Complexity: O(m*n)
# Space Complexity: O(m*n) for memoization plus recursion stack
# Approach: Memoization

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        memo = {}
        def recurse(i1=0,i2=0):
            key = i1,i2
            if key in memo:
                return memo[key]
            elif i1 == len(word1):
                memo[key] = len(word2) - i2
            elif i2 == len(word2):
                memo[key] = len(word1) - i1
            elif word1[i1] == word2[i2]:
                memo[key] = recurse(i1+1,i2+1)
            else:
                memo[key] = 1 + min(recurse(i1+1,i2),recurse(i1+1,i2+1),recurse(i1,i2+1))
            return memo[key]
        return recurse(0,0)                            
        