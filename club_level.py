import pygame
import random
import time
from controller import *
pygame.init()

class Club:
    won = True
    questions = 1
    sayings = 2
    def __init__(self):
        pygame.init()

        #Club Setting
        self.window = pygame.display.set_mode((800, 600))
        self.club_background = pygame.image.load("Sprites//club.png").convert()
        self.club_background2 = pygame.image.load("Sprites//club2.png").convert()
        self.bar = pygame.image.load("Sprites//empty_bar.png").convert()
        self.bar.set_colorkey((0,0,64))

        #Keyboard DDR Setting
        self.speech_bubble = pygame.image.load("Sprites//speech_bubble.png").convert()
        self.directions = ['left', 'up', 'down', 'right']
        self.d = Dialogue()
        
    def run(self):
        Club.won = True
        self.landing_arrows = pygame.sprite.Group()
        self.arrow_group = pygame.sprite.Group()
        #Sounds
        if Controller.insanity < 4:
            self.club_music = pygame.mixer.music.load("Sounds//HOME - Above All.wav")
        else:
            self.club_music = pygame.mixer.music.load("Sounds//Flatline.wav")
        pygame.mixer.music.play(loops=-1, start=0.0)
        
        self.start_tick = pygame.time.get_ticks()
        self.completions = Controller.done_counter[3]
        self.num_seconds = 20 + 5 * self.completions
        
        self.running = True
        for i in self.directions:
            sprite = Arrow(2, i, 0)
            self.landing_arrows.add(sprite)
        
        self.difficultify()
        self.tell_at = self.num_seconds//Club.sayings
        t_list = list(range(Club.sayings))
        for i in range(Club.sayings):
            t_list[i] = i * self.tell_at
        self.d.generate()
        arrow_time = 0
        threshold = random.randrange(int((1/Arrow.rate)*1000), 50 * 1000)
        self.arrow_tick = pygame.time.get_ticks()
        self.on_question = 1
        self.question_handler = 1

        #Last considerations
        self.setting = 1
        self.mooded = False
        their_moods = ["normal", "high", "low"]
        our_background = self.club_background
        tex = random.randint(1,3)
        bad_background = pygame.image.load("Sprites//glitch_texture" + str(tex) + ".png").convert()
        self.chosens = self.Randomize()
        self.phase = 1

        while self.running == True:
            seconds_left = (self.num_seconds - (pygame.time.get_ticks() - self.start_tick)/1000)
            self.window.blit(bad_background, (0,0))
            self.window.blit(our_background, (0,0))
            Controller.score(self, self.window, (255,255,255))
            Controller.insanity_meter(self, self.window, (255,255,255))

            if self.setting == 1:
                if Controller.insanity > 2:
                    our_background.set_colorkey((0,0,64))

                if self.completions > 0:
                    c = Controller.clock(self, self.window, (240, 93, 93), 10, self.start_tick)
                    if Controller.timeout == True:
                        Club.won = False
                        self.arrow_group.empty()
                        self.landing_arrows.empty()
                        self.running = False
                else:
                    self.font = pygame.font.Font("Sprites//times.ttf", 30)
                    if int((pygame.time.get_ticks()-self.start_tick)/1000) % 2 == 0:
                        self.txt_color = (255,255,255)
                    else:
                        self.txt_color = (240,93,93)
                    self.display_font = self.font.render("Click on a character to start mingling", True, self.txt_color)
                    self.window.blit(self.display_font, (160, 10))
                character_group = pygame.sprite.Group()
                server_group = pygame.sprite.Group()
                
                
                for i in range(-1, -len(self.chosens)+2, -1):
                    if self.chosens[i] != "Sprites//bar_server.png" and self.chosens[i] != "Sprites//c_server.png":
                        sprite = Character(self.chosens[i], self.chosens[i-3])
                        if self.mooded == False:
                            feel_num = random.randint(0, (len(their_moods)-1))
                            the_mood = their_moods[feel_num]
                            del their_moods[feel_num]
                            sprite.mood = the_mood
                        character_group.add(sprite)
                character_group.draw(self.window)
                self.window.blit(self.bar, (200, 300))
                if self.chosens[5] == "Sprites//bar_server.png" or self.chosens[5] == "Sprites//c_server.png":
                    sprite = Character(self.chosens[5], self.chosens[2])
                    sprite.mood = their_moods[0]
                    server_group.add(sprite)
                server_group.draw(self.window)
                self.mooded = True

            elif self.setting == 2:
                image_string = self.clicked_character[:-4] + "_front.png"
                image_surface = pygame.image.load(image_string).convert()
                image_surface.set_colorkey((255,255,255))
                self.window.blit(image_surface, (400, 300))
                self.speech_bubble.set_colorkey((255,255,255))
                self.window.blit(self.speech_bubble, (400, 65))
                self.font = pygame.font.Font("Sprites//times.ttf", 45)
                if (self.num_seconds - (pygame.time.get_ticks() - self.start_tick)/1000) < 0 and self.phase == 1:
                    pygame.init()
                    self.start_tick = pygame.time.get_ticks()
                    self.phase = 2
                    if Club.questions > len(Dialogue.answers):
                        Club.questions = len(Dialogue.answers)
                    ticket = random.choice(list(Dialogue.answers))
                    type = random.randint(1,2)
                if self.phase == 1:
                    arrow_time += (pygame.time.get_ticks() - self.arrow_tick)
                    if arrow_time > threshold:
                        self.spawn()
                        arrow_time = 0
                        threshold = random.randrange(int((1/Arrow.rate)*1000), 50*1000)
                        self.arrow_tick = pygame.time.get_ticks()
                    c = Controller.clock(self, self.window, (93, 240, 93), self.num_seconds, self.start_tick)
                    self.d.draw(self.window, self.font)
                    self.landing_arrows.draw(self.window)
                    self.arrow_group.update()
                    self.arrow_group.draw(self.window)
                    our_word = "|"
                    
                    if time.time() > end_time:
                        for i in range(Club.sayings):
                            if t_list[i] == int(seconds_left) and int(seconds_left) > 0:
                                self.d.generate()
                        end_time = time.time() + 1
                else:
                    self.attention1 = self.font.render("Hey! Are you", True, (0,0,0))
                    self.attention2 = self.font.render("even listening?", True, (0,0,0))
                    c = Controller.clock(self, self.window, (240, 93, 93), 6 * Club.questions, self.start_tick)
                    if Controller.timeout == True:
                        Club.won = False
                        self.landing_arrows.empty()
                        self.arrow_group.empty()
                        self.running = False
                    l = len(our_word)
                    self.window.blit(self.attention1, (465,120))
                    self.window.blit(self.attention2, (465, 170))
                    pygame.draw.rect(self.window, (0,0,64), (5, 64, 400, 504))
                    display_ours = self.font.render(our_word, True, (255,255,255))
                    display_line = self.font.render(">", True, (255,255,255))
                    self.window.blit(display_line, (20, 495))
                    self.window.blit(display_ours, (50, 495))
                    if self.question_handler != self.on_question:
                        del Dialogue.answers[ticket]
                        ticket = random.choice(list(Dialogue.answers))
                        self.question_handler = self.on_question
                        type = random.randint(1,2)
                    self.correct = Dialogue.question(self, self.window, type, self.font, ticket)
            
            if Club.won == False:
                self.arrow_group.empty()
                self.landing_arrows.empty()
                self.running = False
            for event in pygame.event.get():
                Controller.basic_command(self, event)
                if Controller.return_to_root == True:
                    Controller.return_to_root = False
                    if Controller.up_insanity == True:
                        Club.won = False
                    else:
                        Club.won = True
                    self.arrow_group.empty()
                    self.landing_arrows.empty()
                    self.running = False
                # Keybinds
                if event.type == pygame.KEYDOWN:
                    if self.setting == 2:
                        if self.phase == 1:
                            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                                Arrow.check(self, 'left')
                            if event.key == pygame.K_UP or event.key == pygame.K_w:
                                Arrow.check(self, 'up')
                            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                                Arrow.check(self, 'down')
                            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                                Arrow.check(self, 'right')
                        elif self.phase == 2:
                            if event.key == pygame.K_RETURN:
                                if our_word[0:l-1] == self.correct:
                                    self.on_question += 1
                                    our_word = "|"
                                    if self.on_question > Club.questions:
                                        Club.won = True
                                        self.landing_arrows.empty()
                                        self.arrow_group.empty()
                                        self.running = False
                                else:
                                    Club.won = False
                            elif event.key == pygame.K_BACKSPACE:
                                our_word = our_word[0:(l-2)]
                                our_word += "|"
                                print("our_word")
                                print(Dialogue.answers)
                            else:
                                our_key = self.font.render(chr(event.key), True, (255,255,255))
                                our_word = our_word[0:(l-1)]
                                our_word += chr(event.key)
                                our_word += "|"
                            display_ours = self.font.render(our_word, True, (255,255,255))
                            self.window.blit(display_ours, (50, 495))        

                # Mouseclick
                if event.type == pygame.MOUSEBUTTONDOWN and self.setting == 1:
                    clicked_pos = event.pos
                    self.clicked_character = self.check_collision(clicked_pos,character_group,server_group)
                    if self.clicked_character != False:
                        self.play_mood = self.clicked_character.mood
                        self.clicked_character = self.clicked_character.file
                        our_background = self.club_background2
                        pygame.init()
                        self.start_tick = pygame.time.get_ticks()
                        end_time = time.time() + 1
                        self.setting = 2
            
            pygame.display.flip()

    def difficultify(self):
        '''
        Adjusts dialogue appearances and arrow speed/rates according to a difficulty level found in the controller
        Called once every time the Club level is loaded
        '''
        dif = Controller.done_counter[3]
        if dif % 2 == 0 and dif != 0:
            Arrow.speed += .25
        elif dif != 0:
            Arrow.rate += .005
        if dif % 3 == 0 and dif != 0:
            if Club.sayings + 2 <= 20:
                Club.questions += 1
                Club.sayings += 2
        if self.isPrime(dif) == True and dif != 0:
            Arrow.speed += .5
            Arrow.rate += .009

    def isPrime(self, n):
        '''
        Accepts a number
        Returns a boolean that's true if the number was prime, false otherwise
        '''
        for i in range(2,int(n**0.5)+1):
            if n%i==0:
                return False
        return True

    def spawn(self):
        '''
        Given a rate, randomly spawn arrows across four arrow columns
        '''
        sprite = Arrow(1, 0, Arrow.speed)
        self.arrow_group.add(sprite)

    def check_collision(self, point, *groups):
        '''
        Given a clicked point and two sprite groups (characters and server)
        return which item in the group was clicked if anything was clicked
        '''
        for group in groups:
            for g in group:
                if g.rect.collidepoint(point):
                        return g

        return False

    def Randomize(self):
        '''
        Returns a list where the first three items are position tuples randomly picked from five possible options
        and the last three items are sprite strings that match with the position three indexes prior.
        Example: (pos1, pos2, pos3, sprite1, sprite2, sprite3)
        '''
        self.chosens = []
        self.positions = self.rand_positions()
        self.characters = self.rand_characters(self.positions)
        self.chosens = self.positions + self.characters
        return self.chosens

    def rand_positions(self):
        '''
        Removes two of the possible character blit positions leaving the three chosen positions to return
        '''
        self.positions = [(200, 210), (325, 150), (450, 90), (575, 30), (550, 200)]
        for i in range(2):
            self.choice = random.choice(self.positions)
            self.positions.remove(self.choice)
        return self.positions

    def rand_characters(self, positions):
        '''
        Takes positions as parameter and selects characters to return based on those positions
        This is mostly randomized except when the bar_server position is selected and this sprite is confirmed to be a part of the returned list of chosen characters.
        This also reponds to insanity by selecting creepier sprites with a higher chance of them appearing with more insanity.
        '''
        self.characters = ["Sprites//bar_man.png", "Sprites//bar_man2.png", "Sprites//bar_woman.png", "Sprites//bar_woman2.png"]

        if Controller.insanity == 2:
            i = random.randint(0,9)
            if i < 5:
                if i == 1:
                    self.characters.remove("Sprites//bar_man.png")
                    self.characters.append("Sprites//c_man.png")
                elif i == 2:
                    self.characters.remove("Sprites//bar_man2.png")
                    self.characters.append("Sprites//c_man2.png")
                elif i == 3:
                    self.characters.remove("Sprites//bar_woman.png")
                    self.characters.append("Sprites//c_woman.png")
                elif i == 4:
                    self.characters.remove("Sprites//bar_woman2.png")
                    self.characters.append("Sprites//c_woman2.png")

        elif Controller.insanity == 3:
            i = random.randint(0,8)
            if i < 5:
                if i == 1:
                    self.characters.remove("Sprites//bar_man.png")
                    self.characters.append("Sprites//c_man.png")
                elif i == 2:
                    self.characters.remove("Sprites//bar_man2.png")
                    self.characters.append("Sprites//c_man2.png")
                elif i == 3:
                    self.characters.remove("Sprites//bar_woman.png")
                    self.characters.append("Sprites//c_woman.png")
                elif i == 4:
                    self.characters.remove("Sprites//bar_woman2.png")
                    self.characters.append("Sprites//c_woman2.png")
            if "Sprites//mantis.png" not in self.characters:
                i = random.randint(0,3)
                self.characters.remove(self.characters[i])
                self.characters.append("Sprites//mantis.png")

        elif Controller.insanity == 4 or Controller.insanity == 5:
            i = random.randint(0,5)
            self.characters.remove("Sprites//bar_man.png")
            self.characters.append("Sprites//c_man.png")
            self.characters.remove("Sprites//bar_man2.png")
            self.characters.append("Sprites//c_man2.png")
            self.characters.remove("Sprites//bar_woman.png")
            self.characters.append("Sprites//c_woman.png")
            self.characters.remove("Sprites//bar_woman2.png")
            self.characters.append("Sprites/c_woman2.png")
            if "Sprites//mantis.png" not in self.characters:
                i = random.randint(0,3)
                self.characters.remove(self.characters[i])
                self.characters.append("Sprites//mantis.png")

        self.chosen_characters = []
        for i in range(len(self.positions)):
            if self.positions[i] == (550,200):
                if Controller.insanity >= 3:
                    top = 10
                    if Controller.insanity == 4:
                        top = 8
                    if Controller.insanity == 5:
                        top = random.randint(5, 6)
                    i = random.randint(0, top)
                    if i < 5:
                        self.chosen_characters.append("Sprites//c_server.png")
                    else:
                        self.chosen_characters.append("Sprites//bar_server.png")
                else:
                    self.chosen_characters.append("Sprites//bar_server.png")
            else:
                self.choice = random.choice(self.characters)
                self.chosen_characters.append(self.choice)
                self.characters.remove(self.choice)

        return self.chosen_characters

