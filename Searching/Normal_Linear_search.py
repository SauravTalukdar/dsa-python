# using a while loop

linear = [1,4,5,7]
find = 2
i = 0
while i<len(linear):
    if linear[i] == find:
        print(f"The element {find} is found at index {i}")
        break
    i+=1  
else:
    print("Element not found")

# using a for loop

elements = [1,5,22,7,55,3]
searching = 5
for i in range(0,len(elements)):
    if elements[i] == searching:
        print(f"Element {searching} found at {i+1} position")
        break
else:
    print("Element not found")
