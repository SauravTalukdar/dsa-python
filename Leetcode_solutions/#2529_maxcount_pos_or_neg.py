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

# Approch: Binary search for finding last negative and finding first positive
def maximum(nums):
    def neg(nums):
        low = 0
        high = len(nums) - 1
        result = -1
        while(low<=high):
            mid = (low+high) // 2
            mid_number = nums[mid]
            if mid_number < 0:
                result = mid
                low = mid + 1
            else:
                high = mid - 1            
        return result 

    def pos(nums):
        low = 0
        high = len(nums) - 1
        result = len(nums)
        while(low<=high):
            mid = (low+high) // 2
            mid_number = nums[mid]
            if mid_number > 0:
                result = mid
                high = mid - 1
            else:
                low = mid + 1    
        return result     

    negative = neg(nums) + 1
    positive = len(nums) - pos(nums) 
    return max(negative,positive)


print(maximum([-2,-1,-1,1,2,3]))
print(maximum([-3,-2,-1,0,0,1,2]))
print(maximum([5,20,66,1314]))
print(maximum([0,0,0]))
   


            




           