# Club Models
class Character(pygame.sprite.Sprite):
    def __init__(self, file, position):
        self.file = file
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(file).convert_alpha()
        self.image = pygame.transform.scale(self.image, (250, 500))
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.topleft = position
        self.mood = "normal"
# Setting 2 Exclusive
class Dialogue:
    used_list = []
    part_1 = ""
    part_2 = ""
    answers = {}
    def __init__(self):
        pass
    def generate(self):
        p_file = open("Dialogue Files//people.txt", "r")
        a_file = open("Dialogue Files//adjectives.txt", "r")
        the_num = random.randint(1, 20)
        the_num2 = random.randint(1, 20)
        line1 = ""
        line2 = ""
        for i in range(the_num):
            line1 = p_file.readline()[:-1]
        for i in range(the_num2):
            line2 = a_file.readline()[:-1]
        p_file.close()
        a_file.close()
        if line1 in Dialogue.used_list or line2 in Dialogue.used_list:
            self.d.generate()
        Dialogue.part_1 = "My " + line1
        Dialogue.part_2 = "is " + line2
        Dialogue.answers[line1] = line2

    def draw(self, window, font):
        '''
        Accepts the window and font as parameters
        Places both lines generated in the init at specific positions
        Designed to look well in setting 2 of the club level.
        '''
        self.display_line1 = font.render(Dialogue.part_1, True, (0,0,0))
        self.display_line2 = font.render(Dialogue.part_2, True, (0,0,0))    
        window.blit(self.display_line1, (465, 120))
        window.blit(self.display_line2, (465, 170))
    
    def question(self, window, type, font, ticket):
        self.heading = font.render("Question 1/" + str(Club.questions), True, (255,255,255))
        window.blit(self.heading, (20, 74))
        self.key = ticket
        if type == 1:
            self.line1 = font.render("How did I describe", True, (255,255,255))
            self.line2 = font.render("my " + str(self.key), True, (255,255,255))
            window.blit(self.line1, (20, 154))
            window.blit(self.line2, (20, 234))
            return Dialogue.answers[self.key]    
        else:
            self.line1 = font.render("Who was described", True, (255,255,255))
            self.line2 = font.render("as " + str(Dialogue.answers[self.key]), True, (255,255,255))
            window.blit(self.line1, (20, 154))
            window.blit(self.line2, (20, 234))
            return self.key
        
