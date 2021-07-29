import pygame
import time
import random
pygame.init()
from pygame.locals import*
screen=pygame.display.set_mode((700,700))
pygame.display.set_caption(('Space Invaders!'))
back=pygame.image.load('Space_back.jpeg')
back=pygame.transform.scale(back,(700,700))
class Ship:
    '''
    ATTRIBUTES:
    - List of bullet objects
    - X position
    - Y position
    - Image
    - Rect(Hitbox)
    - W(Turning motion on/off using a key)
    METHODS:
    - init(Takes no arguments, initializes all attributes)
    - draw
        - Loops over list of bullet objects, and draws them
        - Removes them from the list if they leave the window
        - Use w to connect the key press to the coordinates
        - blit the image onto the screen
    '''
    def __init__(self):
    
        self.bullets=[]
        self.x=350
        self.y=500
        self.image=pygame.image.load('Spaceship.png')
        self.image=pygame.transform.rotozoom(self.image,0,0.2)
        
        self.w=0
        
    def draw(self):
        for b in self.bullets:
            b.draw()
            if b.y<=0:
                self.bullets.remove(b)

        self.rect=screen.blit(self.image,(self.x,self.y))
        
        if self.w==1:
            self.x=self.x-10
            
        if self.w==-1:
            self.x=self.x+10
        
        
class Bullet:
    '''
    ATTRIBUTES:
    - X position
    - Y position
    - Image
    - Rect(Hitbox)

    METHODS:
    - init(Takes x as argument, initializes all attributes)
    - draw
        - blit the image onto the screen
        - decreases the y of the bullet 
    '''
    def __init__(self,x,y,u):
        self.x=x+50
        self.u=u
        self.y=y
        self.lazar=pygame.image.load('LazerBullet.png')
        self.lazar=pygame.transform.rotozoom(self.lazar,0,0.25)
    def draw(self):
        self.rect=screen.blit(self.lazar,(self.x, self.y))
        if self.u==2:
            self.y=self.y-10
        if self.u==1:
            self.y=self.y+10
        
        
class Alien:
    '''
    ATTRIBUTES:
    - X position
    - Y position
    - Image
    - Rect(Hitbox)
    -H(Controlling the direction of the motion)
    METHODS:
    - init(Takes no arguments, initializes all attributes)
    - draw
        - blit the image onto the screen
        - h(controls the horizontal movement of the alien)
    '''
    def __init__(self,x):
        self.color=(123,122,121)
        self.bullets=[]
        self.x=x
        self.y=0
        self.h=1
        self.alien=pygame.image.load('Alien.png')
        self.alien=pygame.transform.rotozoom(self.alien,0,0.05)
    def draw(self):
        for b in self.bullets:
            b.draw()
            if b.y>=600:
                self.bullets.remove(b)
        self.rect=screen.blit(self.alien,(self.x,self.y))
        pygame.draw.rect(screen,self.color,self.rect,1)
        if self.h ==1:
            self.x=self.x+5
        if self.x>=650:
            self.h=0
        if self.h==0:
            self.x=self.x-5
        if self.x<=0:
            self.h=1
            
ship=Ship()
alien=Alien(0)
alien2=Alien(300)   
alienlist=[]
alienlist.append(alien)
alienlist.append(alien2)
#for loop in range
clock=pygame.time.Clock()
while True:
    clock.tick(20)
    
            
    
    
    screen.blit(back,(0,0))

    ship.draw()
    #for loop in range(1,3,1):
    for a in alienlist:
        a.draw()
    for a in alienlist:
        for b in ship.bullets:
            if a.rect.colliderect(b.rect):
                alienlist.remove(a)
                ship.bullets.remove(b)
    for a in alienlist:
        for b in a.bullets:
            if a.rect.colliderect(ship.rect):
                a.bullets.remove(b)
                exit()
    if alienlist==[]:
        print('w0w')
        break
            

    if ship.x<=0:
        ship.x=0
    if ship.x>=600:
        ship.x=600

        #time.sleep(1)
    
    
    
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key==K_LEFT:
                ship.w=1
            if event.key==K_RIGHT:
                ship.w=-1
            if event.key==K_SPACE:
                ship.bullets.append(Bullet(ship.x,ship.y,2))
                
                alien.bullets.append(Bullet(alien.x,alien.y,1))
                alien2.bullets.append(Bullet(alien2.x,alien2.y,1))

        if event.type == KEYUP:
            if event.key==K_LEFT:
                ship.w=0
            if event.key==K_RIGHT:
                ship.w=0
                
                
        if event.type == QUIT:
            pygame.quit()
            exit()
    
        

