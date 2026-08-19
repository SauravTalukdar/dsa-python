# Problem: Two sum
# Leetcode: #1
# Difficulty: Easy
# Time complexity: O(n^2)
# Space complexity: O(1)
# Approch: Brute force(checking every pairs)


def two_sum(nums,target):
    last = len(nums)
    for i in range((last)):
        for j in range(i+1,last):
            if nums[i] + nums[j] == target:
                return [i,j]
    return -1 

# test cases

# 1.
print(two_sum([2,7,11,15],9))
# output: [0,1]

#2.
print(two_sum([3,2,4],6))
# output: [1,2]

#3.
print(two_sum([3,3],6))
# output: [0,1]

#4.
print(two_sum([2,7,11,15],13))
# output: [0,2]

#5.
print(two_sum([],6))
# output: [-1]


           


