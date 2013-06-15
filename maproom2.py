
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
from maproomdungeon import *
from maproomdungeonnorthwall import *
from goblin1 import *
from goblin2 import *
from goblin3 import *
from tilebox import *
#from snake1 import *
from rubysword import *
from beholder import *
from beholderbat import *

class Maproom2(MaproomDungeon):
    "Room with a (big) map"
    def __init__(self,x,y):
        MaproomDungeon.__init__(self,x,y)
        self.background = pygame.image.load('./pics/room-bg2.bmp').convert()
        self.westwall1 = Tilebox(1,1,48,60,1,14,'./pics/walldungeonwest2-48x60.bmp')
        self.eastwall1 = Tilebox(775,1,48,60,1,14,'./pics/walldungeoneast1-48x60.bmp')
        self.tileboxes.append(self.westwall1)
        self.tileboxes.append(self.eastwall1)

        self.gameobjects.append(Goblin3(100,100))
        self.gameobjects.append(Goblin3(150,100))
        self.gameobjects.append(Goblin3(240,140))
        self.gameobjects.append(Goblin3(350,180))
        self.gameobjects.append(Goblin3(380,180))
        self.gameobjects.append(Goblin3(400,100))
        self.gameobjects.append(Goblin3(450,100))
        self.gameobjects.append(Goblin3(540,120))
        #self.gameobjects.append(Snake1(680,140))
        #self.gameobjects.append(Beholder(300,100))
        #self.gameobjects.append(BeholderBat(300,100))
	#self.gameobjects.append(RubySword(400,100))

        #FIX	self.gameobjects.append(Dungeonentrance1(0,0))
##	self.gameobjects.append(Tree2(10,100))
##	self.gameobjects.append(Tree2(100,100))
##	self.gameobjects.append(Tree2(200,120))
##        self.gameobjects.append(Goblin1(50,230))
##        self.gameobjects.append(Goblin1(440,230))
##        b = Box(650,0,150,300)
##        b.setimage('./pics/knightdungeon1-150x350.bmp',0,0,0)
##        self.gameobjects.append(b)
##        # upper crevasses
##        self.gameobjects.append(Box(0,0,375,75))
##        self.gameobjects.append(Box(375,0,100,100))
##        self.gameobjects.append(Box(475,0,100,125))
##        self.gameobjects.append(Box(500,0,120,180))
##        self.gameobjects.append(Box(600,0,50,160))
##        self.gameobjects.append(Box(650,0,25,75))
##        self.gameobjects.append(Box(675,0,75,40))
##        self.gameobjects.append(Box(750,0,50,40))
##        # lower crevasses
##        self.gameobjects.append(Box(500,220,120,400))
##        self.gameobjects.append(Box(0,400,800,100))
        #self.addnorthwall(0,0)
 
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
	
    def isroomupexit(self):
	if self.relativey  > 150:
		return 1
	return 0

    def setxyfromup(self):
        self.relativex = -640 
	self.relativey = -640

    def exit(self, game):
	if self.isroomupexit():
		self.setxyfromup()
		return 1 
	return 0 
 
    def collidesword(self,player):
        for i in self.gameobjects:
	    if i!= None:
	    	id = i.collidewithsword(self,player)
		#self.relativex = self.prevx
		#self.relativey = self.prevy
		return i ## NOTE : returns collided entity (single)
	return None


    def removeobject(self, o):
        for i in range(0,len(self.gameobjects)):
            if self.gameobjects[i] == o:
                self.gameobjects[i] = None
