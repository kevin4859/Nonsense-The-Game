import pygame
import random
from controller import *
pygame.init()

class Maze:
    """
        Maze level Class
    """
    won = False
    x_camera = 0
    y_camera = 0
    def __init__(self):
        """
            Initzation of Maze level
        """
        self.wn = pygame.display.set_mode((800,600), pygame.HWSURFACE)
        self.hedge = pygame.image.load("Sprites//hedge.png")
        self.grass = pygame.image.load("Sprites//grass.png")
        self.hedge_insanity4 = pygame.image.load("Sprites//hedge_insanity4.png")
        self.finish = pygame.image.load("Sprites//finish.png")
        self.boo = pygame.mixer.Sound("Sounds//Demon_Your_Soul_is_mine-BlueMann-1903732045.wav")
        self.insanity2_graphics = pygame.image.load("Sprites//insanity2_maze.png").convert()
        self.player = Player()
        self.active_sprite_list = pygame.sprite.Group()
        self.active_sprite_list.add(self.player)
        self.blacklist = []
        self.finish_list = []
        self.posy = 300-24
        self.posx = 400-24
        self.tile_size = 96
        self.map_height = 25
        self.map_width = 25
        self.move_camera = 0
        self.random_map = random.randint(1,2)
        self.maze_map = self.random_map
        self.eno = 10
        self.test = True
        self.insanity2_pos = -800
        self.insanity5toggle = False
        self.map_list = [["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],
                    ["1","2","2","2","2","1","1","1","1","1","1","1","1","1","1","1","1","1","2","2","2","1","2","1","1"],
                    ["1","2","2","2","2","1","1","1","2","2","2","2","2","2","2","2","2","1","2","1","2","1","2","1","1"],
                    ["1","2","2","2","2","2","2","1","2","1","1","1","1","1","2","1","2","1","2","1","2","1","2","1","1"],
                    ["1","1","1","1","1","1","2","1","2","1","2","2","2","1","2","1","2","1","2","1","2","1","2","1","1"],
                    ["1","2","2","2","2","2","2","1","2","1","2","1","2","1","2","1","2","1","2","1","2","1","2","1","1"],
                    ["1","2","1","1","1","1","1","1","2","1","2","1","2","1","2","1","2","2","2","1","2","1","2","1","1"],
                    ["1","2","1","1","1","1","1","1","1","1","2","1","2","1","2","1","1","1","1","1","2","1","2","1","1"],
                    ["1","2","1","1","1","1","2","2","2","2","2","1","2","2","2","1","2","2","2","2","2","1","2","1","1"],
                    ["1","2","2","2","2","2","2","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","2","1","1"],
                    ["1","1","1","1","1","1","2","2","2","2","2","2","2","2","2","1","2","2","2","1","2","2","2","2","1"],
                    ["1","1","2","2","2","1","2","1","1","1","1","2","2","1","2","1","2","1","2","1","2","1","1","2","1"],
                    ["1","1","2","1","2","1","2","2","2","2","1","1","1","1","2","2","2","1","2","2","2","1","1","2","1"],
                    ["1","1","2","1","2","1","1","1","1","2","2","2","2","1","1","1","1","1","1","1","1","1","1","2","1"],
                    ["1","1","2","1","2","2","2","2","1","1","1","1","2","2","2","2","2","1","2","2","2","2","2","2","1"],
                    ["1","1","2","1","1","1","1","2","2","2","2","1","1","1","1","1","2","1","2","1","1","1","1","1","1"],
                    ["1","1","2","2","2","2","1","1","1","1","2","2","2","2","2","2","2","1","2","2","2","2","2","2","1"],
                    ["1","1","1","1","1","1","1","1","2","1","2","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],
                    ["1","1","2","2","2","2","2","2","2","1","2","1","2","2","2","2","2","1","2","1","2","2","2","1","1"],
                    ["1","1","2","1","1","1","1","1","2","1","2","1","2","1","1","1","2","2","2","1","2","1","2","1","1"],
                    ["1","1","2","2","2","1","2","1","2","2","2","1","2","2","2","1","1","1","1","1","2","1","1","1","1"],
                    ["1","1","2","1","2","1","2","1","1","1","1","1","2","1","2","2","2","2","2","2","2","1","2","2","1"],
                    ["1","1","2","1","2","1","2","1","2","2","2","2","2","1","1","1","1","1","1","1","1","1","2","2","3"],
                    ["1","1","1","1","2","2","2","2","2","1","1","1","2","2","2","2","2","2","2","2","2","2","2","2","1"],
                    ["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"]]

        self.map_list2 = [["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],
                          ["1","2","2","2","2","2","2","2","2","2","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],
                          ["1","2","2","2","2","1","1","1","1","2","2","2","2","2","2","2","2","2","2","2","2","1","1","1","1"],
                          ["1","2","2","2","2","2","2","1","1","2","1","1","1","1","1","1","1","1","1","1","2","1","1","1","1"],
                          ["1","2","2","2","2","1","2","2","2","2","1","2","2","2","2","2","2","2","2","1","2","2","2","2","1"],
                          ["1","1","2","1","2","1","2","2","2","2","1","2","1","1","1","1","1","1","2","1","1","1","1","2","1"],
                          ["1","1","2","1","2","1","1","1","1","1","1","2","1","2","2","2","2","1","2","1","2","2","2","2","1"],
                          ["1","1","2","1","2","2","2","2","2","2","2","2","1","2","1","1","2","1","2","1","2","1","1","1","1"],
                          ["1","1","2","1","2","1","2","2","1","1","1","1","1","2","1","2","2","1","2","1","2","2","2","2","1"],
                          ["1","1","2","1","2","1","2","2","1","2","2","2","1","2","1","2","1","1","2","1","1","1","1","1","1"],
                          ["1","1","2","2","2","1","1","1","1","2","1","2","1","2","1","2","1","2","2","2","2","2","2","2","1"],
                          ["1","1","2","1","2","2","2","1","1","2","1","2","1","2","1","2","1","2","2","2","2","2","2","2","1"],
                          ["1","1","2","1","1","1","2","2","2","2","1","2","1","2","1","2","1","2","1","2","1","2","1","2","1"],
                          ["1","1","2","2","2","1","1","1","1","2","1","2","2","2","1","2","1","2","2","2","1","2","1","2","1"],
                          ["1","1","1","1","2","2","2","2","2","2","1","1","1","1","1","1","1","1","2","1","1","2","1","2","1"],
                          ["1","1","1","2","2","1","1","2","1","1","1","2","2","2","1","2","1","2","2","1","2","2","1","2","1"],
                          ["1","1","1","2","1","1","2","2","1","2","2","2","2","2","1","2","1","1","1","1","2","1","1","2","1"],
                          ["1","2","2","2","1","1","2","2","1","2","1","1","1","1","1","2","2","2","1","2","2","1","1","1","1"],
                          ["1","2","1","1","1","1","1","2","1","2","1","2","2","2","1","2","1","2","1","2","1","1","1","2","1"],
                          ["1","2","1","2","2","2","2","2","1","2","1","2","1","2","1","2","1","2","1","2","2","2","2","2","1"],
                          ["1","2","1","2","1","2","1","1","1","2","1","2","1","2","1","2","1","2","1","1","1","1","2","2","1"],
                          ["1","2","2","2","1","2","2","2","2","2","1","2","1","2","1","2","1","2","1","2","2","2","2","1","1"],
                          ["1","2","1","1","1","2","1","1","1","1","1","2","1","2","1","2","1","2","1","1","1","1","2","2","1"],
                          ["1","2","1","2","2","2","2","2","2","2","2","2","1","2","2","2","1","2","2","2","2","1","1","2","3"],
                          ["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"]]
    # Main loop
    def run(self):
        """
            Main game loop
        """
        if Controller.insanity < 3:
            self.song = pygame.mixer.music.load("Sounds//Tchaikovsky - Valse Sentimentale.wav")
        if Controller.insanity > 2:
            self.song2 = pygame.mixer.music.load("Sounds//Tchaikovsky Distorted.wav")
        pygame.mixer.music.play(loops=-1, start=0.0)
        self.posy = 300-24
        self.posx = 400-24
        self.blacklist = []
        self.finish_list = []
        Maze.y_camera = 0
        Maze.x_camera = 0
        self.start_tick = pygame.time.get_ticks()
        self.running = True
        self.move_camera = 0
        while self.running:
            if Controller.timeout == True:
                self.start_tick = pygame.time.get_ticks()
                Maze.won = False
                self.running = False
            for event in pygame.event.get():
                # Quit button
                Controller.basic_command(self, event)
                if Controller.return_to_root == True:
                    Controller.return_to_root = False
                    if Controller.up_insanity == True:
                        Maze.won = False
                    else:
                        Maze.won = False
                    self.running = False
                if Controller.insanity <= 2:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_w:
                            self.player.go_up()
                            self.move_camera = 1
                        if event.key == pygame.K_a:
                            self.player.go_left()
                            self.move_camera = 2
                        if event.key == pygame.K_s:
                            self.player.go_down()
                            self.move_camera = 3
                        if event.key == pygame.K_d:
                            self.player.go_right()
                            self.move_camera = 4
                        if event.key == pygame.K_UP:
                            self.player.go_up()
                            self.move_camera = 1
                        if event.key == pygame.K_LEFT:
                            self.player.go_left()
                            self.move_camera = 2
                        if event.key == pygame.K_DOWN:
                            self.player.go_down()
                            self.move_camera = 3
                        if event.key == pygame.K_RIGHT:
                            self.player.go_right()
                            self.move_camera = 4
                    elif event.type == pygame.KEYUP:
                        self.move_camera = 0
                        self.player.stop()
                if Controller.insanity >= 3:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_s:
                            self.player.go_up()
                            self.move_camera = 1
                        if event.key == pygame.K_d:
                            self.player.go_left()
                            self.move_camera = 2
                        if event.key == pygame.K_w:
                            self.player.go_down()
                            self.move_camera = 3
                        if event.key == pygame.K_a:
                            self.player.go_right()
                            self.move_camera = 4
                        if event.key == pygame.K_DOWN:
                            self.player.go_up()
                            self.move_camera = 1
                        if event.key == pygame.K_RIGHT:
                            self.player.go_left()
                            self.move_camera = 2
                        if event.key == pygame.K_UP:
                            self.player.go_down()
                            self.move_camera = 3
                        if event.key == pygame.K_LEFT:
                            self.player.go_right()
                            self.move_camera = 4
                    elif event.type == pygame.KEYUP:
                        self.move_camera = 0
                        self.player.stop()
            self.player_rec = pygame.Rect(self.posx,self.posy,48,48)
            if self.move_camera == 1:
                self.posy -= self.eno
                Maze.y_camera -= self.eno
            elif self.move_camera == 2:
                self.posx -= self.eno
                Maze.x_camera -= self.eno
                self.insanity2_pos -= self.eno
            elif self.move_camera == 3:
                self.posy += self.eno
                Maze.y_camera += self.eno
            elif self.move_camera == 4:
                self.posx += self.eno
                Maze.x_camera += self.eno
                self.insanity2_pos += self.eno
            self.wn.fill((0,0,0))

            self.map_build(self.map_list)
            if Controller.insanity == 5 and self.insanity5toggle == False:
                face = insanity5Face()
                self.active_sprite_list.add(face)
                self.insanity5toggle = True
            self.time = int((pygame.time.get_ticks()-self.start_tick)/1000)

            self.active_sprite_list.update()

            self.active_sprite_list.draw(self.wn)
            Controller.insanity_meter(self, self.wn, (255,255,255))
            Controller.score(self, self.wn, (255,255,255))
            for x in self.blacklist:
                if x.colliderect(self.player_rec):
                    self.move_camera = 0
                if x.contains(self.player_rec):
                    Controller.score_current -= 1
                    self.boo.play(loops=1)
                    Controller.insanity += 1
                    if Controller.insanity > 5:
                        Controller.insanity = 5
            for y in self.finish_list:
                if y.colliderect(self.player_rec):
                    Maze.won = True
                    self.running = False
            if Controller.insanity >= 2:
                self.insanity_results(Controller.insanity)
            c = Controller.clock(self, self.wn, (240, 93, 93), 180, self.start_tick)
            pygame.display.flip()

    def map_build(self, map_list):
        """
            Creates map from map_list and blits it based on camera
        """

        if Controller.insanity < 4:
            textures = {"1":self.hedge, "2":self.grass, "3":self.finish}
        elif Controller.insanity >= 3:
            textures = {"1":self.hedge_insanity4, "2":self.grass, "3":self.finish}


        for rows in range(self.map_height):
            for columns in range(self.map_width):
                if textures[map_list[rows][columns]] == self.hedge:
                    self.rec = textures[map_list[rows][columns]].get_rect()
                    self.blacklist += [self.rec.move(columns*self.tile_size, rows*self.tile_size)]
                elif textures[map_list[rows][columns]] == self.hedge_insanity4:
                    self.rec = textures[map_list[rows][columns]].get_rect()
                    self.blacklist += [self.rec.move(columns*self.tile_size, rows*self.tile_size)]
                if textures[map_list[rows][columns]] == self.finish:
                    self.rec1 = textures[map_list[rows][columns]].get_rect()
                    self.finish_list += [self.rec1.move(columns*self.tile_size, rows*self.tile_size)]
                self.wn.blit(textures[map_list[rows][columns]], (columns*self.tile_size - Maze.x_camera, rows*self.tile_size - Maze.y_camera))
    def insanity_results(self, insanity):
        """
            Initzation of Insanity graphics
        """
        insanity_graphics = []
        self.insanity2_graphics.set_colorkey((0,0,0,0))
        if self.insanity2_pos <= -2400:
            self.insanity2_pos = 0
        elif self.insanity2_pos >= 0:
            self.insanity2_pos = -2400
        self.wn.blit(self.insanity2_graphics, (self.insanity2_pos,0))
        if Controller.insanity == 5:
            pass
    def clock(self):
        """
            Initzation of clock
        """
        myfont = pygame.font.Font("Sprites//digital-7.ttf", 55)
        timefont = myfont.render("Time:", True, (240, 93, 93))
        strtimer = str(self.time)
        clocktimer = myfont.render(strtimer, True, (240, 93, 93))
        self.wn.blit(timefont,(300,0))
        self.wn.blit(clocktimer,(400,0))

class Player(pygame.sprite.Sprite):
    """
        Creates player, iterates through player frames
    """

    def __init__(self):

        super().__init__()
        self.change_x = 0
        self.change_y = 0
        self.x_val = 0
        self.y_val = 0

        self.walking_frames_l = []
        self.walking_frames_r = []
        self.walking_frames_d = []
        self.walking_frames_u = []

        self.direction = "D"

        sprite_sheet = SpriteSheet("Sprites//character_walk.png")

        color_key_player = (255,100,178,200)
        image = sprite_sheet.get_image(0, 48, 48, 48, (255,100,178,200))
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(48, 48, 48, 48, (255,100,178,200))
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(96, 48, 48, 48, (255,100,178,200))
        self.walking_frames_l.append(image)

        image = sprite_sheet.get_image(0, 96, 48, 48, (255,100,178,200))
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(48, 96, 48, 48, (255,100,178,200))
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(96, 96, 48, 48, (255,100,178,200))
        self.walking_frames_r.append(image)

        image = sprite_sheet.get_image(0, 0, 48, 48, (255,100,178,200))
        self.walking_frames_d.append(image)
        image = sprite_sheet.get_image(48, 0, 48, 48, (255,100,178,200))
        self.walking_frames_d.append(image)
        image = sprite_sheet.get_image(96, 0, 48, 48, (255,100,178,200))
        self.walking_frames_d.append(image)

        image = sprite_sheet.get_image(0, 144, 48, 48, (255,100,178,200))
        self.walking_frames_u.append(image)
        image = sprite_sheet.get_image(48, 144, 48, 48, (255,100,178,200))
        self.walking_frames_u.append(image)
        image = sprite_sheet.get_image(96, 144, 48, 48, (255,100,178,200))
        self.walking_frames_u.append(image)

        # Set the image the player starts with
        self.image = self.walking_frames_r[0]
        # Set a reference to the image rect.
        self.rect = self.image.get_rect()
        self.rect.move_ip(400-24,300-24)

        self.x_coord = self.rect.left
        self.y_coord = self.rect.top

    def update(self):
        """
            Updates player frames
        """


        # Move left/right
        self.rect.x += self.change_x
        pos = self.rect.x - Maze.x_camera
        if self.direction == "R":
            frame = (pos // 30) % len(self.walking_frames_r)
            self.image = self.walking_frames_r[frame]
        elif self.direction == "L":
            frame = (pos // 30) % len(self.walking_frames_l)
            self.image = self.walking_frames_l[frame]


        # Move up/down
        self.rect.y += self.change_y
        posy = self.rect.y - Maze.y_camera
        if self.direction == "U":
            frame = (posy // 30) % len(self.walking_frames_u)
            self.image = self.walking_frames_u[frame]
        elif self.direction == "D":
            frame = (posy // 30) % len(self.walking_frames_d)
            self.image = self.walking_frames_d[frame]

    # Player-controlled movement:
    def go_left(self):
        self.direction = "L"


    def go_right(self):
        self.direction = "R"

    def go_up(self):
        self.direction = "U"

    def go_down(self):
        self.direction = "D"

    def stop(self):
        self.change_x = 0
class insanity5Face(pygame.sprite.Sprite):
    """
        Creates insanity 5 face effect
    """
    def __init__(self):
        super().__init__()
        sprite_sheet = SpriteSheet("Sprites//creepy.png")
        self.insanity5_frames = []
        color_key_insanity5 = (255,188,200,100)
        for xyx in range(0,321,32):
            image = sprite_sheet.get_image(xyx, 0, 32, 32, color_key_insanity5)
            image = pygame.transform.scale(image, (800, 800))
            self.insanity5_frames.append(image)
        for xy in range(0,321,32):
            image = sprite_sheet.get_image(xy, 32, 32, 32, color_key_insanity5)
            image = pygame.transform.scale(image, (800, 800))
            self.insanity5_frames.append(image)
        for xy1 in range(0,321,32):
            image = sprite_sheet.get_image(xy1, 64, 32, 32, color_key_insanity5)
            image = pygame.transform.scale(image, (800, 800))
            self.insanity5_frames.append(image)
        for xy2 in range(0,321,32):
            image = sprite_sheet.get_image(xy2, 96, 32, 32, color_key_insanity5)
            image = pygame.transform.scale(image, (800, 800))
            self.insanity5_frames.append(image)
        for xy3 in range(0,321,32):
            image = sprite_sheet.get_image(xy3, 128, 32, 32, color_key_insanity5)
            image = pygame.transform.scale(image, (800, 800))
            self.insanity5_frames.append(image)
        for xy4 in range(0,321,32):
            image = sprite_sheet.get_image(xy4, 160, 32, 32, color_key_insanity5)
            image = pygame.transform.scale(image, (800, 800))
            self.insanity5_frames.append(image)
        for xy5 in range(0,321,32):
            image = sprite_sheet.get_image(xy5, 192, 32, 32, color_key_insanity5)
            image = pygame.transform.scale(image, (800, 800))
            self.insanity5_frames.append(image)
        for xy6 in range(0,321,32):
            image = sprite_sheet.get_image(xy6, 224, 32, 32, color_key_insanity5)
            image = pygame.transform.scale(image, (800, 800))
            self.insanity5_frames.append(image)
        for xy7 in range(0, 321,32):
            image = sprite_sheet.get_image(xy7, 256, 32, 32, color_key_insanity5)
            image = pygame.transform.scale(image, (800, 800))
            self.insanity5_frames.append(image)
        for xy8 in range(0,321,32):
            image = sprite_sheet.get_image(xy8, 288, 32, 32, color_key_insanity5)
            image = pygame.transform.scale(image, (800, 800))
            self.insanity5_frames.append(image)
        for xy9 in range(0,321,32):
            image = sprite_sheet.get_image(xy9, 320, 32, 32, color_key_insanity5)
            image = pygame.transform.scale(image, (800, 800))
            self.insanity5_frames.append(image)
        self.index = 0
        self.image = self.insanity5_frames[self.index]
        self.rect = self.image.get_rect()
        self.rect.move_ip(0,-100)
    def update(self):
        """
            Updates insanity 5 face frames 
        """
        self.index += 1
        if self.index >= len(self.insanity5_frames)-1:
            self.index = 120
        self.image = self.insanity5_frames[self.index]
