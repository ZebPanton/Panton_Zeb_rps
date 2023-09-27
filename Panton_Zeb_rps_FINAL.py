# This file was created by: Zeb Panton

# import package
import turtle
from turtle import *
# The os module allows us to access the current directory in order to access assets
import os

#meerly so i could import it's sleep function
#Ryan McElroy showed me this 
from time import * 

#this one is from Mr. Cozort
from random import randint

print("The current working directory is (getcwd): " + os.getcwd())
print("The current working directory is (path.dirname): " + os.path.dirname(__file__))

# setup the game folders using the os module
game_folder = os.path.dirname(__file__)
images_folder = os.path.join(game_folder, 'images')

# setup the width and height for the window
WIDTH, HEIGHT = 1000, 400

rock_w, rock_h = 256, 280

paper_w, paper_h = 256, 204

scissors_w, scissors_h = 256, 170

# setup choice list
choices = ["ROCK","PAPER","SCISSORS"]


# setup the Screen class using the turtle module
screen = turtle.Screen()
screen.setup(WIDTH + 4, HEIGHT + 8)  # fudge factors due to window borders & title bar
screen.setworldcoordinates(0, 0, WIDTH, HEIGHT)
screen.screensize(canvwidth=WIDTH, canvheight=HEIGHT, bg="lightblue")


# canvas object
cv = screen.getcanvas()
# hack to make window not resizable for more reliable coordinates
cv._rootwindow.resizable(False, False)


# setup the rock image using the os module as rock_image
rock_image = os.path.join(images_folder, 'rock.gif')
BOTrock_image = os.path.join(images_folder, 'rock - Copy.gif')
# instantiate (create an instance of) the Turtle class for the rock
rock_instance = turtle.Turtle()
BOTrock_instance = turtle.Turtle()
# setup the paper image using the os module as paper_image
paper_image = os.path.join(images_folder, 'paper.gif')
BOTpaper_image = os.path.join(images_folder, 'paper - Copy.gif')
# instantiate (create an instance of) the Turtle class for the paper
paper_instance = turtle.Turtle()
BOTpaper_instance = turtle.Turtle()
# setup the scissors image using the os module as scissors_image
scissors_image = os.path.join(images_folder, 'scissors.gif')
BOTscissors_image = os.path.join(images_folder, 'scissors - Copy.gif')
# instantiate (create an instance of) the Turtle class for the scissors
scissors_instance = turtle.Turtle()
BOTscissors_instance = turtle.Turtle()


def show_rock(x,y):
    # add the rock image as a shape
    screen.addshape(rock_image)
    # attach the rock_image to the rock_instance
    rock_instance.shape(rock_image)
    # remove the pen option from the rock_instance so it doesn't draw lines when moved
    rock_instance.penup()
    # set the position of the rock_instance
    rock_instance.setpos(x,y)

def show_paper(x,y):
    # add the paper image as a shape
    screen.addshape(paper_image)
    # attach the paper_image to the paper_instance
    paper_instance.shape(paper_image)
    # remove the pen option from the paper_instance so it doesn't draw lines when moved
    paper_instance.penup()
    # set the position of the paper_instance
    paper_instance.setpos(x,y)

def show_scissors(x,y):
    # add the scissors image as a shape
    screen.addshape(scissors_image)
    # attach the scissors_image to the scissors_instance
    scissors_instance.shape(scissors_image)
    # remove the pen option from the scissors_instance so it doesn't draw lines when moved
    scissors_instance.penup()
    # set the position of the scissors_instance
    scissors_instance.setpos(x,y)

def BOTshow_rock(x,y):
    # add the rock image as a shape
    screen.addshape(BOTrock_image)
    # attach the rock_image to the rock_instance
    BOTrock_instance.shape(BOTrock_image)
    # remove the pen option from the rock_instance so it doesn't draw lines when moved
    BOTrock_instance.penup()
    # set the position of the rock_instance
    BOTrock_instance.setpos(x,y)
    
def BOTshow_paper(x,y):
    # add the rock image as a shape
    screen.addshape(BOTpaper_image)
    # attach the rock_image to the rock_instance
    BOTpaper_instance.shape(BOTpaper_image)
    # remove the pen option from the rock_instance so it doesn't draw lines when moved
    BOTpaper_instance.penup()
    # set the position of the rock_instance
    BOTpaper_instance.setpos(x,y)

def BOTshow_scissors(x,y):
    # add the rock image as a shape
    screen.addshape(BOTscissors_image)
    # attach the rock_image to the rock_instance
    BOTscissors_instance.shape(BOTscissors_image)
    # remove the pen option from the rock_instance so it doesn't draw lines when moved
    BOTscissors_instance.penup()
    # set the position of the rock_instance
    BOTscissors_instance.setpos(x,y)

# instantiate a turtle for writing text
text = turtle.Turtle()
text.color('deep pink')
text.hideturtle()
text.penup()
text.setpos(-250,150)   
text.write("Rock, Paper or Scissors?", True, "left", ("Arial", 24, "normal"))

show_rock(-300, 0)
show_paper(0, 0)
show_scissors(300, 0)

# this function uses and x y value, an obj, and width and height 
def collide(x,y,obj,w,h):
    if x < obj.pos()[0] + w/2 and x > obj.pos()[0] - w/2 and y < obj.pos()[1] + h/2 and y > obj.pos()[1] - h/2:
        return True
    else:
        return False

