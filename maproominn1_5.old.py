
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
from blackknight import *
from demon import *
from bombman import *
from turtleflying import *
from ghost1 import *
from ghostwandering import *
from ghostcircling import *
from maproom2 import *
from dungeonmasterkey import *
from dungeonkey1 import *
from mithran import *
from innguardian3 import *
from inndoor import *

class Maproominn1_5(Maproom):
    "Room with a (big) map - Inside Inn"
    def __init__(self,x,y):
        Maproom.__init__(self,x,y)
        self.background = pygame.image.load('./pics/room-bginn1_5.bmp').convert()
        # Inn upper walls
	self.gameobjects.append(Dungeonwall(0,0,160,200))
	self.gameobjects.append(Dungeonwall(0,0,320,120))
	self.gameobjects.append(Dungeonwall(400,300,300,100))
	self.gameobjects.append(Dungeonwall(500,0,200,500))
        # Inn lower walls
        self.gameobjects.append(Dungeonwall(0,300,160,200))
        self.gameobjects.append(Dungeonwall(0,400,500,700))
        self.gameobjects.append(Dungeonwall(440,280,260,220))
        # Inn table
        self.gameobjects.append(Dungeonwall(220,180,160,220))
        # door
        self.gameobjects.append(InnDoor(320,25))
        # guardian
        self.guardian = InnGuardian3(460,90)
        self.gameobjects.append(self.guardian)
        
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
	    if i!= None:
	    	id = i.collide(self,player)
		self.relativex = self.prevx
		self.relativey = self.prevy
		return id
	return 0

    def pickup(self, player):###FIX for each room
        for o in self.gameobjects:
            if (o and o.collide(self, player)):##FIX o.colidepickup
                id = o.pickup(self)
                self.dungeonkey1 = 1
		return id
        return 0
    
    def exit(self, game):
        # FIX
	return 0

    def removeobject(self, o):
        for i in (0,len(self.gameobjects)-1):
            print "o=%s self.gameobjects[i]=%s i=%d" % (o,self.gameobjects[i],i)
            if self.gameobjects[i] == o:
                print "PICKUP or die"
                self.gameobjects[i] = None
		return 

    def collidesword(self,room,player):
        for i in self.gameobjects:
	    if i!= None:
	    	c = i.collide(room,player)
	    	print "i=%s" % i
		if c == 1:
                        print "collision with i=%s!" % i
			return i ## NOTE : returns collided entity (single)
		self.relativex = self.prevx
		self.relativey = self.prevy
	return None

    def setxyfromdoor(self):
        self.relativex = -50
        self.relativey = -350
    
    def isroomdoorexit(self):
	if self.relativex < -140 and self.relativex > -190 and self.relativey > -250 and self.relativey < -230:
            return 1
        return 0

    def setxyfromdoor2(self):
        self.relativex = 0
        self.relativey = 0
    
    def isroomdoorexit2(self):
	if self.relativey > 100:
            return 1
        return 0
    
    def exit(self, game):
        print "x=%d y=%d" % (self.relativex,self.relativey)
	if self.isroomdoorexit():
            self.setxyfromdoor()
            return 1.4
        elif self.isroomdoorexit2():
            self.setxyfromdoor2()
            return 1.6  
##	elif self.isroomdownexit():
##	    self.setxyfromdown()	    
##	    return 1.2
##	#Trap door: elif self.isroomdownexit():
##	#    self.setxyfromdown()	
##	#    return 11
##	else:
	return 0

    def talkto(self):#FIXME needs font
            print "talk to in maproom 1_3"
            ## return self.koboldwiz
            self.guardian.talkcounter = 1
            return self.guardian
