
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
from rope import *
#from snake1 import *
from rubysword import *
from beholder import *
from beholderbat import *
from digdogger import *
from ironknuckle import *
from deeler import *
from daira import *

class MaproomCastle1(MaproomDungeon):
    "Room with a (big) map"
    def __init__(self,x,y):
        MaproomDungeon.__init__(self,x,y)
        #self.background = pygame.image.load('./pics/parapapalace-test.bmp').convert()
        self.background = pygame.image.load('./pics/parapapalace-test.bmp').convert()

	self.WIDTH = 640


        ###self.northwall1 = Tilebox(1,1,60,48,16,1,'./pics/walldungeonnorth2-beholderglass-60x48.bmp')
##        self.northwall1 = Tilebox(1,1,60,48,13,1,'./pics/walldungeonnorth1-60x48.bmp')
##        self.southwall1 = Tilebox(1,200,30,48,13,1,'./pics/walldungeonsouth1-30x48.bmp')
##        self.westwall1 = Tilebox(360,200,48,60,1,10,'./pics/walldungeonwest1-48x60.bmp')
##        self.eastwall1 = Tilebox(775,1,48,60,1,14,'./pics/walldungeoneast1-48x60.bmp')
##        self.tileboxes.append(self.northwall1)
##        self.tileboxes.append(self.westwall1)
##        self.tileboxes.append(self.eastwall1)
##        self.tileboxes.append(self.southwall1)

        ### self.gameobjects.append(Ironknuckle(600,300))
        
        # left NOTE : boxes collide so put them after enemies !
	# roof
        # self.gameobjects.append(Box(0,65,self.WIDTH,50))
	# base
        self.gameobjects.append(Box(0,422,self.WIDTH,400))

	# castle floors
        self.gameobjects.append(Box(200,390,self.WIDTH,400))
        self.gameobjects.append(Box(280,360,self.WIDTH,400))


##        self.gameobjects.append(Bullfrog(500,225))
##        self.gameobjects.append(Bullfrog(600,225))
        # right
        #self.gameobjects.append(Box(650,275,1750,80))
        # left under
        #self.gameobjects.append(Box(0,475,self.WIDTH,80))
##        self.gameobjects.append(Bullfrog(800,425))
##        self.gameobjects.append(Bullfrog(900,425))
        # ropes       
        #self.ropes.append(Rope(605,100,300))

        
 
    def draw(self,screen,player):
        # draw bg
	print "abc> %d" % self.relativey
        ### is in maproomdungeon screen.blit(self.background, (0+self.relativex, 0+self.relativey))
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
	for i in self.ropes:
	    if i != None:
		i.update(self,player)
		i.draw(screen,self)
		
    def isroomdownexit(self):
	if self.relativex  < -500:
		return 1
	return 0

    def setxyfromdown(self):
        self.relativex = 0
	self.relativey = 0

    def exit(self, game):
	if self.isroomdownexit():
		self.setxyfromdown()
		return 2 
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
	### pr.nt "relx=%d" % r.relativex

    def removeobject(self, o):
        for i in range(0,len(self.gameobjects)):
            if self.gameobjects[i] == o:
                self.gameobjects[i] = None
