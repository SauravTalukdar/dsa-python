# Problem: Find First and Last Position of Element in Sorted Array
# Leetcode: #34
# Difficulty: Medium
# Time complexity: O(log n)
# Space complexity: O(1)
# Approch: Binary search for both positions

def first_position(nums,target):
    low = 0
    high = len(nums) - 1
    result = -1
    while(low<=high):
        mid = (low + high) // 2
        mid_number = nums[mid]
        if mid_number == target:
                result = mid
                high = mid - 1      
        elif mid_number < target:
            low = mid + 1
        else:
            high = mid - 1
    return result                   
    

def last_position(nums,target):
    low = 0
    high = len(nums) - 1
    result = -1
    while(low<=high):
        mid = (low + high) // 2
        mid_number = nums[mid]
        if mid_number == target:
                result = mid
                low = mid + 1  
        elif mid_number > target:
            high = mid - 1
        else:
            low = mid + 1
    return result

def search(nums,target):
    first = first_position(nums,target)
    last = last_position(nums,target)  
    return [first,last]

# test cases
# 1.
print(search([5,7,7,8,8,10],8))  

# 2.
print(search([5,7,7,8,8,10],6))

# 3.
print(search([], 0))


    




