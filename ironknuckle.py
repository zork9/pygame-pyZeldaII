
# Copyright (C) Johan Ceuppens 2010
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


import pygame
from pygame.locals import *
from gameobject import *
from stateimagelibrary import *
import random
from time import *
from rng import *

class Ironknuckle(Gameobject):
    "Enemy Knight"
    def __init__(self,xx,yy):
	Gameobject.__init__(self, xx, yy)
        self.w = 48
        self.h = 64

        self.hitpoints = 10

        self.swordimage = pygame.image.load('./pics/ironknuckleredsword1.bmp').convert()
        self.swordimage.set_colorkey((0,0,0)) 
	
        self.swordimage2 = pygame.image.load('./pics/ironknuckleredrightsword1.bmp').convert()
        self.swordimage2.set_colorkey((0,0,0)) 
	
	self.stimlibleft = Stateimagelibrary()	
	self.stimlibright = Stateimagelibrary()	
        image = pygame.image.load('./pics/ironknucklered1-48x64.bmp').convert()
        image.set_colorkey((255,255,255)) 
	self.stimlibleft.addpicture(image)
	image = pygame.image.load('./pics/ironknucklered1-48x64.bmp').convert()
        image.set_colorkey((255,255,255)) 
	self.stimlibleft.addpicture(image)
	image = pygame.image.load('./pics/ironknucklered1-48x64.bmp').convert()
        image.set_colorkey((255,255,255)) 
	self.stimlibleft.addpicture(image)
	image = pygame.image.load('./pics/ironknucklered1-48x64.bmp').convert()
        image.set_colorkey((255,255,255)) 
	self.stimlibleft.addpicture(image)
	image = pygame.image.load('./pics/ironknucklered1-48x64.bmp').convert()
        image.set_colorkey((255,255,255)) 
	self.stimlibleft.addpicture(image)
        image = pygame.image.load('./pics/ironknucklered2-48x64.bmp').convert()
        image.set_colorkey((255,255,255)) 
	self.stimlibleft.addpicture(image)
	image = pygame.image.load('./pics/ironknucklered2-48x64.bmp').convert()
        image.set_colorkey((255,255,255)) 
	self.stimlibleft.addpicture(image)
	image = pygame.image.load('./pics/ironknucklered2-48x64.bmp').convert()
        image.set_colorkey((255,255,255)) 
	self.stimlibleft.addpicture(image)
	image = pygame.image.load('./pics/ironknucklered2-48x64.bmp').convert()
        image.set_colorkey((255,255,255)) 
	self.stimlibleft.addpicture(image)
	image = pygame.image.load('./pics/ironknucklered2-48x64.bmp').convert()
        image.set_colorkey((255,255,255)) 
	self.stimlibleft.addpicture(image)

	image = pygame.image.load('./pics/ironknuckleredright1-48x64.bmp').convert()
        image.set_colorkey((255,255,255)) 
	self.stimlibright.addpicture(image)
	image = pygame.image.load('./pics/ironknuckleredright1-48x64.bmp').convert()
        image.set_colorkey((255,255,255)) 
	self.stimlibright.addpicture(image)
	image = pygame.image.load('./pics/ironknuckleredright1-48x64.bmp').convert()
        image.set_colorkey((255,255,255)) 
	self.stimlibright.addpicture(image)
	image = pygame.image.load('./pics/ironknuckleredright1-48x64.bmp').convert()
        image.set_colorkey((255,255,255)) 
	self.stimlibright.addpicture(image)
	image = pygame.image.load('./pics/ironknuckleredright1-48x64.bmp').convert()
        image.set_colorkey((255,255,255)) 
	self.stimlibright.addpicture(image)
        image = pygame.image.load('./pics/ironknuckleredright2-48x64.bmp').convert()
        image.set_colorkey((255,255,255)) 
	self.stimlibright.addpicture(image)
	image = pygame.image.load('./pics/ironknuckleredright2-48x64.bmp').convert()
        image.set_colorkey((255,255,255)) 
	self.stimlibright.addpicture(image)
	image = pygame.image.load('./pics/ironknuckleredright2-48x64.bmp').convert()
        image.set_colorkey((255,255,255)) 
	self.stimlibright.addpicture(image)
	image = pygame.image.load('./pics/ironknuckleredright2-48x64.bmp').convert()
        image.set_colorkey((255,255,255)) 
	self.stimlibright.addpicture(image)
	image = pygame.image.load('./pics/ironknuckleredright2-48x64.bmp').convert()
        image.set_colorkey((255,255,255)) 
	self.stimlibright.addpicture(image)

        self.stimlibleftfight = Stateimagelibrary()	
	self.stimlibrightfight = Stateimagelibrary()	
	image = pygame.image.load('./pics/ironknuckleredright2-48x64.bmp').convert()
        image.set_colorkey((255,255,255)) 
	self.stimlibrightfight.addpicture(image)
	image = pygame.image.load('./pics/ironknucklered2-48x64.bmp').convert()
        image.set_colorkey((255,255,255)) 
	self.stimlibleftfight.addpicture(image)

	self.stimlibleftfightlow = Stateimagelibrary()	
	self.stimlibrightfightlow = Stateimagelibrary()	
	image = pygame.image.load('./pics/ironknuckleredright2-48x64.bmp').convert()
        image.set_colorkey((255,255,255)) 
	self.stimlibrightfightlow.addpicture(image)
	image = pygame.image.load('./pics/ironknucklered2-48x64.bmp').convert()
        image.set_colorkey((255,255,255)) 
	self.stimlibleftfightlow.addpicture(image)

        self.battlemode = 1

	self.direction = "left"
        self.prevdirection = "left"

        self.CLOSEUPW = 58
        self.counter = 0
        self.fightlow = 0

    def draw(self, screen, room):
        #FIXME - or + room.relativex
	if (self.direction == "left"):
            self.stimlibleft.draw(screen, self.x+room.relativex,self.y+room.relativey)
	elif (self.direction == "right"):
            self.stimlibright.draw(screen, self.x+room.relativex,self.y+room.relativey)
        elif self.direction == "stop":
