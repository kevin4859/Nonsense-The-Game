import pygame
import random
import json
from controller import *

class End:
    def __init__(self):
        pygame.init()
        self.start_tick = pygame.time.get_ticks()
        self.window = pygame.display.set_mode((800,600))
        self.c_title = pygame.image.load("Sprites//c_titlecard.png").convert()
        self.c_title.set_colorkey((255,255,255))
        self.font = pygame.font.Font("Sprites//times.ttf", 45)
        a_string = "You have gone insane."
        self.position = (190, 225)
        self.mode = 1
        self.plural = "s"
        self.running = True
        while self.running == True:
            self.window.fill((0,0,0))
            self.sec = int((pygame.time.get_ticks()-self.start_tick)/1000)
            #Mode one is our display sequence of events
            if self.mode == 1:
                self.display_message = self.font.render(a_string, True, (240, 93, 93))
                if self.sec > 3 and self.sec < 5:
                    a_string = ""
                elif self.sec > 5 and self.sec < 13:
                    if Controller.score_current == 1:
                        self.pural = ""
                    a_string = "You cleared " + str(Controller.score_current) + " scene" + self.plural + "."
                elif self.sec > 12:
                    a_string = ""
                    if self.sec > 14:
                        #Add to a local highscore json file before displaying final screen
                        add = open("highscore.json", "a+")
                        add.close()        
                        our_list = []
                        infile = open("highscore.json", "r")
                        for line in infile:
                            our_list.append(line[:-1])
                        infile.close()
                        add = open("highscore.json", "a+")
                        add.write(str(Controller.score_current) + "\r\n")
                        add.close()
                        our_list = []
                        infile = open("highscore.json", "r")
                        for line in infile:
                            if str(line) != '\n':
                                our_list.append(int(line[:-1]))
                        infile.close()
                        our_list.sort()
                        a_string = "Local highscore: " + str(our_list[-1])
                        
                        self.mode = 2
                self.window.blit(self.display_message, self.position)
            elif self.mode == 2:
                self.display_message = self.font.render(a_string, True, (240, 93, 93))
                pygame.draw.ellipse(self.window, (255,255,255), (150, 50, 500, 250))
                self.window.blit(self.c_title, (200,100))
                self.window.blit(self.display_message, (190, 425))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        exit()

            pygame.display.flip()
