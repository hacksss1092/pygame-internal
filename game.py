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
size = width, height = (1000, 1000)
 
# initiallize the app
pygame.init()
 
SCREEN = pygame.display.set_mode(size) # set window size
pygame.display.set_caption("Menu")
BG = pygame.image.load("assets/Background.png")
BG = pygame.transform.scale(BG, size)
 
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
    right_lane = width/2 + road_w/3
    left_lane = width/2 - road_w/4
 
    running = True
 
    pygame.display.set_caption("Car game")  # set window title
    SCREEN.fill((60, 220, 0)) # set background colour
    # apply changes
    pygame.display.update()
 
# load game background
    game_bg = pygame.image.load("assets/road.jpg")
    
    # load player vehicle
    car = pygame.image.load("assets/truck.png")
    #resize image
    car = pygame.transform.scale(car, (200, 200))
    car_loc = car.get_rect()
    car_loc.center = right_lane, height*0.8
 
    # load enemy vehicle
    enemy_cars = []
    for i in range(5):  # add 5 enemy cars
        car2 = pygame.image.load("assets/car orange.jpg")
        car2 = pygame.transform.scale(car2, (200, 200))
        car2 = pygame.transform.rotate(car2, 270)
        car2_loc = car2.get_rect()
        car2_loc.center = left_lane if i % 2 == 0 else right_lane, -400 - i * 2000
        enemy_cars.append((car2, car2_loc))
 
    counter = 0
    current_lane = right_lane  # start in right lane
    
    # game loop
    while running:
        # handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == K_LEFT:
                    current_lane = left_lane
                elif event.key == K_RIGHT:
                    current_lane = right_lane

        counter += 1

        # update player position to current lane
        car_loc.center = current_lane, height*0.8

        # animate enemy vehicles
        for car2, car2_loc in enemy_cars:
            car2_loc[1] += speed
            if car2_loc[1] > height:
                # randomly select lane
                if random.randint(0,1) == 0:
                    car2_loc.center = right_lane, -200
                else:
                    car2_loc.center = left_lane, -200

        # end game logic
        for car2, car2_loc in enemy_cars:
            if car_loc.colliderect(car2_loc):
                print("GAME OVER! YOUR TRASH!")
                running = False
                break

        # draw background
        SCREEN.blit(game_bg, (0, 0))
        
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
        for car2, car2_loc in enemy_cars:
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
        MENU_RECT = MENU_TEXT.get_rect(center=(500, 200))
 
        PLAY_BUTTON = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(500, 350),
                            text_input="PLAY", font=get_font(32), base_color="#d7fcd4", hovering_color="White")
       
        QUIT_BUTTON = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(500, 500),
                            text_input="QUIT", font=get_font(32), base_color="#d7fcd4", hovering_color="White")
 
        SCREEN.blit(MENU_TEXT, MENU_RECT)
 
        for button in [PLAY_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
       
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()
 
        pygame.display.update()

if __name__ == '__main__':
    main_menu()