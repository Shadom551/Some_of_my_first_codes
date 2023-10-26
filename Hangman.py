import random

def words(l_words):
    return random.choice(l_words)

def existecharacter(character, word):
    return character in word

def screen(word,guesses):
    for character in word:
        if character in guesses:
            print(character,end=' ')
        else:
            print('_',end=' ')
            
def ganar(word,guesses):
    return all(character in guesses for character in word)
    
def three_chances(word):
    amount_guesses = 3
    while amount_guesses > 0:
        guess = input('What word do you think it is?').lower()
        if word == guess:
            print('Congratulations, You are correct!')
        else:
            print(f"That's not it. You still have {amount_guesses} more guesses, try again.")
            amount_guesses -= 1
    print(f'You have no more guesses the word was: {word}.')

def Ahorcado():
    word = words(l_predefinida)
    guesses = []
    amount_guesses = 5
    screen(word,guesses)
    while amount_guesses != 0:
        character = input('\n\nPick a Letter.\n').lower()
        if existecharacter(character,word):
            guesses.append(character)
            if ganar(word,guesses):
                print(f'You have guessed with {amount_guesses} tries remaining, the word was:\n{word}')
                print()
                return
        else:
            amount_guesses -= 1
            print(f"That Character isn't in the word, you have {amount_guesses} tires left, try again.")
            print()
        screen(word,guesses)
    print("You have no more guesses, but because im a great guy, I'll give you three chances to guess the whole word.")
    three_chances(word)
#If you want to use this code to play i recommend you fill this list bellow with words of your own, but I'll leave some anyways.
#The code uses the .lower() method, so the words you use have to be in lower case otherwise the code wont't work.
l_predefinida = ["elephant", "butterfly", "computer", "sunflower", "mountain", "ocean", "chocolate", "giraffe", "happiness", "adventure"]

Ahorcado()