
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
from maproomcat import *
from maproomcastle1 import *
from maproomcastle2 import *
from maproomgraph import *
from maproomdungeonnorthwall import *
from tilebox import *
from rope import *
#from snake1 import *
from rubysword import *
from digdogger import *
from ironknuckle import *
from deeler import *
from daira import *
from elevatorcatcntl import *

class MaproomCatCastle1(MaproomGraph, MaproomCat):
    "Room with a (big) map"
    def __init__(self,xx,yy):
        MaproomGraph.__init__(self)
        MaproomCat.__init__(self,xx,yy)
	node1 = MaproomGraphNode(MaproomCastle1(0,0))
	self.graph.append(node1)
	node2 = MaproomGraphNode(MaproomCastle2(640,0)) ## NOTE x=640
	###self.graph.append(node2)
	self.addrightconnection(0,node2)
	self.graphindex = 0

	self.elevators.append(Elevatorcatcntl(100+640,360-110,48,96)) ### 100 -> elevator.h == 96
 
    def draw(self,screen,player):
        # draw bg
	### print "789> rely=%d %s" % (self.relativey,self)
        ###FIX NOTE blit with these global relx rely 
        ###FIX NOTE xset yset 
	screen.blit(self.graph[self.graphindex].current.background, (self.graph[self.graphindex].current.relativex, self.graph[self.graphindex].current.relativey))
	### self.graph[self.graphindex].current.draw(screen,player)
	
	### print "dir = %s sidedir = %s" % (self.direction, self.sidedirection)
	if self.direction == "south":
		for c in self.graph[self.graphindex].upconnections:
			c.current.xset(self.relativex+0)
			c.current.yset(self.relativey)
			c.current.draw(screen,player)
	if self.direction == "north":
		for c in self.graph[self.graphindex].downconnections:
			c.current.xset(self.relativex+0)
			c.current.yset(self.relativey)
			c.current.draw(screen,player)
	if self.sidedirection == "east":
		for c in self.graph[self.graphindex].leftconnections:
			c.current.xset(self.relativex+0)
			c.current.yset(self.relativey)
			c.current.draw(screen,player)
	if self.sidedirection == "west":
		for c in self.graph[self.graphindex].rightconnections:
			c.current.xset(self.relativex)
			c.current.yset(self.relativey)
			c.current.draw(screen,player)
	for i in self.elevators:
		if i.collide(self,player) == 2:
			i.update(self,player)
		i.draw(screen,self)
	
	#for i in self.elevators:
	#	i.update(self,player)
	####### FIX update code for elevator of concatrooms
    def moveup(self):
        MaproomGraph.moveupnode(self, self.graphindex)
        MaproomCat.moveup(self)

    def movedown(self):
        MaproomGraph.movedownnode(self, self.graphindex)
        MaproomCat.movedown(self)

    def moveleft(self):
        MaproomGraph.moveleftnode(self,self.graphindex)
        MaproomCat.moveleft(self)

    def moveright(self):
        MaproomGraph.moverightnode(self,self.graphindex)
        MaproomCat.moveright(self)

    def fall(self, player):
        self.moveup()
	if self.direction == "south":
		for c in self.graph[self.graphindex].upconnections:
			c.current.yset(self.relativey)
	if self.direction == "north":
		for c in self.graph[self.graphindex].downconnections:
			c.current.yset(self.relativey)
	if self.sidedirection == "east":
		for c in self.graph[self.graphindex].leftconnections:
			c.current.xset(self.relativex)
	if self.sidedirection == "west":
		for c in self.graph[self.graphindex].rightconnections:
			c.current.xset(self.relativex)
        for i in self.graph[self.graphindex].current.gameobjects:
	    if i != None and i.fallcollide(self, player):
                self.movedown()
		if self.direction == "south":
			for c in self.graph[self.graphindex].upconnections:
				c.current.yset(self.relativey)
		if self.direction == "north":
			for c in self.graph[self.graphindex].downconnections:
				c.current.yset(self.relativey)
		if self.sidedirection == "east":
			for c in self.graph[self.graphindex].leftconnections:
				c.current.xset(self.relativex+0)
		if self.sidedirection == "west":
			for c in self.graph[self.graphindex].rightconnections:
				c.current.xset(self.relativex+0)
		return 2 # 1 kills game
        
        return 0

	
    def collideup(self, player): ### KLU	
	for i in self.graph[self.graphindex].current.gameobjects:
	    if i != None and i.collideup(self, player) == 1:
		return 2
	return 0

    def yplus(self,dy): ### FIX NOTE KLU
	self.relativey += dy
	print "123> yplus=%d" % self.relativey
	MaproomGraph.yplus(self,dy,self.graphindex)

###	MaproomGraph.yset(self,self.relativey,self.graphindex)

###	MaproomCat.yplus(self,dy)

#    def yget(self):
#	print "123> y=%d" % self.relativey
#	MaproomGraph.yplus(self,dy,self.graphindex)
#	MaproomCat.yplus(self,dy)
#	self.relativey += dy

    def yset(self,y):
	self.relativey = dy

    def xset(self,x):
	self.relativex = dx

    def MOVEUP(self, room, player):
	for el in self.elevators:
		if el.collide(self,player) == 2:
			el.moveflag = 1	
    def MOVEDOWN(self, room, player):
	for el in self.elevators:
		if el.collide(self,player) == 2:
			el.moveflag = 1	
