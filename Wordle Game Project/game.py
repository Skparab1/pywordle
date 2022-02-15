# Names: Joseph Gerali, Shubham Parab
# Snapshot 1: Wordleword finished, wordleplayer finished. working on game.py

from re import S
import string
import time
from setting import Setting
from wordbank import WordBank
from wordleword import WordleWord
from wordleplayer import WordlePlayer

#======
# markGuess - will "mark" the guess and the alphabet according to the word
#   word - String of word to be guessed
#   guess - WordleWord that have been guessed
#   alphabet - WordleWord of the letters a-z that have been marked
#======
def markGuess(word, guess, alphabet):
    print(type(guess))
    
    for i in range(5):
        if word[i] == guess.word[i]:
            guess.setCorrect(i)
            alphabet.setCorrect(alphabet.word.find(word[i]))
        elif guess.word[i] in word:
            if (getCharAmt(word,guess.word[i]) == 1 and getCharAmt(guess.word,guess.word[i]) == 1): # if theres only one of that character but hthere are two of them 
                print()
                #basically make the first one correct/misplaced and the second one wrong
            guess.setMisplaced(i)
            alphabet.setMisplaced(alphabet.word.find(word[i]))
        else:
            guess.setUnused(i)
            alphabet.setUnused(alphabet.word.find(word[i]))


#======
# playRound(players, words, all_words, settings)
# Plays one round of Wordle. 
# Returns nothing, but modifies the player statistics at end of round
#
#   players - List of WordlePlayers
#   words - Wordbank of the common words to select from
#   all_words - Wordbank of the legal words to guess
#   settings - Settings of game
#======
def playRound(players, words, all_words, settings):
    #answer = words.getRandom()
    answer = 'hello'
    alphabet = WordleWord('abcdefghijklmnopqrstuvwxyz')
    listofGuesses = []
    wordlist = []
    guess = WordleWord('')

    while len(listofGuesses) < 6 and str(guess.word) != answer:
        
        oldGuess = guess
        guess = WordleWord(input("Enter your guess:"))

        while len(guess.word) != 5 or not all_words.contains(guess.word) or guess.word in wordlist:
            guess = WordleWord(input("You can only enter legal 5 letter words, no repeats!:"))

        markGuess(answer, guess, alphabet)

        wordlist.append(guess.word)
        listofGuesses.append(guess)

        for x in range(len(listofGuesses)):
            print(str(x + 1) + ': ', listofGuesses[x])
        
        print(alphabet)

    if guess.word == answer:
        for placeholder in players:
            print("You win!")
            placeholder.updateStats(True, len(listofGuesses))
    else:
        for placeholder in players:
            print("You lost! The word was:" + str(answer))
            placeholder.updateStats(False, 0)


def getCharAmt(word,char):
    charct = 0
    for ch in word:
        if ch == char:
            charct += 1

    return charct

def loadingAnim():
    print('\n'*50)
    print('Loading')
    time.sleep(0.5)
    for i in range(10):
        print('\n'*50)
        print('Loading'+'.'*i)
        time.sleep(0.01)
    time.sleep(1)

def animateWord(word,before,speed):
    for i in range(len(word)+1):
        print('\n'*50)
        print(before)
        print(word[0:i])
        time.sleep(speed)


def playWordle():
    animateWord("Let's play the game of Wordle!",'',0.03)

    # initialize WordBanks
    all_words = WordBank("words_alpha.txt")
    words = WordBank("common5letter.txt")

    # intialize settings to the baseline settings

    settings = Setting()
    settings.setSetting('maxguess', 6)
    settings.setSetting('numplayers', 1)
    settings.setSetting('difficulty', 'normal')

    animateWord('Please enter your name','Let\'s play the game of Wordle!',0.05)
    playerName = input('>')
    players = [WordlePlayer()]

    # start playing rounds of Wordle
    playAgain = True

    loadingAnim()
    while (playAgain):
        print('\n'*50+'Wordle')
        playRound(players, words, all_words, settings)
        playAgain = input('Do you want to play Again').upper() == 'Y'

    #markGuess('hello', guess, alphabet)

    # end game by displaying player stats

    guess = WordleWord('hello')
    alphabet = WordleWord('abcdefghijklmnopqrstuvwxyz')
    markGuess('apple',guess,alphabet)
    print(guess)
    print(alphabet)

        
def main():
    playWordle()

if __name__ == "__main__":
    main()
