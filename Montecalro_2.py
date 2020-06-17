# Creat a dice (1,100)
import random 
from __builtin__ import False

# define true or false of rolldice
def rollDice():
    roll = random.randint(1,100)
    
    if roll == 100:
        print roll,'\n roll was 100, you lose. What are the odds?! Play again.'
        return False
    elif roll <= 50:
        print roll,'roll was 1-50,you lose. Play again! '
        return False
    
    elif 50 < roll < 100:
        print roll,'roll 51-99, you win! *pretty lights flash* Play more'
        return True

def simple_bettor(funds,initial_wager,wager_count):
    value = funds
    wager = initial_wager
    
    currentWager = 0
    
    while currentWager < wager_count:
        if rollDice():  # if true, win money 
            value += wager
        else:
            value -= wager # if false, lose money
        
        currentWager += 1
        print 'Funds: %4d \n' %(value)
        
simple_bettor(1000,100,10)


    

