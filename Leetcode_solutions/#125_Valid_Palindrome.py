# Problem: Valid Palindrome
# LeetCode: #125
# Difficulty: Easy
# Approach 1: build a cleaned lowercase string, compare it with its reverse. O(n) time, O(n) space
# Approach 2: two pointers from both ends, skipping non-alphanumeric characters. O(n) time, O(1) space
# Pattern: two pointers moving inward

'''
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, 
it reads the same forward and backward.
Alphanumeric characters include letters and numbers.
Given a string s, return true if it is a palindrome, or false otherwise.
'''

#test cases
test0 = {
    'input' : {
        's' : "A man, a plan, a canal: Panama"
    },'output': True
}  

test1 = {
    'input' : {
        's' : "race a car"
    },'output': False
}  

test2 = {
    'input' : {
        's': ""
    },'output': True
}

test3 = {
    'input' : {
        's': ".,"
    },'output': True
}

test4 = {
    'input' : {
        's': "0P"
    },'output': False
}

test5 = {
    'input' : {
        's': "ab_a"
    },'output': True
}

test6 = {
    'input' : {
        's': "a"
    },'output': True
}

tests = [test0,test1,test2,test3,test4,test5,test6]

#brute force solution
def palindrome(s):
  clean = "".join(char.lower() for char in s if char.isalnum()) # keep letters and digits only, lowercase
  return clean == clean[::-1] # reads the same backwards?
  
#two pointer approach
  left = 0 
  right = len(s) - 1  # one pointer at each end

  while left < right: # stop when the pointers meet or cross
    if not s[left].isalnum(): 
      left +=1  # can't compare this one, skip it (only left moves)
    elif not s[right].isalnum():
      right -=1 # same on the right (only right moves)
    elif s[left].lower() != s[right].lower():
      return False # both are alphanumeric and they differ
    else:
      left += 1  # they match, so move both inward
      right -=1
  return True  # every pair matched   

for i,t in enumerate(tests):
    result = valid_palindrome2(**t['input'])
    print(i, "PASSED" if result == t['output'] else "FAILED")

#error log
# Bug: pointer updates sat outside the if/elif chain, so skips also moved both pointers
# Bug: compared .isalnum() results (booleans) instead of the characters
# Rule: in a two-pointer loop, ask "which pointer moves in each branch?" and write it out

