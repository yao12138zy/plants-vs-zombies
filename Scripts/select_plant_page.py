import pygame
import constant


class Select_plant_page():
    def __init__(self,screen):
        self.screen = screen
        self.background = pygame.image.load('../Resource/Background/Background_0.jpg')
        self.selected_panel = pygame.image.load('../Resource/Parts/ChooserBackground.png')
        self.plants_storage = pygame.image.load('../Resource/Parts/PanelBackground.png')
        self.start_button = pygame.image.load('../Resource/Parts/StartButton.png')

        """ load card  
        self.peashooter = pygame.transform.scale(pygame.image.load('../Resource/Cards/card_peashooter.png'),constant.peashooter[0])
        """
        self.all_plants = []
        for plant in constant.plants:
            self.all_plants.append([pygame.transform.scale(pygame.image.load("../Resource/Cards/card_{}.png".format(plant)),constant.card_size), constant.plants[plant], plant])
        self.chosen_plants = []

    def export_selected_plants(self):
        return [self.selected_panel,self.all_plants,self.chosen_plants]

    def display(self,pos):
        self.screen.blit(self.background, (0, 0))
        self.screen.blit(self.selected_panel, constant.selected_plant)
        self.screen.blit(self.plants_storage, constant.all_plant_list)

        """ draw cards
         self.screen.blit(self.peashooter, constant.peashooter[1])
        """

        for plant in self.all_plants:
            self.screen.blit(plant[0],plant[1])

        if self.mouse_on_button(pos):
            self.screen.blit(self.start_button,constant.start_button[1])

    def mouse_on_button(self,pos):
        l = constant.start_button[0][0]
        w = constant.start_button[0][1]
        x = constant.start_button[1][0]
        y = constant.start_button[1][1]
        if pos[0] > x and pos[0] < x + l and pos[1] > y and pos[1] < y + w:
            return True
        else:
            return False

    def select_card(self,pos):
        l = constant.card_size[0]
        w = constant.card_size[1]
        for plant in self.all_plants:
            x = plant[1][0]
            y = plant[1][1]
            if pos[0] > x and pos[0] < x + l and pos[1] > y and pos[1] < y + w:
                index = self.all_plants.index(plant)

                if index in self.chosen_plants:
                    # revert back to original position
                    self.all_plants[index][1] = constant.plants[self.all_plants[index][2]]
                    self.chosen_plants[self.chosen_plants.index(index)] = -1
                else:
                    if len(self.chosen_plants) < 8 or self.chosen_plants.count(-1) != 0:
                        flag = False
                        # move to new position
                        for i in range(len(self.chosen_plants)):
                            if self.chosen_plants[i] == -1:
                                self.all_plants[index][1] = constant.slots_for_chosen[i]
                                self.chosen_plants[i] = index
                                flag = True
                                break
                        if not flag:
                            self.all_plants[index][1] = constant.slots_for_chosen[len(self.chosen_plants)]
                            self.chosen_plants.append(index)

