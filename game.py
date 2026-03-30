'''
Author: BB
Date: Mar 2026
Purpose: A simple car game where the player must avoid oncoming traffic.
The player can move left and right to avoid the cars. The game gets
faster over time, and ends when the player collides with an oncoming car.
'''
 
import pygame, sys
from pygame.locals import *
from button import Button
import random
 
# shape parameters
size = width, height = (800, 800)
 
# initiallize the app
pygame.init()
 
SCREEN = pygame.display.set_mode(size) # set window size
pygame.display.set_caption("Menu")
BG = pygame.image.load("assets/Background.png")
 
def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("assets/font.ttf", size)
 
'''
The game loop. This is where the game logic happens, and where the game is
rendered. The game loop runs until the game is over, and then returns to the main menu.
'''
def play():
    '''A function containing the game loop logic.'''
    # animation parameters
    speed = 1
    road_w = int(width/1.6)
    roadmark_w = int(width/80)
    # location parameters
    right_lane = width/2 + road_w/4
    left_lane = width/2 - road_w/4
 
    running = True
 
    pygame.display.set_caption("Car game")  # set window title
    SCREEN.fill((60, 220, 0)) # set background colour
    # apply changes
    pygame.display.update()
 
    # load player vehicle
    car = pygame.image.load("assets/car.png")
    #resize image
    #car = pygame.transform.scale(car, (250, 250))
    car_loc = car.get_rect()
    car_loc.center = right_lane, height*0.8
 
    # load enemy vehicle
    car2 = pygame.image.load("assets/otherCar.png")
    car2_loc = car2.get_rect()
    car2_loc.center = left_lane, height*0.2
 
    counter = 0
    # game loop
    while running:
        counter += 1
 
        # increase game difficulty overtime
        if counter == 5000:
            speed += 0.15
            counter = 0
            print("level up", speed)
 
        # animate enemy vehicle
        car2_loc[1] += speed
        if car2_loc[1] > height:
            # randomly select lane
            if random.randint(0,1) == 0:
                car2_loc.center = right_lane, -200
            else:
                car2_loc.center = left_lane, -200
 
        # end game logic
        if car_loc[0] == car2_loc[0] and car2_loc[1] > car_loc[1] - 250:
            print("GAME OVER! YOU LOST!")
            break
 
        # event listeners
        for event in pygame.event.get():
            if event.type == QUIT:
                # collapse the app
                running = False
            if event.type == KEYDOWN:
                # move user car to the left
                if event.key in [K_a, K_LEFT]:
                    car_loc = car_loc.move([-int(road_w/2), 0])
                # move user car to the right
                if event.key in [K_d, K_RIGHT]:
                    car_loc = car_loc.move([int(road_w/2), 0])
       
        # draw road
        pygame.draw.rect(
            SCREEN,
            (50, 50, 50),
            (width/2-road_w/2, 0, road_w, height))
        # draw centre line
        pygame.draw.rect(
            SCREEN,
            (255, 240, 60),
            (width/2 - roadmark_w/2, 0, roadmark_w, height))
        # draw left road marking
        pygame.draw.rect(
            SCREEN,
            (255, 255, 255),
            (width/2 - road_w/2 + roadmark_w*2, 0, roadmark_w, height))
        # draw right road marking
        pygame.draw.rect(
            SCREEN,
            (255, 255, 255),
            (width/2 + road_w/2 - roadmark_w*3, 0, roadmark_w, height))
 
        # place car images on the screen
        SCREEN.blit(car, car_loc)
        SCREEN.blit(car2, car2_loc)
        # apply changes
        pygame.display.update()
 
'''
Display a main menu with options to play, view options, or quit the game
'''
def main_menu():
    '''This is a docstring and will display when the user hovers over the function name.'''
   
   
    while True:
        SCREEN.blit(BG, (0, 0))
 
        MENU_MOUSE_POS = pygame.mouse.get_pos()
 
        MENU_TEXT = get_font(64).render("MAIN MENU", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(400, 100))
 
        PLAY_BUTTON = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(400, 250),
                            text_input="PLAY", font=get_font(32), base_color="#d7fcd4", hovering_color="White")
       
        OPTIONS_BUTTON = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(400, 400),
                            text_input="OPTIONS", font=get_font(32), base_color="#d7fcd4", hovering_color="White")
       
        QUIT_BUTTON = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(400, 550),
                            text_input="QUIT", font=get_font(32), base_color="#d7fcd4", hovering_color="White")
 
        SCREEN.blit(MENU_TEXT, MENU_RECT)
 
        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
       
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    print("call options function")
                    #options()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()
 
        pygame.display.update()
 
play()
 
 
# collapse application window
pygame.quit()
sys.exit()

if __name__ == '__main__':
    main_menu()