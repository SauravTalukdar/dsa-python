# Problem: Number of times a sorted list was rotated
# Difficulty: Medium
# Time Complexity: O(log n)
# Space Complexity: O(1)
# Approach: Binary search - find index of minimum element compare mid with high to determine which half to search

def rotate(rotated_list):
    low = 0
    high = len(rotated_list) - 1
    while(low<=high):
        mid = (low+high) // 2
        mid_number = rotated_list[mid]
        if low == high:
            return mid
        if rotated_list[mid] > rotated_list[high]:
            low = mid + 1
        else:
            high = mid 
    return - 1

# edge cases
# 1.
print(rotate([5,6,9,0,2,3,4]))
#2.
print(rotate([4,5,6,9,0,2,3]))
#3.
print(rotate([]))
#4.
print(rotate([7,9,1,3,5]))
#5.
print(rotate([3,5,7,9,1]))

