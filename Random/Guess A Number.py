
from random import randint
print ("Guess some number")
Number_Of_Guesses = 0
Guess = []
Correct_Number = randint(1,100)
Wrong_Guesses = []
while Guess != Correct_Number:
    Guess = int(input())
    if Guess != Correct_Number:
        Number_Of_Guesses+=1
        Wrong_Guesses.append(Guess)
    if Guess == Correct_Number:
        print ('Correct ! ' + 'You have guessed correct after ' + str(Number_Of_Guesses )  + ' try ')
        break
    if Guess > 100 or Guess < 1:
        print ('Out of bounds')
    if Guess > Correct_Number + 10 or Guess < Correct_Number -10:
        print ('Cold')
    if Guess < Correct_Number + 11 and Guess > Correct_Number -11:
        print ('Warm')
    if len(Wrong_Guesses)>1 and Guess>Correct_Number and Guess<Wrong_Guesses[-2]:
        print('Warmer')
    if len(Wrong_Guesses)>1 and Guess<Correct_Number and Guess>Wrong_Guesses[-2]:
        print('Warmer')
    if len(Wrong_Guesses)>1 and Guess>Correct_Number and Guess>Wrong_Guesses[-2] and abs(Guess - Correct_Number) <= abs(Correct_Number-Wrong_Guesses[-2]):
        print('Warmer')
    if len(Wrong_Guesses)>1 and Guess<Correct_Number and Guess<Wrong_Guesses[-2] and abs(Correct_Number-Guess) <= abs(Wrong_Guesses[-2]-Correct_Number):
        print('Warmer')
    if len(Wrong_Guesses)>1 and Guess<Correct_Number and Guess<Wrong_Guesses[-2] and abs(Correct_Number-Guess) > abs(Correct_Number-Wrong_Guesses[-2]):
        print('Colder')
    if len(Wrong_Guesses)>1 and Guess>Correct_Number and Guess>Wrong_Guesses[-2] and abs(Guess-Correct_Number) > abs(Wrong_Guesses[-2]-Correct_Number):
        print('Colder')
print(" These were your guesses : ")
print( Wrong_Guesses)





