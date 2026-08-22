# Problem: Number of times a sorted list was rotated
# Difficulty: Medium
# Time Complexity: O(log n)
# Space Complexity: O(1)
# Approach: Binary search - find index of minimum element compare mid with high to determine which half to search

# version1
def rotate1(rotated_list):
    low = 0
    high = len(rotated_list) - 1
    while(low<=high):
        mid = (low+high) // 2
        if low == high:
            return mid
        if rotated_list[mid] > rotated_list[high]:
            low = mid + 1
        else:
            high = mid 
    return 0

# version2
def rotate2(rotated_list):
    low = 0
    high = len(rotated_list) - 1
    while(low<=high):
        mid = (low+high) // 2
        if mid > 0 and rotated_list[mid] < rotated_list[mid - 1]:
            return mid
        elif rotated_list[mid] > rotated_list[high]:
            low = mid + 1
        else:
            high = mid - 1
    return 0

# edge cases
# 1.
print(rotate1([5,6,9,0,2,3,4]))
#2.
print(rotate1([4,5,6,9,0,2,3]))
#3.
print(rotate1([]))
#4.
print(rotate1([7,9,1,3,5]))
#5.
print(rotate1([3,5,7,9,1]))
#6.
print(rotate1([1]))

# Approach: Brute force(linear search) - find index of minimum element compare mid with high to determine which half to search
def rotated_list(nums):
    position = 0
    while(position<len(nums)):
        if position > 0  and nums[position] < nums[position - 1]:
            return position
        position +=1
    return 0

           

