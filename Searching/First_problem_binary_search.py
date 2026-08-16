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






    
      
    
        




    


    
