# Problem: Search in Rotated Sorted Array
# Leetcode: #33
# Difficulty: Medium
# Time complexity: O(log n)
# Space complexity: O(1)

# Approch: Brute force solution
def search_v1(nums,target):
    position = 0
    while(position<len(nums)):
        if nums[position] == target:
            return position
        position +=1
    return -1 

# Approch: Binary search solution

def search(nums,target):
    low = 0
    high = len(nums) - 1
    while(low<=high):
        mid = (low+high) // 2
        mid_number = nums[mid]
        if mid_number == target:
            return mid
        elif mid_number >= nums[low]: #check if the left half is sorted(including mid)
            if nums[low] <= target < nums[mid]: #check if target in this half
                high = mid - 1 #if it is search the left half
            else: #if its not search the left half(unsorted at first,but when loop runs again it also has a part which is sorted)
                low = mid + 1
        elif mid_number < nums[low]: #check if the right half is sorted
            if nums[mid] < target <= nums[high]: #check if target is in this half
                low = mid + 1 #if it is in right half
            else: #if its not in right half
                high = mid - 1              
    return - 1            


# test cases    
# 1.
print(search([4,5,6,7,0,1,2],0))          
#2.
print(search([4,5,6,7,0,1,2],3))          
#3.
print(search([1],0))          
#4.
print(search([],3))          
#5.
print(search([4,5,6,7,0,1,2],4))          
#6.
print(search([4,5,6,7,0,1,2],2))          