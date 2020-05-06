nums = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']
userHand = ['A', 'J', 3, 7]

# def sorthand(hand):
#     for num in hand:
#         if num == "A":
#             num = 11
#         elif isinstance(num,str):
#             num = 10
#         else:
#             num = num

# When sort is called, behind the scenes python will call what we have provided as the key param
# once per every item in the list. So, cardComparator is called for every card in hand and we don't 
# need to worry about iterating. We just need to worry about returning the value at the end
def cardComparator(cardNum):
    if cardNum == 'A':
        cardNum = 11
    elif isinstance(cardNum, str):
        cardNum = 10
    
    return cardNum

userHand.sort(key=cardComparator)
print(userHand)
