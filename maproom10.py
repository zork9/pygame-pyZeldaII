
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
from dungeonkey2 import *
from gohma import *
from gohmaup import *

class Maproom10(Maproom):
    "Room with a (big) map"
    def __init__(self,x,y):
        Maproom.__init__(self,x,y)
        self.background = pygame.image.load('./pics/room-bg10.bmp').convert()	#self.gameobjects.append(Dungeonmasterkey(50,50))
	self.gameobjects.append(Dungeonwall(0,0,300,40))
	self.gameobjects.append(Dungeonwall(0,260,300,40))
	self.gameobjects.append(Dungeonwall(0,0,40,300))
	self.gameobjects.append(Gohma(0,20))
	self.gameobjects.append(GohmaUp(0,200))
	if not self.dungeonkey2:
            self.gameobjects.append(Dungeonkey2GohmaLair(130,130))
##	self.gameobjects.append(Dungeonwall(260,0,40,300))
##	self.gameobjects.append(Mongbat(100,50))
##	self.gameobjects.append(Mongbat(200,100))
##	self.gameobjects.append(Mongbat(100,150))
##	self.gameobjects.append(Mongbat(200,200))


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

    def pickup(self, player):###FIX for each room
        for o in self.gameobjects:
            if (o and o.collide(self, player)):##FIX o.colidepickup
                id = o.pickup(self)
                self.dungeonkey2 = 1
		return id
        return 0
    
    def exit(self, game):
        if self.isroomdownexit():
	    self.setxyfromdown()	
	    return 9
	else:
	    return 0

    def removeobject(self, o):
        for i in (0,len(self.gameobjects)-1):
            if (self.gameobjects[i] and self.gameobjects[i] == o):
                print "PICKUP"
                self.gameobjects[i] = None
