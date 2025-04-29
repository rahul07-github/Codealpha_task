import random

def choose_random_word():
    words = ['python', 'programming', 'hangman', 'challenge', 'computer', 'science', 'artificial', 'intelligence']
    return random.choice(words)

def display_word(word, guessed_letters):
    displayed = ''
    for letter in word:
        if letter in guessed_letters:
            displayed += letter + ' '
        else:
            displayed += '_ '
    return displayed.strip()

def hangman():
    word = choose_random_word()
    guessed_letters = set()
    incorrect_guesses = 0
    max_incorrect = 6  # You can change this limit

    print("Welcome to Hangman!")
    
    while incorrect_guesses < max_incorrect:
        print("\nWord to guess:", display_word(word, guessed_letters))
        print(f"Incorrect guesses left: {max_incorrect - incorrect_guesses}")
        
        guess = input("Guess a letter: ").lower()
        
        if not guess.isalpha() or len(guess) != 1:
            print("Please enter a single valid letter.")
            continue
        
        if guess in guessed_letters:
            print("You already guessed that letter. Try another one.")
            continue
        
        if guess in word:
            print(f"Good job! '{guess}' is in the word.")
            guessed_letters.add(guess)
        else:
            print(f"Sorry, '{guess}' is not in the word.")
            guessed_letters.add(guess)
            incorrect_guesses += 1
        
        if all(letter in guessed_letters for letter in word):
            print("\nCongratulations! You guessed the word:", word)
            break
    else:
        print("\nYou've run out of guesses. The word was:", word)

if __name__ == "__main__":
    hangman()
