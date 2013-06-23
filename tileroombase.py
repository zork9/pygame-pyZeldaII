
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

class TileroomBase:
    "Room with a (big) map"
    def __init__(self,xx,yy):
	self.x = xx
	self.y = yy
	self.relativex = 0
	self.relativey = 0
	self.tile1 = pygame.image.load('./pics/tile-grass-1.bmp').convert()
	self.WIDTH = 160 
	self.HEIGHT = 48 
	self.TILEWIDTH = 16
	self.TILEHEIGHT = 16
         
	self.tilelist =	[], 
	self.gameobjects = []

    def draw(self,screen,player):
        # draw bg
###        screen.blit(self.background, (0+self.relativex, 0+self.relativey))
        # draw walls
###        MaproomDungeon.draw(self,screen)
	for y in range(0, self.WIDTH / self.TILEWIDTH):
		for x in range(0, self.HEIGHT / self.TILEHEIGHT):
			if self.tilelist[x][y] == 1:	
				screen.blit(self.tile1, (self.x+x*self.TILEWIDTH+self.relativex, self.y+y*self.TILEHEIGHT+self.relativey))
			elif self.tilelist[x][y] == 2:	
				screen.blit(self.tile2, (self.x+x*self.TILEWIDTH+self.relativex, self.y+y*self.TILEHEIGHT+self.relativey))

		
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
	return None

    def collideswordlow(self,player):
	return None

    def collideup(self,player):
	return None

    def collidewithropes(self,player):
	return None

    def collide(self,player):
	return None

    def fall(self,player):
	return None

    def moveleft(self):
	self.relativex -= 10

    def moveright(self):
	self.relativex += 10

    def moveup(self):
	self.relativey -= 10

    def movedown(self):
	self.relativey += 10

    def MOVEDOWN(self):
	self.relativey += 10

    def MOVEUP(self):
	self.relativey -= 10

    def removeobject(self, o):
        for i in range(0,len(self.gameobjects)):
            if self.gameobjects[i] == o:
                self.gameobjects[i] = None
