#imports & functions 
import random
import time
import os 

class color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

os.system('clear')   #Title screen-----------------
print(color.BOLD + color.RED + "B", end="")       #
time.sleep(.1)                                    #
print(color.BOLD + color.GREEN + "I", end="")     #
time.sleep(.1)                                    #
print(color.BOLD + color.CYAN + "N", end="")      #
time.sleep(.1)                                    #
print(color.BOLD + color.DARKCYAN + "A", end="")  #
time.sleep(.1)                                    #
print(color.BOLD + color.BLUE + "R", end="")      #
time.sleep(.1)                                    #
print(color.BOLD + color.PURPLE + "Y", end="" + color.END)
time.sleep(.1)                                    #
print(" ")                                        #
print(color.BOLD + color.YELLOW + "Blackjack" + color.END)
#-------------------------------------------------#

deposit = 100000

#First input----------------------------------------------------
print(" ")                           
time.sleep(.1)                       
menu = input("Start(s) or Rules(r) ")
if menu == "s":
    os.system('clear')
    print(color.BOLD + "--------   --------")
    time.sleep(.04)
    print("|      |   |      |")
    time.sleep(.06)
    print("|      |   |      |")
    time.sleep(.06)
    print("|  K   |   |  ♤   |")
    time.sleep(.06)
    print("|      |   |      |")
    time.sleep(.06)
    print("|      |   |      |")
    time.sleep(.08)
    print("--------   --------" + color.END)
    time.sleep(.14)
if menu == "r":
    os.system('clear')
    print(color.BOLD + "Rules:")
    print("Binary blackjack is regular blackjack but only with the numbers 1-10")
    print("There are no aces, no kings queens or jacks. Only 1-10")
    print(color.END + " ")
    input("Press ENTER to continue")
#----------------------------------------------------------------

#clear screen + set balance 
balance = 10000
os.system('clear')
betsize = 0
playertotal = 0

