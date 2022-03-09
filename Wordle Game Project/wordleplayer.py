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
import time

# TODO - make WordlePlayer
class WordlePlayer(Player):

    def __init__(self, name, maxTry):
        super().__init__(name)
        self.maxTry = maxTry
        self.listofTries = []
        self.wins = 0
        self.plays = 0
        self.streak = 0
        self.prevWin = False
        self.maxstreak = 0
    
    def updateStats(self, won, tries):
        self.plays += 1
        self.listofTries.append(tries)
        
        if won == True:
            self.wins += 1
            self.prevWin = True
            
        else: 
            self.prevWin = False
        
        if won == True:
            self.streak += 1
        
        else:
            self.streak = 0
        
        if self.streak > self.maxstreak:
            self.maxstreak = self.streak

    def winPercentage(self):
        if self.plays != 0:
            self.percentage = self.wins / self.plays * 100
            return self.percentage
        else:
            self.percentage = 0
            return self.percentage
    
    def tryAmounts(self):
        amountlist = []
        if self.wins != 0: 
            for a in range(self.maxTry):
                amount = self.listofTries.count(a + 1)
                amountlist.append(amount)
            highestamount = 0
            for value in amountlist:
                if amountlist[value] > highestamount:
                    highestamount = amountlist[value]
        else:
            for b in range(self.maxTry):
                amountlist.append(0)
            highestamount = 1
        return (amountlist, highestamount)

    def gamesPlayed(self):
        return self.plays

    def currentStreak(self):
        return self.streak

    def maxStreak(self):
        return self.maxstreak

    def displayStats(self):
        for i in range (1,51):
            print('\n'*50)
            print(
            "Games Played: " + str(round(i/50*self.plays)) + "\n"
            "Win %: " + str(round(i/50*self.winPercentage())) + "%\n"
            "Current Streak: " + str(round(i/50*self.currentStreak())) + "\n"
            "Max Streak: " + str(round(i/50*self.maxStreak())) + "\n"
            "Guess Distribution")

            for value in range(self.maxTry):
                barlength = int(20 * (self.tryAmounts()[0][value]/self.tryAmounts()[1]) + 1) #this is the max
                barlength = round((i/50) * barlength)
                print("  " + str(value + 1) + ': ' + barlength * "#" + " " + str(round(i/50*self.tryAmounts()[0][value])))
            time.sleep(0.07*i/50)
        
        #print("  " + "1: " + int(20 * (self.tryPercentage()[0]) + 1) * "#" + " " + str(self.try1) + "\n"
        #"  " + "2: " + int(20 * (self.percent2) + 1)* "#" + " " + str(self.try2) + "\n"
        #"  " + "3: " + int(20 * (self.percent3) + 1)* "#" + " " + str(self.try3) + "\n"  
        #"  " + "4: " + int(20 * (self.percent4) + 1) * "#" + " " + str(self.try4) + "\n"
        #"  " + "5: " + int(20 * (self.percent5)+ 1) * "#" + " "+ str(self.try5) + "\n"
        #"  " + "6: " + int(20 * (self.percent6) + 1) * "#" + " " + str(self.try6) + "\n")

    def displayStats2(self):
        for value in range(self.maxTry):
            for i in range (1,50):
                print('\n'*50)
                print(
                "Games Played: " + str(self.plays) + "\n"
                "Win %: " + str(round(self.winPercentage())) + "%\n"
                "Current Streak: " + str(self.currentStreak()) + "\n"
                "Max Streak: " + str(self.maxStreak()) + "\n"
                "Guess Distribution")
                for val in range(self.maxTry):
                    if val > value:
                        barlength = 0
                    if val == value:
                        barlength = int(20 * (self.tryAmounts()[0][val]/self.tryAmounts()[1]) + 1) #this is the max
                        barlength = round((i/50) * barlength)
                    if val < value:
                        barlength = int(20 * (self.tryAmounts()[0][val]/self.tryAmounts()[1]) + 1)
                    print("  " + str(val + 1) + ': ' + barlength * "#" + " " + str(round(i/50*self.tryAmounts()[0][val])))
                time.sleep(0.04*i/50)

Person = WordlePlayer('person', 6)

Person.updateStats(True, 3)
Person.updateStats(True, 3)
Person.updateStats(True, 4)
Person.updateStats(False, 0)
Person.updateStats(True, 5)
Person.updateStats(True, 5)
Person.updateStats(True, 3)
Person.updateStats(True, 2)
Person.updateStats(False, 20)
Person.updateStats(True, 2)
Person.updateStats(True, 3)

# print(Person.gamesPlayed())
# print(Person.winPercentage())
# print(Person.currentStreak())
# print(Person.maxStreak())
#print(Person.tryAmounts())

#Person.displayStats()

#input()


#Person.displayStats2()

#input()
