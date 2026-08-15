# # using a while loop

# linear = [1,4,5,7]
# find = 2
# i = 0
# while i<len(linear):
#     if linear[i] == find:
#         print(f"The element {find} is found at index {i}")
#         break
#     i+=1  
# else:
#     print("Element not found")

# # using a for loop

# elements = [1,5,22,7,55,3]
# searching = 5
# for i in range(0,len(elements)):
#     if elements[i] == searching:
#         print(f"Element {searching} found at {i+1} position")
#         break
# else:
#     print("Element not found")


# finding a card of a specific number in a deck of cards(linear search method)

def locate_card(cards,query):
    position = 0 
    while position < len(cards): #if we used while true , in an empty deck of cards there would be an index error
        if cards[position] == query:
            return position
        position += 1
    return -1   

#case with a filled deck
cards = [13,5,6,88,3,9]
query = 88
print(locate_card(cards,query))

# case with an empty deck
cards = []
query = 88
print(locate_card(cards,query))

