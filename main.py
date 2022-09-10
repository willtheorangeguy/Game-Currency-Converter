# Import Statements
from tkinter import *
import tkinter.messagebox as box

# Game Price Variables
apex = 0.50
boombeach = 0.50
coc = 0.50  # Clash of Clans
egginc = 0.50
fortnite = 0.50
minecraft = 0.50
asphalt = 0.50
clashroyale = 0.50
crossyroad = 0.50
hillclimb1 = 0.50
hillclimb2 = 0.50
mariokart = 0.50
solitaire = 0.50
sudoku = 0.50
mariobros = 0.50
smashbros = 0.50
smashbros = 0.50

# Create Main Window
window = Tk()
window.title('Game Currency - Use this simple app to find how many in-game \
turns you can get!')
title = Label(window, text = 'Game Currency')
titleblurb = Label(window, text = 'Enter the amount of money that you are going to pay for your turns or the worth of the item your are trading in for your turns.')
conversionframe = Frame(window)

# Turn Calculation Functions
turns = 0
def calculateturns_money():
    turns =  float(moneyentry.get()) / 0.50
    apexturns.configure(text = int(turns))

def calculateturns_trade():
    turns = float(tradeentry.get()) / 0.50
    apexturns.configure(text = int(turns))

# Elements for Money Conversion
moneyframe = Frame(conversionframe)
moneytitle = Label(moneyframe, text = 'Cash/Credit')
moneyblurb = Label(moneyframe, text = 'Enter the amount of money you are willing to pay:')
moneyentry = Entry(moneyframe)
moneybutton = Button(moneyframe, text = 'Submit!', command = calculateturns_money)

# Elements for Trade Conversion
tradeframe = Frame(conversionframe)
tradetitle = Label(tradeframe, text = 'Trade')
tradeblurb = Label(tradeframe, text = 'Enter the worth of the item you are trading as if it were brand-new:')
tradeentry = Entry(tradeframe)
tradebutton = Button(tradeframe, text = 'Submit!', command = calculateturns_trade) 

# Game Images
apeximage = PhotoImage(file='img/apex_legends_logo.gif')
boombeachimage = PhotoImage(file='img/boom_beach_logo.gif')
cocimage = PhotoImage(file='img/clash_of_clans_logo.gif') #Clash of Clans
eggincimage = PhotoImage(file='img/egg_inc_logo.gif')
fortniteimage = PhotoImage(file='img/fortnite_logo.gif')
minecraftimage = PhotoImage(file='img/minecraft_logo.gif')
asphaltimage = PhotoImage(file='img/asphalt_logo.gif')
clashroyaleimage = PhotoImage(file='img/clash_royale_logo.gif')
crossyroadimage = PhotoImage(file='img/crossy_road_logo.gif')
hillclimb1image = PhotoImage(file='img/hill_climb_racing_logo.gif')
hillclimb2image = PhotoImage(file='img/hill_climb_racing_2_logo.gif')
mariokartimage = PhotoImage(file='img/mario_kart_logo.gif')
solitaireimage = PhotoImage(file='img/microsoft_solitaire_logo.gif')
sudokuimage = PhotoImage(file='img/sudoku_logo.gif')
mariobrosimage = PhotoImage(file='img/super_mario_bros_logo.gif')
smashbrosimage = PhotoImage(file='img/smash_bros_logo.gif')

# Game Icons, Titles & Turn Values
blurb = Label(window, text = 'The turn numbers in the boxes below are based on the value entered above.')
#Type 1
type1title = Label(window, text = '2 Min In Game')
type1frame = Frame(window)
#Apex
apexframe = Frame(type1frame)
apexicon = Label(apexframe, image = apeximage)
apexname = Label(apexframe, text = 'Apex Legends')
apexturns = Label(apexframe, text = turns, relief = 'groove')

# Pack Statements
#Main Window
title.pack(side = TOP)
titleblurb.pack(side = TOP)
conversionframe.pack(side = TOP)
#Money Conversion
moneytitle.pack(side = TOP)
moneyblurb.pack(side = TOP)
moneybutton.pack(side = RIGHT)
moneyentry.pack(side = LEFT)
moneyframe.pack(side = LEFT, padx = 10, pady = 10)
#Trade Conversion
tradetitle.pack(side = TOP)
tradeblurb.pack(side = TOP)
tradebutton.pack(side = RIGHT)
tradeentry.pack(side = LEFT)
tradeframe.pack(side = LEFT, padx = 10, pady = 10)
#Game Titles & Turn Values
blurb.pack(side = TOP)
type1title.pack(side = TOP)
type1frame.pack(side = TOP)
apexframe.pack(side = LEFT)
apexicon.pack(side = LEFT)
apexname.pack(side = LEFT)
apexturns.pack(side = LEFT)

# Sustain Window
window.mainloop()
