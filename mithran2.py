
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

class Mithran2(Gameobject):
    "BlackKnight"
    def __init__(self,xx,yy):
	Gameobject.__init__(self, xx, yy)
        self.w = 48
        self.h = 48 
	self.stimlibdown = Stateimagelibrary()	
	self.stimlibup = Stateimagelibrary()	
        image = pygame.image.load('./pics/mithran1-48x48.bmp').convert()
        image.set_colorkey((0,0,0)) 
	self.stimlibdown.addpicture(image)	
        image = pygame.image.load('./pics/mithran1-48x48.bmp').convert()
        image.set_colorkey((0,0,0)) 
	self.stimlibdown.addpicture(image)
	image = pygame.image.load('./pics/mithran1-48x48.bmp').convert()
        image.set_colorkey((0,0,0)) 
	self.stimlibdown.addpicture(image)
	image = pygame.image.load('./pics/mithran1-48x48.bmp').convert()
        image.set_colorkey((0,0,0)) 
	self.stimlibdown.addpicture(image)

	image = pygame.image.load('./pics/mithran2-48x48.bmp').convert()
        image.set_colorkey((0,0,0)) 
	self.stimlibdown.addpicture(image)	
        image = pygame.image.load('./pics/mithran2-48x48.bmp').convert()
        image.set_colorkey((0,0,0)) 
	self.stimlibdown.addpicture(image)
	image = pygame.image.load('./pics/mithran2-48x48.bmp').convert()
        image.set_colorkey((0,0,0)) 
	self.stimlibdown.addpicture(image)
	image = pygame.image.load('./pics/mithran2-48x48.bmp').convert()
        image.set_colorkey((0,0,0)) 
	self.stimlibdown.addpicture(image)

        image = pygame.image.load('./pics/mithran3-48x48.bmp').convert()
        image.set_colorkey((0,0,0)) 
	self.stimlibdown.addpicture(image)	
        image = pygame.image.load('./pics/mithran3-48x48.bmp').convert()
        image.set_colorkey((0,0,0)) 
	self.stimlibdown.addpicture(image)
	image = pygame.image.load('./pics/mithran3-48x48.bmp').convert()
        image.set_colorkey((0,0,0)) 
	self.stimlibdown.addpicture(image)
	image = pygame.image.load('./pics/mithran3-48x48.bmp').convert()
        image.set_colorkey((0,0,0)) 
	self.stimlibdown.addpicture(image)

        image = pygame.image.load('./pics/mithran2-48x48.bmp').convert()
        image.set_colorkey((0,0,0)) 
	self.stimlibdown.addpicture(image)	
        image = pygame.image.load('./pics/mithran2-48x48.bmp').convert()
        image.set_colorkey((0,0,0)) 
	self.stimlibdown.addpicture(image)
	image = pygame.image.load('./pics/mithran2-48x48.bmp').convert()
        image.set_colorkey((0,0,0)) 
	self.stimlibdown.addpicture(image)
	image = pygame.image.load('./pics/mithran2-48x48.bmp').convert()
        image.set_colorkey((0,0,0)) 
	self.stimlibdown.addpicture(image)

        image = pygame.image.load('./pics/mithranup1-48x48.bmp').convert()
        image.set_colorkey((0,0,0)) 
	self.stimlibup.addpicture(image)
	image = pygame.image.load('./pics/mithranup1-48x48.bmp').convert()
        image.set_colorkey((0,0,0)) 
	self.stimlibup.addpicture(image)
	image = pygame.image.load('./pics/mithranup1-48x48.bmp').convert()
        image.set_colorkey((0,0,0)) 
	self.stimlibup.addpicture(image)
	image = pygame.image.load('./pics/mithranup1-48x48.bmp').convert()
        image.set_colorkey((0,0,0)) 
	self.stimlibup.addpicture(image)

	image = pygame.image.load('./pics/mithranup2-48x48.bmp').convert()
        image.set_colorkey((0,0,0)) 
	self.stimlibup.addpicture(image)
	image = pygame.image.load('./pics/mithranup2-48x48.bmp').convert()
        image.set_colorkey((0,0,0)) 
	self.stimlibup.addpicture(image)
	image = pygame.image.load('./pics/mithranup2-48x48.bmp').convert()
        image.set_colorkey((0,0,0)) 
	self.stimlibup.addpicture(image)
	image = pygame.image.load('./pics/mithranup2-48x48.bmp').convert()
        image.set_colorkey((0,0,0)) 
	self.stimlibup.addpicture(image)

	image = pygame.image.load('./pics/mithranup3-48x48.bmp').convert()
        image.set_colorkey((0,0,0)) 
	self.stimlibup.addpicture(image)
	image = pygame.image.load('./pics/mithranup3-48x48.bmp').convert()
        image.set_colorkey((0,0,0)) 
	self.stimlibup.addpicture(image)
	image = pygame.image.load('./pics/mithranup3-48x48.bmp').convert()
        image.set_colorkey((0,0,0)) 
	self.stimlibup.addpicture(image)
	image = pygame.image.load('./pics/mithranup3-48x48.bmp').convert()
        image.set_colorkey((0,0,0)) 
	self.stimlibup.addpicture(image)
        	
        image = pygame.image.load('./pics/mithranup2-48x48.bmp').convert()
        image.set_colorkey((0,0,0)) 
	self.stimlibup.addpicture(image)
	image = pygame.image.load('./pics/mithranup2-48x48.bmp').convert()
        image.set_colorkey((0,0,0)) 
	self.stimlibup.addpicture(image)
	image = pygame.image.load('./pics/mithranup2-48x48.bmp').convert()
        image.set_colorkey((0,0,0)) 
	self.stimlibup.addpicture(image)
	image = pygame.image.load('./pics/mithranup2-48x48.bmp').convert()
        image.set_colorkey((0,0,0)) 
	self.stimlibup.addpicture(image)

	self.talkcounter = 0
	self.direction = "down"

    def draw(self, screen, room):
	if (self.direction == "down"):
            self.stimlibdown.draw(screen, self.x+room.relativex,self.y+room.relativey)
	elif (self.direction == "up"):
            self.stimlibup.draw(screen, self.x+room.relativex,self.y+room.relativey)
	    
	     
    def update(self,room):
        sleep(.04) # FIX mithran sleep
	
	if (not self.collideobjectY(room)): 
	    if (self.direction == "down"):
	        self.y -=2
	        self.direction = "up" 
	    elif (self.direction == "up"):
	        self.y +=2
	        self.direction = "down"

	if (self.direction == "up"):
	        self.y -=1 
	elif (self.direction == "down"):
	        self.y +=1

    def collide(self, room, player):
        
	if (player.x > self.x+room.relativex  and 
	player.x < self.x+room.relativex+self.w and 
	player.y > self.y+room.relativey and 
	player.y < self.y+room.relativey + self.h):
	    print "collision with Mithran!"
	    return 2 
	else:
	    return 0 ## for game self.talker

		 
    def talk(self, screen,font):
        if self.talkcounter == 0:
            return
        
        if self.talkcounter > 2:
                self.talkcounter = 0
                return 
        talkover = 0
        while talkover == 0:
            pygame.display.update()
            if self.talkcounter == 1:
                screen.blit(font.render("Welcome.", 8, (255,255,255)), (10,100))
            elif self.talkcounter == 2:
                screen.blit(font.render("Anything is good.", 8, (255,255,255)), (10,100))
            for event in pygame.event.get():
                if event.type == QUIT:
                    return
                elif event.type == KEYDOWN:
                    if event.key == K_z:
                        talkover = 1
                        self.talkcounter += 1
                
