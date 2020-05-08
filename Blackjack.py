from random import randint
import time

# test comment from kyle

deck = []
suits = ['diamonds', 'hearts', 'spades', 'clubs']
nums = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']

dealerHand = []
userHand = []
dealerTotal = 0
userTotal = 0

finished = False
userPocket = 500
winner = "tie"
bet = "NA"

class Card:
  def __init__(self, suit, num):
    self.suit = suit
    self.num = num
  
  def __str__(self):
    return self.suit + ' ' + str(self.num)

def popDeck(index):
  deck.pop(index)

def hitPlayer(playerType):
  random = randint(0, len(deck) - 1)
  playerType.append(deck[random])
  popDeck(random)

def printBoard(shouldReveal):
  print('\nDealer:')

  if shouldReveal:
    for card in dealerHand:
      print(card)
  else:
    print(dealerHand[1])

  print('\nPlayer:')

  for card in userHand:
    print(card)
  print('\n')

def setupGame():
  global bet
  for suit in suits:
    for num in nums:
      c = Card(suit, num)
      deck.append(c)
  bet = "NA"
  while bet == "NA":
    bet = input("How much would you like to bet? $")
    if not bet.isdigit():
      print("Please enter a number.")
      bet = "NA"
    else:
      bet = int(bet)
      if bet > userPocket:
        print("I'm sorry, it looks like you don't have that much. Please try again.")
        bet = "NA" 
      elif bet < 100:
        print("I'm sorry, the minimum bet at this table is $100. Please try again.")
        bet = "NA"
      else:
        bet = bet
        print("You are betting %d" % bet)
        time.sleep(1.5)
  hitPlayer(userHand)
  hitPlayer(dealerHand)
  hitPlayer(userHand)
  hitPlayer(dealerHand)

  printBoard(False)

def cardComparator(card):
  if card.num == 'A':
    card.num = 11
  elif isinstance(card.num, str):
    card.num = 10
  
  return card.num

def checkTotal(hand):
  total = 0
  face = ("J", "Q", "K")
  hand.sort(key=cardComparator)
  for card in hand:
    num = card.num
    if card.num in range(2,11):
      total += num
    elif card.num in face:
      total += 10
    elif card.num == "A" and total < 11:
      total += 11
    elif card.num == "A":
      total += 1
  return total

def checkDecision(decision, userPocket):
  global bet
  if decision == 'hit':
    hitPlayer(userHand)
    time.sleep(2)
    printBoard(False)

    total = checkTotal(userHand)
    if total == 21:
      print('\nYou got 21! You win!')
      winner = "user"
      userPocket += bet

      return True
    elif total > 21:
      print('\nYou bust! Your total is: %d' % total)
      winner = "dealer"
      userPocket -= bet
      return True
  elif decision == 'stay':
    printBoard(True)
    dealerTotal = checkTotal(dealerHand)
    userTotal = checkTotal(userHand)
    print('The dealer has %d' % dealerTotal)
    print('You have %d' % userTotal)
    if dealerTotal <= 21 and dealerTotal > userTotal:
      print('\nYou lost!')
      winner = "dealer"
      userPocket -= bet
    elif dealerTotal == userTotal:
      print('\nYou tied')
      winner = "tie"
    while dealerTotal < userTotal:
      print('\nHitting Dealer...\n')
      hitPlayer(dealerHand)
      time.sleep(1)
      printBoard(True)
      dealerTotal = checkTotal(dealerHand)
      print('\nThe dealer has %d' % dealerTotal)
      print('\nYou have %d' % userTotal)
      if dealerTotal > 21 and userTotal <= 21:
        print("\nCongratulations, you won!")
        winner = "user"
        userPocket += bet
      elif dealerTotal == userTotal:
        print('\nYou tied')
        winner = "tie"
      elif dealerTotal <= 21 and dealerTotal > userTotal:
        print('\nYou lost!')
        winner = "dealer"
        userPocket -= bet
    return True
  else:
    print('What? Try again...')
    return False


# Actual game:
# print("Hello! Welcome to the virtual casino!")
# time.sleep(1)
# print("Please take a seat at one of our fine blackjack tables.")
# time.sleep(2)
# print("It looks like you have $500 to play with...let's get started!")
# time.sleep(1)
while userPocket > 100:
  print("You have $%d" % userPocket)
  setupGame()
  finished = False
  while not finished:
    decision = input('Hit or stay?')
    finished = checkDecision(decision, userPocket)