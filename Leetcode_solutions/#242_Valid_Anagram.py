# Problem: Valid Anagram
# LeetCode: #242
# Difficulty: Easy
# Approach 1: Sort both strings,O(n log n)
# Approach 2: HashMap frequency count,O(n)
# Key insight: anagrams have identical character frequencies

# given two strings s and t we need to return true if t is an anagram of s, otherwise we need to return false
# An anagram is a word or phrase formed by rearranging the letters of another word or phrase
# using all the original letters exactly once. Eg - listen,silent

#test cases
test0 = {
    'input':
    {
        's': "anagram",
        't': "nagaram"
    },'output': True
}
test1 = {
    'input':
    {
        's': "silent",
        't': "listen"
    },'output': True
}
test2= {
    'input':
    {
        's': "rat",
        't': "car"
    },'output': False
}
test3 = {
    'input':
    {
        's': "",
        't': "listen"
    },'output': False
}
test4= {
    'input':
    {
        's': "silent",
        't': ""
    },'output': False
}
test5= {
    'input':
    {
        's': "",
        't': ""
    },'output': True
}

#using built in method, sorted(not optimal)
class Solution:
    def anagram(self,s,t):
        s = sorted(s)
        t = sorted(t)
        if s == t:
            return True
        return False  

#using hashmap(dictionary)
class Solution1:
    def anagram(self,s,t):
        frequency_s = {}
        frequency_t = {}
        for letter in s:
            frequency_s[letter] = frequency_s.get(letter,0) + 1 #we get the value(if no value default will be zero),and increase it by 1
                                                        #if zero(we get 0 + 1=1,else value + 1= 2,3,4..the frequency)
        for letter in t:
            frequency_t[letter] = frequency_t.get(letter,0) + 1  
        # print(f"frequency_s : {frequency_s}, frequency_t : {frequency_t}")        
        return frequency_s == frequency_t           



solution = Solution1()
#testing
s0,t0, output0 = test0['input']['s'],test0['input']['t'], test0['output']
print('Input:', s0)
print('Input:', t0)
print('Expected output:', output0)
result0 = solution.anagram(s0,t0)
print('Actual output:', result0) 

s1,t1, output1 = test1['input']['s'],test1['input']['t'], test1['output']
print('Input:', s1)
print('Input:', t1)
print('Expected output:', output1)
result1 = solution.anagram(s1,t1)
print('Actual output:', result1) 

s2,t2, output2 = test2['input']['s'],test2['input']['t'], test2['output']
print('Input:', s2)
print('Input:', t2)
print('Expected output:', output2)
result2 = solution.anagram(s2,t2)
print('Actual output:', result2) 

s3,t3, output3 = test3['input']['s'],test3['input']['t'], test3['output']
print('Input:', s3)
print('Input:', t3)
print('Expected output:', output3)
result3 = solution.anagram(s3,t3)
print('Actual output:', result3) 

s4,t4, output4 = test4['input']['s'],test4['input']['t'], test4['output']
print('Input:', s4)
print('Input:', t4)
print('Expected output:', output4)
result3 = solution.anagram(s4,t4)
print('Actual output:', result3) 

s5,t5, output5 = test5['input']['s'],test5['input']['t'], test5['output']
print('Input:', s5)
print('Input:', t5)
print('Expected output:', output5)
result5 = solution.anagram(s5,t5)
print('Actual output:', result5)             
