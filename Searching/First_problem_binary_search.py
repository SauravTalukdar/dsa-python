# doing the card problem with binary search

def locate_card(cards,find):
    
    low = 0 
    high = len(cards) - 1
    while(low<=high):
        mid = (low+high)// 2
        mid_number = cards[mid]
        if mid_number == find:
            return f"The element is found in {mid} position"
        elif mid_number < find:
            high = mid - 1
        elif mid_number > find:
            low = mid + 1 
    return -1    

# test cases

# 1.Normal card found at a position
cards = [13,12,11,9,7,5,4,2,0]
find = 5
print(locate_card(cards,find))

# 2.Empty deck
cards = []
find = 5
print(locate_card(cards,find))

# 3.Repeating numbers
cards = [13,12,11,11,9,9,7,5,4,2,0]
find = 5
print(locate_card(cards,find))

# 4.Number to find is repeating
cards = [13,12,11,9,7,5,5,4,2,0]
find = 5
print(locate_card(cards,find))

# 5.Number at last position
cards = [13,12,11,9,7,5]
find = 5
print(locate_card(cards,find))

# 6.Number found at first position
cards = [13,12,11,9,7,5,4,2,0]
find = 13
print(locate_card(cards,find))




    
      
    
        




    


    
