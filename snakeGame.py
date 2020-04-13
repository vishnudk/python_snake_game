import pygame
import random
import array as arr
import numpy as np
def checkBoundary(x,y):
    if x<=6 or x>=646 or y<=6 or y>=646:
        color=(200, 0, 0 )
        if x<=6:
            x=645
        if x>=660:
            x=7
        if y<=6:
            y=645
        if y>=660:
            y=7
    else:
        color= (192, 192, 192)
    return x,y,color
def kitchen():
    x=random.randint(7,645)
    y=random.randint(7,645)
    return x,y
def didHeAteIt(x,y,food_X,food_Y,tailSize):
    fac=10
    if(x>=food_X-fac and x<=food_X+fac and y>=food_Y-fac and y<=food_Y+fac):
        flag=0
        tailSize=tailSize+1
    else:
        flag=1
    return flag,tailSize
def updateCord(last,x,y):
    speed=5
    if last==0:
        y=y-speed
    elif last==1:
        y=y+speed
    elif last==2:
        x=x-speed
    elif last==3:
        x=x+speed
    return x,y
def updateTail(x,y,boady_x,boady_y,tailSize,last,dir):
    print("yes")
    sep=5
    # print(boady_x[0])
    tmp=tailSize
    # if tmp!=-1:
    #     boady_x.append(boady_x[tmp-1])
    #     boady_y.append(boady_y[tmp-1])
    if tailSize>1:
        for i in range(tailSize-1):
            i1=i+1
            # boady_x[tmp-i1]=boady_x[tmp-i1-1]+sep
            # boady_y[tmp-i1]=boady_y[tmp-i1-1]+sep
            if last==0:
                boady_x[tmp-i1]=boady_x[tmp-i1-1]
                boady_y[tmp-i1]=boady_y[tmp-i1-1]+sep
            elif last==1:
                boady_x[tmp-i1]=boady_x[tmp-i1-1]
                boady_y[tmp-i1]=boady_y[tmp-i1-1]-sep
            elif last==2:
                boady_x[tmp-i1]=boady_x[tmp-i1-1]+sep
                boady_y[tmp-i1]=boady_y[tmp-i1-1]
            elif last==3:
                boady_x[tmp-i1]=boady_x[tmp-i1-1]-sep
                boady_y[tmp-i1]=boady_y[tmp-i1-1]


    if last==0:
        boady_x[0]=x
        boady_y[0]=y+sep
    elif last==1:
        boady_x[0]=x
        boady_y[0]=y-sep
    elif last==2:
        boady_x[0]=x+sep
        boady_y[0]=y
    elif last==3:
        boady_x[0]=x-sep
        boady_y[0]=y
    dir[0]=last
    return boady_x,boady_y,dir


def dispTail(boady_x,boady_y,tailSize):
    for i in range(tailSize):
        pygame.draw.rect(screen, color, pygame.Rect(boady_x[i], boady_y[i], 10, 10))
        # print("boad_x and boady_y",boady_x)


pygame.init()
screen = pygame.display.set_mode((700, 700))
done = False
is_blue = True
x = 30
y = 30
clock = pygame.time.Clock()
flag=0
last=0
boady_x= np.zeros((1000, 1)) 
boady_y= np.zeros((1000, 1)) 
dir=np.zeros((1000,1))
tailSize=0
speed=1
while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                        is_blue = not is_blue
        prev_x=x
        prev_y=y

        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP] and last!=1: 
            y -= speed
            last=0
        if pressed[pygame.K_DOWN] and last!=0: 
            y += speed
            last=1
        if pressed[pygame.K_LEFT] and last!=3: 
            x -= speed
            last=2
        if pressed[pygame.K_RIGHT] and last!=2: 
            x += speed
            last=3
        [x,y]=updateCord(last,x,y)
        screen.fill((0, 0, 0))
        if is_blue: color = (0, 128, 255)
        else: color = (100, 100, 0)
        [x,y,clr]=checkBoundary(x,y)
        if clr==(200, 0, 0 ):
            tailSize=tailSize-1
        pygame.draw.rect(screen, color, pygame.Rect(x, y, 10, 10))
        pygame.draw.rect(screen, clr, pygame.Rect(2,1, 700, 700),10)
        if flag==0:
            [foodX,foodY]=kitchen()
            flag=1
            
        [flag,tailSize]=didHeAteIt(x,y,foodX,foodY,tailSize)
        print("tail size ="+str(tailSize))
        for i in range(tailSize):
            print("==============")
            print(boady_x[i])
        [body_x,boady_y,dir]=updateTail(prev_x,prev_y,boady_x,boady_y,tailSize,last,dir)
        print("tail x="+str(len(boady_x)))
        dispTail(boady_x,boady_y,tailSize)
        pygame.draw.rect(screen,  (0, 255, 0 ), pygame.Rect(foodX, foodY, 10, 10))
        print("X="+str(x))
        print("Y="+str(y))
        pygame.display.flip()
        clock.tick(60)
        # sleep(10)
