
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
from maproomcastle3 import *
from maproomcastle4 import *
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
	self.node1 = MaproomGraphNode(MaproomCastle1(0,0))
	self.graph.append(self.node1)
	self.node2 = MaproomGraphNode(MaproomCastle2(640,0)) ## NOTE x=640
	###self.graph.append(self.node2)
	self.node1.addrightconnection(self.node2)
	self.node3 = MaproomGraphNode(MaproomCastle3(640,480)) ## NOTE x=640
	###self.graph.append(self.node3)
	self.node2.adddownconnection(self.node3)
	self.node4 = MaproomGraphNode(MaproomCastle4(0,480)) ## NOTE x=640
	###self.graph.append(self.node3)
	self.node3.adddownconnection(self.node4)
	self.graphindex = 0

	self.elevators.append(Elevatorcatcntl(170+640,360-110,48,96)) ### 100 -> elevator.h == 96
 
    def draw(self,screen,player):
        # draw bg
	### print "789> rely=%d %s" % (self.relativey,self)
        ###FIX NOTE blit with these global relx rely 
        ###FIX NOTE xset yset
	### FIX blit this room with graph 
	screen.blit(self.graph[self.graphindex].current.background, (self.graph[self.graphindex].current.relativex, self.graph[self.graphindex].current.relativey))
	### self.graph[self.graphindex].current.draw(screen,player)
	
	### print "dir = %s sidedir = %s" % (self.direction, self.sidedirection)

	self.drawiter(screen,player,3,self.graph[self.graphindex])

	for i in self.elevators:
		i.draw(screen,self)
		### if i.collide(self,player) == 2 or i.moveflag != 0:
		if i.moveflag != 0:
			i.update(self,player)

    def drawiter(self, screen, player, depth, node):
	if depth > 0:
		### print "direction drawiter = %s conns = %s" % (self.direction,node.downconnections)
		### if going north or south, draw up and down connecteed rooms
		if self.direction == "north" or self.direction == "south" or self.sidedirection == "east" or self.sidedirection == "west":
			for c in node.upconnections:
				### print "UPCONNS= %s" % c.current
				c.current.xset(self.relativex+0)
				c.current.yset(self.relativey)
				c.current.draw(screen,player)
				self.drawiter(screen,player,depth-1,c)
			for c in node.downconnections:
				print "DOWNCONNS= %s" % c.current
				c.current.xset(self.relativex+0)
				c.current.yset(self.relativey)
				c.current.draw(screen,player)
				self.drawiter(screen,player,depth-1,c)
			for c in node.leftconnections:
				c.current.xset(self.relativex+0)
				c.current.yset(self.relativey)
				c.current.draw(screen,player)
				self.drawiter(screen,player,depth-1,c)
			for c in node.rightconnections:
				c.current.xset(self.relativex)
				c.current.yset(self.relativey)
				c.current.draw(screen,player)
				self.drawiter(screen,player,depth-1,c)



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
	if self.direction == "south": ### FIX south ?
		for c in self.graph[self.graphindex].downconnections:
			c.current.yset(self.relativey)
	if self.direction == "north":
		for c in self.graph[self.graphindex].upconnections:
			c.current.yset(self.relativey)
	if self.sidedirection == "east":
		for c in self.graph[self.graphindex].leftconnections:
			c.current.xset(self.relativex)
	if self.sidedirection == "west":
		for c in self.graph[self.graphindex].rightconnections:
			c.current.xset(self.relativex)


	####fall = self.falliter(player, self.graph[self.graphindex].rightconnections[0].downconnections[0], 3)
	fall = self.falliter(player, self.graph[self.graphindex], 4)
	#print "fall=%s" % fall 
	if fall > 0:
		return fall
	else:	
        	return 0

#        for i in self.graph[self.graphindex].current.gameobjects:
#		### NOTE if colliding down on a platform, yset sets the
#		# y value to the coord of the non-faller
#	    if i != None and i.fallcollide(self, player): 
#                self.movedown()
#		print "direction = %s conns= %s" % (self.direction,self.graph[self.graphindex].downconnections)
#			#test
#		#if self.graph[self.graphindex].downconnections:
#		###	self.graph[self.graphindex].downconnections[0].current.xset(self.relativey)
#		if self.direction == "south":
#			for c in self.graph[self.graphindex].upconnections:
#				c.current.yset(self.relativey)
#		if self.direction == "north":
#			for c in self.graph[self.graphindex].downconnections:
#				c.current.yset(self.relativey)
#				#test 
#				self.graph[self.graphindex].downconnections[0].current.xset(self.relativey)
#		if self.sidedirection == "east":
#			for c in self.graph[self.graphindex].leftconnections:
#				c.current.xset(self.relativex+0)
#		if self.sidedirection == "west":
#			for c in self.graph[self.graphindex].rightconnections:
#				c.current.xset(self.relativex+0)
#		return 2 # 1 kills game
#       	return self.falliter(player, 


    def falliter(self, player, node, depth):
	### print ">>>>>>>>>>falliter noderoom=%s direction = %s " % (node.current,self.direction)
	if depth > 0:
        	for i in node.current.gameobjects:
		    	if i != None and i.fallcollide(node.current, player): 
       	        		self.movedown()
				print "FALLCOLLIDE CATCASTLE1 falliter direction = %s sidedirection = %s node.currentroom=%s conns= %s" % (self.direction,self.sidedirection, node.current,node.downconnections)
				return 2
		if self.direction == "north" or self.sidedirection == "west" or self.sidedirection == "east":
			for n in node.downconnections:
				n.current.yset(self.relativey)
				return self.falliter(player,n,depth-1)
			for n in node.upconnections:
				n.current.yset(self.relativey)
				return self.falliter(player,n,depth-1)
			for n in node.leftconnections:
				n.current.xset(self.relativex+0)
				return self.falliter(player,n,depth-1)
			for n in node.rightconnections:
				n.current.xset(self.relativex+0)
				return self.falliter(player,n,depth-1)
		###	return 2 # 1 kills game
	return 0
	
    def collideup(self, player): ### KLU	
	for i in self.graph[self.graphindex].current.gameobjects:
	    if i != None and i.collideup(self, player) == 1:
		return 2
	return 0

    def yplus(self,dy):
	self.relativey += dy
	MaproomGraph.yplus(self,dy,self.graphindex)

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
			el.moveflag = 2 
			el.roomstarty = room.relativey


    def MOVEDOWN(self, room, player):
	for el in self.elevators:
		if el.collide(self,player) == 2:
			el.moveflag = 1
