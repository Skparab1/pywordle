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
class WordlePlayer(Player): # inherit from player

    def __init__(self, name, maxTry): #create variables
        super().__init__(name)
        self.maxTry = maxTry
        self.listofTries = []
        self.wins = 0
        self.plays = 0
        self.streak = 0
        self.maxstreak = 0
    
    def updateStats(self, won, tries): # updates the stats of the player, doesn't return anything
        self.plays += 1 # updates the number of plays
        self.listofTries.append(tries) #adds the amount of tries taken to be used in tryPercentage function
        
        if won == True:  # updates the number of wins
            self.wins += 1
        
        if won == True: # updates the streak
            self.streak += 1
        
        else:
            self.streak = 0
        
        if self.streak > self.maxstreak: # updates max streak when necessary
            self.maxstreak = self.streak

    def winPercentage(self): # returns the win percentage
        if self.plays != 0:
            self.percentage = self.wins / self.plays * 100
            return self.percentage
        else:
            self.percentage = 0
            return self.percentage
    
    def tryAmounts(self): # returns a list wih the amount of tries and the highebst amount of tries for the graph
        amountlist = [] 
        for a in range(self.maxTry):
            amount = self.listofTries.count(a + 1)
            amountlist.append(amount) # creates the list with the amiunt of tries
        highestamount = 1 
        for value in amountlist:
            if amountlist[value] > highestamount:
                highestamount = amountlist[value] # determines the highest amount
        return (amountlist, highestamount)

    def gamesPlayed(self): # returns the number of games played
        return self.plays

    def currentStreak(self): # returns the current streak
        return self.streak

    def maxStreak(self): # returns the max streak
        return self.maxstreak

    def displayStats(self):   #prints out the stats
        for i in range (1,51):
            print('\n'*50)
            print(
            "Games Played: " + str(round(i/50*self.plays)) + "\n"
            "Win %: " + str(round(i/50*self.winPercentage())) + "%\n"
            "Current Streak: " + str(round(i/50*self.currentStreak())) + "\n"
            "Max Streak: " + str(round(i/50*self.maxStreak())) + "\n"
            "Guess Distribution")

            for value in range(self.maxTry):     # animateds the graph when printing it out
                barlength = int(20 * (self.tryAmounts()[0][value]/self.tryAmounts()[1]) + 1) #this is the max
                barlength = round((i/50) * barlength)
                print("  " + str(value + 1) + ': ' + barlength * "#" + " " + str(round(i/50*self.tryAmounts()[0][value])))
            time.sleep(0.07*i/50)
        
        

#testing below

#Person = WordlePlayer('person', 6)

#Person.updateStats(True, 3)
#Person.updateStats(True, 3)
#Person.updateStats(True, 4)
#Person.updateStats(False, 0)
#Person.updateStats(True, 5)
#Person.updateStats(True, 5)
#Person.updateStats(True, 3)
#Person.updateStats(True, 2)
#Person.updateStats(False, 20)
#Person.updateStats(True, 2)
#Person.updateStats(True, 3)

# print(Person.gamesPlayed())
# print(Person.winPercentage())
# print(Person.currentStreak())
# print(Person.maxStreak())
#print(Person.tryAmounts())

#Person.displayStats()

#input()


#Person.displayStats2()

#input()
