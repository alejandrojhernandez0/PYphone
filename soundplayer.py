#Alejandro Hernandez
#soundplayer.py (Final Project)
#December 18, 2013
#COM 110

#Purpose: Runs the sound player app on the PYphone. The user has the freedom
#to play sounds from .wav files that are on the PYphone folder. There are
#multiple options that do change the sound frames of the .wav file.
from pyPhone import *
from wavmod import *
from csaudio import *

class soundplayer:

    def __init__(self,win):
        """Sets app to be run in the window"""

        self.win = win

    def showSoundMenu(self,win):
        """App Menu GUI is created"""

        #---STANDARD MENU GUI---
        self.Menu = Rectangle(Point(200,95),Point(425,500))
        self.Menu.setFill("skyblue")
        self.Menu.setOutline("skyblue")
        self.Menu.draw(self.win)

        self.allTxt = []

        self.Exit = Button(self.win,Point(230,125),30,20,"black")
        self.ExitImg = Image(Point(230,125),"icons/goback.gif")
        self.ExitImg.draw(self.win)
        #---STANDARD MENU GUI---

        self.txt = Text(Point(312.5,275),"Sound Player")
        self.txt.setFill("black")
        self.txt.setStyle("bold")
        self.txt.setSize(15)
        self.txt.draw(self.win)
        self.allTxt.append(self.txt)

        #---PROMPT AND BUTTON GUI---
        self.soundEnt = Entry(Point(312.5,312.5),20)
        self.soundEnt.setFill("white")
        self.soundEnt.draw(self.win)

        self.playB = Button(self.win,Point(312.5,350),60,20,"darkgreen")
        self.txt = Text(Point(312.5,350),"Play")
        self.txt.setFill("white")
        self.txt.setStyle("bold")
        self.txt.setSize(13)
        self.txt.draw(self.win)
        self.allTxt.append(self.txt)

        self.flipB = Button(self.win,Point(382.5,350),60,20,"yellow")
        self.txt = Text(Point(382.5,350),"Flip-Flop")
        self.txt.setFill("black")
        self.txt.setStyle("bold")
        self.txt.setSize(11)
        self.txt.draw(self.win)
        self.allTxt.append(self.txt)

        self.reverseB = Button(self.win,Point(242.5,350),60,20,"black")
        self.txt = Text(Point(242.5,350),"Reverse")
        self.txt.setFill("white")
        self.txt.setStyle("bold")
        self.txt.setSize(11)
        self.txt.draw(self.win)
        self.allTxt.append(self.txt)
        #---PROMPT AND BUTTON GUI---

        #---INSTRUCTIONS GUI---
        self.txt = Text(Point(312.5,150),"Instructions")
        self.txt.setFill("black")
        self.txt.setStyle("bold")
        self.txt.setSize(10)
        self.txt.draw(self.win)
        self.allTxt.append(self.txt)

        self.txt = Text(Point(312.5,170),"Please enter the name of the wav")
        self.txt.setFill("black")
        self.txt.setSize(10)
        self.txt.draw(self.win)
        self.allTxt.append(self.txt)

        self.txt = Text(Point(312.5,190),"file that you want to play. Make sure")
        self.txt.setFill("black")
        self.txt.setSize(10)
        self.txt.draw(self.win)
        self.allTxt.append(self.txt)

        self.txt = Text(Point(312.5,210),"that it has the .wav extension")
        self.txt.setFill("black")
        self.txt.setSize(10)
        self.txt.draw(self.win)
        self.allTxt.append(self.txt)
        
        self.txt = Text(Point(312.5,230),"and it that it is in the program")
        self.txt.setFill("black")
        self.txt.setSize(10)
        self.txt.draw(self.win)
        self.allTxt.append(self.txt)

        self.txt = Text(Point(312.5,250),"folder, then click on button to play.")
        self.txt.setFill("black")
        self.txt.setSize(10)
        self.txt.draw(self.win)
        self.allTxt.append(self.txt)

        self.txt = Text(Point(312.5,400),"Default wav files on program:")
        self.txt.setFill("black")
        self.txt.setStyle("bold")
        self.txt.setSize(10)
        self.txt.draw(self.win)
        self.allTxt.append(self.txt)

        self.txt = Text(Point(312.5,420),"swfaith.wav,swnotry.wav,spam.wav")
        self.txt.setFill("black")
        self.txt.setSize(10)
        self.txt.draw(self.win)
        self.allTxt.append(self.txt)
        #---INSTRUCTIONS GUI---

    def hideSoundMenu(self):
        """All app Menu GUI is deleted after app is exited to main menu"""

        self.Menu.undraw()
        self.Exit.undraw()
        self.ExitImg.undraw()
        self.soundEnt.undraw()
        self.playB.undraw()
        self.flipB.undraw()
        self.reverseB.undraw()

        for text in self.allTxt:
            text.undraw()

    def ifSoundExitClicked(self,pt):
        """Checks if exit for app menu is clicked"""
        
        if(self.Exit.clicked(pt) == True):
            return True
        else:
            return False

    def ifPlayClicked(self,pt):
        """Checks if the play button is clicked"""
        
        if(self.playB.clicked(pt) == True):
            return True
        else:
            return False

    def ifFlipClicked(self,pt):
        """Checks if the flip-flop button is clicked"""
        
        if(self.flipB.clicked(pt) == True):
            return True
        else:
            return False
        
    def ifReverseClicked(self,pt):
        """Checks if the reverse button is clicked"""
        
        if(self.reverseB.clicked(pt) == True):
            return True
        else:
            return False

    def play(self):
        """Plays a sound file (wav) on the computer"""
        
        wav = WavMod(self.soundEnt.getText()) #Gets name of .wav file and plays
        wav.test()

    def flipflop(self):
        """Flips part of a wav file and plays it on computer"""
        
        wav = WavMod(self.soundEnt.getText()) #Gets name of .wav file and plays
        wav.flipflop()

    def reverse(self):
        """Reverses frames of a wav file and plays it on computer"""
        
        wav = WavMod(self.soundEnt.getText()) #Gets name of .wav file and plays
        wav.reverse()
        
        
