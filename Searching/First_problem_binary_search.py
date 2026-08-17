# # doing the card problem with binary search

# def locate_card(cards,find):
    
#     low = 0
#     high = len(cards) - 1
#     while(low<=high):
#         mid = (low+high)// 2
#         mid_number = cards[mid]
#         if mid_number == find:
#             return mid
#         elif mid_number > find:
#             low = mid + 1   
#         elif mid_number < find:
#             high = mid - 1
#     return -1 
            


# # test cases

# # 1.Normal card found at a position
# cards = [13,12,11,9,7,5,4,2,0]
# find = 5
# print(locate_card(cards,find))

# # 2.Empty deck
# cards = []
# find = 5
# print(locate_card(cards,find))

# # 3.Repeating numbers
# cards = [13,12,11,11,9,9,7,5,4,2,0]
# find = 5
# print(locate_card(cards,find))

# # 4.Number to find is repeating
# cards = [13,12,11,9,7,5,5,4,2,0]
# find = 5
# print(locate_card(cards,find))

# # 5.Number at last position
# cards = [13,12,11,9,7,5]
# find = 5
# print(locate_card(cards,find))

# # 6.Number found at first position
# cards = [13,12,11,9,7,5,4,2,0]
# find = 13
# print(locate_card(cards,find))


# 7.handling an edge case where there multiple numbers repeating and our find number is also repeating(finding its first occurence)

def test_location(cards,find,mid):
    mid_number = cards[mid]
    print("mid :",mid,"mid number :",mid_number)
    if mid_number == find:
        #we check if left number of mid number is also same as 'find' 
        # and we did mid-1 >=0 to see if our index is valid and not the first 0th position of our list 
        if mid-1 >= 0 and cards[mid-1] == find: 
            return "left"
        else:
            return "found"
    elif mid_number < find:
        return "left"
    else:
        return "right"

def locate_card(cards,find):
    
    low = 0
    high = len(cards) - 1
    
    while(low<=high):
        mid = (low+high)// 2
        result = test_location(cards,find,mid)
        if result == "found":
            return mid
        elif result == "right":
            low = mid + 1   
        elif result == "left":
            high = mid - 1
    return -1
    
# example  
cards = [8,8,6,6,6,6,6,6,3,2,2,2,0,0,0]
find = 6
print(locate_card(cards,find))           
        
                        





    
      
    
        




    


    
