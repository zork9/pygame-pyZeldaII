
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
from math import *
from rng import *

class Daira(Gameobject):
    "Crocodile man"
    def __init__(self,xx,yy):
	Gameobject.__init__(self, xx, yy)
        self.w = 48
        self.h = 64
        self.hitpoints = 4
        
    
        self.stimlibleft = Stateimagelibrary()
        self.stimlibright = Stateimagelibrary()
        image = pygame.image.load('./pics/daira1-48x64.bmp').convert()
        image.set_colorkey((0,0,255))
        self.stimlibleft.addpicture(image)
        image = pygame.image.load('./pics/daira2-58x64.bmp').convert()
        image.set_colorkey((0,0,255))
        self.stimlibleft.addpicture(image)

        image = pygame.image.load('./pics/dairaright1-48x64.bmp').convert()
        image.set_colorkey((0,0,255))
        self.stimlibright.addpicture(image)
        image = pygame.image.load('./pics/dairaright2-58x64.bmp').convert()
        image.set_colorkey((0,0,255))
        self.stimlibright.addpicture(image)
        
        
	self.talkcounter = 0
	self.direction = "left"

        self.crawling = 1
        self.up = 0

    def draw(self, screen, room):
        #if self.crawling == 1:
        if (self.direction == "left"):
            self.stimlibleft.draw(screen, self.x+room.relativex,self.y+room.relativey)
        elif (self.direction == "right"):
            self.stimlibright.draw(screen, self.x+room.relativex,self.y+room.relativey)
        elif self.direction == "stop":
            1
                
    def update(self,room,player):
#        if abs(player.x-self.x-room.relativex) < 50:
#            self.direction = "left"
#        else:
#            self.direction = "right"
        if player.x+48 < self.x:
            self.direction = "left"
        elif player.x-48 > self.x:
            self.direction = "right"
        # movement in trees towards player
        ###FIXif self.crawling:
        if self.direction == "left":###player.x <= self.x-room.relativex:
            ###self.direction = "left"
            self.x -= 5
        if self.direction == "right":###player.x > self.x-room.relativex:
            ###self.direction = "right"
            self.x += 5
                            
    def collide(self, room, player):
        # FIX BUG
        #print 'gameobject x=%d y=%d player x=%d y=%d' % (self.x,self.y,player.x-room.relativex,player.y-room.relativey)
	if (player.x-room.relativex > self.x-self.w  and 
	player.x-room.relativex < self.x+self.w+self.w and 
	player.y-room.relativey > self.y-self.h and 
	player.y-room.relativey < self.y + self.h +self.h):
	    print "collision with Daira!"
	    return 1 
	else:
	    return 0 ## for game self.talker


    def collidewithsword(self, room, player):
        print 'Daira x=%d y=%d player x=%d y=%d' % (self.x,self.y,player.x-room.relativex,player.y-room.relativey)
	if (player.x-room.relativex > self.x -self.w  and 
	player.x-room.relativex < self.x+self.w and 
	player.y-room.relativey > self.y -self.h and 
	player.y-room.relativey < self.y + self.h):
	    print "collision with Sword Daira!"
	    return 1 
	else:
	    return 0

    def fight(self,room,player,keydown = -1):
        1
