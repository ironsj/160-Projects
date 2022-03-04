import random

name = input("Hello, what is your name? ")
playing = True #variable that checks if the player is still playing

while playing:
    print(name + ", I am thinking of a number between 1 and 100 (both included).")
    print("Can you guess what it is?")
    guess = "" #creates variable for guesses
    count = 0 #variable that counts the number of guesses
    number = random.randint(1,100) #what must be guessed
    while guess != number: #loops until number is guessed, gives approptiate repsonses
        guess = int(input("Guess a number (1-100):"))
        count += 1
        if guess > number:
            print("Your guess is too high. Try again.")
        elif guess < number:
            print("Your guess is too low. Try again.")
        else:
            print(name + ", you won in " + str(count) + " tries. Congratulations!")
            if(count > 7):
                print("That took quite a few guesses. You may want to try a different strategy next time to win in fewer guesses.")
    response = input("Do you want to continue to play? (yes or no)")
    if response == 'yes':
        continue #goes back to beginning of game if player says yes
    else:
        playing = False #exits loop if no

print("Thank you for playing this game. Bye.")
        
    
        
    
