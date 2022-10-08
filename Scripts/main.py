import pygame
import welcome_page as wp
import select_plant_page as sp
import game_one as g1

pygame.init()
screen = pygame.display.set_mode((900, 600))
state = True
main_page = wp.Welcome_page(screen)
select_page = sp.Select_plant_page(screen)
game_one_page = g1.Game_one(screen)
font = pygame.font.Font('freesansbold.ttf', 32)
win_text = font.render('You Win', True, (0,255,0), (0,0,128))
lose_text = font.render('You Lose', True, (0,255,0), (0,0,128))
textRect = win_text.get_rect()

page_number = 0
while state:
    pos = pygame.mouse.get_pos()
    if page_number == 0:
        main_page.display(pos)
    elif page_number == 1:
        select_page.display(pos)
    elif page_number == 2:
        game_one_page.display(pos)
        if game_one_page.end() == 1:
            screen.blit(win_text, textRect)
        elif game_one_page.end() == -1:
            screen.blit(lose_text, textRect)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            state = False
        if event.type == pygame.MOUSEBUTTONUP:
            #print(pos)
            if page_number == 0:
                if main_page.mouse_on_button(pos):
                    page_number = 1
            elif page_number == 1:
                if select_page.mouse_on_button(pos):
                    game_one_page.get_plants_info(select_page.export_selected_plants())
                    page_number = 2
                else:
                    select_page.select_card(pos)
            elif page_number == 2:
                game_one_page.click_event(pos)

        if event.type == pygame.MOUSEMOTION:
            if page_number == 1:
                pass
            elif page_number == 2:
                game_one_page.mouse_motion_event(pos)



    pygame.display.update()