                                            #    SAI HANOOP GHANAGAM    #
                                          ##  date started : 26-1-2018  ##

import pygame
from math import *
import random
import time


pygame.init()

game_width=900
game_height=600
black=(0,0,0)
white=(255,255,255)
red=(255,0,0)
green=(0,255,0)
blue=(0,0,255)
yellow=(255,255,0)

setwindow = pygame.display.set_mode((game_width,game_height))
pygame.display.set_caption('SHOOT')
clock = pygame.time.Clock() 

global score
score=0
 

class player:
  def __init__(self,img,posx=0,posy=game_width//3):
    self.p=pygame.image.load(img)
    self.width=self.p.get_width()
    self.height=self.p.get_height()
    #pd=pygame.image.load(img_dwn)#
    #pd_width=pd.get_width()
    #pd_height=pd.get_height()
    self.pos_x=posx
    self.pos_y=posy
 
  def scored(self,count):
      style = pygame.font.Font("DroidSans.ttf",20)
      text = style.render("SCORE: "+str(count),True,black)
      setwindow.blit(text,(0,0))  
  
     
  def set(self):  
     self.pos_x=0
     self.pos_y=game_width//3
     self.show()
           
  def show(self):
     #setwindow.fill(white)
     setwindow.blit(self.p,(self.pos_x,self.pos_y))

def unpause():
    global pause
    pygame.mixer.music.unpause()
    pause = False 
  
def paused():
   global pause
   pause = True
   pygame.mixer.music.pause()
   while pause:
     for event in pygame.event.get():
       if event.type == pygame.QUIT:
          pygame.quit()
          quit()
       if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
          pause = False  
     #setwindow.fill(white)
     style = pygame.font.Font("DroidSans.ttf",125)
     text = style.render("PAUSED",True,blue)
     setwindow.blit(text,(170,150))
     
     button("Continue",150,450,140,50,green,yellow,unpause)
     button("QUIT",550,450,100,50,red,yellow,quit)
     pygame.display.update()           
     clock.tick(60) 
     
class bullet:
   def __init__(self):
     self.fire = False
     self.bul=pygame.image.load("bullet.png")
     self.width=self.bul.get_width()
     self.height=self.bul.get_height()
     
   def set(self,player):
      self.bul_x = player.pos_x+player.width
      self.bul_y = player.pos_y+(player.height/3)

   def fireit(self):                  
     if self.fire:   
       setwindow.blit(self.bul,(self.bul_x,self.bul_y))       
       self.bul_x+=5
       if self.bul_x == game_width :
         self.fire=False
      
class monster:
   def __init__(self):
     mon="mon1.png"
     i = random.randrange(0,3)
     if i == 0 : mon="mon3.png" 
     elif i == 1 : mon="mon2.png"
     self.m=pygame.image.load(mon)
     self.width=self.m.get_width()
     self.height=self.m.get_height()
     self.pos_x = game_width - self.width
     self.pos_y = random.randrange(0,game_height-self.height)
     self.speed = 2
           
        
   def move(self,player):
      setwindow.blit(self.m,(self.pos_x,self.pos_y))
      if self.pos_x > player.pos_x + player.width:
        self.pos_x -= self.speed
      else:
        global score
        setwindow.fill(white)
        style = pygame.font.Font("DroidSans.ttf",100)
        text = style.render("!YOU LOOSE!",True,red)        
        text2 = style.render("SCORE:"+str(score),True,blue)
        setwindow.blit(text,(100,game_height/4))
        setwindow.blit(text2,(100,(game_height/4)+150))
        
        score=0        
        pygame.display.update()
        time.sleep(5)        
        intro()
        
   def show(self):
     setwindow.blit(self.m,(self.pos_x,self.pos_y))
     
       
   def shot(self,bullet):
      if bullet.bul_y > self.pos_y and bullet.bul_y < self.pos_y+self.height:
        if bullet.bul_x > self.pos_x and bullet.bul_x < self.pos_x+self.width or bullet.bul_x+bullet.width < self.pos_x+self.width and bullet.bul_x+bullet.width > self.pos_x:
           bullet.bul_x = -200
           bullet.fire = False
           self.pos_x = game_width - self.width
           self.pos_y = random.randrange(0,game_height-self.height)
           self.speed+=0.3
           global score 
           score+=1

def help_screen():
 
 while True:
   for event in pygame.event.get():
       if event.type == pygame.QUIT:
          pygame.quit()
          quit()
   setwindow.fill(white)
   style=pygame.font.Font('DroidSans.ttf',25)
   text = style.render( "-------HELP-------",True,black)
   text2=style.render("->press up/down arrow to move  up/down ",True,black) 
   text3=style.render("->press 'd' key to duck ",True,black)
   text4=style.render("->press space key to shoot ",True,black)   
   text5=style.render("->press 'esc' key to pause ",True,black)   
   text6=style.render("->press 'r' key to reset ",True,black)   
   text7=style.render("By HANOOP GHANAGAM",True,black)   

   setwindow.blit(text,(100,100))
   setwindow.blit(text2,(70,150))
   setwindow.blit(text3,(70,200))
   setwindow.blit(text4,(70,250))
   setwindow.blit(text5,(70,300))
   setwindow.blit(text6,(70,350))   
   setwindow.blit(text7,(200,400))

   button("START",150,450,100,50,green,yellow,gameloop)
   button("QUIT",550,450,100,50,red,yellow,quit)
   
   pygame.display.update()

def button(msg,x,y,w,h,ic,ac,action=None):
     p = pygame.mouse.get_pos()    
     click = pygame.mouse.get_pressed()
     pygame.draw.rect(setwindow, ic, (x,y,w,h))
     
     style = pygame.font.Font("DroidSans.ttf",25)
     strt = style.render(msg,True,black)
     
     setwindow.blit(strt,(x+15,y+10))
         
     
     #print(p)         
     for i in range(x,x+w):
            for j in range(y,y+h):
              if i == p[0] and j == p[1]:
                pygame.draw.rect(setwindow, ac, (x,y,w,h))
                setwindow.blit(strt,(x+15,y+10))
                if click[0] == 1 and action != None:
                   action()

              
             
def intro():
  while True:
     for event in pygame.event.get():
       if event.type == pygame.QUIT:
          pygame.quit()
          quit()
       
     setwindow.fill(white)
     style = pygame.font.Font("DroidSans.ttf",80)
     text = style.render("JUST ANOTHER",True,(150,10,50))
     text1 = style.render("-SHOOT THE MONSTER-",True,(150,100,50))
     text2 = style.render("GAME",True,(150,10,50))
     
     
     setwindow.blit(text,(180,100))
     setwindow.blit(text1,(20,200))
     setwindow.blit(text2,(330,300))
     
     button("START",150,450,100,50,green,yellow,gameloop)
     button("QUIT",550,450,100,50,red,yellow,quit)
     button("HELP",350,450,100,50,blue,yellow,help_screen)
     pygame.display.update()           
     clock.tick(60) 

           
def gameloop():

   
   player1 = player("player1.png")
   player1.set()
   
   mon = []
   for i in range(4):     
     mon.append(monster())
   #mimg=["mon1.png","mon2.png","mon3.png"]
   bul = []
   i=0             
   y_change=0
   duck = False
   while True:
     setwindow.fill(white)
            
     for event in pygame.event.get():
        
        if event.type==pygame.QUIT:
          pygame.quit()
          quit()
        if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_DOWN:     
             y_change=8
          if event.key == pygame.K_UP:
             y_change=-8
          if event.key == pygame.K_r:
            gameloop()   
          if event.key == pygame.K_ESCAPE:
            paused()     
          if event.key == pygame.K_d:
             duck = not duck
             if duck: 
              player1 = player("p1d.png",player1.pos_x,player1.pos_y)   
             else:
              player1 = player("player1.png",player1.pos_x,player1.pos_y)   
             
          if event.key == pygame.K_SPACE:             
              bul.append(bullet())                            
              bul[i].set(player1)
              bul[i].fire=True
              i+=1     
        if event.type == pygame.KEYUP:
          if event.key == pygame.K_DOWN or event.key == pygame.K_UP:     
             y_change=0
         
     player1.pos_y += y_change 
     if player1.pos_y < 0 :  
       player1.pos_y = 0 
     elif player1.pos_y + player1.height > game_height:
       player1.pos_y= game_height - player1.height       
     #mon.append(monster())
     player1.show()
     #mon.show()
     
     #mon.move(player1)
     for m in mon:
      
      m.show()
      m.move(player1)
      
      for b in bul:
        b.fireit()
        m.shot(b)      
     player1.scored(score)  
     pygame.display.update()
     clock.tick(50)
   
intro()
pygame.quit()
quit()
