#----------------------------------------------------------------------------
#               Chapter 10 - Controllers and Graphics (Breakout)
#
#       Created by: PMP
#       Created on: February 6, 2020
#
#-----------------------------------------------------------------------------
import sys
import pygame


# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
PINK = (249, 38, 219)

pygame.init()

#Functions
def draw_block(screen,x,y):
    pygame.draw.rect(screen,GREEN,[x,y,125,20])

def draw_circle(screen,x):
    pygame.draw.circle(screen,WHITE,x,10)

def draw_paddle(screen,mouse_x):
    pygame.draw.rect(screen,PINK,[mouse_x,650,150,15])

def main():
    myfont = pygame.font.SysFont('Comic Sans MS', 30)
    life=1
    xspeed=10
    yspeed=10
    ball_position=[400,200]
    position_list=[[50,50],[195,50],[340,50],[485,50],[630,50],[50,100],[195,100],[340,100],[485,100],[630,100],[50,150],[195,150],[340,150],[485,150],[630,150]]
    score = 0
     
    size = (800, 700)
    screen = pygame.display.set_mode(size)
     
    pygame.display.set_caption("Breakout")
 
    done = False
 
    clock = pygame.time.Clock()
    while not done:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
                pygame.quit()
                sys.exit()

    #-------------------------Game Logic--------------------------------
                
        ball_position[0]+=xspeed
        ball_position[1]+=yspeed

        if ball_position[0] >= 800 or ball_position[0] <= 0:
              xspeed=-xspeed

        if ball_position[1] >= 700 or ball_position[1] <= 0:
              yspeed=-yspeed

        #Mouse
        pos=pygame.mouse.get_pos()
        mouse_x=pos[0]
        mouse_y= pos[1]

        if mouse_x >= 650:
              mouse_x=650

        if mouse_x <= 0:
              mouse_x=0

        pygame.mouse.set_visible(False)

        #Game Life
        if ball_position[1] >= 700:
            life -= 1
            yspeed=-yspeed
              
        if life == 0:    
            done=True
            pygame.quit()
            sys.exit()

        if score == 15:
            done=True
            pygame.quit()
            sys.exit()

        #Paddle Collision
        paddle_x1=mouse_x
        paddle_x2=mouse_x+150
        paddle_y=635
        if paddle_x1 <= ball_position[0] <= paddle_x2 and  ball_position[1]>=paddle_y:
            yspeed=-yspeed


        #Block Collision
         
        for i in range(len(position_list)):
            if position_list[i][0] <= ball_position[0] <= position_list[i][0]+125 and ball_position[1] == position_list[i][1]+20:
                yspeed=-yspeed
                del position_list[i]
                score += 1
                break
    
        
        # ------------- Drawing Code ----------------
     
        screen.fill(BLACK)

        #Drawing Blocks
        for i in range(len(position_list)):
            draw_block(screen,position_list[i][0],position_list[i][1])
        
        #Drawing Paddle
        draw_paddle(screen,mouse_x)

        #Drawing Ball
        draw_circle(screen,ball_position)

        #Score Text
        score_font = myfont.render('Score: '+ str(score), False, WHITE)
        screen.blit(score_font,(650,650))
    
        pygame.display.flip()
 
        clock.tick(60)

    pygame.sys.quit()
    
main()
