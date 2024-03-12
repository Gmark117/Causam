import time
import Assets
from Menu import Menu

class MatchMenu(Menu):
    def __init__(self, game):
        super().__init__(game)

        # Get the list of states for this menu and set the current one
        self.states = Assets.match_menu_states  # ['Mode', 'AI Strength', 'Side',
                                                #  'Back', 'Start Simulation']
        self.default_state = len(self.states) - 1
        self.state  = self.states[self.default_state]

        # Initialise the possible options and their iterators
        self.mode_options   = Assets.mode_options
        self.side_options   = Assets.side_options

        self.mode     = 0   # ["Player vs Player", "Player vs AI"]
        self.ai_stren = 3   # 1 through 10
        self.side     = 0   # ["White", "Black", "Random"]
       
        # Define positions for menu text
        self.align_left      = self.mid_w - 50
        self.align_right     = self.mid_w + 50
        self.subtitle_height = self.mid_h - 170
        
        self.states_x = [self.align_left] * (len(self.states)-2)
        self.states_x.extend([self.mid_w] * 2)
        self.states_y = [self.mid_h -  90,  # Mode
                         self.mid_h -  50,  # AI Strength
                         self.mid_h -  10,  # Side
                         self.mid_h +  30,  # Back
                         self.mid_h + 130]  # Start Simulation
        
        # Set the initial position of the cursor
        self.cursor_offset = -30

        self.cursor_x = [self.align_left - 110 + self.cursor_offset,  # Mode
                         self.align_left - 250 + self.cursor_offset,  # AI Strength
                         self.align_left -  85 + self.cursor_offset,  # Side
                         self.mid_w      -  45 + self.cursor_offset,  # Back
                         -100]                                        # Start Simulation
        self.cursor_y = [self.states_y[0],  # Mode
                         self.states_y[1],  # AI Strength
                         self.states_y[2],  # Side
                         self.states_y[3],  # Back
                         -100]              # Start Simulation
        
        self.cursor_pos = [self.cursor_x[self.default_state],
                           self.cursor_y[self.default_state]]

        # Set the seed input cursor position
        self.input_cursor_offset = 25

        # Initialize the number input flag
        self.number_input = False  
    
    # Display the Simulation menu
    def display(self):
        self.run_display = True

        while self.run_display:
            # Check for inputs
            self.game.check_events()
            self.check_input()
            time.sleep(0.05)

            # Set background 
            self.game.display.blit(self.dark_bg,(0,0))

            # Display sound and volume options
            # TITLE
            self.draw_text('Simulation Settings', 50,
                           self.mid_w,
                           self.subtitle_height,
                           Assets.Fonts['BIG'].value,
                           Assets.Colors['WHITE'].value,
                           Assets.RectHandle['CENTER'].value)
            # VOICES
            self.draw_text('Mode', 25,
                           self.states_x[0],
                           self.states_y[0],
                           Assets.Fonts['SMALL'].value,
                           Assets.Colors['WHITE'].value,
                           Assets.RectHandle['MIDRIGHT'].value)
            self.draw_text('AI Strength', 25,
                           self.states_x[1],
                           self.states_y[1],
                           Assets.Fonts['SMALL'].value,
                           Assets.Colors['WHITE'].value,
                           Assets.RectHandle['MIDRIGHT'].value)
            self.draw_text('Side', 25,
                           self.states_x[2],
                           self.states_y[2],
                           Assets.Fonts['SMALL'].value,
                           Assets.Colors['WHITE'].value,
                           Assets.RectHandle['MIDRIGHT'].value)
            self.draw_text('Back', 25,
                           self.states_x[3],
                           self.states_y[3],
                           Assets.Fonts['SMALL'].value,
                           Assets.Colors['WHITE'].value,
                           Assets.RectHandle['CENTER'].value)
            self.draw_text('Start Simulation',
                           100 if self.state==self.states[self.default_state] else 80,
                           self.states_x[4],
                           self.states_y[4],
                           Assets.Fonts['BIG'].value,
                           Assets.Colors['GREEN'].value if self.state==self.states[self.default_state]
                           else Assets.Colors['EUCALYPTUS'].value,
                           Assets.RectHandle['CENTER'].value)
            
            # VALUES
            self.draw_text(f'{self.mode_options[self.mode]}', 25,
                           self.align_right,
                           self.states_y[0],
                           Assets.Fonts['SMALL'].value,
                           Assets.Colors['GREEN'].value,
                           Assets.RectHandle['MIDLEFT'].value)
            self.draw_text(f'{self.ai_stren}', 25,
                           self.align_right,
                           self.states_y[1],
                           Assets.Fonts['SMALL'].value,
                           Assets.Colors['GREEN'].value,
                           Assets.RectHandle['MIDLEFT'].value)
            self.draw_text(f'{self.side_options[self.side]}', 25,
                           self.align_right,
                           self.states_y[2],
                           Assets.Fonts['SMALL'].value,
                           Assets.Colors['GREEN'].value,
                           Assets.RectHandle['MIDLEFT'].value)
            
            # CURSOR
            self.draw_text('X', 30,
                           self.cursor_pos[0],
                           self.cursor_pos[1],
                           Assets.Fonts['SMALL'].value,
                           Assets.Colors['GREEN'].value,
                           Assets.RectHandle['CENTER'].value)

            self.game.blit_screen()
            
            # Reset state and cursor position
            if self.run_display==False:
                self.state      = self.states[self.default_state]
                self.cursor_pos = [self.cursor_x[self.default_state],
                                   self.cursor_y[self.default_state]]

    # Handle user input
    def check_input(self):
        # Check if the player wants to move the cursor
        [self.cursor_pos, self.state] = self.move_cursor(self.states, self.state, self.cursor_pos,
                                                         self.cursor_x, self.cursor_y)
        
        # Depending on the current option, delete the last input or go back to the Main menu
        if self.game.BACK_KEY:
            self.play_button(self.game.options.button_sound)
            self.run_display = self.to_main_menu()
            return

        # Set the value of the current option
        if self.game.START_KEY:
            self.play_button(self.game.options.button_sound)

            match self.state:
                case 'Start Simulation':
                    self.game.playing = True
                    self.run_display = False
                    self.game.blit_screen()
                case 'Back':
                    # Go back to the Main menu
                    self.run_display = self.to_main_menu()
                case 'Mode':
                    self.mode = 1 if self.mode==0 else 0
                case 'AI Strength':
                    match self.ai_stren:
                        case 10:
                            self.ai_stren = 1
                        case _:
                            self.ai_stren += 1
                case 'Side':
                    match self.side:
                        case 0: self.side = 1
                        case 1: self.side = 2
                        case 2: self.side = 0
