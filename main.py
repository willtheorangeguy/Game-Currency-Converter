# Import Statements
from tkinter import *
import tkinter.messagebox as box

# Game Price Variables
apex = 0.50
boombeach = 0.50
coc = 0.50
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
window.title('Game Currency - Use this simple app to find how many in-game turns you can get!')

title = Label(window, text = 'Game Currency', fg = "blue")
titleblurb = Label(window, text = 'Enter the amount of money that you are '  \
    'going to pay for your turns or the worth of the item your are trading in for your turns.')
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
moneytitle = Label(moneyframe, text = 'Cash', fg = "green")
moneyblurb = Label(moneyframe, text = 'Enter the amount of money\nyou are willing to pay:')
moneyentry = Entry(moneyframe)
moneybutton = Button(moneyframe, text = 'Submit!', command = calculateturns_money)

# Money Conversion Pack Statements
moneytitle.pack(side = TOP)
moneyblurb.pack(side = TOP)
moneyentry.pack(side = LEFT, padx = 10)
moneybutton.pack(side = RIGHT, padx = 10)

# Elements for Trade Conversion
tradeframe = Frame(conversionframe)
tradetitle = Label(tradeframe, text = 'Trade', fg = "purple")
tradeblurb = Label(tradeframe, text = 'Enter the worth of the item you are trading\nas if it were brand-new:')
tradeentry = Entry(tradeframe)
tradebutton = Button(tradeframe, text = 'Submit!', command = calculateturns_trade) 

# Trade Conversion Pack Statements
tradetitle.pack(side = TOP)
tradeblurb.pack(side = TOP)
tradeentry.pack(side = LEFT, padx = 10)
tradebutton.pack(side = RIGHT, padx = 10)

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
# Type 1
type1title = Label(window, text = '2 Minutes In Game')
type1frame = Frame(window)

# Apex
apexframe = Frame(type1frame)
apexicon = Label(apexframe, image = apeximage)
apexname = Label(apexframe, text = 'Apex Legends')
apexturns = Label(apexframe, text = " " + str(turns) + " ", relief = 'groove')
apexicon.pack(side = LEFT, padx = 10)
apexturns.pack(side = RIGHT)
apexname.pack(side = RIGHT, padx = 5)

# Pack Statements
# Main Window
title.grid(row = 1, column = 1, columnspan = 4)
titleblurb.grid(row = 2, column = 1, columnspan = 4)
conversionframe.grid(row = 3, column = 1, columnspan = 4)

# Money Conversion
moneyframe.grid(row = 4, column = 1, columnspan = 2)

# Trade Conversion
tradeframe.grid(row = 4, column = 3, columnspan = 2)

# Game Titles & Turn Values
blurb.grid(row = 5, column = 1, columnspan = 4)
type1title.grid(row = 6, column = 1, columnspan = 2)
type1frame.grid(row = 7, column = 1, columnspan = 2)
apexframe.grid(row = 8, column = 1, columnspan = 1)

# Sustain Window
window.mainloop()
