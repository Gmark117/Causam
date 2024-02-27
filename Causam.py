import os
import pygame
import Assets
from MainMenu import MainMenu

class Causam:
    def __init__(self):
        # Center the game window
        os.environ['SDL_VIDEO_CENTERED'] = '1'

        # Initialise pygame features
        pygame.init()

        # If we run the game we are not necessary playing
        self.running, self.playing = True, False

        # Initialise key flags to navigate in the menu
        self.UP_KEY,   self.DOWN_KEY, self.START_KEY = False, False, False
        self.BACK_KEY, self.LEFT_KEY, self.RIGHT_KEY = False, False, False
        
        self.to_windowed()

        # Initialise each menu and set the current one
        self.options         = OptionsMenu(self)
        self.main_menu       = MainMenu(self)
        self.credits         = CreditsMenu(self)
        self.simulation      = SimulationMenu(self)
        self.curr_menu       = self.main_menu


    #   ____     _     __  __  _____   _       ___    ___   ____  
    #  / ___|   / \   |  \/  || ____| | |     / _ \  / _ \ |  _ \ 
    # | |  _   / _ \  | |\/| ||  _|   | |    | | | || | | || |_) |
    # | |_| | / ___ \ | |  | || |___  | |___ | |_| || |_| ||  __/ 
    #  \____|/_/   \_\|_|  |_||_____| |_____| \___/  \___/ |_|    
    
    # Run the simulation
    def game_loop(self):
        if self.playing:
            pass


    #  __  __     _     _   _     _      ____  _____      ___  _   _  ____   _   _  _____  ____  
    # |  \/  |   / \   | \ | |   / \    / ___|| ____|    |_ _|| \ | ||  _ \ | | | ||_   _|/ ___|
    # | |\/| |  / _ \  |  \| |  / _ \  | |  _ |  _|       | | |  \| || |_) || | | |  | |  \___ \
    # | |  | | / ___ \ | |\  | / ___ \ | |_| || |___      | | | |\  ||  __/ | |_| |  | |   ___) |
    # |_|  |_|/_/   \_\|_| \_|/_/   \_\ \____||_____|    |___||_| \_||_|     \___/   |_|  |____/

    # Check player inputs
    def check_events(self):
        pass

    # Reset pushed key flags
    def reset_keys(self):
        self.UP_KEY,   self.DOWN_KEY, self.START_KEY = False, False, False
        self.BACK_KEY, self.LEFT_KEY, self.RIGHT_KEY = False, False, False


    #  __  __     _     _   _     _      ____  _____      ____   ___  ____   ____   _         _    __   __
    # |  \/  |   / \   | \ | |   / \    / ___|| ____|    |  _ \ |_ _|/ ___| |  _ \ | |       / \   \ \ / /
    # | |\/| |  / _ \  |  \| |  / _ \  | |  _ |  _|      | | | | | | \___ \ | |_) || |      / _ \   \ V /
    # | |  | | / ___ \ | |\  | / ___ \ | |_| || |___     | |_| | | |  ___) ||  __/ | |___  / ___ \   | |
    # |_|  |_|/_/   \_\|_| \_|/_/   \_\ \____||_____|    |____/ |___||____/ |_|    |_____|/_/   \_\  |_|

    # Update the display
    def blit_screen(self):
        self.window.blit(self.display, (0, 0))
        pygame.display.update()
        self.reset_keys()

    # Maximise the window
    def to_maximised(self):
        # Choose and set window dimensions
        self.width = Assets.FULLSCREEN_W
        self.height = Assets.FULLSCREEN_H

        # Initialise window
        self.display = pygame.Surface((self.width,self.height))
        self.window = pygame.display.set_mode((self.width,self.height), pygame.SCALED)
        
        # Set window title
        pygame.display.set_caption('Cave Game')

        # Set game icon
        pygame.display.set_icon(pygame.image.load(Assets.Images['GAME_ICON'].value))
        # pygame.display.set_icon(pygame.image.load(Assets.Images['GAME_ICON_BG'].value))

        return self.display

    # Return to the originial window dimensions
    def to_windowed(self):
        # Choose and set window dimensions
        self.width = Assets.DISPLAY_W
        self.height = Assets.DISPLAY_H

        # Initialise window
        self.display = pygame.Surface((self.width,self.height))
        self.window  = pygame.display.set_mode((self.width,self.height), pygame.SCALED)

        # Set window title
        pygame.display.set_caption('Cave Game')

        # Set game icon
        pygame.display.set_icon(pygame.image.load(Assets.Images['GAME_ICON'].value))
        # pygame.display.set_icon(pygame.image.load(Assets.Images['GAME_ICON_BG'].value))

        return self.display
