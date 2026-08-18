# the brute for way to do it(linearly)
def two_sum(nums,target):
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i] + nums[j] == target:
                return i,j
    return -1            
nums = [2,7,11,15]
target = 9
print(two_sum(nums,target))

nums = [3,2,4]
target = 6
print(two_sum(nums,target))

nums = [3,3]
target = 6
print(two_sum(nums,target))

nums = [2,7,11,15]
target = 13
print(two_sum(nums,target))


