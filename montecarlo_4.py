import random
from __builtin__ import False, True
import time

import matplotlib
import matplotlib.pyplot as plt
import numpy as np


print 'Let\'s start'

#define rolldise as cascual
def rollDice():
    roll = random.randint(1,100)
    if  roll%2==0:
        return False
    else:
        return True

def doubler_bettor(funds,chips,gamecount):
    money = funds
    income = chips
    
    Xcount = []
    Ymoney = []
    
    currentwager = 1
    previouswager = 'win'
    previouswagerAmount = chips 
    
    while currentwager <= gamecount:
        if previouswager =='win':
            print 'We won the last wager'
            if rollDice():
                money += income
                print money
                Xcount.append(currentwager)
                Ymoney.append(money)
            else:
                money -= income
                previouswager = 'loss'
                print money
                previouswagerAmount = income
                Xcount.append(currentwager)
                Ymoney.append(money)
                if money < 0:
                    print'we went broke after'.currentwager,'bets'
                    currentwager += 100000000
        elif previouswager =='loss':
            print 'we lost the last one, so we will be smart and double'
            if rollDice():
                income = previouswagerAmount * 2
                print 'we won',income
                money += income
                print money
                income = chips
                previouswager = 'win'
                Xcount.append(currentwager)
                Ymoney.append(money)
            else:
                income = previouswagerAmount * 2
                print 'we lost',income
                money -=income
                if money < 0:
                    print 'we went broke after',currentwager,'bets'
                    currentwager += 100000
                    
                print money
                previouswager = 'loss'
                
                previouswagerAmount =income
                Xcount.append(currentwager)
                Ymoney.append(money)
                     
        currentwager += 1    
        
        
    print money
    plt.plot(Xcount,Ymoney) 
 
doubler_bettor(10000,100,100)
plt.show()

time.sleep(555)
                 
#define game role, initial money, each step and palytime
#If not enough money then break up (money = 0)
def game(funds,chips,gamecount):
    money = funds
    income = chips
    wintime = 0
    
    Xcount = []
    Ymoney = []
    count = 0   
    
    while count <gamecount:
        if rollDice():
            money += income
            wintime += 1
        else:
            money -= income
           
        Xcount.append(count)
        Ymoney.append(money)
        
        if money <= 0:
            money = 1 #define number 1 as breakup
            break
        
        
        count += 1
#     if money == 1:
#         print 'you\'ve breakup'
#     else:
#         print 'you got %d for %d times.' %(money,wintime)

#     #plot figure for each peopole
#     plt.plot(Xcount,Ymoney)
    

    
    return money

# If you got more than initial money then win.
def winner():
    if game(10000,100,10000) > 10000 :
        return True
    else:
        return False

# there are 100 people play this game, count how many people win    
n = 0
winnerpeople = 0
breakuppeople = 0
losepeople =0
fundsdata = []
while n <100:
    #game(10000,100,100)
    fundsdata.append(game(10000,100,10000))
    if winner():
        winnerpeople += 1
    elif winner() == 1:
        breakuppeople += 1
    else:
        losepeople += 1
    n += 1


print 'winner:', winnerpeople
print 'broke people',breakuppeople
print 'loser:',losepeople

fundsdata = [i for i in fundsdata if i != 1] # delete all elements that are equal to 1, i.e. money is equal to 0


#         
#print fundsdata
print max(fundsdata),min(fundsdata)

# #show plot for all people in single figure
# plt.xlabel('count')
# plt.ylabel('money')
# plt.show()

# show 100 people money distribution
#plt.plot(fundsdata)
#plt.show()


    
    
        
    




    
    
    
