import time
import random
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

i = 0
edging = 0
balance = 100


while balance > 0:
    while i < 16:
        os.system('clear')
        r1 = random.randint(4,7)
        if i >= 12:
            time.sleep(.07)
        print(color.BOLD + str(r1), end=" " + color.END)
        time.sleep(.06)
        i = i + 1
        if i >= 5:
            r2 = random.randint(4,7)
            if i >= 12:
                time.sleep(.07)
            print(color.BOLD + str(r2), end=" " + color.END)
            time.sleep(.06)
            if i >= 10:
                r3 = random.randint(4,7)
                if i >= 12:
                    time.sleep(.07)
                print(color.BOLD + str(r3), end=" " + color.END)
                time.sleep(.06)
                if i == 15:
                    if r1 == r2:
                        while edging <= 6:
                            os.system('clear')
                            print(r1, end= " ")
                            print(r2, end= " ")
                            r3 = random.randint(4,7)
                            print(r3, end=" ")
                            time.sleep(.4)
                            edging = edging + 1
                            if edging == 7 and r1 == r2 != r3:
                                print(":(")
                                time.sleep(.8)
                            if r1 == r2 == r3 and edging == 7:
                                for i in range(10):
                                    os.system('clear')
                                    print(color.BOLD + color.RED + str(r1), " ", str(r2), " ", str(r3) + color.END)
                                    print("Full line " + str(r1) + "'s!")
                                    time.sleep(.1)
                                    os.system('clear')
                                    print(color.BOLD + color.YELLOW + str(r1), " ", str(r2), " ", str(r3) + color.END)
                                    print("Full line " + str(r1) + "'s!")
                                    time.sleep(.1)
                                    os.system('clear')
                                    print(color.BOLD + color.GREEN + str(r1), " ", str(r2), " ", str(r3) + color.END)
                                    print("Full line " + str(r1) + "'s!")
                                    time.sleep(.1)
                                    os.system('clear')
                                    print(color.BOLD + color.BLUE + str(r1), " ", str(r2), " ", str(r3) + color.END)
                                    print("Full line " + str(r1) + "'s!")
                                    time.sleep(.1)
                                    os.system('clear')
                                    print(color.BOLD + color.PURPLE + str(r1), " ", str(r2), " ", str(r3) + color.END)
                                    print("Full line " + str(r1) + "'s!")
                                    time.sleep(.1)
                                edging = edging + 100
                                r1 = r1 * 10
                                print("+ $" + str(r1))
                                time.sleep(1.2)
                                print(" ")
                                balance = balance + r1 
                                print(color.BOLD + color.GREEN + "Current balance: $" + str(balance) + color.END)
                                time.sleep(1.2)
                        edging = 0 
                    print(" ")
                    print(" ")
                    if balance > 50:
                        print(color.BOLD + color.GREEN + "Current balance: $" + str(balance) + color.END)
                        time.sleep(.6)
                    if balance <= 50 and balance > 20:
                        print(color.BOLD + color.YELLOW + "Current balance: $" + str(balance) + color.END)
                        time.sleep(.8)
                    if balance <= 20:
                        print(color.BOLD + color.RED + "Current balance: $" + str(balance) + color.END)
                        time.sleep(1)
                    input(" ")
    
    i = 0
    balance = balance - 5
print(color.BOLD + color.RED + "Current balance: $" + str(balance) + color.END)
time.sleep(1)
print(" ")
print(color.UNDERLINE + "The bank has declined your card." + color.END)
time.sleep(2)
print(" ")
print("PRESS ENTER TO CONTINUE")
input(" ")
os.system('clear')
print("Would you like to dip into your college savings?")
q = input("y/n: ")
if q == "y":
    os.system('clear')
    balance = balance + 150
    print(color.BOLD + color.GREEN + "Current balance: $" + str(balance) + color.END)
    while balance > 0:
        while i < 16:
            os.system('clear')
            r1 = random.randint(4,7)
            if i >= 12:
                time.sleep(.07)
            print(color.BOLD + str(r1), end=" " + color.END)
            time.sleep(.06)
            i = i + 1
            if i >= 5:
                r2 = random.randint(4,7)
                if i >= 12:
                    time.sleep(.07)
                print(color.BOLD + str(r2), end=" " + color.END)
                time.sleep(.06)
                if i >= 10:
                    r3 = random.randint(4,7)
                    if i >= 12:
                        time.sleep(.07)
                    print(color.BOLD + str(r3), end=" " + color.END)
                    time.sleep(.06)
                    if i == 15:
                        if r1 == r2:
                            while edging <= 6:
                                os.system('clear')
                                print('\033[? 25l', end="")
                                print(r1, end= " ")
                                print(r2, end= " ")
                                r3 = random.randint(4,7)
                                print(r3, end=" ")
                                time.sleep(.4)
                                edging = edging + 1
                                if edging == 7 and r1 == r2 != r3:
                                    print(":(")
                                    time.sleep(.8)
                                if r1 == r2 == r3 and edging == 7:
                                    for i in range(10):
                                        os.system('clear')
                                        print(color.BOLD + color.RED + str(r1), " ", str(r2), " ", str(r3) + color.END)
                                        print("Full line " + str(r1) + "'s!")
                                        time.sleep(.1)
                                        os.system('clear')
                                        print(color.BOLD + color.YELLOW + str(r1), " ", str(r2), " ", str(r3) + color.END)
                                        print("Full line " + str(r1) + "'s!")
                                        time.sleep(.1)
                                        os.system('clear')
                                        print(color.BOLD + color.GREEN + str(r1), " ", str(r2), " ", str(r3) + color.END)
                                        print("Full line " + str(r1) + "'s!")
                                        time.sleep(.1)
                                        os.system('clear')
                                        print(color.BOLD + color.BLUE + str(r1), " ", str(r2), " ", str(r3) + color.END)
                                        print("Full line " + str(r1) + "'s!")
                                        time.sleep(.1)
                                        os.system('clear')
                                        print(color.BOLD + color.PURPLE + str(r1), " ", str(r2), " ", str(r3) + color.END)
                                        print("Full line " + str(r1) + "'s!")
                                        time.sleep(.1)
                                    edging = edging + 100
                                    r1 = r1 * 10
                                    print("+ $" + str(r1))
                                    time.sleep(1.2)
                                    print(" ")
                                    balance = balance + r1 
                                    print(color.BOLD + color.GREEN + "Current balance: $" + str(balance) + color.END)
                                    time.sleep(1.2)
                            edging = 0 
                        print(" ")
                        print(" ")
                        if balance > 50:
                            print(color.BOLD + color.GREEN + "Current balance: $" + str(balance) + color.END)
                            time.sleep(.6)
                        if balance <= 50 and balance > 20:
                            print(color.BOLD + color.YELLOW + "Current balance: $" + str(balance) + color.END)
                            time.sleep(.8)
                        if balance <= 20:
                            print(color.BOLD + color.RED + "Current balance: $" + str(balance) + color.END)
                            time.sleep(1)
                    
    
        i = 0
        balance = balance - 5
    os.system('clear')
    print("You have used up all of your money and are now bankurpt.")
    time.sleep(3)
    print(" ")
    print("You know the only option left...")
    time.sleep(2)
    print(" ")
    print("do it.")
    time.sleep(1)
    print(" ")
    print("You won't.")
if q == "n":
    os.system('clear')
    print("You've made the right decision.")





