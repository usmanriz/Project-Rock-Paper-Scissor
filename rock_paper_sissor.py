import random

choices = ["rock", "paper", "scissor"]

user1 = input("What's your name? ")
user1_answer = input("%s, do you want to choose rock, paper, or scissor? " % user1)

# Generate a random choice for the computer
computer_choice = random.choice(choices)

print("Computer's choice:", computer_choice)


def compare(u1, c):
    if u1 == c:
        return("It's a tie!")
    elif u1 == 'rock':
        if c == 'scissor':
            return("Rock wins!")
        else:
            return("Paper wins!")
    elif u1 == 'scissor':
        if c == 'paper':
            return("Scissor wins!")
        else:
            return("Rock wins!")
    elif u1 == 'paper':
        if c == 'rock':
            return("Paper wins!")
        else:
            return("Scissor wins!")
    else:
        return("Invalid input! You have not entered rock, paper, or scissor. Try again.")

result = compare(user1_answer, computer_choice)

if "wins" in result:
    print("Congratulations, %s! %s" % (user1, result))
else:
    print(result)



import random
choices = ["Rock","Paper","Scissor"]
# take input from user 
person = input("Enter your name: ")
ans = (f"{person},what you want to choose, rock, paper, scissor" )