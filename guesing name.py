"""
hello , this is a guessing game where we are trying to compare whether 
the guessed number matches the  'secret_number'
"""
print('In this game, you have three chances to guess a secret number. ')
secret_number=6
guessing_count=0
guessing_limit=3      #the while loop will be executed three times
while guessing_count<guessing_limit:    #asks the user to guess
    guess=int(input('guess between 0-9: '))  #every guess is added 1 until it reaches 3 and there it ends
    guessing_count+= 1    #the computer checks and evaluates the guess given
    if guess==secret_number:  #if the guess matches 6 you get the the print statement below
        print('hey, you won!') 
        
        break #the break function breaks the while loop
    #if the user gets any other thing, the print statement below is executed
else:
    print('you lost!')