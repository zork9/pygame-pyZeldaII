
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
from box import *
from archgohma import *
from demon import *
from mithranhouse import *
from toadstool import *

class Maproom13(Maproom):
    "Room with a (big) map"
    def __init__(self,x,y):
        Maproom.__init__(self,x,y)
        self.background = pygame.image.load('./pics/room-bg13.bmp').convert()
        ##  upper wall
        b = Box(0,0,1000,300)
	b.setimage('./pics/nopicture.bmp',0,0,255)
	## down wall
	b = Box(0,1000,1000,40)
	b.setimage('./pics/nopicture.bmp',0,0,255)
	##  left wall
	b = Box(0,0,40,1000)
	b.setimage('./pics/nopicture.bmp',0,0,255)
	##  right wall
	b = Box(1000,0,40,1000)
	b.setimage('./pics/nopicture.bmp',0,0,255)

	self.gameobjects.append(b)
	## arch gohmas
	self.gameobjects.append(ArchGohma(300,300))
	self.gameobjects.append(ArchGohma(100,700))
	self.gameobjects.append(ArchGohma(700,400))
	self.gameobjects.append(ArchGohma(700,700))
	## possessed demonic knights
	self.gameobjects.append(Demon(300,400))
	self.gameobjects.append(Demon(400,400))
	self.gameobjects.append(Demon(500,400))
	self.gameobjects.append(Demon(600,400))
	## House of Mithran
	self.gameobjects.append(Mithranhouse(500,500,200,200))
	## Giant Toadstools
	self.gameobjects.append(Toadstool(600,400))
	self.gameobjects.append(Toadstool(700,400))
	self.gameobjects.append(Toadstool(600,500))
	self.gameobjects.append(Toadstool(60,700))
	self.gameobjects.append(Toadstool(248,450))
	self.gameobjects.append(Toadstool(80,800))
	self.gameobjects.append(Toadstool(220,480))
	self.gameobjects.append(Toadstool(300,500))
	self.gameobjects.append(Toadstool(210,550))
	self.gameobjects.append(Toadstool(780,780))
	self.gameobjects.append(Toadstool(648,350))
	self.gameobjects.append(Toadstool(805,630))
	
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

    def isroomdownexit(self):
	if self.relativex  <= 100 and self.relativey < -1080:### and self.relativey < 20:
		return 1
	return 0

    def setxyfromdown(self):
        self.relativex = 0
	self.y = 80

    def isroomhouseexit(self):
	if self.relativex  < -400 and self.relativex > - 600 and self.relativey < -400 and self.relativey > - 600:### and self.relativey < 20:
		return 1
	return 0

    def setxyfromhouse(self):
        self.relativex = 0
	self.relativey = 0
	
	
    def exit(self, game):
        print "x=%d y=%d" % (self.relativex,self.relativey)
        if self.isroomdownexit():
	    self.setxyfromdown()	    
	    return 12
	if self.isroomhouseexit():
	    self.setxyfromhouse()	    
	    return 14
	#FIXME Trap door: elif self.isroomdownexit():
	#    self.setxyfromdown()	
	#    return 11
	else:
	    return 0

    def removeobject(self, o):
        for i in (0,len(self.gameobjects)-1):
            if (self.gameobjects[i] and self.gameobjects[i] == o):
                print "PICKUP"
                self.gameobjects[i] = None
