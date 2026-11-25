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
def valid_palindrome1(s):
    clean_text = "".join(char.lower() for char in s if char.isalnum())
    return clean_text == clean_text[::-1]

for i,t in enumerate(tests):
    result = valid_palindrome1(**t['input'])
    print(i, "PASSED" if result == t['output'] else "FAILED")



