import pygame
import time
from math import sqrt
pygame.init()


width,height=600,600
dotWidth,dotheight=20,20
win = pygame.display.set_mode((width,height))
caption = pygame.display.set_caption("Following bot")
clock = pygame.time.Clock()
frames = 60

#TARGET
targetX = 200
targetY = 200
n1 = 1
n2 = 1
n3 = 1
n4 = 1
n5 = 1
n6 = 1
n7 = 1
n8 = 1
posX = 100
posY = 100
stop = True
run = True
dot= pygame.Rect(100,100,dotWidth,dotheight)
bot= pygame.Rect(100,100,dotWidth,dotheight)

#EXTRA SPEED
framesTaken = 1
currentLenth = 1
h1 = 1
h2 = 1
speedNeeded = 1
needSpeed = False

#TEXT
text_font = pygame.font.SysFont("Arial",20)
def text(text,font,X,Y):
    img = font.render(text,True,(0,0,0))
    win.blit(img,(X,Y))

while run:

    clock.tick(frames)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_q] and needSpeed == False:
        needSpeed = True
    if keys[pygame.K_w] and needSpeed:
        needSpeed = False
        speedNeeded = 1
            
    win.fill((255,90,90))
    text(":- Ashok Suthar",text_font,10,570)

    #DISTACNCE OF BOT FROM THE TARGET
    lenX = targetX - dot.x
    lenY = targetY - dot.y

    #MOUSE LOCATON FINDER
    mouseX,mouseY = pygame.mouse.get_pos()
    clicked = pygame.mouse.get_pressed()[0]


    #VALUES MODIFIER FOR SHORTED DISTANCE
    if lenX > lenY and lenX > 0 and lenY > 0:
        n1 = lenY/lenX
    else:
        n1 = 1
    if lenX < lenY and lenX > 0 and lenY > 0:
        n2 = lenX/lenY
    else:
        n2 = 1
    if (lenX*-1) < lenY and lenX < 0 and lenY > 0:
        n3 = (lenX*-1)/lenY
    else:
        n3 = 1
    if (lenX*-1) > lenY and lenX < 0 and lenY > 0:
        n4 = lenY/(lenX*-1)
    else:
        n4 = 1
    if (lenX*-1) > (lenY*-1) and lenX < 0 and lenY < 0:
        n5 = (lenY*-1)/(lenX*-1)
    else:
        n5 = 1
    if (lenX*-1) < (lenY*-1) and lenX < 0 and lenY < 0:
        n6 = (lenX*-1)/(lenY*-1)
    else:
        n6 = 1
    if lenX < (lenY*-1) and lenX > 0 and lenY < 0:
        n7 = lenX/(lenY*-1)
    else:
        n7 = 1
    if lenX > (lenY*-1) and lenX > 0 and lenY < 0:
        n8 = (lenY*-1)/lenX
    else:
        n8 = 1
    

    #IGNORE IT
    if clicked:
        targetX = mouseX
        targetY = mouseY
        

    #MAIN DOT WHICH TAKES SHORTER DISTANCE,(Line 71 FOR EXTRA ELEMENT),(YOU CAN IGNORE 'speedNeeded' VARIABLE BECAUSE ITS BY DEFAULT 1)
    if dot.x < targetX:
        if targetX > dot.x +10:
            dot.x += 3*n2*n7*speedNeeded
    
    if dot.x > targetX:
        if targetX < dot.x+20:
            dot.x -= 3*n3*n6*speedNeeded
    
    if dot.y < targetY:
        if targetY > dot.y+10:
            dot.y += 3*n1*n4*speedNeeded
    
    if dot.y > targetY:
        if targetY < dot.y+20:
            dot.y -= 3*n5*n8*speedNeeded

    #SIMPLE BUT LONG DISTANCE TRAVELING BOT'S VALUE
    if bot.x < targetX:
        if targetX > bot.x +10:
            bot.x += 3

    if bot.x > targetX:
        if targetX < bot.x+20:
            bot.x -= 3
    
    if bot.y < targetY:
        if targetY > bot.y+10:
            bot.y += 3
    
    if bot.y > targetY:
        if targetY < bot.y+20:
            bot.y -= 3
    
    #TEXT PLACE
    text(":- White travels shortest distance",text_font,10,10)
    text(":- Black travels simple but long distance",text_font,10,40)


    #DRAWING CUBES
    pygame.draw.rect(win,(255,255,255),dot)
    pygame.draw.rect(win,(0,0,0),bot)
    
    #EXTRA SPEED,('speedNeeded' VARIABLE IS MODIFIES HERE)
    #BY DEFAULT IT'S OFF. PRESS 'q' TO START AND 'w' TO STOP WHILE CODE IS RUNNING. 
    #IT MIGHT NOT WORK SOME TIME
    if needSpeed:
        if clicked:
            if lenX > 0 and lenY > 0 and lenX > lenY:
                framesTaken = lenY/3
                currentLenth = framesTaken * 3*n1*n4
                h1 = sqrt(2*(lenY**2))
                h2 = sqrt((lenY**2) + (currentLenth**2))
                speedNeeded = h1/h2
            elif lenX > 0 and lenY > 0 and lenX < lenY:
                framesTaken = lenX/3
                currentLenth = framesTaken * 3*n2*n7
                h1 = sqrt(2*(lenX**2))
                h2 = sqrt((lenX**2) + (currentLenth**2))
                speedNeeded = h1/h2
            elif lenX < 0 and lenY > 0 and (lenX*-1) > lenY:
                framesTaken = lenY/3
                currentLenth = framesTaken * 3*n1*n4
                h1 = sqrt(2*(lenY**2))
                h2 = sqrt((lenY**2) + (currentLenth**2))
                speedNeeded = h1/h2
            elif lenX < 0 and lenY > 0 and (lenX*-1) < lenY:
                framesTaken = (lenX*-1)/3
                currentLenth = framesTaken * 3*n3*n6
                h1 = sqrt(2*((lenX*-1)**2))
                h2 = sqrt(((lenX*-1)**2) + (currentLenth**2))
                speedNeeded = h1/h2
            elif lenX < 0 and lenY < 0 and (lenX*-1) > (lenY*-1):
                framesTaken = (lenY*-1)/3
                currentLenth = framesTaken * 3*n5*n8
                h1 = sqrt(2*((lenY*-1)**2))
                h2 = sqrt(((lenY*-1)**2) + (currentLenth**2))
                speedNeeded = h1/h2
            elif lenX < 0 and lenY < 0 and (lenX*-1) < (lenY*-1):
                framesTaken = (lenX*-1)/3
                currentLenth = framesTaken * 3*n3*n6
                h1 = sqrt(2*((lenX*-1)**2))
                h2 = sqrt(((lenX*-1)**2) + (currentLenth**2))
                speedNeeded = h1/h2
            elif lenX > 0 and lenY < 0 and lenX > (lenY*-1):
                framesTaken = (lenY*-1)/3
                currentLenth = framesTaken *  3*n5*n8
                h1 = sqrt(2*((lenY*-1)**2))
                h2 = sqrt(((lenY*-1)**2) + (currentLenth**2))
                speedNeeded = h1/h2
            elif lenX > 0 and lenY < 0 and lenX < (lenY*-1):
                framesTaken = lenX/3
                currentLenth = framesTaken * 3*n2*n7
                h1 = sqrt(2*(lenX**2))
                h2 = sqrt((lenX**2) + (currentLenth**2))
                speedNeeded = h1/h2
            else:
                speedNeeded = 1
        
    pygame.display.update()
    # 2 SECONDS DELAY IN STARTING
    if stop:
        time.sleep(2)
        stop = False