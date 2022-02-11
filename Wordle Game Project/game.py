from re import S
import string
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
    pass

#======
# playRound(players, words, all_words, settings)
# Plays one round of Wordle. 
# Returns nothing, but modifies the player statistics at end of round
#
#   players - List of WordlePlayers
#   words - Wordbank of the common words to select from
#   all_words - Wordbank of the legal words to guess
#   settings - Settings of game
#======#
def playRound(players, words, all_words, settings):
    #answer = words.getRandom()
    answer = 'hello'
    alphabet = WordleWord('abcdefghijklmnopqrstuvwxyz')
    listofGuesses = []
    guess = ''

    while len(listofGuesses) < 6 and str(guess) != answer:
        
        oldGuess = guess
        guess = input("Enter your guess:")

        while len(guess) != 5 or not all_words.contains(guess) or guess in listofGuesses:
            guess = input("You can only enter legal 5 letter words, no repeats!:")

        markGuess(answer, guess, alphabet)
    
        listofGuesses.append(guess)

        for x in range(len(listofGuesses)):
            print(str(x + 1) + ': ' + listofGuesses[x])
        
        print(alphabet)

    if str(guess) == answer:
        for placeholder in players:
            placeholder.updateStats(True, len(listofGuesses))
    else:
        for placeholder in players:
            placeholder.updateStats(False, 0)




def playWordle():
    print("Let's play the game of Wordle!")

    # initialize WordBanks
    all_words = WordBank("words_alpha.txt")
    words = WordBank("common5letter.txt")

    # intialize settings to the baseline settings
    settings = Setting()
    settings.setSetting('maxguess', 6)
    settings.setSetting('numplayers', 1)
    settings.setSetting('difficulty', 'normal')

    playerName = input('Please enter your name >')
    player1 = WordlePlayer()

    # start playing rounds of Wordle
    playAgain = True

    while (playAgain):
        playRound(player1, words, all_words, settings)
        playAgain = input('Do you want to play Again').upper() == 'Y'

    # end game by displaying player stats

    player1.displayStats()


def main():
    playWordle()

if __name__ == "__main__":
    main()