
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

class Goblin1(Gameobject):
    "Goblin"
    def __init__(self,xx,yy):
	Gameobject.__init__(self, xx, yy)
        self.w = 48
        self.h = 48

        self.hitpoints = 3
        
	self.stimlibdown = Stateimagelibrary()	
	self.stimlibup = Stateimagelibrary()	
        image = pygame.image.load('./pics/goblin1-48x48.bmp').convert()
        image.set_colorkey((0,0,0)) 
	self.stimlibdown.addpicture(image)	
        image = pygame.image.load('./pics/goblin1-48x48.bmp').convert()
        image.set_colorkey((0,0,0)) 
	self.stimlibdown.addpicture(image)
	image = pygame.image.load('./pics/goblin1-48x48.bmp').convert()
        image.set_colorkey((0,0,0)) 
	self.stimlibdown.addpicture(image)
	image = pygame.image.load('./pics/goblin1-48x48.bmp').convert()
        image.set_colorkey((0,0,0)) 
	self.stimlibdown.addpicture(image)

	image = pygame.image.load('./pics/goblin2-48x48.bmp').convert()
        image.set_colorkey((0,0,0)) 
	self.stimlibdown.addpicture(image)	
        image = pygame.image.load('./pics/goblin2-48x48.bmp').convert()
        image.set_colorkey((0,0,0)) 
	self.stimlibdown.addpicture(image)
	image = pygame.image.load('./pics/goblin2-48x48.bmp').convert()
        image.set_colorkey((0,0,0)) 
	self.stimlibdown.addpicture(image)
	image = pygame.image.load('./pics/goblin2-48x48.bmp').convert()
        image.set_colorkey((0,0,0)) 
	self.stimlibdown.addpicture(image)

        image = pygame.image.load('./pics/goblin1-48x48.bmp').convert()
        image.set_colorkey((0,0,0)) 
	self.stimlibdown.addpicture(image)	
        image = pygame.image.load('./pics/goblin1-48x48.bmp').convert()
        image.set_colorkey((0,0,0)) 
	self.stimlibdown.addpicture(image)
	image = pygame.image.load('./pics/goblin1-48x48.bmp').convert()
        image.set_colorkey((0,0,0)) 
	self.stimlibdown.addpicture(image)
	image = pygame.image.load('./pics/goblin1-48x48.bmp').convert()
        image.set_colorkey((0,0,0)) 
	self.stimlibdown.addpicture(image)
	
        image = pygame.image.load('./pics/goblin3-48x48.bmp').convert()
        image.set_colorkey((0,0,0)) 
	self.stimlibdown.addpicture(image)	
        image = pygame.image.load('./pics/goblin3-48x48.bmp').convert()
        image.set_colorkey((0,0,0)) 
	self.stimlibdown.addpicture(image)
	image = pygame.image.load('./pics/goblin3-48x48.bmp').convert()
        image.set_colorkey((0,0,0)) 
	self.stimlibdown.addpicture(image)
	image = pygame.image.load('./pics/goblin3-48x48.bmp').convert()
        image.set_colorkey((0,0,0)) 
	self.stimlibdown.addpicture(image)

        image = pygame.image.load('./pics/goblin2-48x48.bmp').convert()
        image.set_colorkey((0,0,0)) 
	self.stimlibdown.addpicture(image)	
        image = pygame.image.load('./pics/goblin2-48x48.bmp').convert()
        image.set_colorkey((0,0,0)) 
	self.stimlibdown.addpicture(image)
	image = pygame.image.load('./pics/goblin2-48x48.bmp').convert()
        image.set_colorkey((0,0,0)) 
	self.stimlibdown.addpicture(image)
	image = pygame.image.load('./pics/goblin2-48x48.bmp').convert()
        image.set_colorkey((0,0,0)) 
	self.stimlibdown.addpicture(image)

        image = pygame.image.load('./pics/goblinup1-48x48.bmp').convert()
        image.set_colorkey((0,0,0)) 
	self.stimlibup.addpicture(image)
	image = pygame.image.load('./pics/goblinup1-48x48.bmp').convert()
        image.set_colorkey((0,0,0)) 
	self.stimlibup.addpicture(image)
	image = pygame.image.load('./pics/goblinup1-48x48.bmp').convert()
        image.set_colorkey((0,0,0)) 
	self.stimlibup.addpicture(image)
	image = pygame.image.load('./pics/goblinup1-48x48.bmp').convert()
        image.set_colorkey((0,0,0)) 
	self.stimlibup.addpicture(image)

	image = pygame.image.load('./pics/goblinup2-48x48.bmp').convert()
        image.set_colorkey((0,0,0)) 
	self.stimlibup.addpicture(image)
	image = pygame.image.load('./pics/goblinup2-48x48.bmp').convert()
        image.set_colorkey((0,0,0)) 
	self.stimlibup.addpicture(image)
	image = pygame.image.load('./pics/goblinup2-48x48.bmp').convert()
        image.set_colorkey((0,0,0)) 
	self.stimlibup.addpicture(image)
	image = pygame.image.load('./pics/goblinup2-48x48.bmp').convert()
        image.set_colorkey((0,0,0)) 
	self.stimlibup.addpicture(image)

	image = pygame.image.load('./pics/goblinup3-48x48.bmp').convert()
        image.set_colorkey((0,0,0)) 
	self.stimlibup.addpicture(image)
	image = pygame.image.load('./pics/goblinup3-48x48.bmp').convert()
        image.set_colorkey((0,0,0)) 
	self.stimlibup.addpicture(image)
	image = pygame.image.load('./pics/goblinup3-48x48.bmp').convert()
        image.set_colorkey((0,0,0)) 
	self.stimlibup.addpicture(image)
	image = pygame.image.load('./pics/goblinup3-48x48.bmp').convert()
        image.set_colorkey((0,0,0)) 
	self.stimlibup.addpicture(image)
        	
        image = pygame.image.load('./pics/goblinup2-48x48.bmp').convert()
        image.set_colorkey((0,0,0)) 
	self.stimlibup.addpicture(image)
	image = pygame.image.load('./pics/goblinup2-48x48.bmp').convert()
        image.set_colorkey((0,0,0)) 
	self.stimlibup.addpicture(image)
	image = pygame.image.load('./pics/goblinup2-48x48.bmp').convert()
        image.set_colorkey((0,0,0)) 
	self.stimlibup.addpicture(image)
	image = pygame.image.load('./pics/goblinup2-48x48.bmp').convert()
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
        sleep(.04) # FIX goblin sleep
	
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
        # FIX BUG
        print 'goblin x=%d y=%d player x=%d y=%d' % (self.x,self.y,player.x-room.relativex,player.y)
	if (player.x-room.relativex > self.x  and 
	player.x-room.relativex < self.x+self.w and 
	player.y-room.relativey > self.y and 
	player.y-room.relativey < self.y + self.h):
	    print "collision with Goblin!"
	    return 1 
	else:
	    return 0 ## for game self.talker
