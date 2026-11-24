# Problem: Longest Consecutive Sequence
# LeetCode: #128
# Difficulty: Medium
# Approach 1: sort, then walk once keeping the current run and the best run. O(n log n) time, O(n) space
# Approach 2: set, count only from numbers that start a run. O(n) time, O(n) space

'''
An unsorted array of integers,nums is given.
We have to return the length of the longest consecutive elements sequence.
You must write an algorithm that runs in O(n) time.
the numbers in the sequence may not be next to each other
like 1,2,3,4 here nums = [100, 4, 200, 1, 3, 2]  →  4      (the sequence 1, 2, 3, 4)
'''

#test cases
test0 = {
    'input' : {
        'nums': [100,4,200,1,3,2]
    },'output': 4
}  

test1 = {
    'input' : {
        'nums': [0,3,7,2,5,8,4,6,0,1]
    },'output': 9
}  

test2 = {
    'input' : {
        'nums': [1,0,1,2]
    },'output': 3
}  

test3 = {
    'input' : {
        'nums': []
    },'output': 0
}  

test4 = {
    'input' : {
        'nums': [2]
    },'output': 1
}

test5 = {
    'input' : {
        'nums': [1,1,1,1]
    },'output': 1
} 

test6 = {
    'input' : {
        'nums': [-2,-1,0,1]
    },'output': 4
}  

test7 = {
    'input' : {
        'nums': [10,20,40]
    },'output': 1
}  

tests = [test0,test1,test2,test3,test4,test5,test6,test7]

#sorting approach
def lcs1(nums):
    if not nums:
        return 0
    count = 1
    best = 1
    new_nums = sorted(nums)
    for i in range(1,len(new_nums)):
        if new_nums[i] == new_nums[i-1] + 1:
            count +=1
            
        elif new_nums[i] == new_nums[i-1]:
            continue
        else:
            count = 1
        best = max(best,count)    
    return best

#set approach
def lcs2(nums):
    if not nums:  # empty list has no sequence
        return 0
    new_nums = set(nums) # O(1) lookups, and duplicates disappear
    best = 1  # any non-empty list has a run of at least 1
    for x in new_nums:  # loop over the set, so duplicates can't repeat work
        if x - 1 not in new_nums:  # x is the START of a run(count) if nothing sits just below it
            count = 1    # a new run starts at length 1
            while x + 1 in new_nums:  # walk upward while the next number exists
                count +=1
                x +=1
            best = max(best,count)   # keep the longest run seen so far
    return best      

# Why O(n) even with a while inside a for:
# the while loop only runs from the start of a run, and each run is walked once,
# so every number is visited at most about twice in total (once in the for, once in a walk).
# Without the "x - 1 not in set" check, every number would start its own walk and it would be O(n^2).

for i,t in enumerate(tests):
    result = lcs2(**t['input'])
    print(i, "PASSED" if result == t['output'] else "FAILED")