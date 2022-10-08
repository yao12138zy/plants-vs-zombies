import pygame
import constant


class Welcome_page():

    def __init__(self,screen):

        self.screen = screen
        self.background = pygame.image.load('../Resource/Background/MainMenu.png')
        self.start_button_off = pygame.transform.scale(pygame.image.load('../Resource/Parts/Adventure_1.png'), constant.advanture_button_info[0])
        self.start_button_on = pygame.transform.scale(pygame.image.load('../Resource/Parts/Adventure_0.png'), constant.advanture_button_info[0])
    def display(self,mouse_pos):
        self.screen.blit(self.background, (0, 0))
        result = self.mouse_on_button(mouse_pos)
        if result:
            self.screen.blit(self.start_button_on,constant.advanture_button_info[1])
        else:
            self.screen.blit(self.start_button_off,constant.advanture_button_info[1])

    def mouse_on_button(self,mouse_pos):
        l = constant.advanture_button_info[0][0]
        w = constant.advanture_button_info[0][1]
        x = constant.advanture_button_info[1][0]
        y = constant.advanture_button_info[1][1]
        if mouse_pos[0] > x and mouse_pos[0] < x + l and mouse_pos[1] > y and mouse_pos[1] < y + w:
            return True
        else:
            return False