"""
(C) 2016 - 2022. All rights reserved.
"""

import sys
from cx_Freeze import setup, Executable

base = None
if sys.platform == 'win32' : base = 'Win32GUI'

opts = { 'include_files' : ['img/apex_legends_logo.gif', 'img/asphalt_logo.gif', 'img/boom_beach_logo.gif', 'img/clash_of_clans_logo.gif', 'img/clash_royale_logo.gif', 'img/crossy_road_logo.gif', 'img/egg_inc_logo.gif', 'img/fortnite_logo.gif', 'img/hill_climb_racing_logo.gif', 'img/hill_climb_racing_2_logo.gif', 'img/mario_kart_logo.gif', 'img/microsoft_solitaire_logo.gif', 'img/minecraft_logo.gif', 'img/smash_bros_logo.gif', 'img/sudoku_logo.gif', 'img/super_mario_bros_logo.gif'] , 'includes' : ['re'] }

setup(
    name = 'Game Currency Converter' ,
    version = '1.0.0' ,
    description = 'Convert money into the amount of time that can be spent playing each game.' ,
    author = '@willtheorangeguy' ,
    options = {'build_exe' : opts } ,
    executables = [ Executable( 'main.py' , base = base ) ] )
