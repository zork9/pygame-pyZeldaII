
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
from rng import *
from time import *

class Goblin2(Gameobject):
    "Goblin"
    def __init__(self,xx,yy):
	Gameobject.__init__(self, xx, yy)
        self.w = 48
        self.h = 48

        self.hitpoints = 3
        
	self.stimlibleft = Stateimagelibrary()	
	self.stimlibright = Stateimagelibrary()	
        image = pygame.image.load('./pics/goblin2left1-48x48.bmp').convert()
        image.set_colorkey((0,0,0)) 
	self.stimlibleft.addpicture(image)	
        image = pygame.image.load('./pics/goblin2left2-48x48.bmp').convert()
        image.set_colorkey((0,0,0)) 
	self.stimlibleft.addpicture(image)
        image = pygame.image.load('./pics/goblin2right1-48x48.bmp').convert()
        image.set_colorkey((0,0,0)) 
	self.stimlibright.addpicture(image)	
        image = pygame.image.load('./pics/goblin2right2-48x48.bmp').convert()
        image.set_colorkey((0,0,0)) 
	self.stimlibright.addpicture(image)

	self.talkcounter = 0
	self.direction = "left"

    def draw(self, screen, room):
	if (self.direction == "left"):
            self.stimlibleft.draw(screen, self.x+room.relativex,self.y+room.relativey)
	elif (self.direction == "right"):
            self.stimlibright.draw(screen, self.x+room.relativex,self.y+room.relativey)
	    
	     
    def update(self,room,player):
        sleep(.04) # FIX goblin sleep
#	if (not self.collideobjectY(room)): 
#	    if (self.direction == "right"):
#	        self.x -=2
#	        self.direction = "left" 
#	    elif (self.direction == "left"):
#	        self.x +=2
#	        self.direction = "right"

	if player.x < self.x:
		self.x -= 2
	elif player.x > self.x+self.w:
		self.x += 2	
	if player.y < self.y:
		self.y -= 2
	elif player.y > self.y+self.h:
		self.y += 2	

	if (self.direction == "left"):
	        self.x -=2
	elif (self.direction == "right"):
	        self.x +=2

    def fight(self,room,player):
        self.fightcounter = 1
        #print 'fight'
        o = player.collidesword(room,self)
        #print 'fight %s' % o
        if o:
            print 'player is hit!'
            player.hitwithsword(RNG().rollgoblinknife())
