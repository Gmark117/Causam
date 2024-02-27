import os
import tkinter
import math
from enum import Enum

root = tkinter.Tk()


#  ____   _____  _____  _____  ___  _   _   ____  ____  
# / ___| | ____||_   _||_   _||_ _|| \ | | / ___|/ ___|
# \___ \ |  _|    | |    | |   | | |  \| || |  _ \___ \
#  ___) || |___   | |    | |   | | | |\  || |_| | ___) |
# |____/ |_____|  |_|    |_|  |___||_| \_| \____||____/

# Game directory: ..\CAUSAM
GAME_DIR = os.path.dirname(os.path.abspath(__file__))

# Display dimensions
DISPLAY_W    = 1200
DISPLAY_H    = 750
FULLSCREEN_W = root.winfo_screenwidth() - 5
FULLSCREEN_H = root.winfo_screenheight() - 70

# Lists for menu voices and settings
main_menu_states     = ['Start', 'Options', 'Credits', 'Exit']
options_menu_states  = ['Game Volume', 'Music Volume', 'Button Sound', 'Back']
sim_menu_states      = ['Mode', 'Map Dimension', 'Seed', 'Drones', 'Back', 'Start Simulation']
mode_options         = ["Cave exploration", "Rescue mission"]
map_options          = ["Small", "Medium", "Big"]
seed                 = [     5,       19,    837]


#   ____  _         _     ____   ____   _____  ____  
#  / ___|| |       / \   / ___| / ___| | ____|/ ___| 
# | |    | |      / _ \  \___ \ \___ \ |  _|  \___ \ 
# | |___ | |___  / ___ \  ___) | ___) || |___  ___) |
#  \____||_____|/_/   \_\|____/ |____/ |_____||____/ 

class Colors(Enum):
        BLACK        = (  0,   0,   0)
        WHITE        = (255, 255, 255)
        GREY         = (112, 128, 144)

        RED          = (255,   0,   0)
        ORANGE       = (255, 128,   0)
        YELLOW       = (255, 255,  51)

        GREEN        = ( 51, 255,  51)
        GREENDARK    = (117, 132, 104)
        EUCALYPTUS   = ( 95, 133, 117)

        BLUE         = (  0,   0, 153)
        L_BLUE       = ( 51, 255, 255)

        VIOLET       = (153,  51, 255)
        PINK         = (255,  51, 153)

        BROWN        = (165,  42,  42)
               
class Fonts(Enum):
        BIG          = os.path.join(GAME_DIR, 'Assets', 'Fonts', 'Cave-Stone.ttf')  
        SMALL        = os.path.join(GAME_DIR, 'Assets', 'Fonts', '8-BIT.TTF') 

class Audio(Enum):
        AMBIENT      = os.path.join(GAME_DIR, 'Assets', 'Audio', 'filename.ext')
        BUTTON       = os.path.join(GAME_DIR, 'Assets', 'Audio', 'Button.wav')

class Images(Enum):
        BACKGROUND   = os.path.join(GAME_DIR, 'Assets', 'Images', 'filename.ext')

class RectHandle(Enum):
        CENTER       = 'Center'
        MIDTOP       = 'Midtop'
        MIDRIGHT     = 'Midright'
        MIDLEFT      = 'Midleft'


#  _____  _   _  _   _   ____  _____  ___   ___   _   _  ____  
# |  ___|| | | || \ | | / ___||_   _||_ _| / _ \ | \ | |/ ___|
# | |_   | | | ||  \| || |      | |   | | | | | ||  \| |\___ \
# |  _|  | |_| || |\  || |___   | |   | | | |_| || |\  | ___) |
# |_|     \___/ |_| \_| \____|  |_|  |___| \___/ |_| \_||____/

# Calculate the square of the passed argument
def sqr(x):
        return x**2
