# Problem: Maximum Count of Positive Integer and Negative Integer
# Leetcode: #2529
# Difficulty: Easy
# Time complexity: O(n)
# Space complexity: O(1)
# Approch: Brute force

def max_count(nums):
    pos = 0
    neg = 0
    for i in nums:
        if i < 0:
            neg += 1
        elif i > 0:
            pos += 1

    return max(pos,neg)  

print(max_count([-2,-1,-1,1,2,3]))
print(max_count([-3,-2,-1,0,0,1,2]))
print(max_count([5,20,66,1314]))



           
