# Problem: Two sum
# Leetcode: #1
# Difficulty: Easy
# Time complexity: O(n^2)
# Space complexity: O(1)

# Approch1: Brute force(checking every pairs)
def two_sum(nums,target):
    last = len(nums)
    for i in range((last)):
        for j in range(i+1,last):
            if nums[i] + nums[j] == target:
                return [i,j]
    return -1 

# Approach2: HashMap — store each number with its index
#           check if complement (target - num) exists in map
# Time Complexity: O(n) — single pass with hashmap
# Space Complexity: O(n) — storing numbers in dictionary
def two_sum1(nums,target):
    data = {} #this stores number and its index(number:index)
    index = 0 #start from zero
    for num in nums: #loop through the list of nums 
        complement = target - num #find the complement(eg:complement = 9 - 2 = 7,in [2,7,11,15])
        if complement in data: #if complement in out data dictionary
            return [data[complement],index] #return the complements index(data[complement] and the current index)
        data[num] = index #else add the number(num) : index pair in the dict
        index +=1  #keep increasing the loop index(so we can iterate the list)
    return -1   

#we can also reduce the manual counter and use enumerate to track the index

def two_sum2(nums,target):
    data = {}
    for index,num in enumerate(nums):
        complement = target - num
        if complement in data:
            return [data[complement],index]
        data[num] = index    

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


           


