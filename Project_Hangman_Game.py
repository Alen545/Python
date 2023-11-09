import random
import wordFile
chosenWord = random.choice(wordFile.words)
lives = 6
display = []
print('Let\'s play Hangman!!')
print('You have only 6 lives so try to guess the word within 6 attempts! GOOD LUCK!!')
for x in range(len(chosenWord)):
    display += ['_']
print(display)
gameOver = False
while not gameOver:
    guessedLetter = input('Guess a letter:').lower()
    for position in range(len(chosenWord)):
        letter = chosenWord[position]
        if letter == guessedLetter:
            display[position] = guessedLetter
    print(display)
    if guessedLetter not in chosenWord:
        print('You lose an attempt!!')
        lives -= 1
        print(f'Remaining chance are {lives}')
        if lives == 0:
            gameOver == True
            print('YOU LOSE!!')
    if '_' not in display:
        gameOver == True
        print('YOU WIN!!')











