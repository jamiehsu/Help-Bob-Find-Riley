# Mario.py - Game

import random
from tkinter import *
import tkinter as tk
import tkinter.font as font

root = Tk()

# Lay out our GUI
# parent is Frame
class Application(Frame):
    # class attributes
    WIDTH = 1000
    HEIGHT = 700
    IMAGE_SIZE = 60

    def __init__(self, window):
        # call parent contructor, Frame

        super().__init__(window)
        self.grid()  # displays

        self.goombaMovementCounter = 1
        self.power = 3
        # Canvas - private instance variable
        self.canvas = Canvas(self, width=Application.WIDTH, height=Application.HEIGHT, bg = "grey")

        self.canvas.grid()

        # Images - private instance variables
        self.imageMario = PhotoImage(file="bob.png")
        self.dog1 = PhotoImage(file="dog1.gif")
        self.dog2 = PhotoImage(file="dog2.gif")
        self.dog3 = PhotoImage(file="dog3.gif")
        self.background = PhotoImage(file = "blurredMap.png")
        self.winner = PhotoImage(file = "blueShirtGuy.png")
        self.banner = PhotoImage(file = "winnerbanner.png")
        self.cheer = PhotoImage(file = "Cheering.png")
        self.white = PhotoImage(file="white.png")
        self.person1 = PhotoImage(file="person1.png")
        self.person2 = PhotoImage(file="person2.png")
        self.cookie = PhotoImage(file="cookie.png")

        background = self.canvas.create_image(500, 350, image=self.background)
        # create Mario - private instance variables

        self.player = self.canvas.create_image(Application.IMAGE_SIZE, Application.HEIGHT / 2, image= self.imageMario)

        self.timer = self.canvas.create_text(100, 100, font=("Purisa", 50), text="")

        # create enemies - local variables


        enemy1 = self.canvas.create_image(500, 350, image=self.dog1)
        enemy2 = self.canvas.create_image(300, 150, image=self.dog2)
        enemy3 = self.canvas.create_image(750, 500, image=self.dog3)

        cookie1 = self.canvas.create_image(300, 350, image=self.cookie)
        cookie2 = self.canvas.create_image(900, 350, image=self.cookie)
        cookie3 = self.canvas.create_image(500, 600, image=self.cookie)
        cookie4 = self.canvas.create_image(450, 150, image=self.cookie)


        # create enemyList - private instance variable
        self.enemyList = []
        self.enemyList.append(enemy1)
        self.enemyList.append(enemy2)
        self.enemyList.append(enemy3)

        self.foodList = []
        self.foodList.append(cookie1)
        self.foodList.append(cookie2)
        self.foodList.append(cookie3)
        self.foodList.append(cookie4)

        # bind keyboard
        self.canvas.bind("<Key>", self.key)
        # focus input on canvas
        self.canvas.focus_set()

        # kick off the gameLoop

        # Intro Page
        self.IntroBackground = self.canvas.create_image(500, 350, image=self.background)
        self.intro = self.canvas.create_text(500, 280, font=("Purisa", 50), text="Welcome! Help Bob catch Riley!")
        self.startButton = Button(self.canvas, text="START", command=self.gameLoop)
        self.startButton.config(height=3, width=10)
        myFont = font.Font(family='Helvetica', size=20, weight='bold')
        self.startButton['font'] = myFont
        self.startButton.place(x=450, y=350)

        self.scoreButton = tk.Button(self.canvas, text="View Top 3 Scores", command=self.seeScoreBoard)
        self.scoreButton.config(height=3, width=20)
        self.scoreButton['font'] = myFont
        self.scoreButton.place(x=200000, y=200000)
        # self.gameLoop()

    # Sets up the key bindings


    def key(self, event):
        #code goes here
        if event.keysym == "Up" or event.keysym == "w":
            self.canvas.move(self.player, 0, -self.power)
        elif event.keysym == "Down" or event.keysym == "s":
            self.canvas.move(self.player, 0, self.power)
        elif event.keysym == "Left" or event.keysym == "a":
            self.canvas.move(self.player, -self.power, 0)
        elif event.keysym == "Right" or event.keysym == "d":
            self.canvas.move(self.player, self.power, 0)
        self.canvas.update()

    # def update_clock(self):
    #     self.label.configure(text=self.goombaMovementCounter)
    #     self.after(1000, self.update_clock)

    def seeScoreBoard(self):
        self.scoreButton.place(x=200000, y=200000)
        msg = ""
        num = 1
        white = self.canvas.create_image(500, 350, image=self.white)

        fileIn = open("scoreRank.txt", "r")
        for line in fileIn:
            line = line.strip()
            msg += str(num) + ". " + line + " second(s)" + "\n"
            num += 1

        yourScore = self.canvas.create_text(500, 200, font=("Purisa", 50), text="Your score: " + str(self.goombaMovementCounter) + " second(s)")
        score = self.canvas.create_text(500, 300, font=("Purisa", 25), text=msg)

        fileIn.close()

    # Game Loop
    def gameLoop(self):

        self.startButton.place(x=10000,y=10000)
        time = self.goombaMovementCounter //4
        lastRoundCoords = self.canvas.coords(self.player)

        if self.goombaMovementCounter == 1:
            self.canvas.delete(self.intro)
            self.canvas.delete(self.IntroBackground)

        self.canvas.delete(self.player)
        self.canvas.delete(self.timer)

        if self.goombaMovementCounter % 2 == 1:
            self.player = self.canvas.create_image(lastRoundCoords[0], lastRoundCoords[1], image=self.person1)
        elif self.goombaMovementCounter % 2 == 0:
            self.player = self.canvas.create_image(lastRoundCoords[0], lastRoundCoords[1], image=self.person2)
        self.timer = self.canvas.create_text(100, 100, font=("Purisa", 50), text=time)

        coords = self.canvas.bbox(self.player)
        collisions = self.canvas.find_overlapping(coords[0], coords[1], coords[2], coords[3])

        # randomly move our enemies


        # for enemy in self.enemyList:
        #     moveX = (self.goombaMovementCounter % 51) - 25
        #     self.canvas.move(enemy, moveX, 0)


        # if self.goombaMovementCounter % 2 == 1:
        for enemy in self.enemyList:
            move0 = random.randint(-500, 500)
            num = random.randint(0, 3)
            if num == 0:
                self.canvas.move(enemy, move0, 0)
                if self.canvas.bbox(enemy)[0] not in range(950):
                    self.canvas.move(enemy, -move0, 0)
                    # Don't let the enemy go off the screen
            elif num == 1:
                self.canvas.move(enemy, 0, move0)
                if self.canvas.bbox(enemy)[1] not in range(650):
                    self.canvas.move(enemy, 0, -move0)
            elif num == 2:
                self.canvas.move(enemy, move0, move0)
                if self.canvas.bbox(enemy)[1] not in range(650) or self.canvas.bbox(enemy)[0] not in range(950):
                    self.canvas.move(enemy, -move0, -move0)



        # Check for collisions
        for collision in collisions:
            if collision in self.enemyList:
                # if coords[3] <= self.canvas.bbox(collision)[1]:
                self.canvas.delete(collision)
                self.enemyList.remove(collision)
            if collision in self.foodList:
                self.power += 5
                self.canvas.delete(collision)
                self.foodList.remove(collision)


        # Don't let Mario go off the screen
        if coords[0] >= 1000:
            self.canvas.move(self.player,-1000,0)
        elif coords[2] <= 0:
            self.canvas.move(self.player,1000,0)
        elif coords[1] >= 700:
            self.canvas.move(self.player,0,-700)
        elif coords[3] <= 0:
            self.canvas.move(self.player,0,700)

        if len(self.enemyList) == 0:
            scoreList = []
            white = self.canvas.create_image(500, 350, image=self.white)
            winner = self.canvas.create_image(500, 160, image=self.winner)
            banner = self.canvas.create_image(500, 460, image=self.banner)
            cheer = self.canvas.create_image(500,630, image=self.cheer)
            score = self.canvas.create_text(500, 310,font=("Purisa", 35), text= "It only took you " + str(self.goombaMovementCounter) + " seconds!!")
            fileRead = open("scoreRank.txt", "r")
            for line in fileRead:
                line = line.strip()
                scoreList.append(int(line))
                if len(scoreList) <= 3:
                    scoreList.append(self.goombaMovementCounter)
                else:
                    if self.goombaMovementCounter < int(line):
                        scoreList.remove(int(line))
                        scoreList.append(self.goombaMovementCounter)
            fileRead.close()
            scoreList.sort()
            fileWrite = open("scoreRank.txt", "w")
            for score in scoreList[0:3]:
                print(score, file = fileWrite)
            fileWrite.close()


            self.scoreButton.place(x=390, y=340)

        else:
            self.goombaMovementCounter += 1
            self.after(250, self.gameLoop)


def main():
    root.title("Help Bob Catch Riley!")
    root.geometry("1000x700")
    app = Application(root)
    root.mainloop()

main()
