#===========================================================================
# Description: WordleWord(word)
# Inherits from the FancyWord class and adds methods for the Wordle game
#
# Methods
#    isCorrect(pos) - boolean - return True if character at pos is correct
#    isMisplaced(pos) - boolean - return True if character at pos is misplaced
#    isNotUsed(pos) - boolean - return True if character at pos is not in word
#    setCorrect(pos) - integer - set character are pos correct and colors accordingly
#    setMisplaced(pos) - integer - set character are pos misplaced and colors accordingly
#    setNotUsed(pos) - integer - set character are pos misplaced and colors accordingly
#===========================================================================
from fancyword import FancyWord

class WordleWord(FancyWord):

    def setCorrect(self,pos):
        self.setColorAt(pos,'green') # at position pos, set char of wordleword green

    def setMisplaced(self,pos):
        self.setColorAt(pos,'yellow') # at position pos, set char of wordleword yellow 
    
    def setNotUsed(self,pos):
        self.setColorAt(pos,'gray') # at position pos, set char of wordleword gray

    def isCorrect(self,pos):
        return self.colorAt(pos) == 'green' # if the color at pos is green then return true else return false

    def isMisplaced(self,pos):
        return self.colorAt(pos) == 'yellow' # if the color at pos is yellow then return true else return false

    def isNotUsed(self,pos):
        return self.colorAt(pos) == 'gray' # if the color at pos is gray then return true else return false



#testing below

#guess1 = WordleWord('hello')

#for i in range(5):
#    guess1.setMisplaced(i)

#print(guess1)
#print(guess1.isMisplaced(1))

