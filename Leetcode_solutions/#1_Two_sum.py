# the brute for way to do it

def two_sum(nums,target):
    last = len(nums)
    for i in range((last)):
        for j in range(i+1,last):
            if nums[i] + nums[j] == target:
                return [i,j]
    return -1 

# test cases

# 1.
nums = [2,7,11,15]
target = 9
print(two_sum(nums,target))

#2.
nums = [3,2,4]
target = 6
print(two_sum(nums,target))

#3.
nums = [3,3]
target = 6
print(two_sum(nums,target))

#4.
nums = [2,7,11,15]
target = 13
print(two_sum(nums,target))

#5.
nums = []
target = 6
print(two_sum(nums,target))



           


