import time
import random

spins = 0 
balence = 30

while balence > -1000:
    input(" ")
    rndnum1 = random.randint(1,7)
    rndnum2 = random.randint(1,7)
    rndnum3 = random.randint(1,7)           
    print(rndnum1, rndnum2, rndnum3) 
    time.sleep(.08)
    rndnum4 = random.randint(1,7)
    rndnum5 = random.randint(1,7)
    rndnum6 = random.randint(1,7)
    print(rndnum4, rndnum5, rndnum6)
    time.sleep(.08)
    rndnum7 = random.randint(1,7)
    rndnum8 = random.randint(1,7)
    rndnum9 = random.randint(1,7)
    print(rndnum7, rndnum8, rndnum9)
    time.sleep(.08)
    print(" ")
    if rndnum1 == rndnum2 == rndnum3:
        print("Full line!")
        print("Line 1")
        print("+ $" + str(rndnum1 * 50))
        print(" ")
        balence = balence + (rndnum1*50)
        
    if rndnum4 == rndnum5 == rndnum6:
        print("Full line!")
        print("Line 2")
        print("+ $" + str(rndnum4 * 50))
        print(" ")
        balence = balence + (rndnum4*50)
        
    if rndnum7 == rndnum8 == rndnum9:
        print("Full line!")
        print("Line 3")
        print("+ $" + str(rndnum7 * 50))
        print(" ")
        balence = balence + (rndnum7*50)
        
    if rndnum1 == rndnum2 == rndnum3 == rndnum4 == rndnum5 == rndnum6 == rndnum7 == rndnum8 == rndnum9: 
        print("Full screen!")
        print("+ $" + str(rndnum1 * 200))
        print(" ")
        if rndnum9 == 7:
            print(" ")
            print("MAX WIN!")
            print(" ")
            balence = balence + (rndnum1*200)
            
        else:
            balence = balence + (rndnum1 * 200)
            
    if rndnum1 == rndnum5 == rndnum9:
        print("Diagnol line!")
        print("+ $" + str(rndnum1 * 20))
        print(" ")
        balence = balence + (rndnum1 * 20)
        
    if rndnum7 == rndnum5 == rndnum3:
        print("Diagnol line!")
        print("+ $" + str(rndnum7 * 20))
        print(" ")
        balence = balence + (rndnum7 * 20)
        
    if rndnum1 == rndnum2:
        print("Doubles!")
        print("Line 1")
        print("+ $" + str(rndnum1 * 5))
        print(" ")
        balence = balence + (rndnum1 * 5)
        
    if rndnum4 == rndnum5:
        print("Doubles!")
        print("Line 2")
        print("+ $" + str(rndnum4 * 5))
        print(" ")
        balence = balence + (rndnum4 * 5)
        
    if rndnum7 == rndnum8:
        print("Doubles!")
        print("Line 3")
        print("+ $" + str(rndnum7 * 5))    
        print(" ")
        balence = balence + (rndnum7 * 5)
        
    if rndnum1 == rndnum5 == rndnum3:
        print("Curve win!")
        print("Line 1")
        print("+ $" + str(rndnum1 * 15)) 
        print(" ")
        balence = balence + (rndnum1 * 15)
        
    if rndnum7 == rndnum5 == rndnum9:
        print("Curve win!")
        print("Line 3")
        print("+ $" + str(rndnum7 * 15)) 
        print(" ")
        balence = balence + (rndnum7 * 15)
    
    balence = balence - 25 
    time.sleep(.05)
    print("Balance= $" + str(balence))
