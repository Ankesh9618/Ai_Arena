import subprocess
import time
import os

x=0

print("Welcome to The AI Arena!!!\n")
time.sleep(2)

print("Please wait till we check your system for all the dependencies.")

for i in range(5):
    time.sleep(1)
    print(".")


os.system('cmd /c "py -m pip install pygame"')
time.sleep(2)

print("\nThank you for waiting!!!\n")
time.sleep(2)

print("We hope you have a good time here playing against your AI buddies!!!\n")
time.sleep(4)

print("What would you like to play today?\n")

while(x<1):
    
    print("1. Tic Tac Toe")
    print("2. Minesweeper")
    print("3. NIM")
    print("4. Exit")
    print("")
    choice = int(input("Enter your choice:  "))
    print("")

                        
    if choice == 1:
        os.system("python ticrunner.py")
        print("\nCan we interest you in another?\n")
                                        
    elif choice == 2:
        os.system("python minesweeperrunner.py")
        print("\nCan we interest you in another?\n")
                                        
    elif choice == 3:
        os.system("python nimrunner.py")
        print("\nCan we interest you in another?\n")
                                        
    elif choice == 4:
        print("Thank you for playing with us :)")
        time.sleep(3)
        exit(0)
    else:
        print("!!!Please enter a valid choice!!!\n")
            
