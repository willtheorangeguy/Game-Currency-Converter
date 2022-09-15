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
    boomturns.configure(text = int(turns))
    cocturns.configure(text = int(turns))
    eggturns.configure(text = int(turns))
    fortniteturns.configure(text = int(turns))
    minecraftturns.configure(text = int(turns))
    asphaltturns.configure(text = int(turns))
    royaleturns.configure(text = int(turns))
    crossyturns.configure(text = int(turns))
    hillturns.configure(text = int(turns))
    climbturns.configure(text = int(turns))
    kartturns.configure(text = int(turns))
    solitaireturns.configure(text = int(turns))
    sudokuturns.configure(text = int(turns))
    marioturns.configure(text = int(turns))

def calculateturns_trade():
    turns = float(tradeentry.get()) / 0.50
    apexturns.configure(text = int(turns))
    boomturns.configure(text = int(turns))
    cocturns.configure(text = int(turns))
    eggturns.configure(text = int(turns))
    fortniteturns.configure(text = int(turns))
    minecraftturns.configure(text = int(turns))
    asphaltturns.configure(text = int(turns))
    royaleturns.configure(text = int(turns))
    crossyturns.configure(text = int(turns))
    hillturns.configure(text = int(turns))
    climbturns.configure(text = int(turns))
    kartturns.configure(text = int(turns))
    solitaireturns.configure(text = int(turns))
    sudokuturns.configure(text = int(turns))
    marioturns.configure(text = int(turns))

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
blurb = Label(window, text = 'The turn or action numbers in the boxes below are based on the value entered above.')
# Type 1
type1title = Label(window, text = '2 Minutes In Game')
type1frame = Frame(window)
# Type 2
type2title = Label(window, text = '1 In Game Action')
type2frame = Frame(window)

# Apex
apexframe = Frame(type1frame)
apexicon = Label(apexframe, image = apeximage)
apexname = Label(apexframe, text = 'Apex Legends')
apexturns = Label(apexframe, text = " " + str(turns) + " ", relief = 'groove')
apexicon.pack(side = LEFT, padx = 10)
apexturns.pack(side = RIGHT)
apexname.pack(side = RIGHT, padx = 5)

# Boom Beach
boomframe = Frame(type1frame)
boomicon = Label(boomframe, image = boombeachimage)
boomname = Label(boomframe, text = 'Boom Beach')
boomturns = Label(boomframe, text = " " + str(turns) + " ", relief = 'groove')
boomicon.pack(side = LEFT, padx = 10)
boomturns.pack(side = RIGHT)
boomname.pack(side = RIGHT, padx = 5)

# Clash of Clans
cocframe = Frame(type1frame)
cocicon = Label(cocframe, image = cocimage)
cocname = Label(cocframe, text = 'Clash of Clans')
cocturns = Label(cocframe, text = " " + str(turns) + " ", relief = 'groove')
cocicon.pack(side = LEFT, padx = 10)
cocturns.pack(side = RIGHT)
cocname.pack(side = RIGHT, padx = 5)

# Egg, Inc.
eggframe = Frame(type1frame)
eggicon = Label(eggframe, image = eggincimage)
eggname = Label(eggframe, text = 'Egg, Inc.')
eggturns = Label(eggframe, text = " " + str(turns) + " ", relief = 'groove')
eggicon.pack(side = LEFT, padx = 10)
eggturns.pack(side = RIGHT)
eggname.pack(side = RIGHT, padx = 5)

# Fortnite
fortniteframe = Frame(type1frame)
fortniteicon = Label(fortniteframe, image = fortniteimage)
fortnitename = Label(fortniteframe, text = 'Fortnite')
fortniteturns = Label(fortniteframe, text = " " + str(turns) + " ", relief = 'groove')
fortniteicon.pack(side = LEFT, padx = 10)
fortniteturns.pack(side = RIGHT)
fortnitename.pack(side = RIGHT, padx = 5)

# Minecraft
minecraftframe = Frame(type1frame)
minecrafticon = Label(minecraftframe, image = minecraftimage)
minecraftname = Label(minecraftframe, text = 'Minecraft')
minecraftturns = Label(minecraftframe, text = " " + str(turns) + " ", relief = 'groove')
minecrafticon.pack(side = LEFT, padx = 10)
minecraftturns.pack(side = RIGHT)
minecraftname.pack(side = RIGHT, padx = 5)

# Asphalt 9
asphaltframe = Frame(type2frame)
asphalticon = Label(asphaltframe, image = asphaltimage)
asphaltname = Label(asphaltframe, text = 'Ashpalt 9 (one race)')
asphaltturns = Label(asphaltframe, text = " " + str(turns) + " ", relief = 'groove')
asphalticon.pack(side = LEFT, padx = 10)
asphaltturns.pack(side = RIGHT)
asphaltname.pack(side = RIGHT, padx = 5)

# Clash Royale
royaleframe = Frame(type2frame)
royaleicon = Label(royaleframe, image = clashroyaleimage)
royalename = Label(royaleframe, text = 'Clash Royale (one battle)')
royaleturns = Label(royaleframe, text = " " + str(turns) + " ", relief = 'groove')
royaleicon.pack(side = LEFT, padx = 10)
royaleturns.pack(side = RIGHT)
royalename.pack(side = RIGHT, padx = 5)

