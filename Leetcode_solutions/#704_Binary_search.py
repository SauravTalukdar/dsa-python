# Problem: Binary search
# Leetcode: #704
# Difficulty: Easy
# Time complexity: O(log n)
# Space complexity: O(1)
# Approch: Binary search

def binary_search(nums,target):
    low = 0
    high = len(nums) - 1
    while(low<=high):
        mid = (low+high) // 2
        mid_number = nums[mid]
        if mid_number == target:
            return mid
        elif mid_number < target:
            low = mid + 1
        else:
            high = mid - 1   
    return -1 

# test cases
# 1.Normal case
print(binary_search([-1,0,3,5,9,12], 9))  

# 2.Target not in nums
print(binary_search(nums = [-1,0,3,5,9,12], target = 2))

#3.List is empty
print(binary_search([],3))

#4.Target in first position
print(binary_search([2,5,7,9],2))

#5.Target in last position
print(binary_search([2,5,7,9],9))
