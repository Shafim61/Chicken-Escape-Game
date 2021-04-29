#My first complete game.
#Chicken escape game......escape from the chicken by pressing "Left and Right arrow keys"
#Enjoy!!!

import pygame
import random

screen_size = [360,600]
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Chicken Escape Game")
pygame.font.init()

background = pygame.image.load("background.png")
user = pygame.image.load("user.png")
chicken = pygame.image.load("chicken.png")

def display_score(Score):
    font = pygame.font.SysFont("Comic Sans Ms",35)
    score_text = "Score: " + str(Score)
    text_image = font.render(score_text,True,(0,255,0))
    screen.blit(text_image,[15,10])
    
def random_chicken():
    return -1*random.randint(100,1500)

chicken_y = [random_chicken(),random_chicken(),random_chicken()]
user_x = 145
Score=0

def crashed(idx):
    global Score
    global keep_alive
    Score = Score-5
    chicken_y[idx]=random_chicken()
    print("Crashed with chicken!!")
    print("Score = ",Score)
    if Score < -50:
        keep_alive = False

def update_chicken_position(idx):
    global Score
    if chicken_y[idx] > 600:
        Score+=10
        print(Score)
        chicken_y[idx]=random_chicken()
    else:
        chicken_y[idx]+=0.9


keep_alive = True

while keep_alive:
    pygame.event.get()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT] and user_x < 290 :
        user_x+=1
    elif keys[pygame.K_LEFT] and user_x > 0 :
        user_x-=1 
    elif keys[pygame.K_q] ==True:
        keep_alive = False 

    screen.blit(background,[0,0])
    screen.blit(chicken,[0,chicken_y[0]])
    screen.blit(chicken,[120,chicken_y[1]])
    screen.blit(chicken,[230,chicken_y[2]])
    screen.blit(user,[user_x,520])

    update_chicken_position(0)
    update_chicken_position(1)
    update_chicken_position(2)

    if chicken_y[0] > 500 and user_x < 75:
        crashed(0)
    if chicken_y[1] > 500 and user_x > 100 and user_x < 200:
        crashed(1)    
    if chicken_y[2] > 500 and user_x > 220 and user_x < 270:
        crashed(2)

    display_score(Score)    
    pygame.display.update()

    #khela hobe khela hobeeeee....



