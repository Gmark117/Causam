import Assets
from Menu import Menu

class CreditsMenu(Menu):
    def __init__(self, game):
        super().__init__(game)

        # Define positions for the texts
        self.subtitle_height  = self.mid_h - 150
        self.states_y         = [self.mid_h - 10, self.mid_h + 140]
        
        # Set the position of the cursor
        self.cursor_pos = [self.mid_w - 75, self.states_y[1]]

    def display(self):
        self.run_display = True

        while self.run_display:
            # Check for inputs
            self.game.check_events()
            if self.game.START_KEY or self.game.BACK_KEY:
                self.play_button(self.game.options.button_sound)
                self.run_display = self.to_main_menu()
            
            # Set background
            self.game.display.blit(self.background, (0,0))

            # Display credits
            # TITLE
            self.draw_text('Credits', 60,
                           self.mid_w,
                           self.subtitle_height,
                           Assets.Fonts['BIG'].value,
                           Assets.Colors['WHITE'].value,
                           Assets.RectHandle['MIDTOP'].value)
            
            # CREDITS
            self.draw_text('GianMarco Lavacca ( 224558 )', 30,
                           self.mid_w,
                           self.states_y[0],
                           Assets.Fonts['SMALL'].value,
                           Assets.Colors['WHITE'].value,
                           Assets.RectHandle['CENTER'].value)
            
            # VOICES
            self.draw_text('Back', 25,
                           self.mid_w,
                           self.states_y[1],
                           Assets.Fonts['SMALL'].value,
                           Assets.Colors['WHITE'].value,
                           Assets.RectHandle['CENTER'].value)
            
            # CURSOR
            self.draw_text('X', 30,
                           self.cursor_pos[0],
                           self.cursor_pos[1],
                           Assets.Fonts['SMALL'].value,
                           Assets.Colors['GREEN'].value,
                           Assets.RectHandle['CENTER'].value)
            
            self.game.blit_screen()
