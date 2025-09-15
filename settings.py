class Settings:
    '''A class to store all seettings for Alien Invasion.'''

    def __init__(self):
        ''''Initialize the game's settings.'''
        # Screen settings. 
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Ship settings
        self.ship_speed = 1.5

        # bullet settings
        self.bullet_speed = 2.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (139, 0, 0)
        self.bullet_allowd = 3
        
        