
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
from maproombase import *

class Maproom(MaproomBase):
    "Room with a (big) map"
    def __init__(self,x,y):
        MaproomBase.__init__(self,x,y)
        self.gameobjects = []
        ### NOTE all items which can only pickup once (see maproomXXX.py)
        self.dungeonkey1 = 0
        self.dungeonkey2 = 0
        self.masterkey = 0

        
    def draw(self,screen):
	##print "x=%d" % self.relativex 
        screen.blit(self.background, (0+self.relativex, 0+self.relativey))

    def pickup(self, player):
        return 0

    def undomove(self):
        if self.direction == "north":
            self.movedown()
            self.movedown()
        elif self.direction == "south":
            self.moveup()
            self.moveup()
        elif self.direction == "west":
            self.moveright()
            self.moveright()
        elif self.direction == "east":
            self.moveleft()
            self.moveleft()
 
    def moveup(self):
        self.direction = "north"
	self.prevx = self.relativex
	self.prevy = self.relativey + 10
        self.relativey = self.relativey - 10

    def movedown(self):
        self.direction = "south"
	self.prevx = self.relativex
	self.prevy = self.relativey - 10
        self.relativey = self.relativey + 10

    def moveleft(self):
        self.direction = "west"
	self.prevx = self.relativex + 10
	self.prevy = self.relativey
        self.relativex = self.relativex - 10

    def moveright(self):
        self.direction = "east"
	self.prevx = self.relativex - 10
	self.prevy = self.relativey
        self.relativex = self.relativex + 10

        
    def setxyfromleft(self):
        self.relativex = 0 
        self.relativey = 100

    def isroomleftexit(self):
	if self.relativex > 100 and self.relativey > -10:#FIX and self.relativey < -10 - 48:
		return 1
	return 0

    def setxyfromright(self):
        self.relativex = 100 
        self.relativey = 0

    def isroomrightexit(self):
	if self.relativex < -110 and self.relativey > -10:
		return 1
	return 0

    def setxyfromup(self):
        self.relativex = 0 
        self.relativey = -100

    def isroomupexit(self):
	if self.relativex >= 0 and self.relativey > 100 and self.relativey < 200:
		return 1
	return 0

    def setxyfromdown(self):
        self.relativex = 0 
        self.relativey = -100

    def isroomdownexit(self):
	if self.relativex  >= 0 and self.relativex <= 80 and self.relativey < -80:### and self.relativey < 20:
		return 1
	return 0

    def removeobject(self, o):
        for i in self.gameobjects:
	    if i!= None:
                if i == o:
                    i = None ###FIXME2

    def talkto(self):
        return None

    def collidesword(self,room,player):
        for i in self.gameobjects:
	    if i!= None:
	    	id = i.collide(room,player)
                ##self.relativex = self.prevx
		##self.relativey = self.prevy
		return i ## NOTE : returns collided entity (single)
	return None

    def hitwithsword(self, o):
        hitp = o.hit()
        if hitp < 0:
            self.removeobject(o)
