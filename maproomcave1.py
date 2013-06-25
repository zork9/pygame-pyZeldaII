
# Copyright (C) Johan Ceuppens 2010-2013
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
from koboldwizard import *
from tilebox import *
#from snake1 import *
from rubysword import *
from rope import *

class MaproomCave1(MaproomDungeon):
    "Room with a (big) map"
    def __init__(self,x,y):
        MaproomDungeon.__init__(self,x,y)
        self.background = pygame.image.load('./pics/bg-3-underground1-1400x480.bmp').convert()
	# ground level
        self.gameobjects.append(Box(0,440,1400,400))
	# roof 
        self.gameobjects.append(Box(0,0,1400,300))
        #self.gameobjects.append(Snake1(680,140))
        #self.gameobjects.append(Beholder(300,100))
        #self.gameobjects.append(BeholderBat(300,100))
	#self.gameobjects.append(RubySword(400,100))
        self.ropes.append(Rope(605,100,340))

 
    def draw(self,screen,player):
        # draw bg
        screen.blit(self.background, (0+self.relativex, 0+self.relativey))
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
	for r in self.ropes:
		r.update(self,player)
		r.draw(screen,self)

	
    def isroomupexit(self):
	if self.relativex > 275:
		return 1.1 
	return 0

    def setxyfromup(self):
        self.relativex = -640 
	self.relativey = -0

    def exit(self, game):
	if self.isroomupexit():
		self.setxyfromup()
		return 1.1 
	return 0 
 
    def collidesword(self,player):
        for i in self.gameobjects:
	    if i!= None:
	    	id = i.collidewithsword(self,player)
		#self.relativex = self.prevx
		#self.relativey = self.prevy
		return i ## NOTE : returns collided entity (single)
	return None

    def talkto(self, player):
        return self.gameobjects[1] 

    def moveright(self):
        self.direction = "east"
        self.sidedirection = "east"
	self.prevx = self.relativex - 1
	self.prevy = self.relativey
        self.relativex = self.relativex + 10
	### print "relx=%d" % self.relativex

    def removeobject(self, o):
        for i in range(0,len(self.gameobjects)):
            if self.gameobjects[i] == o:
                self.gameobjects[i] = None
