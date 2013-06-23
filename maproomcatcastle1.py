
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
from maproomcat import *
from maproomcastle1 import *
from maproomgraph import *
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

class MaproomCatCastle1(MaproomGraph, MaproomCat):
    "Room with a (big) map"
    def __init__(self,xx,yy):
        MaproomGraph.__init__(self)
        MaproomCat.__init__(self,xx,yy)
        #self.background = pygame.image.load('./pics/parapapalace-test.bmp').convert()
	self.graph.append(MaproomGraphNode(MaproomCastle1(0,0)))

	self.graphindex = 0
 
    def draw(self,screen,player):
        # draw bg
        ###screen.blit(self.background, (0+self.relativex, 0+self.relativey))
	self.graph[self.graphindex].current.draw(screen,player)
	
	print "dir = %s sidedir = %s" % (self.direction,self.sidedirection)
	if self.direction == "south":
		for c in self.graph[self.graphindex].upconnections:
			c.draw(screen,player)
	if self.direction == "north":
		for c in self.graph[self.graphindex].downconnections:
			c.draw(screen,player)
	if self.sidedirection == "east":
		for c in self.graph[self.graphindex].leftconnections:
			c.draw(screen,player)

	if self.sidedirection == "west":
		for c in self.graph[self.graphindex].rightconnections:
			c.draw(screen,player)

    def moveup(self):
        MaproomGraph.moveup(self,self.graphindex)
        MaproomCat.moveup(self)

    def movedown(self):
        MaproomGraph.movedown(self,self.graphindex)
        MaproomCat.movedown(self)

    def moveleft(self):
        MaproomGraph.moveleft(self,self.graphindex)
        MaproomCat.moveleft(self)

    def moveright(self):
        MaproomGraph.moveright(self,self.graphindex)
        MaproomCat.moveright(self)

	
