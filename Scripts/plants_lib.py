import pygame
import constant
import random
import datetime
import numpy as np
import helper_functions as hf


class Sunshine():
    def __init__(self,x=0,y=0):
        if x == 0:
            self.x = random.randint(constant.sunshine_x_range[0],constant.sunshine_x_range[1])
        else:
            self.x = x

        self.y = y
        self.sunshine = pygame.transform.scale(pygame.image.load('../Resource/Parts/sunshine_new.png'),
                                               constant.sunshine_size)
        self.y_max = random.randint(200,550)
        self.y_max_timestamp = None

    def fall(self):
        if self.y < self.y_max:
            self.y += constant.sunshine_fall_speed
        elif not self.y_max_timestamp:
            self.y_max_timestamp = datetime.datetime.now()

    def get_timestamp(self):
        return self.y_max_timestamp

    def display(self,screen):
        screen.blit(self.sunshine, (self.x, self.y))

    def pick_up(self,pos):  # 当鼠标点到阳光的时候，return True，
        l = constant.sunshine_size[0]
        w = constant.sunshine_size[1]
        if pos[0] > self.x and pos[0] < self.x + l and pos[1] > self.y and pos[1] < self.y + w:
            return True
        else:
            return False


class Sunshine_generator():
    def __init__(self):
        self.sunshines = []
        self.curr_stamp = datetime.datetime.now()
        self.change_number = 0
        self.first = True

    def update(self):
        now = datetime.datetime.now()
        diff = (now - self.curr_stamp).total_seconds()
        interval = 2*random.random() + constant.sunshine_generate_inverval
        for s in self.sunshines:
            s.fall()
            if s.get_timestamp():
                stay_time = (now - s.get_timestamp()).total_seconds()
                if stay_time >= constant.sunshine_vanish_time:
                    self.sunshines.pop(self.sunshines.index(s))

        if self.first:
            if diff >= 5:
                self.sunshines.append(Sunshine())
                self.curr_stamp = now
                self.first = False
        else:
            if diff >= interval:
                self.sunshines.append(Sunshine())
                self.curr_stamp = now

    def display(self,screen):
        self.update()
        for s in self.sunshines:
                s.display(screen)

    def click_events(self,pos):
        c = 0
        for s in self.sunshines:
            if s.pick_up(pos):
                c = c + 1
                index = self.sunshines.index(s)
                self.sunshines.pop(index)

        self.change_number = c

    def get_added_number(self):
        return self.change_number


class Plant():
    def __init__(self,x,y,type):
        self.health = 100
        self.able_attack = True
        self.attack_damage = 10
        self.attack_range = (1,1)
        self.position = [x,y]
        self.curr_stamp = datetime.datetime.now()
        self.image = pygame.transform.scale(pygame.image.load("../Resource/Images/{}.png".format(type)),
                                        constant.plant_image_size)

    def in_range(self,pos_list):
        if not self.able_attack:
            return False
        elif self.attack_damage == 0 or self.attack_range == (0,0):
            return False
        else:
            pass

    def attack(self, zombie_list):
        for zombie in zombie_list:
            zombie.damaged(self.attack_damage)
            self.attack_motion()

    def damaged(self,amount):
        self.health -= amount

    def is_death(self):
        if self.health <= 0:
            return True
        else:
            return False

    def display(self,screen):
        screen.blit(self.image, self.position)


class Sunflower(Plant):
    def __init__(self,x,y):
        super().__init__(x,y,"sunflower")
        self.attack_damage = 0
        self.attack_range = (0,0)
        self.able_attack = False
        self.interval =  random.randint(10,20)
        self.sunlight = None
        self.start = True


    def produce_sunlight(self):
        if not self.sunlight:
            now = datetime.datetime.now()
            diff = (now - self.curr_stamp).total_seconds()
            #print("{} : {}".format(diff,self.interval))
            if diff >= self.interval:
                self.sunlight = Sunshine(self.position[0],self.position[1])
                self.curr_stamp = now
                self.interval = random.randint(constant.sunflower_generate_interval[0], \
                                               constant.sunflower_generate_interval[1])

        else:
            now = datetime.datetime.now()
            if (now - self.curr_stamp).total_seconds() >= 4:
                self.sunlight = None

    def display(self, screen):
        self.produce_sunlight()
        screen.blit(self.image, self.position)
        if self.sunlight:
            self.sunlight.display(screen)

    def click_event(self, pos):
        if self.sunlight:
            if self.sunlight.pick_up(pos):
                self.sunlight = None
                return True
        return False


