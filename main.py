#Alejandro Hernandez
#main.py (Final Project)
#December 18, 2013
#COM 110

#Purpose: Runs a PYphone on the window. The PYphone is an interactive
#app on a graphical window that can be used by the user to play games
#and run mini-applications that are on it.
from pyPhone import *

def main():

    win = GraphWin("pyPhone",600,600)
    #Creates the "PYphone" on the graphical window
    phone = pyPhone(win)

    pt = win.getMouse()
    
    #As long as the off button is not clicked...
    while (phone.isOffClicked(pt) == False):

        #Instructions app is run
        if (phone.ifInfoClicked(pt) == True):
            phone.showInfoMenu(win)
            pt = win.getMouse()
            while(phone.ifInfoExitClicked(pt) == False):
                if(phone.isOffClicked(pt) == True):
                    win.close()
                    
                pt = win.getMouse()

            phone.hideInfoMenu()
        #Instructions app is run

        #Settings app is run
        elif(phone.ifSettingClicked(pt) == True):
            phone.showSettingMenu(win)
            while(phone.ifSettingExitClicked(pt) == False):
                if(phone.changeMCOLOR(pt) == True):
                    phone.setBackground()
                elif(phone.changeTCOLOR(pt) == True):
                    phone.setFontColor()
                elif(phone.changeTSTYLE(pt) == True):
                    phone.setFontType()
                elif(phone.isOffClicked(pt) == True):
                    win.close()
                    
                pt = win.getMouse()
                
            phone.hideSettingMenu()
        #Settings app is run

        #Rock paper scissors (RPS) app is run
        elif(phone.ifRpsClicked(pt) == True):
            rps = rockpaperscissors(win)
            rps.showRpsMenu(win)
            while(rps.ifRpsExitClicked(pt) == False):
                if(rps.ifRock(pt) == True or rps.ifPaper(pt) == True or rps.ifScissors(pt) == True):
                    rps.doGame()
                elif(phone.isOffClicked(pt) == True):
                    win.close()
                    
                pt = win.getMouse()

            rps.hideRpsMenu()        
        #Rock paper scissors (RPS) app is run

        #Dice roll app is run
        elif(phone.ifDiceClicked(pt) == True):
            dice = diceroll(win)
            dice.showDiceMenu(win)
            while(dice.ifDiceExitClicked(pt) == False):
                if(dice.ifRoll(pt) == True):
                    dice.doGame()
                elif(phone.isOffClicked(pt) == True):
                    win.close()
                    
                pt = win.getMouse()

            dice.hideDiceMenu()
        #Dice roll app is run
            
        #Coin flip app is run
        elif(phone.ifCoinClicked(pt) == True):
            coin = coinflip(win)
            coin.showCoinMenu(win)
            while(coin.ifCoinExitClicked(pt) == False):
                if(coin.ifHeads(pt) == True or coin.ifTails(pt) == True):
                    coin.doGame()
                elif(phone.isOffClicked(pt) == True):
                    win.close()
                    
                pt = win.getMouse()

            coin.hideCoinMenu()
        #Coin flip app is run

        #Internet app is run
        elif(phone.ifInternetClicked(pt) == True):
            www = internet(win)
            www.showInternetMenu(win)
            while(www.ifInternetExitClicked(pt) == False):
                if(www.ifSearchClicked(pt) == True):
                    www.doSearch()
                elif(phone.isOffClicked(pt) == True):
                    win.close()
                    
                pt = win.getMouse()

            www.hideInternetMenu()
        #Internet app is run

        #Sound player app is run
        elif(phone.ifSoundClicked(pt) == True):
            sound = soundplayer(win)
            sound.showSoundMenu(win)
            while(sound.ifSoundExitClicked(pt) == False):
                if(sound.ifPlayClicked(pt) == True):
                    sound.play()
                elif(sound.ifFlipClicked(pt) == True):
                    sound.flipflop()
                elif(sound.ifReverseClicked(pt) == True):
                    sound.reverse()
                elif(phone.isOffClicked(pt) == True):
                    win.close()
                    
                pt = win.getMouse()

            sound.hideSoundMenu()
        #Sound player app is run

        #Calculator app is run
        elif(phone.ifCalcClicked(pt) == True):
            calc = calculator(win)
            calc.showCalcMenu(win)
            while(calc.ifCalcExitClicked(pt) == False):
                if(calc.ifAdd(pt) == True):
                    calc.giveAnswer()
                elif(calc.ifSubtract(pt) == True):
                    calc.giveAnswer()
                elif(calc.ifMultiply(pt) == True):
                    calc.giveAnswer()
                elif(calc.ifDivide(pt) == True):
                    calc.giveAnswer()
                elif(phone.isOffClicked(pt) == True):
                    win.close()
                    
                pt = win.getMouse()

            calc.hideCalcMenu()
        #Calculator app is run

        #Note editor app is run
        elif(phone.ifNotesClicked(pt) == True):
            note = noteseditor(win)
            note.showNotesMenu(win)
            while(note.ifNotesExitClicked(pt) == False):
                if(note.ifWrite(pt) == True):
                    note.WriteToNewFile()
                elif(phone.isOffClicked(pt) == True):
                    win.close()
                    
                pt = win.getMouse()

            note.hideNotesMenu()
        #Note editor app is run
        
        pt = win.getMouse()

    #Off button turns off phone
    win.close()
          
main()
