import pygame
import sys
import random

def ball_animation():
    global ball_speed_x,ball_speed_y,player_score,oppenent_score

    ball.x+=ball_speed_x
    ball.y+=ball_speed_y

    if ball.top<=0 or ball.bottom>=window_height:
        ball_speed_y*=-1
    if ball.left<=0:
        ball_restart()
        oppenent_score+=1
    if ball.right>=window_width:
        ball_restart()
        player_score+=1

def player_animation():
    player.y+=player_speed
    
    if player.top<=0:
        player.top=0
    if player.bottom>=window_height:
        player.bottom=window_height

def oppenent_ai():
    if oppenent.top<ball.y:
        oppenent.top+=oppenent_speed
    if oppenent.top>ball.y:
        oppenent.top-=oppenent_speed

def ball_restart():
    global ball_speed_x,ball_speed_y
    ball.center=(window_width/2,window_height/2)
    ball_speed_x*=random.choice((1,-1))
    ball_speed_y*=random.choice((1,-1))


pygame.init()
clock=pygame.time.Clock()

window_width=700
window_height=600
bg=pygame.image.load("tzKyzs.png")


screen=pygame.display.set_mode((window_width,window_width))
pygame.display.set_caption("Pong Game")




ball=pygame.Rect(window_width/2-15,window_height/2-15,30,30)
player=pygame.Rect(10,window_height/2-70,10,140)
oppenent=pygame.Rect(window_width-20,window_height/2-70,10,140)
bg_color=pygame.Color(255,255,255)
light_grey=(200,200,200)

ball_speed_x=5 * random.choice((1,-1))
ball_speed_y=5 * random.choice((1,-1))
ball_speed_x+=1
ball_speed_y+=1
player_speed=0
oppenent_speed=6

player_score=0
oppenent_score=0
game_font=pygame.font.Font("freesansbold.ttf",25)



while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_DOWN:
                player_speed+=7
            if event.key==pygame.K_UP:
                player_speed-=7
        if event.type==pygame.KEYUP:
            if event.key==pygame.K_DOWN:
                player_speed-=7
            if event.key==pygame.K_UP:
                player_speed+=7

    screen.blit(bg, (0, 0))
    pygame.draw.rect(screen,bg_color,player)
    pygame.draw.rect(screen,bg_color,oppenent)
    pygame.draw.ellipse(screen,bg_color,ball)
    player_text=game_font.render("Player Score:"+str(player_score),False,light_grey)
    screen.blit(player_text,(70,600))
    oppenent_text=game_font.render("Oppenent Score:"+str(oppenent_score),False,light_grey)
    screen.blit(oppenent_text,(400,600))
    

    if ball.colliderect(player) or ball.colliderect(oppenent):
        ball_speed_x*=-1

    

    ball_animation()
    player_animation()
    oppenent_ai()

    pygame.display.flip()
    clock.tick(60)