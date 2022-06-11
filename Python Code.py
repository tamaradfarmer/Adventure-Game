import time
import random


def pause(message):
    print(message)
    time.sleep(2)


def valid_input(question, right, left):
    while True:
        response = input(question).lower()
        if right in response:
            break
        if left in response:
            break
        else:
            pause("Sorry, I don't understand.")
    return response


def random_parts():
    scenarios = ["A deer runs in the road, you to swerve into the trees.",
                 "A bear throws your car into some bushes,",
                 "You were texting and driving. You swerve off the road",]
    print(random.choice(scenarios))


def intro():
    pause("Hello, Welcome to your adventure")
    pause("You are driving to your camp site when")
    pause(random_parts())
    pause("You are now lost in a forest")
    pause("With a broken car")
    pause("There are two directions you can go to look for help.")
    pause("You can go right into the trees. You hear a lot of scary noise.")
    pause("you can go left into the trees. It is quiet.")


def going_right():
    pause("You have now gone right.")
    pause("The forestbegins to thin.")
    pause("The noises get louder.")
    pause(" You exit the trees and...")
    pause(" You come accross a big road full of cars where you can get help.")
    pause(" You are now safe. Congrats!")


def going_left():
    pause("You went left.")
    pause("The forest is quiet but really dense")
    pause("You see an opening ahead of you.")
    pause("Heading towards the opening, you trip on some vines.")
    pause("You have fallen into a pit. You are trapped.")


def decisions():
    response=valid_input("Please choose a direction.",
                          "Will you go left or right?")
    if right in response:
        print(going_right())
    elif left in response:
        print(going_left())
    pause("Game Over")


def play_again():
    response=valid_input("Do you want to play again?",
                          "Please say yes or no")
    if no in response:
        pause("OK, Bye!")
    elif yes in response:
        pause("Yay, Let's play!")
        decisions()


def Game():
    intro()
    decisions()
    play_again()
Game()
