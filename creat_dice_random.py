# Creat a dice (1,100)
import random 

# define rendom # 1,100, 
def rollDice():
    roll = random.randint(1,100)
    return roll

x = 0

while x < 100:
    result = rollDice()
    print result # print # that is less than 100
    x += 1
    
print 'All Done'
