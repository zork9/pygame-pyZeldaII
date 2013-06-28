
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

class MaproomGraphNode:
    "Room lst ADT"
    def __init__(self, current):
	self.leftconnections = [] 
	self.rightconnections = [] 
	self.upconnections = [] 
	self.downconnections = [] 
	self.current = current ### This is the Room itself
 
class MaproomGraph:
    "Room lst ADT"
    def __init__(self):
	self.graph = []
	
    def addleftconnection(self, index, node):
	self.graph[index].leftconnections.append(node)

    def addrightconnection(self, index, node):
	self.graph[index].rightconnections.append(node)

    def addupconnection(self, index, node):
	self.graph[index].upconnections.append(node)

    def adddownconnection(self, index, node):
	self.graph[index].downconnections.append(node)

    def moveupnode(self, index):
	self.graph[index].current.moveup()
	for i in self.graph[index].downconnections:
		i.current.moveup()

    def movedownnode(self, index):
	self.graph[index].current.movedown()
	for i in self.graph[index].upconnections:
		i.current.movedown()

    def moveleftnode(self, index):
	self.graph[index].current.moveleft()
	for i in self.graph[index].rightconnections:
		i.current.moveleft()

    def moverightnode(self, index):
	self.graph[index].current.moveright()
	for i in self.graph[index].leftconnections:
		i.current.moveright()

    def yplus(self, dy, index):
	### FIX use yset for all
	self.graph[index].current.yplus(dy)
	for c in self.graph[index].leftconnections:
		c.current.yplus(dy)
	for c in self.graph[index].rightconnections:
		c.current.yplus(dy)
	for c in self.graph[index].upconnections:
		c.current.yplus(dy)
	for c in self.graph[index].downconnections:
		c.current.yplus(dy)

    def xset(self, x, index):
	### FIX use yset for all
	print "8888888888888888> %s" % self.graph[index].current
	self.graph[index].current.xset(x)

    def xget(self, index):
	### FIX use yset for all
	return self.graph[index].current.xget()

    def yset(self, y, index):
	### FIX use yset for all
	print "8888888888888888> %s" % self.graph[index].current
	self.graph[index].current.yset(y)

    def yget(self, index):
	### FIX use yset for all
	return self.graph[index].current.yget()

    def draw(self,screen,player):
	screen.blit(self.graph[self.graphindex].current.background, 
	(self.graph[self.graphindex].current.relativex, self.graph[self.graphindex].current.self.relativey))
	# FIX draw connections


