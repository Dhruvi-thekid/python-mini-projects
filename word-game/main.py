# Word Guessing Game 
import random
word_bank = ['python', 'java', 'kotlin', 'javascript', 'ruby', 'swift', 'go', 'rust']
word = random.choice(word_bank)

guessed_word = ['_'] * len(word)
attempts = 10

while attempts > 0:
    print("\nCurrent word:" + ''.join(guessed_word))

    guess = input("Guess a letter: ").lower()

    if guess in word:
        for i in range (len(word)):
            if word[i] == guess:
                guessed_word[i] = guess
        print("👍Great! You found a letter.")
    else:
        attempts = attempts - 1 
        print("👾Wrong guess. Attempts left:" + str(attempts))

    if '_' not in guessed_word:
        print("🎉Congratulations! You've guessed the word:", word)
        break

    if attempts == 0 and '_' in guessed_word:
        print("😔Sorry, you've run out of attempts. The word was:", word)
        break
