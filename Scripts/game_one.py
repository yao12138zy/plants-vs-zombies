import pygame
import constant
import plants_lib
import zombie_lib
import helper_functions as hf


class Game_one():
    def __init__(self, screen):
        self.screen = screen
        self.background = pygame.image.load('../Resource/Background/Background_0_game_one.png')

        self.plants = plants_lib.Plants_collector()  # plants
        self.zombies = zombie_lib.Zombie_generator() # zombies

        self.panel = None
        self.all_plants = None
        self.chosen_plants = None
        self.sunlight = 50
        self.text = pygame.font.Font('freesansbold.ttf',constant.font_size)
        self.sunshine = None

        """ 0 --> default ; 1 --> add plants; 2 --> remove plants """
        self.click_purpose = 0
        self.chosen_index = -1

        """ for mouse moving; reset when click  """
        self.target_image = None


    def get_plants_info(self, info):
        self.panel = info[0]
        self.all_plants = info[1]
        self.chosen_plants = info[2]
        self.sunshine = plants_lib.Sunshine_generator()

    def display(self,pos):
        self.update()
        self.screen.blit(self.background, (0, 0))
        if self.panel:
            self.screen.blit(self.panel, constant.panel)
            self.screen.blit(self.text.render(str(self.sunlight),True,(0,0,0)), constant.font_pos)
        for index in self.chosen_plants:
            if index != -1:
                self.screen.blit(self.all_plants[index][0],self.all_plants[index][1])

        self.plants.display(self.screen)
        self.zombies.display(self.screen)
        self.sunshine.display(self.screen)

        if self.target_image:
            shifted_pos = (pos[0] - constant.card_size[0]//2, pos[1] - constant.card_size[1]//2)
            self.screen.blit(self.target_image, shifted_pos)

    def mouse_motion_event(self,pos):  # when mouse is moving --> display image
        if self.click_purpose == 1:
            if not self.target_image:
                plant_name = hf.get_key_from_value(constant.plant_index, self.chosen_index)
                for plant_info in self.all_plants:
                    if plant_info[2] == plant_name:
                        self.target_image = plant_info[0]

    def click_event(self, pos):
        if self.click_purpose == 0:  # this mode allows pick sunlight, click chosen cards, clicks sholve.
            self.sunshine.click_events(pos)
            self.sunlight += self.sunshine.get_added_number()*constant.each_sunshine_worth
            self.plants.click_events(pos)
            self.sunlight += self.plants.get_added_number() * constant.each_sunshine_worth

            for index in self.chosen_plants:
                if hf.inside_rect(self.all_plants[index][1], constant.card_size, pos):
                    self.chosen_index = constant.plant_index[self.all_plants[index][2]]
                    if self.sunlight >= constant.plant_price[self.chosen_index]:
                        self.click_purpose = 1
                    break
        elif self.click_purpose == 1:  # this mode allows add plants only
            [status, r, c] = self.plants.is_valid_pos(pos)
            if status:
                self.sunlight -= constant.plant_price[self.chosen_index]
                self.plants.add_plant(self.chosen_index, pos)
            self.target_image = None
            self.click_purpose = 0
            self.chosen_index = -1


    def update(self):
        self.zombies.update(self.plants)
        self.plants.update(self.zombies)

    def end(self):
        return self.zombies.end()
