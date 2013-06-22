
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
from blackknight import *
from demon import *
from bombman import *
from turtleflying import *
from ghost1 import *
from ghostwandering import *
from ghostcircling import *
from maproom2 import *
from dungeonmasterkey import *
from dungeonkey1 import *

class Maproom5(Maproom):
    "Room with a (big) map"
    def __init__(self,x,y):
        Maproom.__init__(self,x,y)
        self.background = pygame.image.load('./pics/room-bg5.bmp').convert()
        ###	self.gameobjects.append(Bombman(100,50))
###	self.gameobjects.append(Bombman(200,100))
###	self.gameobjects.append(Bombman(100,150))
	self.gameobjects.append(GhostWandering(200,200))
	self.gameobjects.append(GhostWandering(200,240))
	self.gameobjects.append(Ghostcircling(20,20))
	self.gameobjects.append(Dungeonwall(0,0,300,10))
	self.gameobjects.append(Dungeonwall(0,290,300,10))
	self.gameobjects.append(Dungeonwall(0,0,10,300))
	self.gameobjects.append(Dungeonwall(290,0,10,300))
	# NOTE eventually keep last for easy removal
	if not self.dungeonkey1:
            self.gameobjects.append(Dungeonkey1(40,250))
            
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
	    if i!= None:
	    	id = i.collide(self,player)
		self.relativex = self.prevx
		self.relativey = self.prevy
		return id
	return 0

    def setxyfromroomtotower(self):
        self.x = 0 
        self.y = -100

    def isroomtowerexit(self):
	if self.relativex > -10 and self.relativex < 15 and self.relativey > 40:
		return 1
	return 0


    def pickup(self, player):###FIX for each room
        for o in self.gameobjects:
            if (o and o.collide(self, player)):##FIX o.colidepickup
                id = o.pickup(self)
                self.dungeonkey1 = 1
		return id
        return 0
    
    def exit(self, game):
        if self.isroomrightexit():
	    self.setxyfromright()	
	    return 4
	elif self.isroomtowerexit():
	    self.setxyfromroomtotower()	
	    return 6
	else:
	    return 0

    def removeobject(self, o):
        for i in (0,len(self.gameobjects)-1):
            print "o=%s self.gameobjects[i]=%s i=%d" % (o,self.gameobjects[i],i)
            if self.gameobjects[i] == o:
                print "PICKUP or die"
                self.gameobjects[i] = None
		return 

    def collidesword(self,room,player):
        for i in self.gameobjects:
	    if i!= None:
	    	c = i.collide(room,player)
	    	print "i=%s" % i
		if c == 1:
                        print "collision with i=%s!" % i
			return i ## NOTE : returns collided entity (single)
		self.relativex = self.prevx
		self.relativey = self.prevy
	return None


