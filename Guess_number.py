#This is guess a number game. Within 6 tries the user has to guess the number, otherwise the loop will break
"""
#Code using while loop

username = input("Hello. What is your name?\n")
print("Well, " + username + " I am thinking of a number between 1 and 20")
selected_num = 5
choosen_num = 0
counter = 0
while(choosen_num != selected_num):
    if counter > 5:
        print("Nope, The number I was thinking of was " + str(selected_num) + ".")
        exit()
    choosen_num = int(input("Take a guess\n"))
    if choosen_num > selected_num:
        counter = counter + 1
        print("Your guess is too high")
    else:
        counter = counter + 1
        print("Your guess is too low")


print("Good job, " + username + "! You guessed my number in " + str(counter) + " guesses")

"""
# Using for loop
import random

username = input("Hello. What is your name?\n")
print("Well, " + username + " I am thinking of a number between 1 and 20")
random_number = random.randint(1,20)
selected_number = 0

for guessesTaken in range(1,7):
    selected_number = int(input("Take a guess\n"))
    if random_number > selected_number:
        print("Your guess is too low")
    elif random_number < selected_number:
        print("Your guess is too high")
    else:
        break

if random_number == selected_number:
    print("Good job, " + username + "! You guessed my number in " + str(guessesTaken) + " guesses")
else:
    print("Nope, The number I was thinking of was " + str(random_number) + ".")