#Begin game------------------------------
while balance >= 1:
    os.system('clear')
    print("Balance = $" + str(balance))
    print(" ")
    betsize = input("What amount would you like to bet? (1-" + str(balance) + ")")
    if int(betsize) > balance:
        os.system('clear')
        print(".", end="")
        time.sleep(.3)
        print(".", end="")
        time.sleep(.3)
        print(".", end="")
        time.sleep(.3)
        os.system('clear')
        print("You can't bet that much, asshole.")
        input(" ")
        continue
    if int(betsize) < 1:
        os.system('clear')
        print("You have to bet something. ")
        continue 
    c1 = random.randint(1,10)
    c2 = random.randint(1,10)     #c1 is the dealers cards
    c3 = random.randint(1,10)
    c4 = random.randint(1,10)
    c5 = random.randint(1,10)
    c6 = random.randint(1,10)
    c7 = random.randint(1,10)
    c8 = random.randint(1,10)
    c9 = random.randint(1,10)
    c10 = random.randint(1,10)
    pc1 = random.randint(1,10)
    pc2 = random.randint(1,10)      #pc1 is the players cards 
    pc3 = random.randint(1,10)
    pc4 = random.randint(1,10)
    pc5 = random.randint(1,10)
    pc6 = random.randint(1,10)
    pc7 = random.randint(1,10)
    pc8 = random.randint(1,10)
    pc9 = random.randint(1,10)
    pc10 = random.randint(1,10)
    playertotal = pc1 + pc2
    balance = int(balance) - int(betsize) 
    os.system('clear') #---------------#
    print("Dealing cards", end="")     #
    time.sleep(.3)                     #
    print(".", end="")                 #
    time.sleep(.3)                     #
    print(".", end="")                 # loading animation 
    time.sleep(.3)                     #
    print(".")                         #
    time.sleep(.5)                     #
    os.system('clear') #---------------#
    print("Dealer:")   #---------------------------#
    print("--------   --------")                   #
    print("|      |   |      |")                   #
    print("|  " + str(c1) + "   |   |  ♤   |")    #
    print("|      |   |      |")                   #
    print("|      |   |      |")                   #
    print("--------   --------")                   # 
    print("   ")                                   #
    time.sleep(.1)                         # dealer cards and your cards
    print("Your cards:")                           #
    print("--------   --------")                   #
    print("|      |   |      |")                   #
    print("|  " + str(pc1) + "   |   |  " + str(pc2) + "   |")
    print("|      |   |      |")                   #
    print("|      |   |      |")                   #
    print("--------   --------")                   #
    print("   ")               
    playertotal = pc1 + pc2                    #
    hitorstay = input("Hit(h) or stay(s)? ")#------#

    if hitorstay == "h":
        os.system('clear')
        print(" ")
        print("Dealer:")   #---------------------------#
        print("--------   --------")                   #
        print("|      |   |      |")                   #
        print("|  " + str(c1) + "   |   |  ♤   |")    #
        print("|      |   |      |")                   #
        print("|      |   |      |")                   #
        print("--------   --------")                   # 
        print("   ")         
        print("Your cards:")    #Hit or stay if hit: 
        print(" ")
        print("--------   --------   --------")                     
        print("|      |   |      |   |      |")                 
        print("|  " + str(pc1) + "   |   |  " + str(pc2) + "   |   |  " + str(pc3) + "   |")
        print("|      |   |      |   |      |")                  
        print("|      |   |      |   |      |")                 
        print("--------   --------   --------")
        print("   ")               
        playertotal = pc1 + pc2 + pc3
        print("Player total: " + str(playertotal))
        if playertotal > 21:
            
            print("Player busts!")
            input(" ")
            if balance == 0:
                if deposit == 0:
                    break
            if deposit != 0:
                if balance == 0:
                    os.system('clear')
                    print("You are out of money")
                    depo = input("How much would you like to deposit? (1-" + str(deposit) + ")")
                    deposit = deposit - int(depo)
                    balance = balance + int(depo)
                    os.system('clear')
                    print("Amount remaining in emergency fund: $" + str(deposit))
                    input(" ")
                    continue  
        hitorstay = input("Hit(h) or stay(s)? ")#------#
    
        if hitorstay == "h":
            os.system('clear')
            print(" ")
            print("Dealer:")   #---------------------------#
            print("--------   --------")                   #
            print("|      |   |      |")                   #
            print("|  " + str(c1) + "   |   |  ♤   |")    #
            print("|      |   |      |")                   #
            print("|      |   |      |")                   #
            print("--------   --------")                   # 
            print(" ")
            print("Your cards:")    #Hit or stay if hit: 
            print(" ")
            print("--------   --------   --------   --------")               
            print("|      |   |      |   |      |   |      |")                 
            print("|  " + str(pc1) + "   |   |  " + str(pc2) + "   |   |  " + str(pc3) + "   |   |  " + str(pc4) + "   |")
            print("|      |   |      |   |      |   |      |")                  
            print("|      |   |      |   |      |   |      |")                 
            print("--------   --------   --------   --------")
            print("   ")        
            playertotal = pc1 + pc2 + pc3 + pc4
            print("Player total: " + str(playertotal))
            if playertotal > 21:
                print("Player busts!")
                input(" ")
                if balance == 0:
                    if deposit == 0:
                        break
                if deposit != 0:
                    if balance == 0:
                        os.system('clear')
                        print("You are out of money")
                        depo = input("How much would you like to deposit? (1-" + str(deposit) + ")")
                        deposit = deposit - int(depo)
                        balance = balance + int(depo)
                        os.system('clear')
                        print("Amount remaining in emergency fund: $" + str(deposit))
                        input(" ")
                        continue  
            hitorstay = input("Hit(h) or stay(s)? ")#------#
        
            if hitorstay == "h":
                os.system('clear')
                print(" ")
                print("Dealer:")   #---------------------------#
                print("--------   --------")                   #
                print("|      |   |      |")                   #
                print("|  " + str(c1) + "   |   |  ♤   |")    #
                print("|      |   |      |")                   #
                print("|      |   |      |")                   #
                print("--------   --------")                   # 
                print(" ")
                print("Your cards:")    #Hit or stay if hit: 
                print(" ")
                print("--------   --------   --------   --------   --------")        
                print("|      |   |      |   |      |   |      |   |      |")  
                print("|  " + str(pc1) + "   |   |  " + str(pc2) + "   |   |  " + str(pc3) + "   |   |  " + str(pc4) + "   |   |  " + str(pc5) + "   |")
                print("|      |   |      |   |      |   |      |   |      |")             
                print("|      |   |      |   |      |   |      |   |      |")                 
                print("--------   --------   --------   --------   --------")
                print("   ")   
                playertotal = pc1 + pc2 + pc3 + pc4 + pc5
                print("Player total: " + str(playertotal))
                if playertotal > 21:
                    print("Player busts!")
                    input(" ")
                    if balance == 0:
                        if deposit == 0:
                            break
                    if deposit != 0:
                        if balance == 0:
                            os.system('clear')
                            print("You are out of money")
                            depo = input("How much would you like to deposit? (1-" + str(deposit) + ")")
                            deposit = deposit - int(depo)
                            balance = balance + int(depo)
                            os.system('clear')
                            print("Amount remaining in emergency fund: $" + str(deposit))
                            input(" ")
                            continue 
                hitorstay = input("Hit(h) or stay(s)? ")#------#

                if hitorstay == "h":
                    os.system('clear')
                    print(" ")
                    print("Dealer:")   #---------------------------#
                    print("--------   --------")                   #
                    print("|      |   |      |")                   #
                    print("|  " + str(c1) + "   |   |  ♤   |")    #
                    print("|      |   |      |")                   #
                    print("|      |   |      |")                   #
                    print("--------   --------")                   # 
                    print(" ")
                    print("Your cards:")    #Hit or stay if hit: 
                    print(" ")
                    print("--------   --------   --------   --------   --------   --------")       
                    print("|      |   |      |   |      |   |      |   |      |   |      |")
                    print("|  " + str(pc1) + "   |   |  " + str(pc2) + "   |   |  " + str(pc3) + "   |   |  " + str(pc4) + "   |   |  " + str(pc5) + "   |   |  " + str(pc6) + "   |")
                    print("|      |   |      |   |      |   |      |   |      |   |      |")            
                    print("|      |   |      |   |      |   |      |   |      |   |      |")            
                    print("--------   --------   --------   --------   --------   --------")
                    print("   ")   
                    playertotal = pc1 + pc2 + pc3 + pc4 + pc5 + pc6
                    print("Player total: " + str(playertotal))
                    if playertotal > 21:
                        print("Player busts!")
                        input(" ")
                        if balance == 0:
                            if deposit == 0:
                                break
                        if deposit != 0:
                            if balance == 0:
                                os.system('clear')
                                print("You are out of money")
                                depo = input("How much would you like to deposit? (1-" + str(deposit) + ")")
                                deposit = deposit - int(depo)
                                balance = balance + int(depo)
                                os.system('clear')
                                print("Amount remaining in emergency fund: $" + str(deposit))
                                input(" ")
                                continue 
                    hitorstay = input("Hit(h) or stay(s)? ")#------#

                    if hitorstay == "h":
                        print("You have so many cards, you win.")
                        input(" ")
                        balance = balance + int(betsize) * 2
                        time.sleep(.9)
                        print("Winnings: $" + str(int(betsize) * 2))
                        input(" ")
                        continue
                    
                    



           #stay
    os.system('clear')
    print(".", end="")
    time.sleep(.2)
    print(".", end="")
    time.sleep(.2)
    print(".", end="")
    time.sleep(.2)
    os.system('clear')
    print("Your total: " + str(playertotal))
    print("   ")
    print("Dealer:")
    print("--------   --------")
    print("|      |   |      |")
    print("|  " + str(c1) + "   |   |  ♤   |")
    print("|      |   |      |")
    print("|      |   |      |")
    print("--------   --------")
    print("   ")
    time.sleep(.25)
    os.system('clear')
    print("Your total: " + str(playertotal))
    print("   ")
    print("Dealer:")
    print("--------   |‾‾| ")
    print("|      |   |   ‾‾|")
    print("|  " + str(c1) + "   |   | " + str("♤") + "   |")
    print("|      |   |     |")
    print("|      |    ‾‾|  |")
    print("--------      |__|")
    print("   ")
    time.sleep(.17)
    os.system('clear')
    print("Your total: " + str(playertotal))
    print("   ")
    print("Dealer:")
    print("--------   |")
    print("|      |   |")
    print("|  " + str(c1) + "   |   |")
    print("|      |    |")
    print("|      |    |")
    print("--------    |")
    print("   ")
    time.sleep(.17)
    os.system('clear')
    print("Your total: " + str(playertotal))
    print("   ")
    print("Dealer:")
    print("--------      |‾‾|")
    print("|      |   |‾‾   |")
    print("|  " + str(c1) + "   |   |     |")
    print("|      |   |   __|")
    print("|      |   |  |")
    print("--------   |__|")
    print("   ")
    time.sleep(.17)
    os.system('clear')
    print("Your total: " + str(playertotal))
    print("   ")
    print("Dealer:")
    print("--------   --------")
    print("|      |   |      |")
    print("|  " + str(c1) + "   |   |  " + str(c2) + "   |")
    print("|      |   |      |")
    print("|      |   |      |")
    print("--------   --------")
    print("   ")
    dealertotal = c1 + c2 
    input(" ")
    if dealertotal == playertotal:
        print("Dealer stays with " + str(dealertotal))
        print(" ")
        print("Push")
        input(" ")
        balance = int(balance) + int(betsize) 

    if dealertotal > 16 and dealertotal <= 21:
        print("Dealer stays with " + str(dealertotal))
        if playertotal > dealertotal and playertotal < 22:
            balance = balance + int(betsize) * 2
            print(" ")
            print("You win!")
            time.sleep(.4)
            print("Winnings: $" + str(int(betsize) * 2))
            input(" ")
        if playertotal < dealertotal:
            print(" ")
            print("Dealer wins $" + str(betsize))
            time.sleep(.4)
            input(" ")
            if balance == 0:
                if deposit == 0:
                    break
            if deposit != 0:
                if balance == 0:
                    os.system('clear')
                    print("You are out of money")
                    depo = input("How much would you like to deposit? (1-" + str(deposit) + ")")
                    deposit = deposit - int(depo)
                    balance = balance + int(depo)
                    os.system('clear')
                    print("Amount remaining in emergency fund: $" + str(deposit))
                    input(" ")
                    continue 
    if dealertotal > 21:
        balance = balance + int(betsize) * 2
        print("Dealer busts with " + str(dealertotal))
        print(" ")
        print("You win!")
        time.sleep(.4)
        print("Winnings: $" + str(int(betsize) * 2))
        input(" ")
    if c1 + c2 < 17:  #3rd card
        os.system('clear')
        print("Your total: " + str(playertotal))
        print("   ")
        print("Dealer:")
        print("--------   --------   --------")        
        print("|      |   |      |")              
        print("|  " + str(c1) + "   |   |  " + str(c2) + "   |")
        print("|      |   |      |")    
        print("|      |   |      |")  
        print("--------   --------")
        print("   ")   
        time.sleep(.04)     
        os.system('clear')
        print("Your total: " + str(playertotal))
        print("   ")
        print("Dealer:")
        print("--------   --------   |      |")          
        print("|      |   |      |   --------")             
        print("|  " + str(c1) + "   |   |  " + str(c2) + "   |")
        print("|      |   |      |")     
        print("|      |   |      |")
        print("--------   --------")
        print("   ")   
        time.sleep(.05)   
        os.system('clear')
        print("Your total: " + str(playertotal))
        print("   ")
        print("Dealer:")
        print("--------   --------   |      |")
        print("|      |   |      |   |      |")
        print("|  " + str(c1) + "   |   |  " + str(c2) + "   |   --------")
        print("|      |   |      |")     
        print("|      |   |      |")
        print("--------   --------")
        print("   ")   
        time.sleep(.06)  
        os.system('clear')
        print("Your total: " + str(playertotal))
        print("   ")
        print("Dealer:")
        print("--------   --------   |  " + str(c3) + "   |")
        print("|      |   |      |   |      |")
        print("|  " + str(c1) + "   |   |  " + str(c2) + "   |   |      |")
        print("|      |   |      |   --------")
        print("|      |   |      |")
        print("--------   --------")
        print("   ")   
        time.sleep(.08) 
        os.system('clear')
        print("Your total: " + str(playertotal))
        print("   ")
        print("Dealer:")
        print("--------   --------   |      |")
        print("|      |   |      |   |  " + str(c3) + "   |")
        print("|  " + str(c1) + "   |   |  " + str(c2) + "   |   |      |")
        print("|      |   |      |   |      |")
        print("|      |   |      |   --------")
        print("--------   --------")
        print("   ")   
        time.sleep(.1)    
        os.system('clear')
        print("Your total: " + str(playertotal))
        print("   ")
        print("Dealer:")
        print("--------   --------   --------")
        print("|      |   |      |   |      |")
        print("|  " + str(c1) + "   |   |  " + str(c2) + "   |   |  " + str(c3) + "   |")
        print("|      |   |      |   |      |")
        print("|      |   |      |   |      |")
        print("--------   --------   --------")
        print("   ")   
        time.sleep(.06)     
        dealertotal = c1 + c2 + c3
        print(" ")
        input(" ")
        if playertotal == dealertotal:
            print("Dealer stays with " + str(dealertotal))
            print(" ")
            print("Push")
            input(" ")
            balance = int(balance) + int(betsize) 
        if dealertotal > 16 and dealertotal <= 21:
            print("Dealer stays with " + str(dealertotal))
            if playertotal > dealertotal and playertotal < 22:
                balance = balance + int(betsize) * 2
                print(" ")
                print("You win!")
                time.sleep(.6)
                print("Winnings: $" + str(int(betsize) * 2))
                input(" ")
            if playertotal < dealertotal:
                print(" ")
                print("Dealer wins $" + str(betsize))
                time.sleep(.8)
                input(" ")
                if balance == 0:
                    if deposit == 0:
                        break
                if deposit != 0:
                    if balance == 0:
                        os.system('clear')
                        print("You are out of money")
                        depo = input("How much would you like to deposit? (1-" + str(deposit) + ")")
                        deposit = deposit - int(depo)
                        balance = balance + int(depo)
                        os.system('clear')
                        print("Amount remaining in emergency fund: $" + str(deposit))
                        input(" ")
                        continue 
        if dealertotal > 21:
            balance = balance + int(betsize) * 2
            print("Dealer busts with " + str(dealertotal))
            print(" ")
            print("You win!")
            time.sleep(.6)
            print("Winnings: $" + str(int(betsize) * 2))
            input(" ")
        if c1 + c2 + c3 < 17:    #4th card
            os.system('clear')
            print("Your total: " + str(playertotal))
            print("   ")
            print("Dealer:")
            print("--------   --------   --------   --------")               
            print("|      |   |      |   |      |   |      |")                 
            print("|  " + str(c1) + "   |   |  " + str(c2) + "   |   |  " + str(c3) + "   |   |  " + str(c4) + "   |")
            print("|      |   |      |   |      |   |      |")                  
            print("|      |   |      |   |      |   |      |")                 
            print("--------   --------   --------   --------")
            print("   ")        
            dealertotal = c1 + c2 + c3 + c4
            print(" ")
            input(" ")
            if playertotal == dealertotal:
                print("Dealer stays with " + str(dealertotal))
                print(" ")
                print("Push")
                input(" ")
                balance = int(balance) + int(betsize) 
            if dealertotal > 16 and dealertotal <= 21:
                print("Dealer stays with " + str(dealertotal))
                if playertotal > dealertotal and playertotal < 22:
                    balance = balance + int(betsize) * 2
                    print(" ")
                    print("You win!")
                    time.sleep(.4)
                    print("Winnings: $" + str(int(betsize) * 2))
                    input(" ")
                if playertotal < dealertotal:
                    print(" ")
                    print("Dealer wins $" + str(betsize))
                    time.sleep(.4)
                    input(" ")
                    if balance == 0:
                        if deposit == 0:
                            break
                    if deposit != 0:
                        if balance == 0:
                            os.system('clear')
                            print("You are out of money")
                            depo = input("How much would you like to deposit? (1-" + str(deposit) + ")")
                            deposit = deposit - int(depo)
                            balance = balance + int(depo)
                            os.system('clear')
                            print("Amount remaining in emergency fund: $" + str(deposit))
                            input(" ")
                            continue 
            if dealertotal > 21:
                balance = balance + int(betsize) * 2
                print("Dealer busts with " + str(dealertotal))
                print(" ")
                print("You win!")
                time.sleep(.4)
                print("Winnings: $" + str(int(betsize) * 2))
                input(" ")
            if c1 + c2 + c3 + c4 < 17:  #5th card
                os.system('clear')
                print("Your total: " + str(playertotal))
                print("   ")
                print("Dealer:")
                print("--------   --------   --------   --------   --------")        
                print("|      |   |      |   |      |   |      |   |      |")  
                print("|  " + str(c1) + "   |   |  " + str(c2) + "   |   |  " + str(c3) + "   |   |  " + str(c4) + "   |   |  " + str(c5) + "   |")
                print("|      |   |      |   |      |   |      |   |      |")             
                print("|      |   |      |   |      |   |      |   |      |")                 
                print("--------   --------   --------   --------   --------")
                print("   ")   
                dealertotal = c1 + c2 + c3 + c4 + c5
                print(" ")
                input(" ")
                if playertotal == dealertotal:
                    print("Dealer stays with " + str(dealertotal))
                    print(" ")
                    print("Push")
                    input(" ")
                    balance = int(balance) + int(betsize) 
                if dealertotal > 16 and dealertotal <= 21:
                    
                    print("Dealer stays with " + str(dealertotal))
                    if playertotal > dealertotal and playertotal < 22:
                        balance = balance + int(betsize) * 2
                        print(" ")
                        print("You win!")
                        time.sleep(.6)
                        print("Winnings: $" + str(int(betsize) * 2))
                        input(" ")
                    if playertotal < dealertotal:
                        print(" ")
                        print("Dealer wins $" + str(betsize))
                        time.sleep(.8)
                        input(" ")
                        if balance == 0:
                            if deposit == 0:
                                break
                        if deposit != 0:
                            if balance == 0:
                                os.system('clear')
                                print("You are out of money")
                                depo = input("How much would you like to deposit? (1-" + str(deposit) + ")")
                                deposit = deposit - int(depo)
                                balance = balance + int(depo)
                                os.system('clear')
                                print("Amount remaining in emergency fund: $" + str(deposit))
                                input(" ")
                                continue 
                if dealertotal > 21:
                    balance = balance + int(betsize) * 2
                    
                    print("Dealer busts with " + str(dealertotal))
                    print(" ")
                    print("You win!")
                    time.sleep(.6)
                    print("Winnings: $" + str(int(betsize) * 2))
                    input(" ")
                if c1 + c2 + c3 + c4 + c5 < 17:   #6th card
                    os.system('clear')
                    print("Your total: " + str(playertotal))
                    print("   ")
                    print("Dealer:")
                    print("--------   --------   --------   --------   --------   --------")       
                    print("|      |   |      |   |      |   |      |   |      |   |      |")
                    print("|  " + str(c1) + "   |   |  " + str(c2) + "   |   |  " + str(c3) + "   |   |  " + str(c4) + "   |   |  " + str(c5) + "   |   |  " + str(c6) + "   |")
                    print("|      |   |      |   |      |   |      |   |      |   |      |")            
                    print("|      |   |      |   |      |   |      |   |      |   |      |")            
                    print("--------   --------   --------   --------   --------   --------")
                    print("   ")   
                    dealertotal = c1 + c2 + c3 + c4 + c5 + c6
                    print(" ")
                    input(" ")
                    if playertotal == dealertotal:
                        print("Dealer stays with " + str(dealertotal))
                        print(" ")
                        print("Push")
                        input(" ")
                        balance = int(balance) + int(betsize) 
                    if dealertotal > 16 and dealertotal <= 21:
                        
                        print("Dealer stays with " + str(dealertotal))
                        if playertotal > dealertotal and playertotal < 22:
                            balance = balance + int(betsize) * 2
                            print(" ")
                            print("You win!")
                            time.sleep(.6)
                            print("Winnings: $" + str(int(betsize) * 2))
                            input(" ")
                        if playertotal < dealertotal:
                            print(" ")
                            print("Dealer wins $" + str(betsize))
                            time.sleep(.8)
                            input(" ")
                            if balance == 0:
                                if deposit == 0:
                                    break
                            if deposit != 0:
                                if balance == 0:
                                        os.system('clear')
                                        print("You are out of money")
                                        depo = input("How much would you like to deposit? (1-" + str(deposit) + ")")
                                        deposit = deposit - int(depo)
                                        balance = balance + int(depo)
                                        os.system('clear')
                                        print("Amount remaining in emergency fund: $" + str(deposit))
                                        input(" ")
                                        continue 
                    if dealertotal > 21:
                        balance = balance + int(betsize) * 2
                        
                        print("Dealer busts with " + str(dealertotal))
                        print(" ")
                        print("You win!")
                        time.sleep(.6)
                        print("Winnings: $" + str(int(betsize) * 2))
                        input(" ")
                    if dealertotal < 17:
                        os.system('clear')
                        print(".", end="")
                        time.sleep(.2)
                        print(".", end="")
                        time.sleep(.2)
                        print(".", end="")
                        time.sleep(.2)
                        os.system('clear')
                        print("Dealer ran out of cards")
                        print(" ")
                        print("I guess we'll just try that again")
                        print(" ")
                        balance = int(balance) + int(betsize) 
os.system('clear')        
print("You have a problem")
time.sleep(1.2)
print(" ")
print("You have gambled away everything you have")
time.sleep(1.6)
print(" ")
print("You are screwed")