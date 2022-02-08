#===========================================================================
# class FancyWord
# Description: a colored word - each letter has a color attribute
#
# Methods
#    updateStats(won, tries) - 'won' - True if guessed word correctly
#                            - 'tries' - number of tries it took to guess word
#                            - This is called at the end of each game to update
#                              the game stats for this player
#    winPercentage() - returns % of how many games were won over all time
#    gamesPlayed() - returns the number of games played over all time 
#    currentStreak() - returns the current win streak; it will return 0 if
#                      the last game was lost
#    maxStreak() - returns the longest winning streak
#    displayStats() - prints out nice display of all the Wordle player stats
#    
#    Games Played: 3
#    Win %: 100.00
#    Current Streak: 3
#    Max Streak: 3
#    Guess Distribution
#      1: ########### 1
#      2: # 0                        <-- min bar length is 1
#      3: # 0
#      4: ##################### 2    <-- max bar length is 21
#      5: # 0
#      6: # 0
#=============
from player import Player

# TODO - make WordlePlayer
class WordlePlayer(Player):

    def __init__(self):
        self.wins = 0
        self.plays = 0
        self.streak = 0
        self.prevWin = False
        self.maxstreak = 0
        self.try1 = 0
        self.try2 = 0
        self.try3 = 0
        self.try4 = 0
        self.try5 = 0
        self.try6 = 0
    
    def updateStats(self, won, tries):
        self.plays += 1
        if won == True:
            self.wins += 1
            self.prevWin = True
            
        else: 
            self.prevWin = False
        
        if self.prevWin == True and won == True:
            self.streak += 1
        
        else:
            self.streak = 0
        
        if self.streak > self.maxstreak:
            self.maxstreak = self.streak

        if tries == 1:
            self.try1 += 1
        
        elif tries == 2:
            self.try2 += 1
        
        elif tries == 3:
            self.try3 += 1
        
        elif tries == 4:
            self.try4 += 1
        
        elif tries == 5:
            self.try5 += 1
        
        elif tries == 6:
            self.try6 += 1
            
    def winPercentage(self):
        if self.plays != 0:
            return self.wins / self.plays * 100
        else:
            return 0

    def gamesPlayed(self):
        return self.plays

    def currentStreak(self):
        return self.streak

    def maxStreak(self):
        return self.maxstreak

    def displayStats(self):
        print(
            "Games Played: " + str(self.plays) + "\n"
            "Win Percentage: " + str(self.wins / self.plays * 100) + "\n"
            "Current Win Streak: " + str(self.streak) + "\n"
            "Max Win Streak " + str(self.maxstreak) + "\n"
            "Guess Distribution")
        print("  " + "1: " + int(20 * (self.try1 / self.wins) + 1) * "#" + " " + str(self.try1) + "\n"
        "  " + "2: " + int(20 * (self.try2 / self.wins) + 1)* "#" + " " + str(self.try2) + "\n"
        "  " + "3: " + int(20 * (self.try3 / self.wins) + 1)* "#" + " " + str(self.try3) + "\n"  
        "  " + "4: " + int(20 * (self.try4 / self.wins) + 1) * "#" + " " + str(self.try4) + "\n"
        "  " + "5: " + int(20 * (self.try5 / self.wins)+ 1) * "#" + " "+ str(self.try5) + "\n"
        "  " + "6: " + int(20 * (self.try6 / self.wins) + 1) * "#" + " " + str(self.try6) + "\n")

# Person = WordlePlayer()

# Person.updateStats(True, 5)
# Person.updateStats(True, 4)
# Person.updateStats(True, 4)
# Person.updateStats(False, 0)
# Person.updateStats(True, 3)
# Person.updateStats(True, 1)

# print(Person.gamesPlayed())
# print(Person.winPercentage())
# print(Person.currentStreak())
# Print(Person.maxStreak())

# Person.displayStats()