# function that passes through wn onlick

def mouse_pos(x, y):
    text.setpos(-250,150)              #sets text to be at top of screen
    text.clear()                       #when player clicks then it clears whatever they clicked before
    if collide(x,y,rock_instance, rock_w, rock_h):
        print("player chose scissors")
        validityProgram("rock")
    elif collide(x,y,paper_instance, paper_w, paper_h):
        print("player chose scissors")
        validityProgram("paper")
    elif collide(x,y,scissors_instance, scissors_w, scissors_h):
        print("player chose scissors")
        validityProgram("scissors")
    else:
        print("you dumbbutt")
        text.write("You chose... ", True, "right", ("Arial", 24, "normal"))
        sleep(1)
        text.write("wrong", True, "left", ("Arial", 24, "normal"))



def rpsProgram(playerFinalInput, botInput):
    print(playerFinalInput) 
    print(botInput)
    if botInput + 1 == playerFinalInput or botInput == len(choices)-1 and playerFinalInput == 0: #testing if player wins
        DisplayText(choices[playerFinalInput], choices[botInput])
        rock_instance.shape("blank")              
        scissors_instance.shape("blank")
        paper_instance.shape("blank")
        ImageAnimation(playerFinalInput, botInput)
        text.setpos(0,0)
        text.write("You won! 🗿🗿", False, "center", ("Arial", 100, "normal"))
        print("player won")
    elif playerFinalInput + 1 == botInput or playerFinalInput == len(choices)-1 and botInput == 0: #bot wins you bozo
        DisplayText(choices[playerFinalInput], choices[botInput])
        rock_instance.shape("blank")
        scissors_instance.shape("blank")
        paper_instance.shape("blank")
        ImageAnimation(playerFinalInput, botInput)
        text.setpos(0,0)
        text.write("You lost 🙈🙈", False, "center", ("Arial", 100, "normal"))
        print("player lost")
    elif botInput == playerFinalInput:  #testing if player and bot tied
        DisplayText(choices[playerFinalInput], choices[botInput])
        rock_instance.shape("blank")
        scissors_instance.shape("blank")
        paper_instance.shape("blank")
        ImageAnimation(playerFinalInput, botInput)
        text.setpos(0,0)
        text.write("You tied 😆😆", False, "center", ("Arial", 100, "normal"))
        print("player tied")
    else: #Something went wrong, luckily never proc'd for me 
        print("Bro who coded this 😭")

def replayProgram(replaydata): #asks if the player wants to play
    if replaydata.upper() == "YES" or replaydata.upper() == "TRUE":
        playerInput = input("Rock, Paper, or Scissors? ")
        validityProgram(playerInput)
    elif replaydata.upper() == "NO" or replaydata.upper() == "FALSE":
        print("thanks for playing")
    else:
        print("you've input a nonvalid option")

def validityProgram(validityTest):
    testAttempt = 0
    while validityTest.upper() != choices[0 + testAttempt]:             #goes through whole list testing if input is valid
        testAttempt += 1
        if testAttempt == len(choices):
            print("you've input a nonvalid option")
            break 
    else: #if loops moves onto else then input == valid. Moves onto my amazing system
        rpsProgram(choices.index(validityTest.upper()),choices.index(choices[randint(0,len(choices)-1)]))

def DisplayText(playerDisplay, botDisplay):
    text.write("You chose ", True, "left", ("Arial", 24, "normal"))
    text.write(playerDisplay, True, "left", ("Arial", 24, "normal"))
    text.write(" and the bot chose  ", True, "left", ("Arial", 24, "normal"))
    text.write(botDisplay, True, "left", ("Arial", 24, "normal"))

#manually made it move the images for every possibility, couldn't think of another way to do it
#problem: if bot and player choose same image then it there's only one instance of each image.
def ImageAnimation(playerChoice, botChoice):
    if playerChoice == 0:       #if player chooses rock
        if botChoice == 0:
            show_rock(-300, 0)
            BOTshow_rock(300, 0)
        elif botChoice == 1:
            show_rock(-300, 0)
            BOTshow_paper(300, 0)
        elif botChoice == 2:
            show_rock(-300, 0)
            BOTshow_scissors(300, 0)
        else:
            print("idk man")
    elif playerChoice == 1:     #player choice is paper
        if botChoice == 0:
            show_paper(-300, 0)
            BOTshow_rock(300, 0)
        elif botChoice == 1:
            show_paper(-300, 0)
            BOTshow_paper(300, 0)
        elif botChoice == 2:
            show_paper(-300, 0)
            BOTshow_scissors(300, 0)
        else:
            print("idk man")
    elif playerChoice == 2:     #player choice is scissors
        if botChoice == 0:
            show_scissors(-300, 0)
            BOTshow_rock(300, 0)
        elif botChoice == 1:
            show_scissors(-300, 0)
            BOTshow_paper(300, 0)
        elif botChoice == 2:
            show_scissors(-300, 0)
            BOTshow_scissors(300, 0)
        else:
            print("idk man")
    else:
        print("playerChoice isn't valid")



# user this to get mouse position
screen.onclick(mouse_pos)
# runs mainloop for Turtle - required to be last
screen.mainloop()


# validityProgram() #initiates the first loop
