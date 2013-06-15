
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
from knight import *
from mongbat import *
from maproom2 import *
from dungeonmasterkey import *
from gohma import *
from gohmaup import *
from gohmaright import *
from demon import *

class Maproom9(Maproom):
    "Room with a (big) map"
    def __init__(self,x,y):
        Maproom.__init__(self,x,y)
        self.background = pygame.image.load('./pics/room-bg9.bmp').convert()	#self.gameobjects.append(Dungeonmasterkey(50,50))
	self.gameobjects.append(Dungeonwall(0,0,300,40))
	self.gameobjects.append(Dungeonwall(0,260,300,40))
	self.gameobjects.append(Dungeonwall(0,0,40,300))
        self.gameobjects.append(Dungeonwall(260,0,40,300))
	### self.gameobjects.append(GohmaRight(50,50))
	self.gameobjects.append(Demon(50,50))

    def draw(self,screen):
        screen.blit(self.background, (0+self.relativex, 0+self.relativey))
        for i in self.gameobjects:
	    if i:
                i.draw(screen,self)
 
    def collide(self, player):
	for i in self.gameobjects:
	    if i != None:
		i.update(self)	
	for i in self.gameobjects:
            if i != None:
                id = i.collide(self,player)
                self.relativex = self.prevx
		self.relativey = self.prevy
		return id
	return 0

##    def pickup(self, player):
##        for o in self.gameobjects:
##            if (o and o.collidepickup(self, player)):
##                o.pickup(self)
##                return
##

    def exit(self, game):
        if self.isroomrightexit():
	    self.setxyfromright()	
	    return 8
	elif self.isroomdownexit():
	    self.setxyfromdown()	
	    return 10
	else:
	    return 0

    def removeobject(self, o):
        for i in (0,len(self.gameobjects)-1):
            if (self.gameobjects[i] and self.gameobjects[i] == o):
                print "PICKUP"
                self.gameobjects[i] = None
