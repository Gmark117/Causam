import pygame
import pygame.mixer as mix
import Assets

class Menu():
    def __init__(self, game):
        # Initialise the mixer module for audio
        mix.init()  
        
        # Store the game instance to access its variables and methods
        self.game = game
        
        # Define positions
        self.mid_w = Assets.DISPLAY_W/2
        self.mid_h = Assets.DISPLAY_H/2
        
        # Initialise flag to control the menu loop
        self.run_display = True
        
        # Load backgrounds
        self.background = pygame.image.load(Assets.Images['BACKGROUND'].value)
        self.dark_bg    = pygame.image.load(Assets.Images['DARK_BG'].value)
        self.board      = pygame.image.load(Assets.Images['BOARD'].value)

        # Load the ambient audio file
        mix.music.load(Assets.Audio['AMBIENT'].value)  
        
        # Load the button click sound
        self.button = mix.Sound(Assets.Audio['BUTTON'].value)
        self.button.set_volume(0.5)
        
    # Write title and menu voices
    def draw_text(self, text, size, x, y, font, color, handle):
        # Create a text surface
        style        = pygame.font.Font(font, size)
        text_surface = style.render(text, True, color)
        
        # Dimensions of the writtable rectangle
        text_rect = text_surface.get_rect()

        # Choose the point of the surface to which the coordinates refer
        match handle:
            case 'Center':
                text_rect.center = (x,y)
            case 'Midtop':
                text_rect.midtop = (x,y)
            case 'Midright':
                text_rect.midright = (x,y)
            case 'Midleft':
                text_rect.midleft = (x,y)
        
        # Burn the text on the display
        self.game.display.blit(text_surface,text_rect)
    
    # Move the cursor between menu voices
    def move_cursor(self, states, state, cursor_pos, x_coords = [], y_coords = []):
        # Look for the current state in the list
        for i in range(len(states)):
            # If no input to change state was given, do nothing
            if (not self.game.UP_KEY) and (not self.game.DOWN_KEY):
                break

            # If the input was to go up, update the cursor position and the state
            if state == states[i] and self.game.UP_KEY:
                cursor_pos = [x_coords[(i-1) % len(states)], y_coords[(i-1) % len(states)]]
                state      = states[(i-1) % len(states)]
                break
            
            # If the input was to go down, update the cursor position and the state
            if state == states[i] and self.game.DOWN_KEY:
                cursor_pos = [x_coords[(i+1) % len(states)], y_coords[(i+1) % len(states)]]
                state      = states[(i+1) % len(states)]
                break
        
        return cursor_pos, state

    # Play the button sound if the toggle allows it
    def play_button(self, switch):
        if switch == 'on':
            self.button.play()

    # Change the display back to the main menu
    def to_main_menu(self):
        self.game.curr_menu = self.game.main_menu
        display_flag = False
        
        return display_flag
    