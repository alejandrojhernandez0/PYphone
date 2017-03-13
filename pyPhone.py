#Alejandro Hernandez
#pyPhone.py (Final Project)
#December 18, 2013
#COM 110

from pyButton import *
from graphics import *
from time import *
from random import *

from diceroll import *
from coinflip import *
from rockpaperscissors import *
from internet import *
from soundplayer import *
from calculator import *
from noteseditor import *

#Purpose: Creates all the GUI for the actual "PYphone" and its menu and also
#gets the PYphone app buttons to work.

#*Note that the user infomation and settings apps are bound to this
#PYphone class, as they do not have their own individual classes
class pyPhone:

    def __init__(self,win):
        """Creates the pyPhone GUI on a new graphical window"""

    #GUI
    #---
        self.win = win

        #---Default GUI for Phone being Created---

        #---PYphone GUI---
        self.body = Rectangle(Point(180,65),Point(445,550))
        self.body.setFill("white")
        self.body.setOutline("grey")
        self.body.setWidth(4)
        self.body.draw(self.win)
        self.screen = Rectangle(Point(200,95),Point(425,500))
        self.screen.setFill("lightblue")
        self.screen.setOutline("lightblue")
        self.screen.draw(self.win)
        #---PYphone GUI---

        self.allText = []
        self.allImgs = []

        #---Button GUI---
        #On and Off Buttons
        self.on = Button(win,Point(250,525),30,30,"darkgreen")
        self.off = Button(win,Point(375,525),30,30,"darkred")
        #---Button GUI---

        #---Loading Animation---
        loading = Text(Point(312.5,300),"Loading.")
        loading.setStyle("bold")
        loading.setSize(14)
        loading.draw(self.win)
        sleep(.5)
        loading.undraw()
        
        loading = Text(Point(312.5,300),"Loading..")
        loading.setStyle("bold")
        loading.setSize(14)
        loading.draw(self.win)
        sleep(.5)
        loading.undraw()
        
        loading = Text(Point(312.5,300),"Loading...")
        loading.setStyle("bold")
        loading.setSize(14)
        loading.draw(self.win)
        sleep(.5)
        loading.undraw()
        #---Loading Animation---

        #---Button GUI---
        #App Row 1
        self.info = Button(self.win,Point(256.25,196.25),42,42,"black")
        img = Image(Point(256.25,196.25),"icons/info.gif")
        img.draw(self.win)
        txt = Text(Point(256.25,226),"Information")
        txt.setSize(6)
        txt.setStyle("bold")
        txt.draw(self.win)
        self.allImgs.append(img)
        self.allText.append(txt)
        
        self.setting = Button(self.win,Point(312.5,196.25),42,42,"black")
        img = Image(Point(312.5,196.25),"icons/settings.gif")
        img.draw(self.win)
        txt = Text(Point(312.5,226),"Settings")
        txt.setSize(6)
        txt.setStyle("bold")
        txt.draw(self.win)
        self.allImgs.append(img)
        self.allText.append(txt)
        
        self.rps = Button(self.win,Point(368.75,196.25),42,42,"black")
        img = Image(Point(368.75,196.25),"icons/rps.gif")
        img.draw(self.win)
        txt = Text(Point(368.75,226),"RPS")
        txt.setSize(6)
        txt.setStyle("bold")
        txt.draw(self.win)
        self.allImgs.append(img)
        self.allText.append(txt)

        #App Row 2
        self.dice = Button(self.win,Point(256.25,297.5),42,42,"black")
        img = Image(Point(256.25,297.5),"icons/dice.gif")
        img.draw(self.win)
        txt = Text(Point(256.25,326.75),"Dice Roll")
        txt.setSize(6)
        txt.setStyle("bold")
        txt.draw(self.win)
        self.allImgs.append(img)
        self.allText.append(txt)
        
        self.coin = Button(win,Point(312.5,297.5),42,42,"black")
        img = Image(Point(312.5,297.5),"icons/coin.gif")
        img.draw(self.win)
        txt = Text(Point(312.5,326.75),"Coin Flip")
        txt.setSize(6)
        txt.setStyle("bold")
        txt.draw(self.win)
        self.allImgs.append(img)
        self.allText.append(txt)
        
        self.internet = Button(self.win,Point(368.75,297.5),42,42,"black")
        img = Image(Point(368.75,297.5),"icons/internet.gif")
        img.draw(self.win)
        txt = Text(Point(368.75,326.75),"Internet")
        txt.setSize(6)
        txt.setStyle("bold")
        txt.draw(self.win)
        self.allImgs.append(img)
        self.allText.append(txt)

        #App Row 3
        self.sound = Button(self.win,Point(256.25,398.75),42,42,"black")
        img = Image(Point(256.25,398.75),"icons/sound.gif")
        img.draw(self.win)
        txt = Text(Point(256.25,427.50),"Sound Player")
        txt.setSize(6)
        txt.setStyle("bold")
        txt.draw(self.win)
        self.allImgs.append(img)
        self.allText.append(txt)

        
        self.calc = Button(self.win,Point(312.5,398.75),42,42,"black")
        img = Image(Point(312.5,398.75),"icons/calc.gif")
        img.draw(self.win)
        txt = Text(Point(312.5,427.50),"Calculator")
        txt.setSize(6)
        txt.setStyle("bold")
        txt.draw(self.win)
        self.allImgs.append(img)
        self.allText.append(txt)


        self.notes = Button(self.win,Point(368.75,398.75),42,42,"black")
        img = Image(Point(368.75,398.75),"icons/notes.gif")
        img.draw(self.win)
        txt = Text(Point(368.75,427.50),"Note Editor")
        txt.setSize(6)
        txt.setStyle("bold")
        txt.draw(self.win)
        self.allImgs.append(img)
        self.allText.append(txt)
        #---Button GUI---
    #---
    #GUI
    
    #All these check for mouse clicks on each app button
    #--------------------------------------------------- 
    def ifInfoClicked(self,pt):
        """Checks if information button is clicked"""
        if(self.info.clicked(pt) == True):
            return True

    def ifSettingClicked(self,pt):
        """Checks if settings button is clicked"""
        if(self.setting.clicked(pt) == True):
            return True
    
    def ifRpsClicked(self,pt):
        """Checks if rock paper scissors button is clicked"""
        if(self.rps.clicked(pt) == True):
            return True
    
    def ifDiceClicked(self,pt):
        """Checks if dice roll button is clicked"""
        if(self.dice.clicked(pt) == True):
            return True
    
    def ifCoinClicked(self,pt):
        """Checks if coin flip button is clicked"""
        if(self.coin.clicked(pt) == True):
            return True
    
    def ifInternetClicked(self,pt):
        """Checks if internet button is clicked"""
        if(self.internet.clicked(pt) == True):
            return True
    
    def ifSoundClicked(self,pt):
        """Checks if sound player button is clicked"""
        if(self.sound.clicked(pt) == True):
            return True
    
    def ifCalcClicked(self,pt):
        """Checks if calculator button is clicked"""
        if(self.calc.clicked(pt) == True):
            return True
    
    def ifNotesClicked(self,pt):
        """Checks if notes editor button is clicked"""
        if(self.notes.clicked(pt) == True):
            return True
    #---------------------------------------------------
    #All these check for mouse clicks on each app button
        

    #Checks for mouse click on off button
    #--------------------------------------------------
    def isOffClicked(self,pt):
        """Checks if PYphone's off button is clicked"""
        if(self.off.clicked(pt) == True):
            return True
        else:
            return False
    #--------------------------------------------------
    #Checks for mouse click on off button
        
      
    #Info App
    #--------
    def showInfoMenu(self,win):
        """App Menu GUI is created"""

        #---STANDARD MENU GUI---
        self.infoMenu = Rectangle(Point(200,95),Point(425,500))
        self.infoMenu.setFill("black")
        self.infoMenu.setOutline("black")
        self.infoMenu.draw(self.win)

        self.infoExit = Button(win,Point(230,125),30,20,"black")
        self.infoExitImg = Image(Point(230,125),"icons/goback.gif")
        self.infoExitImg.draw(self.win)
        #---STANDARD MENU GUI---

        self.infoTxt = []

        #---INSTRUCTIONS GUI---
        self.txt = Text(Point(312.5,190),"User Information")
        self.txt.setFill("white")
        self.txt.setSize(15)
        self.txt.setStyle("bold")
        self.txt.draw(self.win)
        self.infoTxt.append(self.txt)

        self.txt = Text(Point(312.5,220),"Welcome to the PYphone! If you want to stop")
        self.txt.setFill("white")
        self.txt.setSize(8)
        self.txt.draw(self.win)
        self.infoTxt.append(self.txt)

        self.txt = Text(Point(312.5,240),"using the phone, click on the red button below")
        self.txt.setFill("white")
        self.txt.setSize(8)
        self.txt.draw(self.win)
        self.infoTxt.append(self.txt)

        self.txt = Text(Point(312.5,260),"to close the program. If you want to use an")
        self.txt.setFill("white")
        self.txt.setSize(8)
        self.txt.draw(self.win)
        self.infoTxt.append(self.txt)

        self.txt = Text(Point(312.5,280),"app, click on the icon under the app name.")
        self.txt.setFill("white")
        self.txt.setSize(8)
        self.txt.draw(self.win)
        self.infoTxt.append(self.txt)

        self.txt = Text(Point(312.5,300),"If you want to go back to the main screen on")
        self.txt.setFill("white")
        self.txt.setSize(8)
        self.txt.draw(self.win)
        self.infoTxt.append(self.txt)

        self.txt = Text(Point(312.5,320),"the phone, click on the grey box with the")
        self.txt.setFill("white")
        self.txt.setSize(8)
        self.txt.draw(self.win)
        self.infoTxt.append(self.txt)

        self.txt = Text(Point(312.5,340),"white arrow. The apps will have their own")
        self.txt.setFill("white")
        self.txt.setSize(8)
        self.txt.draw(self.win)
        self.infoTxt.append(self.txt)

        self.txt = Text(Point(312.5,360),"instructions if you need any help. Enjoy!")
        self.txt.setFill("white")
        self.txt.setSize(8)
        self.txt.draw(self.win)
        self.infoTxt.append(self.txt)

        self.txt = Text(Point(312.5,450),"Made By: Alex Hernandez 17'")
        self.txt.setFill("white")
        self.txt.setSize(10)
        self.txt.setStyle("bold")
        self.txt.draw(self.win)
        self.infoTxt.append(self.txt)
        
        self.txt = Text(Point(312.5,470),"COM 110")
        self.txt.setFill("white")
        self.txt.setSize(10)
        self.txt.setStyle("bold")
        self.txt.draw(self.win)
        self.infoTxt.append(self.txt)
        #---INSTRUCTIONS GUI---

    def hideInfoMenu(self):
        """All app Menu GUI is deleted after app is exited to main menu"""

        self.infoMenu.undraw()
        self.infoExit.undraw()
        self.infoExitImg.undraw()

        for text in self.infoTxt:
            text.undraw()

    def ifInfoExitClicked(self,pt):
        """Checks if exit for app menu is clicked"""
        
        if(self.infoExit.clicked(pt) == True):
            return True
        else:
            return False
    #--------
    #Info App
        
        
    #Settings App
    #------------
    def showSettingMenu(self,win):
        """App Menu GUI is created"""

        #---STANDARD MENU GUI---
        self.settingMenu = Rectangle(Point(200,95),Point(425,500))
        self.settingMenu.setFill("black")
        self.settingMenu.setOutline("black")
        self.settingMenu.draw(self.win)
        #---STANDARD MENU GUI---

        self.settingTxt = []
        self.settingEnt = []
        self.settingBut = []

        #---Settings buttons---
        self.mcBut = Button(self.win,Point(358,310),30,20,"red")
        self.settingBut.append(self.mcBut)
        self.txt = Text(Point(358,310),"OK")
        self.txt.setFill("white")
        self.txt.setStyle("bold")
        self.txt.setSize(11)
        self.txt.draw(self.win)
        self.settingTxt.append(self.txt)

        self.tcBut = Button(self.win,Point(358,370),30,20,"red")
        self.settingBut.append(self.tcBut)
        self.txt = Text(Point(358,370),"OK")
        self.txt.setFill("white")
        self.txt.setStyle("bold")
        self.txt.setSize(11)
        self.txt.draw(self.win)
        self.settingTxt.append(self.txt)

        self.tsBut = Button(self.win,Point(358,430),30,20,"red")
        self.settingBut.append(self.tsBut)
        self.txt = Text(Point(358,430),"OK")
        self.txt.setFill("white")
        self.txt.setStyle("bold")
        self.txt.setSize(11)
        self.txt.draw(self.win)
        self.settingTxt.append(self.txt)
        #---Settings buttons---

        #---STANDARD MENU GUI---
        self.settingExit = Button(win,Point(230,125),30,20,"black")
        self.settingBut.append(self.settingExit)
        self.settingExitImg = Image(Point(230,125),"icons/goback.gif")
        self.settingExitImg.draw(self.win)
        #---STANDARD MENU GUI---

        #---INSTRUCTIONS GUI---
        self.txt = Text(Point(312.5,170),"Settings")
        self.txt.setFill("white")
        self.txt.setSize(15)
        self.txt.setStyle("bold")
        self.txt.draw(self.win)
        self.settingTxt.append(self.txt)

        self.txt = Text(Point(312.5,200),"Type in entry box next to option. Click")
        self.txt.setFill("white")
        self.txt.setSize(8)
        self.txt.draw(self.win)
        self.settingTxt.append(self.txt)

        self.txt = Text(Point(312.5,220),"OK under the option's entry box to")
        self.txt.setFill("white")
        self.txt.setSize(8)
        self.txt.draw(self.win)
        self.settingTxt.append(self.txt)

        self.txt = Text(Point(312.5,240),"activate the new change.")
        self.txt.setFill("white")
        self.txt.setSize(8)
        self.txt.draw(self.win)
        self.settingTxt.append(self.txt)
        #---INSTRUCTIONS GUI---

        #---Settings Options GUI---
        self.txt = Text(Point(250,280),"Menu Color:")
        self.txt.setFill("white")
        self.txt.setSize(10)
        self.txt.draw(self.win)
        self.settingTxt.append(self.txt)

        self.txt = Text(Point(250,340),"Text Color:")
        self.txt.setFill("white")
        self.txt.setSize(10)
        self.txt.draw(self.win)
        self.settingTxt.append(self.txt)

        self.txt = Text(Point(250,400),"Text Style:")
        self.txt.setFill("white")
        self.txt.setSize(10)
        self.txt.draw(self.win)
        self.settingTxt.append(self.txt)

        self.mColor = Entry(Point(360,280),12)
        self.mColor.setFill("white")
        self.mColor.draw(self.win)
        self.settingEnt.append(self.mColor)
    
        self.tColor = Entry(Point(360,340),12)
        self.tColor.setFill("white")
        self.tColor.draw(self.win)
        self.settingEnt.append(self.tColor)

        self.tStyle = Entry(Point(360,400),12)
        self.tStyle.setFill("white")
        self.tStyle.draw(self.win)
        self.settingEnt.append(self.tStyle)
        #---Settings Options GUI---
        
    def hideSettingMenu(self):
        """All app Menu GUI is deleted after app is exited to main menu"""

        self.settingMenu.undraw()
        self.settingExit.undraw()
        self.settingExitImg.undraw()

        for text in self.settingTxt:
            text.undraw()

        for entry in self.settingEnt:
            entry.undraw()

        for button in self.settingBut:
            button.undraw()
        
    def ifSettingExitClicked(self,pt):
        """Checks if exit for app menu is clicked"""
        
        if(self.settingExit.clicked(pt) == True):
            return True
        else:
            return False

    def changeMCOLOR(self,pt):
        """Checks if button for changing menu (screen) color is clicked"""   
        if(self.mcBut.clicked(pt) == True):
            return True
        else:
            return False

    def changeTCOLOR(self,pt):
        """Checks if button for changing text color is clicked"""
        if(self.tcBut.clicked(pt) == True):
            return True
        else:
            return False

    def changeTSTYLE(self,pt):
        """Checks if button for changing text font is clicked"""
        if(self.tsBut.clicked(pt) == True):
            return True
        else:
            return False
    #------------
    #Settings App


    #Mutators from Settings
    #----------------------      
    def setBackground(self):
        """Changes background color of screen on the PYphone"""
        color = self.mColor.getText()
        self.screen.setFill(color)

    def setFontColor(self):
        """Changes font color of menu text on the PYphone"""
        color = self.tColor.getText()
        for text in self.allText:
            text.setFill(color)

    def setFontType(self):
        """Changes font type of menu text on the PYphone"""
        font = self.tStyle.getText()
        for text in self.allText:
            text.setFace(font)
        
    #----------------------
    #Mutators from Settings
