# the brute for way to do it(linearly)
def two_sum(nums,target):
    fir = 0
    sec = 1
    while(fir<=len(nums)-1):
        if nums[fir] + nums[sec] == target:
            return fir,sec
        else:
            fir += 1
            sec += 1
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

