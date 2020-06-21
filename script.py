import random

money = 100

#Write your game of chance functions here

def coin_flip(guess, bet):
  
  flip = random.randint(1, 2)
  
  print('Coin flipped')

  if flip == 1:
        print('The coin toss result was heads.')

  if flip == 2:
        print('The coin toss result was tails.')

  if (flip == 1 and guess.lower() == 'heads'):
      print('You guessed heads! You got it right! You won + str(bet) + $!')
      return +bet

  elif (flip == 2 and guess.lower() == 'tails'):
      print('You guessed tails! You got it right! You won '+ str(bet) +'$!')
      return +bet

  else:
      print("I'm sorry you guessed wrong, you lost ' + str(bet) +'$!")
      return -bet

#Call your game of chance functions here

def chohan(guess, bet):

  print('\nCho Han')

  dice1 = random.randint(1, 6)
  dice2 = random.randint(1, 6)
  result = dice1 + dice2
  
  print('Two dices rolled!')

  if (result % 2 == 0 and guess.lower() == 'Even'):
      print('You guessed even and you got it right! You won '+ str(bet) +'$!')
      return +bet

  elif (result % 2 != 0 and guess.lower() == 'Odd'):
      print('You guessed odd and you got it right! You won '+ str(bet) +'$!')
      return +bet
  else:
      print('Your guess was wrong and now you have lost '+str(bet)+'$!')
      return -bet 

#Guess the highest number card functions here 

def card(bet):

  print('\nCard bet')

  deck = [i for i in range(1,14)]*4

  card1 = deck.pop(random.randint(0,52))

  card2 = deck.pop(random.randint(0,51))
  
  print ('Your card is:', card1)
  print ('My card is:', card2)

  if card1 < card2:
       print ('You Lost!')
       return -bet
  elif card1 > card2:
       print ('You win!')
       return bet
  else:
    print ("It's a Tie!")
    return 0

#Rules of roulette functions here 

def roulette(guess, bet):
    
    number = random.randint(0,36)

    print('\nRoulette')

    if number == 37:
      print ("The wheel has landed on 00")
    else:
      print ("The winner number is:", number)
    if number == 0 or number == 37:
      print ("You Lost!")
      return -bet
    elif guess == number:
      print ("You win big!")
      return bet * 35
    elif ((number % 2 ) == 0 and guess == "Even") or ((number % 2 ) == 1 and guess == "Odd"):
      print ("You win!")
      return bet
    else:
      print ("You Lost!")
      return -bet

#betting on all games functions here

money += coin_flip("Tails",10)
print(money)
money += chohan("Odd",10)
print(money)
money += card(10)
print(money)
money += roulette(2,10)
print(money)