
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
from maproom import *
from maproomdungeonnorthwall import *
from maproomdungeonsouthwall import *
from maproomdungeonwestwall import *
from maproomdungeoneastwall import *

class MaproomDungeon(MaproomBase):
    "Room with a (big) map"
    def __init__(self,x,y):
        MaproomBase.__init__(self,x,y)
        self.northwalls = []
        self.southwalls = []
        self.westwalls = []
        self.eastwalls= []
        self.gameobjects = []
        self.tileboxes = []
        self.pits = []
        self.ropes = []
        
    def addnorthwall(self, x,y):
        self.northwalls.append(MaproomNorthDungeonWall(x,y))

    def addsouthwall(self, x,y):
        self.southwalls.append(MaproomSouthDungeonWall(x,y))

    def addwestwall(self, x,y):
        self.westwalls.append(MaproomWestDungeonWall(x,y))

    def addeastwall(self, x,y):
        self.eastwalls.append(MaproomEastDungeonWall(x,y))
        
    def draw(self,screen):
	##print "x=%d" % self.relativex 
        screen.blit(self.background, (0+self.relativex, 0+self.relativey))
        for w in self.northwalls:
            w.draw(screen,self.relativex,self.relativey)

    def collidewithropes(self, player):	
	for i in self.ropes:
	    if i != None and i.collidewithrope(self, player):
		return 2
	return 0

      
# NOTE player can be enemy 
    def collide(self, player):	
	for i in self.gameobjects:
	    if i != None and i.collide(self, player):
		return 2 # 1 kills game
	for i in self.northwalls:
	    if i != None and i.collide(self, player):
		return 2
	for i in self.southwalls:
	    if i != None and i.collide(self, player):
		return 2
	for i in self.westwalls:
	    if i != None and i.collide(self, player):
		return 2
	for i in self.eastwalls:
	    if i != None and i.collide(self, player):
		return 2
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
	    if i != None and i.fallcollide(self, player):
                self.movedown()
		return 2 # 1 kills game
        
        return 0