# Crossy Road
crossyframe = Frame(type2frame)
crossyicon = Label(crossyframe, image = crossyroadimage)
crossyname = Label(crossyframe, text = 'Crossy Road (one run)')
crossyturns = Label(crossyframe, text = " " + str(turns) + " ", relief = 'groove')
crossyicon.pack(side = LEFT, padx = 10)
crossyturns.pack(side = RIGHT)
crossyname.pack(side = RIGHT, padx = 5)

# Hill Climb Racing
hillframe = Frame(type2frame)
hillicon = Label(hillframe, image = hillclimb1image)
hillname = Label(hillframe, text = 'Hill Climb Racing (one race)')
hillturns = Label(hillframe, text = " " + str(turns) + " ", relief = 'groove')
hillicon.pack(side = LEFT, padx = 10)
hillturns.pack(side = RIGHT)
hillname.pack(side = RIGHT, padx = 5)

# Hill Climb Racing 2
climbframe = Frame(type2frame)
climbicon = Label(climbframe, image = hillclimb2image)
climbname = Label(climbframe, text = 'Hill Climb Racing 2 (one race)')
climbturns = Label(climbframe, text = " " + str(turns) + " ", relief = 'groove')
climbicon.pack(side = LEFT, padx = 10)
climbturns.pack(side = RIGHT)
climbname.pack(side = RIGHT, padx = 5)

# Mario Kart
kartframe = Frame(type2frame)
karticon = Label(kartframe, image = mariokartimage)
kartname = Label(kartframe, text = 'Mario Kart (one race)')
kartturns = Label(kartframe, text = " " + str(turns) + " ", relief = 'groove')
karticon.pack(side = LEFT, padx = 10)
kartturns.pack(side = RIGHT)
kartname.pack(side = RIGHT, padx = 5)

# Microsoft Solitaire Collection
solitaireframe = Frame(type2frame)
solitaireicon = Label(solitaireframe, image = solitaireimage)
solitairename = Label(solitaireframe, text = 'Microsoft Solitaire Collection (one game)')
solitaireturns = Label(kartframe, text = " " + str(turns) + " ", relief = 'groove')
solitaireicon.pack(side = LEFT, padx = 10)
solitaireturns.pack(side = RIGHT)
solitairename.pack(side = RIGHT, padx = 5)

# Microsoft Sudoku
sudokuframe = Frame(type2frame)
sudokuicon = Label(sudokuframe, image = sudokuimage)
sudokuname = Label(sudokuframe, text = 'Microsoft Sudoku (one game)')
sudokuturns = Label(sudokuframe, text = " " + str(turns) + " ", relief = 'groove')
sudokuicon.pack(side = LEFT, padx = 10)
sudokuturns.pack(side = RIGHT)
sudokuname.pack(side = RIGHT, padx = 5)

# New Super Mario Bros
marioframe = Frame(type2frame)
marioicon = Label(marioframe, image = mariobrosimage)
marioname = Label(marioframe, text = 'New Super Mario Bros (one level)')
marioturns = Label(marioframe, text = " " + str(turns) + " ", relief = 'groove')
marioicon.pack(side = LEFT, padx = 10)
marioturns.pack(side = RIGHT)
marioname.pack(side = RIGHT, padx = 5)

# Pack Statements
# Main Window
title.grid(row = 1, column = 1, columnspan = 5)
titleblurb.grid(row = 2, column = 1, columnspan = 5)
conversionframe.grid(row = 3, column = 1, columnspan = 5)

# Money Conversion
moneyframe.grid(row = 4, column = 1, columnspan = 2)

# Trade Conversion
tradeframe.grid(row = 4, column = 3, columnspan = 3)

# Game Titles & Turn Values
blurb.grid(row = 5, column = 1, columnspan = 5)
type1title.grid(row = 6, column = 1, columnspan = 2)
type1frame.grid(row = 7, column = 1, columnspan = 2)
type2title.grid(row = 6, column = 3, columnspan = 3)
type2frame.grid(row = 7, column = 3, columnspan = 3)
apexframe.grid(row = 8, column = 1, columnspan = 1)
boomframe.grid(row = 8, column = 2, columnspan = 1)
cocframe.grid(row = 9, column = 1, columnspan = 1)
eggframe.grid(row = 9, column = 2, columnspan = 1)
fortniteframe.grid(row = 10, column = 1, columnspan = 1)
minecraftframe.grid(row = 10, column = 2, columnspan = 1)
asphaltframe.grid(row = 8, column = 3, columnspan = 1)
royaleframe.grid(row = 8, column = 4, columnspan = 1)
crossyframe.grid(row = 8, column = 5, columnspan = 1)
hillframe.grid(row = 9, column = 3, columnspan = 1)
climbframe.grid(row = 9, column = 4, columnspan = 1)
kartframe.grid(row = 9, column = 5, columnspan = 1)
solitaireframe.grid(row = 10, column = 3, columnspan = 1)
sudokuframe.grid(row = 10, column = 4, columnspan = 1)
marioframe.grid(row = 10, column = 5, columnspan = 1)

# Sustain Window
window.mainloop()
