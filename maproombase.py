
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
        self.enemies = []
        self.gameobjects = []
        self.tileboxes = []
	self.roofs = []
        self.pits = []
        self.ropes = []
       	self.elevators = []
        self.background = pygame.image.load('./pics/blank.bmp').convert()
        self.direction = "north"
        self.sidedirection = "north"
        self.changeroomnumber = 0 
 
    def yminus(self, dy):
	self.prevy = self.relativey 
	self.relativey -= dy
 
    def yplus(self, dy):
	self.prevy = self.relativey 
	self.relativey += dy
 
    def yget(self):
	return self.relativey 
 
    def yset(self, y):
	self.prevy = self.relativey 
	self.relativey = y
 
    def xget(self):
	return self.relativex 
 
    def xset(self, x):
	self.prevx = self.relativex 
	self.relativex = x
 
    def draw(self,screen):
        screen.blit(self.background, (0+self.relativex, 0+self.relativey))

    def collidewithropes(self, player):	
	for i in self.ropes:
	    if i != None and i.collidewithrope(self, player):
		return 2
	return 0

    def collide(self, player):	
	for i in self.gameobjects:
	    if i != None and i.collide(self, player):
		return 2 # 1 kills game
	for i in self.tileboxes:
		if i != None and i.collide(self,player):
			#self.undomove()
	                # FIXME self.undomove()
			return 2 
	for i in self.pits:
		if i != None and i.collide(self,player):
			return 2
	return 0

    def collidewithenemy(self, enemy):
	for t in self.tileboxes:
		if t != None and t.collidewithenemy(self,enemy):
                    enemy.undomove()
                    return 2 # 1 kills game
        return 0


    def fall(self, player):
        self.moveup()
        for i in self.gameobjects:
	    if i != None and i.fallcollide(self, player) != 0:
                self.movedown()
		return 2 # 1 kills game
        
        return 0
	## NOTE override gameobj with i.collideup() == 2 when jumping high onto a platform

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

	### NOTE dummy function for non overworld maps ## FIX
    def MOVEDOWN(self,room,player):
	1	
 
	### NOTE dummy function for non overworld maps ## FIX
    def MOVEUP(self, room, player):
	1	
 
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
        self.sidedirection = "west"
	self.prevx = self.relativex + 1
	self.prevy = self.relativey
        self.relativex = self.relativex - 10
	### print "relx=%d" % self.relativex
	
    def moveright(self):
	if self.relativex >= 0:
		self.moveleft()
        self.direction = "east"
        self.sidedirection = "east"
	self.prevx = self.relativex - 1
	self.prevy = self.relativey
        self.relativex = self.relativex + 10
	### print "relx=%d" % self.relativex

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

    def collideswordmedium(self,player):
        for i in self.enemies:
	    if i != None:
	        if i.collidewithswordmedium(self,player) != None:
		    return i ## NOTE : returns collided entity (single)
	return None

    def collideswordlow(self,player):
        for i in self.enemies:
	    if i!= None:
	    	if i.collidewithswordlow(self,player) != None:
		    return i ## NOTE : returns collided entity (single)
	return None

    def collideup(self,player):
	for i in self.roofs:
		if i.collideup(self, player):
			print ">>>>>>>>>>> collideup"
			return 2
	return 0

