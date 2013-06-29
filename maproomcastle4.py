
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
from maproomdungeon import *
from maproomdungeonnorthwall import *
from tilebox import *
from boxcat import *
from elevatorcat import *
from rope import *
#from snake1 import *
from rubysword import *
from digdogger import *
from ironknuckle import *
from deeler import *
from daira import *

class MaproomCastle4(MaproomDungeon):
    ""
    def __init__(self,x,y):
        MaproomDungeon.__init__(self,x,y)
        self.background = pygame.image.load('./pics/parapapalace-4-640x480.bmp').convert()

	self.WIDTH = 640

	self.offsetx = x
	self.offsety = y

        self.gameobjects.append(Ironknuckle(self.offsetx+600,self.offsety+340))
        
        # left NOTE : boxes collide so put them after enemies !
	# roof
        ### self.gameobjects.append(Boxcat(self.offsetx,self.offsety,self.WIDTH,50))
	# base
        self.gameobjects.append(Boxcat(self.offsetx,self.offsety+422,self.WIDTH,40))

	# left platforms
        self.gameobjects.append(Boxcat(self.offsetx+0,self.offsety+235,200,40))
	# right platforms
        self.gameobjects.append(Boxcat(self.offsetx+310,self.offsety+235,200,40))

    def draw(self,screen,player):
        # draw bg
	### print "abc> %d" % self.relativey
        ### is in maproomdungeon screen.blit(self.background, (0+self.relativex, 0+self.relativey))
	screen.blit(self.background, (self.offsetx+self.relativex, self.offsety+self.relativey))
        # draw walls
        MaproomDungeon.draw(self,screen)
        for t in self.tileboxes:
            t.draw(screen,self.relativex,self.relativey)
        #self.southwall1.draw(screen,self.relativex,self.relativey)
        # draw gameobjects
        for i in self.gameobjects:
	    if i != None:
		i.update(self,player)
		i.draw(screen,self)
	for i in self.ropes:
	    if i != None:
		i.update(self,player)
		i.draw(screen,self)
		
    def isroomdownexit(self):
	###if self.relativex  < -500:
	###	return 1
	return 0

    def setxyfromdown(self):
        self.relativex = 0
	self.relativey = 0

    def exit(self, game):
	#if self.isroomdownexit():
	#	self.setxyfromdown()
	#	return 2 
	return 0 
 
    def collidesword(self,player):
        for i in self.gameobjects:
	    if i!= None:
	    	id = i.collidewithsword(self,player)
		#self.relativex = self.prevx
		#self.relativey = self.prevy
		return i ## NOTE : returns collided entity (single), put enemies before walls in gameobjects
	return None

    def collideswordlow(self,player):
        for i in self.gameobjects:
	    if i!= None:
	    	id = i.collidewithswordlow(self,player)
		#self.relativex = self.prevx
		#self.relativey = self.prevy
		return i ## NOTE : returns collided entity (single), put enemies before walls in gameobjects
	return None

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
	### print "self.lx=%d" % self.self.lativex
	
    def moveright(self):
	if self.relativex >= 0:
		self.moveleft()
        self.direction = "east"
        self.sidedirection = "east"
	self.prevx = self.relativex - 1
	self.prevy = self.relativey
        self.relativex = self.relativex + 10
	### print "relx=%d" % r.relativex

    def removeobject(self, o):
        for i in range(0,len(self.gameobjects)):
            if self.gameobjects[i] == o:
                self.gameobjects[i] = None
