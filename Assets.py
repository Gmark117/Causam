import os
import tkinter
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
FULLSCREEN_W = 1694
FULLSCREEN_H = 856

IMAGE_DIM = 70

# Lists for menu voices and settings
main_menu_states     = ['Start', 'Options', 'Credits', 'Exit']
options_menu_states  = ['Game Volume', 'Music Volume', 'Button Sound', 'Back']
sim_menu_states      = ['Mode', 'AI Strength', 'Side', 'Back', 'Start Simulation']
mode_options         = ["Player vs Player", "Player vs AI"]
side_options         = ["Green", "Blue", "Random"]

# Nodes positions
              # A,   B,   C,   D,   E,   F,   G,    H,    I,    J,    K
nodes_pos_x = [85, 235, 385, 535, 685, 835, 985, 1135, 1285, 1435, 1585]
nodes_pos_y = [
        [428],                                          # A
        [245,315,392,468,543,613],                      # B
        [54,129,204,279,354,429,504,579,654,729,804],   # C
        [90,165,240,315,390,465,540,615,690,765],       # D
        [129,204,279,354,429,504,579,654,729],          # E
        [165,240,315,390,465,540,615,690],              # F
        [204,279,354,429,504,579,654],                  # G
        [165,240,315,390,465,540,615,690],              # H
        [129,204,279,354,429,504,579,654,729],          # I
        [90,165,240,315,390,465,540,615,690,765],       # J
        [54,129,204,279,354,429,504,579,654,729,804]    # K
]

# Pieces positions
           # [A01, B02, B03, B04, B05, C01, C03, C05, C07, C09, C11]
greens_x = [ 85, 235, 235, 235, 235, 385, 385, 385, 385, 385, 385]
greens_y = [428, 315, 392, 468, 543,  54, 204, 354, 504, 654, 804]

          # [G03, G05,  H03,  H04,  H05,  H06,  I03,  I04,  I05,  I06,  I07]
blues_x = [985, 985, 1135, 1135, 1135, 1135, 1285, 1285, 1285, 1285, 1285]
blues_y = [354, 504,  315,  390,  465,  540,  279,  354,  429,  504,  579]

           # G04
h_blue_x = [985]
h_blue_y = [429]


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
        AMBIENT      = os.path.join(GAME_DIR, 'Assets', 'Audio', 'Temp_Ambient.mp3')
        BUTTON       = os.path.join(GAME_DIR, 'Assets', 'Audio', 'Button.wav')

class Images(Enum):
        BACKGROUND   = os.path.join(GAME_DIR, 'Assets', 'Images', 'Causam_Background.png')
        BOARD        = os.path.join(GAME_DIR, 'Assets', 'Images', 'Causam_Board.png')
        GREEN_STONE  = os.path.join(GAME_DIR, 'Assets', 'Images', 'Causam_G_Stone.png')
        BLUE_STONE   = os.path.join(GAME_DIR, 'Assets', 'Images', 'Causam_B_Stone.png')
        H_BLUE_STONE = os.path.join(GAME_DIR, 'Assets', 'Images', 'Causam_HB_Stone.png')
        SELECT_RING  = os.path.join(GAME_DIR, 'Assets', 'Images', 'Causam_Selection_Ring.png')
        NEXT_NODE    = os.path.join(GAME_DIR, 'Assets', 'Images', 'Causam_Next_Node.png')
        GAME_ICON    = os.path.join(GAME_DIR, 'Assets', 'Images', 'Causam_Board.png')

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

def node_label(level, node_num):
        letter = ''
        
        match level:
                case 0: letter = 'A'
                case 1: letter = 'B'
                case 2: letter = 'C'
                case 3: letter = 'D'
                case 4: letter = 'E'
                case 5: letter = 'F'
                case 6: letter = 'G'
                case 7: letter = 'H'
                case 8: letter = 'I'
                case 9: letter = 'J'
                case 10: letter = 'K'
        
        label = letter + str(node_num+1)

        return label
