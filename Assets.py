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
IMG_OFFSET = - int(IMAGE_DIM/2) + 2

# Lists for menu voices and settings
main_menu_states     = ['Start', 'Options', 'Credits', 'Exit']
options_menu_states  = ['Game Volume', 'Music Volume', 'Button Sound', 'Back']
sim_menu_states      = ['Mode', 'AI Strength', 'Side', 'Back', 'Start Simulation']
mode_options         = ["Player vs Player", "Player vs AI"]
side_options         = ["White", "Black", "Random"]

# Nodes
def node_label(level, node_num):
        letter = ''
        
        match level:
                case   85: letter = 'A'
                case  235: letter = 'B'
                case  385: letter = 'C'
                case  535: letter = 'D'
                case  685: letter = 'E'
                case  835: letter = 'F'
                case  985: letter = 'G'
                case 1135: letter = 'H'
                case 1285: letter = 'I'
                case 1435: letter = 'J'
                case 1585: letter = 'K'
        
        label = letter + str(node_num+1)

        return label

              # A,   B,   C,   D,   E,   F,   G,    H,    I,    J,    K
nodes_pos_x = [85, 235, 385, 535, 685, 835, 985, 1135, 1285, 1435, 1585]
nodes_pos_y = [
                                 [428],                            # A
                    [245, 315, 392, 468, 543, 613],                # B
        [ 54, 129, 204, 279, 354, 429, 504, 579, 654, 729, 804],   # C
           [ 90, 165, 240, 315, 390, 465, 540, 615, 690, 765],     # D
              [129, 204, 279, 354, 429, 504, 579, 654, 729],       # E
                 [165, 240, 315, 390, 465, 540, 615, 690],         # F
                    [204, 279, 354, 429, 504, 579, 654],           # G
                 [165, 240, 315, 390, 465, 540, 615, 690],         # H
              [129, 204, 279, 354, 429, 504, 579, 654, 729],       # I
           [ 90, 165, 240, 315, 390, 465, 540, 615, 690, 765],     # J
        [ 54, 129, 204, 279, 354, 429, 504, 579, 654, 729, 804]    # K
]

nodes_up_border   = [ 'D1', 'E1', 'F1', 'G1', 'H1', 'I1',  'J1']
nodes_down_border = ['D10', 'E9', 'F8', 'G7', 'H8', 'I9', 'J10']
nodes_lvl_A  = ['A1']
nodes_lvl_B  = ['B1', 'B2', 'B3', 'B4', 'B5', 'B6']
nodes_lvl_C  = ['C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9', 'C10', 'C11']
nodes_lvl_K = ['K1', 'K2', 'K3', 'K4', 'K5', 'K6', 'K7', 'K8', 'K9', 'K10', 'K11']
nodes_internal = []
for x in range(3,10):
       for y in range(1, len(nodes_pos_y[x])-1):
              nodes_internal.append(node_label(x,y))
all_nodes = []
for x in range(len(nodes_pos_x)):
       for y in range(len(nodes_pos_y[x])):
              all_nodes.append(node_label(nodes_pos_x[x],y))

# Pieces positions
w_nodes  = ['A1','B2','B3','B4','B5','C1','C3','C5','C7','C9','C11']
greens_x = [  85, 235, 235, 235, 235, 385, 385, 385, 385, 385,  385]
greens_y = [ 428, 315, 392, 468, 543,  54, 204, 354, 504, 654,  804]

b_nodes  = ['G3', 'G5', 'H3', 'H4', 'H5', 'H6', 'I3', 'I4', 'I5', 'I6', 'I7']
blues_x  = [ 985,  985, 1135, 1135, 1135, 1135, 1285, 1285, 1285, 1285, 1285]
blues_y  = [ 354,  504,  315,  390,  465,  540,  279,  354,  429,  504,  579]

h_b_node = ['G4']
h_blue_x = [ 985]
h_blue_y = [ 429]


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

def is_occupied(x, y):
        for i in range(len(nodes_pos_x)):
                for j in range(len(nodes_pos_y)):
                        return True if (x==nodes_pos_x[i] and y==nodes_pos_y[j]) else False

def update_selection(nodes, next_nodes, selection, sprite):
        if sprite.selected:
                selection.add(sprite)
        elif selection.sprite.id == sprite.id:
                selection.remove(sprite)
        
        get_next_nodes(selection, nodes, next_nodes)

def get_next_nodes(selection, nodes, next_nodes):
        # Return next viable nodes
        for i in range(len(all_nodes)):
                if selection.sprite.curr_node == all_nodes[i]:
                        match all_nodes[i][0]:
                                case 'A': next_from_first(nodes, next_nodes)
                                case 'B': next_from_second(selection, nodes, next_nodes)
                                #case 'C': next_from_third(selection, nodes, next_nodes)
                                #case 'K': next_from_last(selection, nodes, next_nodes)
                                #case   _: next_from_inside(selection, nodes, next_nodes)

def turn_on(node, next_nodes):
        node.visible = True
        next_nodes.add(node)
        
def turn_off(node, next_nodes):
        node.visible = False
        next_nodes.remove(node)

def next_from_first(nodes, next_nodes):
        for node in nodes:
                if node.id[0] == 'B':
                        turn_off(node, next_nodes) if node.visible else turn_on(node, next_nodes)

def next_from_second(selection, nodes, next_nodes):
        curr_id = selection.sprite.curr_node
        for node in nodes:
                if (node.id[0] == 'A'
                    or (node.id[0] == 'B' and (int(node.id[1:])==int(curr_id[1:])-1 or int(node.id[1:])==int(curr_id[1:])+1))
                    or (node.id[0] == 'C' and int(node.id[1:])==(2 * int(curr_id[1:]) - 1))
                    ):
                        turn_off(node, next_nodes) if node.visible else turn_on(node, next_nodes)

#def next_from_third(selection, nodes, next_nodes):
#def next_from_last(selection, nodes, next_nodes):
#def next_from_inside(selection, nodes, next_nodes):

#  ____   _   _  _      _____  ____  
# |  _ \ | | | || |    | ____|/ ___| 
# | |_) || | | || |    |  _|  \___ \ 
# |  _ < | |_| || |___ | |___  ___) |
# |_| \_\ \___/ |_____||_____||____/ 

'''
Movements:
- Pieces move between points along the lines
- White pieces causes one piece adjacent to their new position to move one step to the left (One level lower)
- Black pieces causes one piece adjacent to their new position to move one step to the right (One level higher)
- The Black high piece causes one piece adjacent to their new position to move one step to the right OR to the left (Player Choice)

Rules:
- All semi-circles at the end are filled by White pieces     --> WHITE WINS
- All non semi-circles at the end are filled by White pieces --> BLACK WINS
- Pieces cannot move from the last level
- Black pieces cannot occupy the last level
- Multiple pieces cannot occupy the same node
- You cannot displace a piece as an effect of your move if the destination node is occupied
'''