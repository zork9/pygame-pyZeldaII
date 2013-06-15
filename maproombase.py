
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
from koboldwizard import *
from time import *

class MaproomBase:
    "Room with a (big) map"
    def __init__(self,x,y):
        ###Room.__init__(self)
        self.prevx = x
        self.prevy = y
        self.relativex = x
        self.relativey = y 
        self.background = pygame.image.load('./pics/blank.bmp').convert()
        self.direction = "north"
        
    def draw(self,screen):
	##print "x=%d" % self.relativex 
        screen.blit(self.background, (0+self.relativex, 0+self.relativey))

    def undomove(self):
        if self.direction == "north":
            self.movedown()
            #self.movedown()
        elif self.direction == "south":
            self.moveup()
            #self.moveup()
        elif self.direction == "west":
            self.moveright()
            #self.moveright()
        elif self.direction == "east":
            self.moveleft()
            #self.moveleft()
 
    def moveup(self):
        self.direction = "north"
	self.prevx = self.relativex
	self.prevy = self.relativey + 1
        self.relativey = self.relativey - 10

    def movedown(self):
        self.direction = "south"
	self.prevx = self.relativex
	self.prevy = self.relativey - 1
        self.relativey = self.relativey + 10

    def moveleft(self):
        self.direction = "west"
	self.prevx = self.relativex + 1
	self.prevy = self.relativey
        self.relativex = self.relativex - 10

    def moveright(self):
        self.direction = "east"
	self.prevx = self.relativex - 1
	self.prevy = self.relativey
        self.relativex = self.relativex + 10

    def setxyup(self):
        self.x = -80 
        self.y = -80

    def setxydown(self):
        self.x = -80 
        self.y = -80

    def talkto(self):
        return None

    def pickup(self, player):
        for i in range(0,len(self.gameobjects)):
	    o = self.gameobjects[i]
            if o and o.collide(self, player):
                id = o.pickup(self)
		self.gameobjects[i] = None
                return id# FIX 3 
        return 0


    def collidesword(self,player):
        for i in self.gameobjects:
	    if i!= None:
	    	c = i.collide(self,player)
		if c == 1:
			return i ## NOTE : returns collided entity (single)
		self.relativex = self.prevx
		self.relativey = self.prevy
        return None
