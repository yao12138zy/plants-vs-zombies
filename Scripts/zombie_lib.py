import pygame
import constant
import random
import datetime



class Zombie():
    def __init__(self, x, y, type):
        self.health = 40
        self.attack_damage = 40
        self.move_speed = 0.1
        self.position = [x, y]
        self.attack_time = datetime.datetime.now()
        self.half_life_image = None
        self.image = pygame.transform.scale(pygame.image.load("../Resource/Images/{}_zombie.png".format(type)),
                                            constant.zombie_image_size)

    def attack(self, plant):
        now = datetime.datetime.now()
        if (self.attack_time - now).total_seconds() >= 0.5:
            plant.damaged(self.attack_damage)
            self.attack_time = now

    def damaged(self, amount):
        self.health -= amount

    def is_death(self):
        if self.health <= 0:
            return True
        else:
            return False

    def move(self):
        self.position[0] -= self.move_speed

    def get_position(self):
        return self.position   # left-top point

    def reach_house(self):
        if self.position[0] <= constant.house_x_pos:
            return True
        else:
            return False

    def display(self,screen):
        screen.blit(self.image,(self.position[0],self.position[1]))


class Basic_zombie(Zombie):
    def __init__(self,x,y):
        super().__init__(x, y, "basic")


class Conehead_zombie(Zombie):
    def __init__(self,x,y):
        super().__init__(x, y, "conehead")
        self.health = constant.conehead_zombie_health
        self.half_life_image = pygame.transform.scale(pygame.image.load("../Resource/Images/basic_zombie.png"),
                                            constant.zombie_image_size)

    def display(self,screen):
        if self.health >= constant.conehead_zombie_health/2:
            screen.blit(self.image, (self.position[0], self.position[1]))
        else:
            screen.blit(self.half_life_image, (self.position[0], self.position[1]))


class Buckethead_zombie(Zombie):
    def __init__(self,x,y):
        super().__init__(x, y, "buckethead")
        self.health = constant.buckethead_zombie_health
        self.half_life_image = pygame.transform.scale(pygame.image.load("../Resource/Images/basic_zombie.png"),
                                                      constant.zombie_image_size)

    def display(self,screen):
        if self.health >= constant.buckethead_zombie_health/2:
            screen.blit(self.image, (self.position[0], self.position[1]))
        else:
            screen.blit(self.half_life_image, (self.position[0], self.position[1]))


class Football_zombie(Zombie):
    def __init__(self,x,y):
        super().__init__(x, y, "football")
        self.health = constant.football_zombie_health
        self.move_speed = constant.football_zombie_move_speed


class Zombie_generator():
    def __init__(self):
        self.zombies = []
        self.curr_stamp = datetime.datetime.now()
        self.interval = None
        self.gen_numbers = 0
        self.end_numbers = 0
        self.map = [[],[],[],[],[]]

    def add_zombie(self,index,row):

        #self.map[row].append()
        if index == 0:
            self.zombies.append(Basic_zombie(constant.zombie_x_start,constant.zombie_y_pos[row]))
        elif index == 1:
            self.zombies.append(Conehead_zombie(constant.zombie_x_start, constant.zombie_y_pos[row]))
        elif index == 2:
            self.zombies.append(Buckethead_zombie(constant.zombie_x_start, constant.zombie_y_pos[row]))
        elif index == 3:
            self.zombies.append(Football_zombie(constant.zombie_x_start, constant.zombie_y_pos[row]))
        else:
            pass


    def display(self,screen):
        for zombie in self.zombies:
            zombie.display(screen)

    def generate_zombies(self):
        if self.gen_numbers >= constant.total_zombies:
            return
        if not self.interval:
            self.interval = random.randint(5,15)
        now = datetime.datetime.now()
        if (now - self.curr_stamp).total_seconds() >= self.interval:
            row = random.randint(0, 4)
            index = random.randint(0, 1)
            self.add_zombie(index,row)
            self.gen_numbers += 1
            self.curr_stamp = now
            self.interval = None

    def end(self):
        for zombie in self.zombies:
            if zombie.position[0] <= 165:
                return -1
        if self.end_numbers >= constant.total_zombies:
            return 1

        return 0

    def update(self,plant_collector):
        #print(self.interval,self.zombies)
        self.generate_zombies()
        for zombie in self.zombies:
            if zombie.is_death():
                self.end_numbers += 1
                self.zombies.remove(zombie)
                continue

            attack = False
            for plant in plant_collector.plants:
                if zombie.position[0] - plant.position[0] >=0 and zombie.position[0] - plant.position[0]<=5 \
                    and plant.position[1] - zombie.position[1] == 20:


                    zombie.attack(plant)
                    attack = True
                    break

            if not attack:
                zombie.move()