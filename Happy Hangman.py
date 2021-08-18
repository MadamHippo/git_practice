
import random, time

fruits = ['watermelon', 'coconut', 'blueberry', 'banana', 'apricot', 'pineapple','cantaloupe', 'grapefruit','jackfruit','papaya', 'strawberry'] 
heroes = ['hawkeye', 'batman', 'spiderman', 'wolverine', 'mystique', 'superman', 'deadpool', 'daredevil', 'antman', 'aquaman', 'groot']
animals = ['chipmunk', 'dinosaur', 'turtle', 'giraffe', 'hippopotamus', 'coyote', 'crocodile', 'porcupine', 'butterfly', 'shark', 'wombat']
states = ["mississippi", 'missouri', 'wyoming', 'delaware', 'florida', 'louisana', 'arizona', 'nebraska', 'oregon', 'washington', 'georgia']

chosen_word_template = []
user_guesses = []
category = ""
playGame = "Y"
failed_sayings = ["Good try buddy.", "Nice try, but try again.", "Don't give up! Try again.", "So close."]
playGame = True
runGame = True

name = input("Hi there, What's your name?: ")
print("Well, welcome to Happy Hangman! " + name.title() + " let's play!")
time.sleep(1)
print("The objective of the game is to guess the secret word chosen by the computer.")
time.sleep(1)
print("Each incorrect guess results in an extra balloon added to Mr. Hangman.")
time.sleep(1)
print("You have limited guesses to complete the secret word.")
time.sleep(1)
print("After many wrong guesses, Mr. Hangman will be holding too many balloons to stay on the ground, he will be carry away by wind and it's game over for you!")
time.sleep(2)
print("You can guess only one letter at a time. Don't forget to press 'enter' after each guess.")
time.sleep(1)
print("Ready? Game on!")
time.sleep(1)

while runGame:
    while True:
        if category.upper() == "F":
            chosen_word = random.choice(fruits)
            break
        elif category.upper() == "H":
            chosen_word = random.choice(heroes)
            break
        elif category.upper() == "A":
            chosen_word = random.choice(animals)
            break
        elif category.upper() == "S":
            chosen_word = random.choice(states)
            break
        else: category = input("Please enter a valid secret word category! F for Fruits / H for Heroes / A for Animals / S for U.S. States / X to exit game. ").strip() 
        
        if category.upper() == "X":
            print("Bye bye! See you next time!")
            playGame: False
            break

    if playGame:
        chosen_word_list = list(chosen_word)
        attempts = (len(chosen_word))

        def chosen_word_letters():
            print("Your guesses so far: " + ' '.join(chosen_word_template))
            print("You have " + str(attempts) + " remaining guesses.")
            
    #Adding blank lines to userGuesslist to create the blank secret word

        for blank in chosen_word_list:
            chosen_word_template.append("_")
        print("The number of allowed guesses remaining: " + str(attempts))

    #Starting the Game

        while True:
            print("Guess your letter: ")
            guess = input()
        
            if guess in chosen_word_list: #correct guess
                print("Good job.")

                for index in range(len(chosen_word_list)):
                    if guess == chosen_word_list[index]:
                        chosen_word_template[index] = guess.upper()
                        chosen_word_letters()
            
            elif guess in user_guesses:
                    print("Already tried that, try another letter.")
            else:
                attempts -= 1
                user_guesses.append(guess)
                
                failed_saying = random.choice(failed_sayings)
                print(failed_saying)
                print("Remaining tries: " + str(attempts))
            
        
            joined_list = ''.join(chosen_word_template)

    #Win Loss Logic
            if joined_list.upper() == chosen_word.upper():
                print("You win!")
                break
            elif attempts == 0:
                print("Too many wrong guesses! Better luck next time.")
                print("The answer was " + chosen_word.upper())
                break

#Another Game?

    anotherGame = input("Do you want to play again? Y to continue, any other key to quit.")

    if anotherGame.upper() == "Y":
        runGame = True
        chosen_word_template = []
        user_guesses = []
        category = input("Please enter a valid word category! F for Fruits / H for Heroes / A for Animals / S for U.S. States / X to exit game. ").strip()
    
    else:
        runGame = False
        print("Thanks for playing Happy Hangman! See you next time!")

