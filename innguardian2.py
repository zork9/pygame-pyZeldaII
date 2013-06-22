
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

class InnGuardian2(Gameobject):
    "Inn Guardian 2, left to right"
    def __init__(self,xx,yy):
	Gameobject.__init__(self, xx, yy)
        self.w = 48
        self.h = 48 
	self.stimlibleft = Stateimagelibrary()	
	self.stimlibright = Stateimagelibrary()	
        image = pygame.image.load('./pics/innguardian2.1-48x48.bmp').convert()
        image.set_colorkey((0,0,255)) 
	self.stimlibleft.addpicture(image)	
        image = pygame.image.load('./pics/innguardian2.2-48x48.bmp').convert()
        image.set_colorkey((0,0,255)) 
	self.stimlibleft.addpicture(image)	
        image = pygame.image.load('./pics/innguardian2.3-48x48.bmp').convert()
        image.set_colorkey((0,0,255)) 
	self.stimlibleft.addpicture(image)	

        image = pygame.image.load('./pics/innguardianright2.1-48x48.bmp').convert()
        image.set_colorkey((0,0,255)) 
	self.stimlibright.addpicture(image)	
        image = pygame.image.load('./pics/innguardianright2.2-48x48.bmp').convert()
        image.set_colorkey((0,0,255)) 
	self.stimlibright.addpicture(image)	
        image = pygame.image.load('./pics/innguardianright2.3-48x48.bmp').convert()
        image.set_colorkey((0,0,255)) 
	self.stimlibright.addpicture(image)	

	self.direction = "left"

    def draw(self, screen, room):
	if (self.direction == "left"):
            self.stimlibleft.draw(screen, self.x+room.relativex,self.y+room.relativey)
	elif (self.direction == "right"):
            self.stimlibright.draw(screen, self.x+room.relativex,self.y+room.relativey)
	    
	     
    def update(self,room):
        sleep(.05) # FIX darkkngith sleep
	if (random.randint(0,100) == 0 and self.direction == "left"):
	   self.direction = "right"
	elif (random.randint(0,100) == 0 and self.direction == "right"):
	   self.direction = "left"

	if (not self.collideobjectX(room)): 
	    if (self.direction == "left"):
	        self.x +=2
	        self.direction = "right" 
	    elif (self.direction == "right"):
	        self.x -=2
	        self.direction = "left"


	if (self.direction == "left"):
	        self.x -=1 
	elif (self.direction == "right"):
	        self.x +=1

    def collide(self, room, player):
	if (player.x > self.x+room.relativex  and 
	player.x < self.x+room.relativex+self.w and 
	player.y > self.y+room.relativey and 
	player.y < self.y+room.relativey + self.h):
	    print "collision with Inn Guardian 2!"
	    return 2 
	else:
	    return 0

    def talk(self, screen,font):
        if self.talkcounter == 0:
            return
        
        if self.talkcounter > 4:
                self.talkcounter = 0
                return 
        talkover = 0
        while talkover == 0:
            pygame.display.update()
            if self.talkcounter == 1:
                screen.blit(font.render("This is the Friendly Arm Inn.", 6, (255,255,255)), (10,100))
            elif self.talkcounter == 2:
                screen.blit(font.render("I am a guardian of the inn.", 6, (255,255,255)), (10,100))
            elif self.talkcounter == 3:
                screen.blit(font.render("The Innkeeper is named Yuan.", 6, (255,255,255)), (10,100))
            elif self.talkcounter == 4:
                screen.blit(font.render("Back in the day, he was a good warrior.", 6, (255,255,255)), (10,100))
            for event in pygame.event.get():
                if event.type == QUIT:
                    return
                elif event.type == KEYDOWN:
                    if event.key == K_z:
                        talkover = 1
                        self.talkcounter += 1
                	 
