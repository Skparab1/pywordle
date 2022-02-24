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
    #print(type(word))
    #print(type(guess))
     
    for i in range(5):
        #print('went into loop')
        if word[i] == guess.word[i]:
            guess.setCorrect(i)
            alphabet.setCorrect(alphabet.word.find(word[i]))
            #print('went into correct if')
        elif guess.word[i] in word:
            goOut = False
            if (getCharAmt(word,guess.word[i]) == 1 and getCharAmt(guess.word,guess.word[i]) > 1): # if theres only one of that character but hthere are two of them 
                #print('corner case override 1')
                for j in range(5): # go through the word
                    if (word[j] == guess.word[j] and guess.word[j] == guess.word[i]): #if the guess is the same anywhere
                        #print('one was correct, marked, for letter',guess.word[j])
                        guess.setCorrect(j)    
                        goOut = True


                if (not goOut): 
                    for j in range(5):
                        if (guess.word[j] in word and guess.word[j] == guess.word[i]):
                                guess.setMisplaced(j)
                                #print('none were correct, marked first')
                                goOut = True
                                if i != j:
                                    guess.setNotUsed(i)
                                break
            else:
                guess.setMisplaced(i)
                #print(guess,word)
                #print(guess.word[i],word[i])
                #print(getCharAmt(word,word[i]),getCharAmt(guess.word,guess.word[i]))
                #print('no override')

            if (not alphabet.isCorrect(alphabet.word.find(guess.word[i]))):
                alphabet.setMisplaced(alphabet.word.find(guess.word[i]))
            
            #print('went into misp if')
        else:
            guess.setNotUsed(i)
            if (not alphabet.isCorrect(alphabet.word.find(guess.word[i])) and not alphabet.isMisplaced(alphabet.word.find(guess.word[i]))):
                alphabet.setNotUsed(alphabet.word.find(guess.word[i]))
            #print('went into unused if')

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
    answer = 'roman'
    alphabet = WordleWord('abcdefghijklmnopqrstuvwxyz')
    listofGuesses = []
    wordlist = []
    guess = WordleWord('')

    while len(listofGuesses) < 6 and str(guess.word) != answer:
        
        guess = WordleWord(input("Enter your guess:").lower().strip())

        while len(guess.word) != 5 or not all_words.contains(guess.word) or guess.word in wordlist:
            if guess.word == '?____' or guess.word == '_?___' or guess.word == '__?__' or guess.word == '___?_' or guess.word == '____?':
                hintValue = guess.word.find('?')
                hintWord = guess.word.replace('?', answer[hintValue])
                print("You're hint is: ", hintWord)
                guess = WordleWord(input("Now enter your guess:").lower().strip())
                #hintlist.append() Determine number of hints with settings or something
            else:
                if '/usr/local/opt/python@3.9/bin/python3.9 "/Volumes/GoogleDrive/My Drive/Intro cs workspace/Wordle Game Project/game.py"' in guess.word:
                    raise NameError('Run again!')
                if len(guess.word) < 5:
                    guess = WordleWord(input("Your guess is too short! Enter another guess:").lower().strip())
                elif len(guess.word) > 5:
                    guess = WordleWord(input("Your guess is too long! Enter another guess:").lower().strip())
                elif not all_words.contains(guess.word):
                    guess = WordleWord(input("Your guess is not an English word! Enter another guess:").lower().strip())
                elif guess.word in wordlist:
                    guess = WordleWord(input("You already guessed that word! Enter another guess").lower().strip())

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
    try:
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
        players = [WordlePlayer(playerName)]
        loadingAnim()

    except:
        playerName = ''
        players = [WordlePlayer(playerName)]

    # start playing rounds of Wordle
    playAgain = True

    while (playAgain):
        print('\n'*50+'Wordle')
        playRound(players, words, all_words, settings)
        playerInput = input('Do you want to play again?').upper().strip()
        while playerInput != 'Y' and playerInput != 'N':
            playerInput = input("Please only use y/n").upper().strip()
            
        playAgain = playerInput == 'Y'

    #markGuess('hello', guess, alphabet)

    # end game by displaying player stats
    for player in players:
        player.displayStats()
        
    #guess = WordleWord('hello')
    #alphabet = WordleWord('abcdefghijklmnopqrstuvwxyz')
    #markGuess('apple',guess,alphabet)
    #print(guess)
    #print(alphabet)

        
def main():
    playWordle()

if __name__ == "__main__":
    main()
