#Tips
#Convey our thought process to the interviewer by stating things out loud, or writing comments for it


#Question - Given two strings A and B , find the minimum number of steps required to convert A to B .
# (Each operation is counted as one step). You have 3 operations permited on a word - insert,delete and replace a character
#Example- I N T E * N T I O N 
#         * E X E C U T I O N

#input
str1 = "intention"          
str2 = "execution"          
#output
output1 = 5 #(we did five operations in this example)

#function signature
def min_steps(str1,str2):
    pass

#test cases
'''
1. general case(listed above)
2. no changes required
3. all the characters need to be changed
4. equal length
5. unequal length
6. one of the strings is empty
7. only insertion,only deletion,only replacement
'''

'''
1.Recursive solution:
- if the first character is equal, then ignore from both strings
- if the first character is not equal
  i. either it has to be deleted
    - 1 + recursively solve after ignoring the first character of the first string(str1)
  ii. or swapped 
    - 1 + recursively solve after ignoring the first character of each string(str1,str2)
  iii. or a character inserted before
    - 1 + recursively solve after ignoring the first character of second string(str2) 
  then pick the minimum of these three(as we need min steps)   
- end case(base case)
  i. Nothing left in str2(second string) but there are characters in str1(first string)
    - return number of characters left in str1      
  ii. Nothing left in str1 but there are characters in str2
    - return number of characters left in str2
'''
#recursive solution
#Time complexity - O(3^n)
def min_steps(str1,str2,i1=0,i2=0): #i1 is a pointer for str1,i2 is a pointer for str2
    if i1 == len(str1):
        return len(str2) - i2
    elif i2 == len(str2):
        return len(str1) - i1
    elif str1[i1] == str2[i2]: #both equal ,ignore both characters and move forward
        return min_steps(str1,str2,i1+1,i2+1)
    else: #characters are not equal
        return 1 + min(min_steps(str1,str2,i1+1,i2),#deleted
        min_steps(str1,str2,i1+1,i2+1),#swapped
        min_steps(str1,str2,i1,i2+1))#inserted before

print(min_steps(str1,str2))
print(min_steps("", "abc"))                
print(min_steps("abc", ""))                 
print(min_steps("abc", "abc"))          
print(min_steps("abc", "xyz")) 