##            r = randint(0,2)
##            if r == 0:
            if self.fightlow == 0:
                if self.prevdirection == "left":
                    self.stimlibleftfight.drawstatic(screen, self.x+room.relativex,self.y+room.relativey,0)
                    if self.counter > 0:
                        self.counter -= 1
                        screen.blit(self.swordimage,(self.x+room.relativex-self.w+5,self.y+room.relativey))
                elif self.prevdirection == "right":
                    self.stimlibrightfight.drawstatic(screen, self.x+room.relativex,self.y+room.relativey,0)
                    if self.counter > 0:
                        self.counter -= 1
                        screen.blit(self.swordimage2,(self.x+room.relativex-self.w+5,self.y+room.relativey))
                else:
                    if self.counter > 0:
                        self.counter -= 1
                        screen.blit(self.swordimage2,(self.x+room.relativex-self.w+5,self.y+room.relativey))

            elif self.fightlow == 1:
                if self.prevdirection == "left":
                    self.stimlibleftfightlow.drawstatic(screen, self.x+room.relativex,self.y+room.relativey,0)
                    if self.counter > 0:
                        self.counter -= 1
                        screen.blit(self.swordimage,(self.x+room.relativex-self.w+5,self.y+room.relativey))
                elif self.prevdirection == "right":
                    self.stimlibrightfightlow.drawstatic(screen, self.x+room.relativex,self.y+room.relativey,0)
                    if self.counter > 0:
                        self.counter -= 1
                        screen.blit(self.swordimage2,(self.x+room.relativex-self.w+5,self.y+room.relativey+self.h/2))
                else:
                    if self.counter > 0:
                        self.counter -= 1
                        screen.blit(self.swordimage2,(self.x+room.relativex-self.w+5,self.y+room.relativey+self.h/2))

            else:
                #print 'UNKOWN code switch'
                if self.prevdirection == "left":
                    self.stimlibleft.drawstatic(screen, self.x+room.relativex,self.y+room.relativey,0)
                else:
                    self.stimlibright.drawstatic(screen, self.x+room.relativex,self.y+room.relativey,0)
	
    def update(self,room,player):
        # combat for ironknuckle i.e. move in and fight like a knight
        if not self.battlemode:
            if (random.randint(0,100) == 0 and self.direction == "left"):
                self.prevdirection = "left"
                self.direction = "right"
            elif (random.randint(0,100) == 0 and self.direction == "right"):
                self.prevdirection = "right"
                self.direction = "left"
        # seek player
        else:
            if abs(player.x - self.x-room.relativex) < self.CLOSEUPW:
                self.prevdirection = self.direction
                self.direction = "stop"
            elif player.x+48 < self.x:
                self.direction = "left"
            elif player.x-48 > self.x:
                self.direction = "right"

        

	if (not self.collideobjectX(room)): 
	    if (self.direction == "left"):
	        self.x +=2
	        self.direction = "right" 
	    elif (self.direction == "right"):
	        self.x -=2
	        self.direction = "left"
	        
        if (self.direction == "stop"):
            #FIXME          
            #self.fight(room,player,0)
            if player.duck:
                if randint(0,10) == 0:
                    self.fightlow = 1
                    player.hitwithenemyweapon(RNG().rollironknuckle())
                    self.counter = 1000
                else:
                    self.fightlow = -1
            else:
                if randint(0,10) == 0:
                    # Hit random high or low
                    if randint(0,2) == 0:
                        self.fightlow = 0
                    else:
                        self.fightlow = 1
                    self.counter = 1000
                    player.hitwithenemyweapon(RNG().rollironknuckle())
                else:
                    self.fightlow = -1


	if (self.direction == "left"):
	        self.x -=1 
	elif (self.direction == "right"):
	        self.x +=1

    def collide(self, room, player):        
	if (player.x > self.x-room.relativex-self.w  and 
	player.x < self.x-room.relativex+self.w+self.w and 
	player.y > self.y-room.relativey-self.h and 
	player.y < self.y-room.relativey + self.h +self.h):
	    print "collision with Ironknuckle Knight!"
	    if player.hit():
		return 1 
	    else:
	    	return 2 
	else:
	    return 0

		 
    def collidewithsword(self, room, player):
        print 'Ironknuckle x=%d y=%d player x=%d y=%d' % (self.x,self.y,player.x-room.relativex,player.y-room.relativey)
	if (player.x-room.relativex > self.x  and 
	player.x-room.relativex < self.x+self.w and 
	player.y-room.relativey > self.y and 
	player.y-room.relativey < self.y + self.h):
	    print "collision with Sword Ironknuckle!"
	    return 1 
	else:
	    return 0


    def fight(self,room,player,keydown):
        self.fightcounter = 1
        # FIXME FIGHT!
        
        o = player.collidewithenemyweapon(room,self)
        
        if o:
            print 'FIGHT!'
            if keydown != 2:
            # FIXME roll
                player.hitwithenemyweapon(RNG().rollgoblinknife())
