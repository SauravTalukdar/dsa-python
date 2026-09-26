# Problem: Longest Common Subsequence
# LeetCode: #1143
# Difficulty: Medium
# Time Complexity: O(n1 * n2)
# Space Complexity: O(n1 * n2) — 2D table
# Approach: DP table — table[i][j] = LCS of first i chars and first j chars
# Base case: row 0 and column 0 = 0 (empty string)

#test cases
T0 = {
    'input': {
        'text1': 'abcde',
        'text2': 'ace'
    },
    'output': 3
}

T1 = {
    'input': {
        'text1': [1, 3, 5, 6, 7, 2, 5, 2, 3],
        'text2': [6, 2, 4, 7, 1, 5, 6, 2, 3]
    },
    'output': 5
}

T2 = {
    'input': {
        'text1': 'longest',
        'text2': 'stone'
    },
    'output': 3
}

T3 = {
    'input': {
        'text1': 'abc',
        'text2': 'def'
    },
    'output': 0 #there are no common subsequence so the empty sequence is a subsequence
}

T4 = {
    'input': {
        'text1': 'dense',
        'text2': 'condensed'
    },
    'output': 5
}

T5 = {
    'input': {
        'text1': '',
        'text2': 'opkpoiklklj'
    },
    'output': 0
}

T6 = {
    'input': {
        'text1': '',
        'text2': ''
    },
    'output': 0
}

T7 = {
    'input': {
        'text1': 'abc',
        'text2': 'abc'
    },
    'output': 3
}

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n1,n2 = len(text1),len(text2)
        table = [[0 for x in range(n2+1)] for x in range(n1+1)]
        for i in range(n1):
            for j in range(n2):
                if text1[i] == text2[j]:
                    table[i+1][j+1] = 1 + table[i][j]
                else:
                     table[i+1][j+1] = max(table[i][j+1],table[i+1][j])
        return table[-1][-1]                  
        