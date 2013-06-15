
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
from maproom import *
from tree import *
from tree2 import *
from dungeonentrance1 import *
from maproom2 import *
from goblin1 import *
from box import *

class Maproom1_1_1(Maproom):
    "Room with a (big) map - west of knight's castle"
    def __init__(self,x,y):
        Maproom.__init__(self,x,y)
        self.background = pygame.image.load('./pics/room-bg1_1_1.bmp').convert()
        #FIX	self.gameobjects.append(Dungeonentrance1(0,0))
	self.gameobjects.append(Tree2(10,100))
	self.gameobjects.append(Tree2(100,100))
	self.gameobjects.append(Tree2(200,120))
        self.gameobjects.append(Goblin1(50,230))
        self.gameobjects.append(Goblin1(440,230))
        b = Box(650,0,150,300)
        b.setimage('./pics/knightdungeon1-150x350.bmp',0,0,0)
        self.gameobjects.append(b)
        # upper crevasses
        self.gameobjects.append(Box(0,0,375,75))
        self.gameobjects.append(Box(375,0,100,100))
        self.gameobjects.append(Box(475,0,100,125))
        self.gameobjects.append(Box(500,0,120,180))
        self.gameobjects.append(Box(600,0,50,160))
        self.gameobjects.append(Box(650,0,25,75))
        self.gameobjects.append(Box(675,0,75,40))
        self.gameobjects.append(Box(750,0,50,40))
        # lower crevasses
        self.gameobjects.append(Box(500,220,120,400))
        self.gameobjects.append(Box(0,400,800,100))

 
    def draw(self,screen):
        screen.blit(self.background, (0+self.relativex, 0+self.relativey))
        for i in self.gameobjects:
	    if i != None:
		i.draw(screen,self)

    def collide(self, player):
	for i in self.gameobjects:
	    if i != None: 
		i.update(self)	
	for i in self.gameobjects:
	    if i != None and i.collide(self, player):
		self.relativex = self.prevx
		self.relativey = self.prevy
		return  

    def isroomdownexit(self):
	if self.relativex  < -140 and self.relativex > -200 and self.relativey < -210:### and self.relativey < 20:
		return 1
	return 0

    def setxyfromdown(self):
        self.relativex = 0
	self.relativey = 0

    def isroomleftexit(self):
	if self.relativex  > 100:
		return 1
	return 0

    def setxyfromleft(self):
        self.relativex = 0
	self.relativey = 0
	

    def exit(self, game):
        # To Mithran and Gohma's Lair and Lady of the Lake Knight Chateau
        print 'x=%d y=%d' % (self.relativex,self.relativey)
	if self.relativey < -50 and self.relativex < -580:
	    game.setxy(0,-80)	
	    return 2#FIX
        # To south 
	elif self.isroomdownexit():
            self.setxyfromdown()
            return 1.1#FIX
        # To the west
        elif self.isroomleftexit():
            self.setxyfromleft()
            return 1.1#FIX
	else:
	    return 0 
 
    def collidesword(self,room,player):
        for i in self.gameobjects:
	    if i!= None:
	    	c = i.collide(room,player)
		if c == 1:
			return i ## NOTE : returns collided entity (single)
		self.relativex = self.prevx
		self.relativey = self.prevy
	return None
