import pygame
import time
import random
from controller import *
class Menu:
    start = False
    def __init__(self):
        init = pygame.init()
        init2 = pygame.mixer.init()
        self.window = pygame.display.set_mode((800,600))
        self.title = pygame.image.load("Sprites//titlecard.png").convert()
        self.start_button_unpressed = pygame.image.load("Sprites//start1.png").convert()
        self.start_button_pressed = pygame.image.load("Sprites//start2.png").convert()
        self.instruct_button_unpressed = pygame.image.load("Sprites//instruct1.png").convert()
        self.instruct_button_pressed = pygame.image.load("Sprites//instruct2.png").convert()
        self.quit_button_unpressed = pygame.image.load("Sprites//quit1.png").convert()
        self.quit_button_pressed = pygame.image.load("Sprites//quit2.png").convert()
        self.setting_button_unpressed = pygame.image.load("Sprites//settings1.png").convert()
        self.setting_button_pressed = pygame.image.load("Sprites//settings2.png").convert()
        self.res_button_unpressed = pygame.image.load("Sprites//res1.png").convert()
        self.res_button_pressed = pygame.image.load("Sprites//res2.png").convert()
        self.song = pygame.mixer.music.load("Sounds//Party Hard OST - Main Theme 2 (Felipe Adorno Vassao).wav")
        self.bg2 = pygame.Surface((800,600))
        self.bg2.set_alpha(0)
        self.bg2.fill((255,255,255))
        # Method Calls
        our_color = self.background()
        pygame.mixer.music.play(loops=-1, start=0.0)
        i = 0
        self.running = True
        self.music = True
        self.menu_act = 0

        # Main Menu Loop
        while self.running:

            #Scrolling Background Image
            i -= 1
            rel_x = i % 800
            self.window.fill(our_color)
            self.window.blit(self.menu_background, (rel_x - 800, 0))
            if rel_x < 800:
                self.window.blit(self.menu_background, (rel_x, 0))

            for event in pygame.event.get():
                # Quit button
                if event.type == pygame.QUIT:
                    if self.menu_act == 0:
                        pygame.quit()
                        exit()
                    elif self.menu_act == 1:
                        self.menu_act = 0
                    elif self.menu_act == 2:
                        self.menu_act = 0

                # Keybinds
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        if self.menu_act == 0:
                            pygame.quit()
                            exit()
                        elif self.menu_act == 1:
                            self.menu_act = 0
                        elif self.menu_act == 2:
                            self.menu_act = 0

            #Title and Buttons
            if self.music == False:
                pygame.mixer.music.stop()
            if self.menu_act == 0:
                self.title_pic()
                self.buttons()
            elif self.menu_act == 1:
                self.instruct()
            elif self.menu_act == 2:
                self.music_buttons()
            if Menu.start == False:
                self.running = True
            else:
                self.running = False

            pygame.display.flip()

    def background(self):
        '''
           creates background
        '''
        x1 = random.randint(0, 255)
        x2 = random.randint(0, 255)
        x3 = random.randint(0, 255)
        rand_color = (x1,x2,x3)
        self.window.fill((x1,x2,x3))
        self.menu_background = pygame.image.load("Sprites//movingbackground.png").convert()
        self.menu_background.set_colorkey((255,255,255))
        self.window.blit(self.menu_background, (0, 0))
        return rand_color

    def title_pic(self):
        '''
           blits title image onto surface
        '''
        pygame.draw.ellipse(self.window, (255,255,255), (150, 50, 500, 250))
        self.title.set_colorkey((255,255,255))
        self.window.blit(self.title, (200,100))
    def text(self, x, y, z, a):
        myfont = pygame.font.Font("Sprites//times.ttf", z)
        textsurface = myfont.render(a, True, (0, 0, 0))
        self.window.blit(textsurface,(x,y))
    def button_method(self, blit1, blit2, x1, x2, y1, y2, unpressed, pressed):
        """
           method for creating buttons
        """
        unpressed = pygame.transform.scale(unpressed, (126, 60))
        pressed = pygame.transform.scale(pressed, (126, 60))
        self.window.blit(unpressed, (blit1, blit2))
        mouse_posx = pygame.mouse.get_pos()[0]
        mouse_posy = pygame.mouse.get_pos()[1]
        if mouse_posx < x1 and mouse_posx > x2 and mouse_posy > y1 and mouse_posy < y2:
            self.window.blit(pressed, (blit1,blit2))
            return True
    def buttons(self):
        # Start button
        y = self.button_method(37,400,163,37,400,460, self.start_button_unpressed, self.start_button_pressed)
        x = pygame.mouse.get_pressed()
        self.text(47,402,50,"Start")
        if x[0] == 1 and y == True:
            Menu.start = True
            return
        # Instruction button
        y = self.button_method(237,400,363,237,400,460, self.instruct_button_unpressed, self.instruct_button_pressed)
        x = pygame.mouse.get_pressed()
        self.text(259,402,50,"Info")
        if x[0] == 1 and y == True:
            self.menu_act = 1
        # Settings button
        y = self.button_method(437,400,563,437,400,460, self.setting_button_unpressed, self.setting_button_pressed)
        x = pygame.mouse.get_pressed()
        self.text(458,418,30,"Settings")
        if x[0] == 1 and y == True:
            self.menu_act = 2
        #Quit button
        y = self.button_method(637,400,763,637,400,460, self.quit_button_unpressed, self.quit_button_pressed)
        x = pygame.mouse.get_pressed()
        self.text(657,402,50,"Quit")
        if x[0] == 1 and y == True:
            pygame.quit()
            exit()
    def instruct(self):
        myfont = pygame.font.Font("Sprites//times.ttf", 30)
        textsurface = myfont.render('Press start to play.', True, (0, 0, 0))
        self.bg2.set_alpha(100)
        self.window.blit(self.bg2, (0,0))
        self.window.blit(textsurface,(0,0))
    def music_buttons(self):
        pygame.draw.rect(self.window, (255,255,255), (150, 50, 500, 250))
        # Music on button
        y = self.button_method(237,200,363,237,200,260, self.res_button_unpressed, self.res_button_pressed)
        x = pygame.mouse.get_pressed()
        self.text(250,220,22,"Music On")
        if x[0] == 1 and y == True:
            if self.music != True:
                self.music = True
                pygame.mixer.music.play(loops=-1, start=0.0)
        # Music off
        y = self.button_method(437,200,563,437,200,260, self.res_button_unpressed, self.res_button_pressed)
        x = pygame.mouse.get_pressed()
        self.text(450,220,22,"Music Off")
        if x[0] == 1 and y == True:
            self.music = False
        self.text(320, 120, 30, "Sound Settings")