class Wallnut(Plant):
    def __init__(self,x,y):
        super().__init__(x,y,"wallnut")
        self.health = constant.wallnut_health
        self.attack_damage = 0
        self.attack_range = (0, 0)
        self.able_attack = False


class Cherrybomb(Plant):
    def __init__(self, x, y):
        super().__init__(x, y, "cherrybomb")
        self.attack_damage = constant.cherrybomb_attack_damage
        self.attack_range = (3, 3)  # grid-based for now


class Bullet():
    def __init__(self,x,y,damage):
        self.position = [x,y]
        self.damage = damage
        self.image = pygame.transform.scale(pygame.image.load("../Resource/Images/peashooter_bullet.png"),constant.bullet_size)

    def display(self,screen):
        screen.blit(self.image,self.position)

    def move(self):
        self.position[0] += 3


class Peashooter(Plant):
    def __init__(self, x, y):
        super().__init__(x, y, "peashooter")
        self.bullet_list = []
        self.attack_range = [9,1]

    def attack(self,zombie_list):
        for bullet in self.bullet_list:
            bullet_attack = False
            for zombie in zombie_list:
                if zombie.position[0] - bullet.position[0] >=0 and zombie.position[0] - bullet.position[0] <=5 \
                    and bullet.position[1] - zombie.position[1] == 20:
                    self.bullet_list.remove(bullet)
                    bullet_attack = True
                    zombie.damaged(bullet.damage)
                    break

            if not bullet_attack:
                bullet.move()

        if zombie_list:
            now = datetime.datetime.now()
            if (now - self.curr_stamp).total_seconds() >= 1:
                self.bullet_list.append(Bullet(self.position[0],self.position[1],self.attack_damage))
                self.curr_stamp = now




    def display(self,screen):

        for bullet in self.bullet_list:
            bullet.display(screen)
        screen.blit(self.image, self.position)

class Plants_collector():
    def __init__(self):
        self.plants = []
        self.change_number = 0
        self.map = np.full((5,9),-1)

    def get_row_col_from_pos(self, pos):
        for row in range(len(constant.grass_positions)):
            for col in range(len(constant.grass_positions[0])):
                if hf.inside_rect(constant.grass_positions[row][col], constant.plant_image_size,pos):
                    return [row,col]
        return [-1,-1]

    def is_valid_pos(self,pos):
        [r,c] = self.get_row_col_from_pos(pos)
        if r != -1 and c != -1:
            return [True,r,c]
        else:
            return [False,-1,-1]

    def update(self,zombie_generator):

        for plant in self.plants:
            if plant.is_death():
                self.plants.remove(plant)
                continue

            if plant.able_attack:
                attack_list = []
                x_range = plant.attack_range[0]*77
                y_range = plant.attack_range[1]*95

                for zombie in zombie_generator.zombies:
                    if zombie.position[0] - plant.position[0] >= 0 and zombie.position[0] - plant.position[0] <= x_range \
                        and plant.position[1] - zombie.position[1] == 20:
                        attack_list.append(zombie)
                plant.attack(attack_list)



    def add_plant(self,index,pos):
        [status,r,c] = self.is_valid_pos(pos)
        if status:
            if self.map[r][c] == -1:
                self.map[r][c] = index
                if index == 0:
                    self.plants.append(Sunflower(constant.grass_positions[r][c][0],constant.grass_positions[r][c][1]))
                elif index == 1:
                    self.plants.append(Peashooter(constant.grass_positions[r][c][0],constant.grass_positions[r][c][1]))
                elif index == 2:
                    self.plants.append(Cherrybomb(constant.grass_positions[r][c][0],constant.grass_positions[r][c][1]))
                elif index == 3:
                    self.plants.append(Wallnut(constant.grass_positions[r][c][0], constant.grass_positions[r][c][1]))

    def remove_plant(self,pos):
        [r, c] = self.get_row_col_from_pos(pos)
        if self.map[r][c] != -1:
            self.map[r][c] = -1
            for plant in self.plants:
                    if plant.position[0] == constant.grass_positions[r][c][0] \
                        and plant.position[1] == constant.grass_positions[r][c][1]:
                        index = self.plants.index(plant)
                        self.plants.pop(index)
                        break


    def click_events(self,pos):
        c = 0
        for plant in self.plants:
            if isinstance(plant,Sunflower):
                effect = plant.click_event(pos)
                if effect:
                    c = c + 1
        self.change_number = c

    def get_added_number(self):
        return self.change_number

    def display(self,screen):

        for plant in self.plants:
            plant.display(screen)
        #print("\n")