# Given n elements, each of which has a weight and a profit, 
# determine the maximum profit that can be obtained by selecting a subset of the elements weighing no more than w.
# Eg - profits [2,3,1,5,4,7]
#      weights [4,5,1,3,2,5] 
#      capacity(w) - 15, we find the combinations of weights which is no more than 15
#                       (and also take the combinations which can give us max profit)

#input -  1. weights : A list of numbers containing weights
#         2. profits : A list of numbers containing profits(same length as weights)
#         3. capacity : The maximum weight allowed

#output - max_profit : maximum profit that can be obtained by selecting elements of total weight no more than capacity.

#test cases
# 1.Some generic test cases
# 2.All the elements can be included
# 3.None of the elements can be included
# 4.Only one of the elements can be included
# 5.You do not use the complete capacity

test0 = {
    'input' : {
        'capacity' : 165,
        'weights' : [23, 31, 29, 44, 53, 38, 63, 85, 89, 82],
        'profits' : [92, 57, 49, 68, 60, 43, 67, 84, 87, 72]
    },
    'output' : 309
}
test1 = {
    'input' : {
        'capacity' : 3,
        'weights' : [4,5,6],
        'profits' : [1,2,3]
    },
    'output' : 0
}
test2 = {
    'input' : {
        'capacity' : 4,
        'weights' : [4,5,1],
        'profits' : [1,2,3]
    },
    'output' : 3
}
test3 = {
    'input' : {
        'capacity' : 170,
        'weights' : [41, 50, 49, 59, 55, 57, 60],
        'profits' : [442, 525, 511, 593, 546, 564, 617]
    },
    'output' : 1735
}
test4 = {
    'input' : {
        'capacity' : 15,
        'weights' : [4,5,6],
        'profits' : [1,2,3]
    },
    'output' : 6
}
test5 = {
    'input' : {
        'capacity' : 15,
        'weights' : [4,5,1,3,2,5],
        'profits' : [2,3,1,5,4,7]
    },
    'output' : 19
}

tests = [test0, test1, test2, test3, test4, test5]

#Recursive solution
def max_profit_recursive(weights,profits,capacity, idx = 0):
    if idx == len(weights):
        return 0
    elif weights[idx] > capacity:
        return max_profit_recursive(weights,profits,capacity,idx + 1)
    else:
        option1 = max_profit_recursive(weights,profits,capacity,idx + 1)
        option2 = profits[idx] +  max_profit_recursive(weights,profits,capacity - weights[idx],idx + 1) 
        return max(option1,option2)

#testing
for i, test in enumerate(tests):
    result = max_profit_recursive(**test['input'])
    passed = result == test['output']
    status = "PASSED" if passed else "FAILED"
    print(f"Test {i}: {status} | Expected: {test['output']}, Got: {result}")



