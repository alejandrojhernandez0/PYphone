#Alejandro Hernandez
#noteseditor.py (Final Project)
#December 18, 2013
#COM 110

#Runs the notes editor app on the PYphone. User has the ability
#the write down something in the prompt and save it to a new
#file [which the user can name] to the PYphone folder.
from pyPhone import *
class noteseditor:

    def __init__(self,win):
        """Sets app to be run in the window"""

        self.win = win

    def showNotesMenu(self,win):
        """App Menu GUI is created"""

        #---STANDARD MENU GUI---
        self.Menu = Rectangle(Point(200,95),Point(425,500))
        self.Menu.setFill("tan")
        self.Menu.setOutline("tan")
        self.Menu.draw(self.win)

        self.Exit = Button(self.win,Point(230,125),30,20,"black")
        self.ExitImg = Image(Point(230,125),"icons/goback.gif")
        self.ExitImg.draw(self.win)
        #---STANDARD MENU GUI---

        self.allTxt = []

        #---BUTTON GUI---
        self.writeB = Button(self.win,Point(312.5,320),80,20,"brown")
        self.txt = Text(Point(312.5,320),"Write Notes")
        self.txt.setFill("white")
        self.txt.setStyle("bold")
        self.txt.setSize(10)
        self.txt.draw(self.win)
        self.allTxt.append(self.txt)
        #---BUTTON GUI---

        self.txt = Text(Point(312.5,260),"Note Editor")
        self.txt.setFill("brown")
        self.txt.setStyle("bold")
        self.txt.setSize(15)
        self.txt.draw(self.win)
        self.allTxt.append(self.txt)

        self.txEnt = Entry(Point(312.5,290),20)
        self.txEnt.setFill("white")
        self.txEnt.draw(self.win)

        #---INSTRUCTIONS GUI---
        self.txt = Text(Point(312.5,380),"Write name of text file")
        self.txt.setFill("brown")
        self.txt.setSize(12)
        self.txt.draw(self.win)
        self.allTxt.append(self.txt)
        
        self.txt = Text(Point(312.5,400),"you want to save notes to:")
        self.txt.setFill("brown")
        self.txt.setSize(12)
        self.txt.draw(self.win)
        self.allTxt.append(self.txt)
        #---INSTRUCTIONS GUI---

        self.svEnt = Entry(Point(312.5,425),15)
        self.svEnt.setFill("white")
        self.svEnt.draw(self.win)

        #---INSTRUCTIONS GUI---
        self.txt = Text(Point(312.5,130),"Instructions")
        self.txt.setFill("brown")
        self.txt.setStyle("bold")
        self.txt.setSize(10)
        self.txt.draw(self.win)
        self.allTxt.append(self.txt)

        self.txt = Text(Point(312.5,150),"Fill in both entry boxes, the entry box")
        self.txt.setFill("brown")
        self.txt.setSize(8)
        self.txt.draw(self.win)
        self.allTxt.append(self.txt)

        self.txt = Text(Point(312.5,170),"over the write notes button is what you")
        self.txt.setFill("brown")
        self.txt.setSize(8)
        self.txt.draw(self.win)
        self.allTxt.append(self.txt)

        self.txt = Text(Point(312.5,190),"want written into the text file. Check the")
        self.txt.setFill("brown")
        self.txt.setSize(8)
        self.txt.draw(self.win)
        self.allTxt.append(self.txt)

        self.txt = Text(Point(312.5,210),"folder to find your text file. Also, don't")
        self.txt.setFill("brown")
        self.txt.setSize(8)
        self.txt.draw(self.win)
        self.allTxt.append(self.txt)

        self.txt = Text(Point(312.5,230),"forget to name your file as well!")
        self.txt.setFill("brown")
        self.txt.setSize(8)
        self.txt.draw(self.win)
        self.allTxt.append(self.txt)
        #---INSTRUCTIONS GUI---
        
    def hideNotesMenu(self):
        """All app Menu GUI is deleted after app is exited to main menu"""

        self.Menu.undraw()
        self.Exit.undraw()
        self.ExitImg.undraw()
        self.writeB.undraw()
        self.txEnt.undraw()
        self.svEnt.undraw()

        for text in self.allTxt:
            text.undraw()

    def ifNotesExitClicked(self,pt):
        """Checks if exit for app menu is clicked"""
        
        if(self.Exit.clicked(pt) == True):
            return True
        else:
            return False

    def ifWrite(self,pt):
        """Checks if write notes button is clicked"""
        
        if(self.writeB.clicked(pt) == True):
            return True
        else:
            return False

    def WriteToNewFile(self):
        """Writes the entered notes to a new text file"""

        #If entry box for file name is not empty
        if(self.svEnt.getText() != ""):
            #Save written stuff to this named file
            newfile = open(self.svEnt.getText() + ".txt", "w")
            newfile.write(self.txEnt.getText())
            file = self.svEnt.getText()

        #If entry box for file name is empty
        elif(self.svEnt.getText() == ""):
            #Save written stuff to a default txt file (notes.txt)
            newfile = open("notes.txt", "w")
            newfile.write(self.txEnt.getText())
            file = "notes"
        
        newfile.close()

        #Prompts the user the name of the file where the text was
        #written and saved to
        self.txt1 = Text(Point(312.5,450),"Your text was saved to:")
        self.txt1.setFill("brown")
        self.txt1.setStyle("bold")
        self.txt1.setSize(10)
        self.txt1.draw(self.win)

        self.txt2 = Text(Point(312.5,470),file+".txt")
        self.txt2.setFill("brown")
        self.txt2.setStyle("bold")
        self.txt2.setSize(10)
        self.txt2.draw(self.win)

        #Undraws prompt and resets so another new file can be saved after
        sleep(2)
        self.txt1.undraw()
        self.txt2.undraw()
        
