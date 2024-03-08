#IMPORTANT!!
#Press "g" to hide Lines and "h" to reveal again.
#Press "Up","Down","Left","Right" to change the speed of Pendulam

import pygame as py
import math
py.init()

#WINDOW SETUP
FPS = 25
clock =  py.time.Clock()
win = py.display.set_mode((500,350))
caption = py.display.set_caption("Pendulam motion by Pythagorous THM")

#PENDULAM VALUES
length=p=100
speed = 4
x=0
Pendulam_motion = 100 #(0 : 100)

#TEXT
text_font = py.font.SysFont("Arial",20)
def text(text,font,X,Y):
    img = font.render(text,True,(0,0,0))
    win.blit(img,(X,Y))

#PYTHAGOROUS THM
def pythogorus(P,B):
    H = float(math.sqrt((P**2)-((B*Pendulam_motion)**2)))
    return H

#EXTRA ELEMENT
color_line = True
while True:
    #FPS
    clock.tick(FPS)
    
    #BASE VALUE
    b=math.sin(math.radians(x))
    
    #SPEED OF PENDULAM
    x += speed

    #PYTHAGOROUS THM VALUE
    h=pythogorus(p,b)

    #EXTRA VALUES
    ball = (b*Pendulam_motion)+250,h+100

    #INDICATION LINE   
    y_height = h + 100
    Z = 250,h+100

    for event in py.event.get():
        if event.type == py.QUIT:
            py.quit()
            break

    keys = py.key.get_pressed()
    if keys[py.K_UP] and Pendulam_motion < 100:
        Pendulam_motion += 1
    if keys[py.K_DOWN] and Pendulam_motion > 0:
        Pendulam_motion -= 1
    if keys[py.K_LEFT] and speed > 0:
        speed -= 0.1
    if keys[py.K_RIGHT] and speed < 7:
        speed += 0.1
    if keys[py.K_g] and color_line:
        color_line = False
    if keys[py.K_h] and color_line == False:
        color_line = True


    #BG COLOUR
    win.fill((255,255,255))

    #DRAWING
    #ROPE
    py.draw.line(win,(100,100,100),(250,100),ball, width=4)
    #GREEN AND BLUE INDICATIN LINE
    if color_line:
        py.draw.line(win,(50,255,50),(250,100),Z, width=3)
        py.draw.line(win,(50,55,255),(250,y_height),ball, width=3)
    #MAIN POINT
    py.draw.line(win,(0,0,0),(100,100),(400,100), width=2)
    py.draw.circle(win,(0,0,0),(250,100),5, width=0)
    #BALL
    py.draw.circle(win,(255,100,100),ball,10)
    py.draw.circle(win,(10,10,10),ball,10,width=4)

    #TEXT
    X_val =  int((b*Pendulam_motion))
    
    py.draw.circle(win,(50,50,255),(20,225),10)
    text(str(X_val),text_font,40,215)
    py.draw.circle(win,(50,255,50),(20,250),10)
    text("(0,0)",text_font,253,74)
    text(str(int(h)),text_font,40,240)
    text("Ball position =",text_font,10,275)
    text("-By Ashok Suthar",text_font,10,10)
    text("Ball Speed  Press(UP,DOWN) =",text_font,10,300)
    text("Video Speed  Press(LEFT,RIGHT) =",text_font,10,325)
    text(str(X_val),text_font,118,275)
    text(",",text_font,140,275)
    text(str(int(h)),text_font,145,275)
    text(str(Pendulam_motion),text_font,245,300)
    text(str(int(speed)),text_font,275,325)

    py.display.update()