class Arrow(pygame.sprite.Sprite):
    position = (0,0)
    rate = .021
    speed = 1
    def __init__(self, type, h, speed):
        pygame.sprite.Sprite.__init__(self)
        #Where type 1 are flying arrows and 2 are the landing arrows
        if type == 1:
            self.image = pygame.image.load("Sprites//arrow.png").convert_alpha()
            ar_direc = {'left': self.image, 'right': pygame.transform.rotate(self.image, 180), 'up': pygame.transform.rotate(self.image, 270), 'down': pygame.transform.rotate(self.image, 90)}
            self.rect = self.image.get_rect()
            ar_start = {'left': (5, 600), 'up': (105, 600), 'down': (205, 600), 'right': (305, 600)}
            direction = [i for i in ar_start]
            random.shuffle(direction)
            direction=direction[0]
            self.image = ar_direc[direction]
            self.position = ar_start[direction]
            Arrow.position = self.position
            self.rect.topleft = Arrow.position
        elif type == 2:
            if Controller.insanity != 5:
                self.image = pygame.image.load("Sprites//arrow_orange.png").convert()
            else:
                insane_arrow = "Sprites//insane_arrow" + str(random.randint(1,3)) + ".png"
                self.image = pygame.image.load(insane_arrow).convert_alpha()
            ar_direc = {'left': self.image, 'right': pygame.transform.rotate(self.image, 180), 'up': pygame.transform.rotate(self.image, 270), 'down': pygame.transform.rotate(self.image, 90)}
            self.rect = self.image.get_rect()
            ar_end = {'left': (5, 64), 'up': (105, 64), 'down': (205, 64), 'right': (305, 64)}
            self.image = ar_direc[h]
            self.end_position = ar_end[h]
            self.rect.topleft = self.end_position
            self.new_pos = 0

    def update(self):
        self.x = self.position[0]
        self.new_pos = float(self.position[1]) - float(Arrow.speed)
        self.position = (self.x, self.new_pos)
        self.rect.topleft = self.position
        if self.position[1] < 35:
            Dialogue.used_list = []
            Club.won = False
            
    def check(self, pressed):
        y_list = []
        for arrow in self.arrow_group:
            if arrow.new_pos in range(35, 160):
                y_list.append(arrow.new_pos)
                y_list.sort()
                if arrow.new_pos == y_list[0]:
                    if arrow.position[0] == 5 and pressed == 'left':
                        arrow.kill()
                        return
                    if arrow.position[0] == 105 and pressed == 'up':
                        arrow.kill()
                        return 
                    if arrow.position[0] == 205 and pressed == 'down':
                        arrow.kill()
                        return
                    if arrow.position[0] == 305 and pressed == 'right':
                        arrow.kill()
                        return                   
        Club.won = False
