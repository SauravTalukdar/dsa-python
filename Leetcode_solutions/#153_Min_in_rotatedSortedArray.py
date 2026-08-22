# Problem: Find Minimum in Rotated Sorted Array
# LeetCode: #153
# Difficulty: Medium
# Time Complexity: O(log n)
# Space Complexity: O(1)

# Approach 1 - neighbour comparison
# requires mid > 0 boundary check, needed extra return statement for edge case

def findmin_v1(nums):
    low = 0
    high = len(nums) - 1
    while(low<=high):
        mid = (low+high) // 2
        mid_number = nums[mid]
        if mid > 0 and mid_number < nums[mid - 1]:
            return mid_number
        elif mid_number > nums[high]:
            low = mid + 1
        else:
            high = mid - 1
    return nums[low] #this method wont handle case 6 (only one element)       

# Approach 2 - mid vs high comparison  
# cleaner, handles all cases through same logic, no patches needed

def findmin_v2(nums):
    low = 0
    high = len(nums) - 1
    while(low<=high):
        mid = (low+high) // 2
        mid_number = nums[mid]
        if low == high:
            return mid_number
        elif mid_number > nums[high]:
            low = mid + 1
        else:
            high = mid 
    return -1        

# test_cases
#1.
print(findmin_v2([11,12,13,15,17]))                               
#2.
print(findmin_v2([3,4,5,1,2]))                                                     
#3.
print(findmin_v2([4,5,6,7,0,1,2]))                                                            
#4.
print(findmin_v2([12,13,15,17,10]))  
#5.
print(findmin_v2([]))
#6.  
print(findmin_v2([1]))  
                             