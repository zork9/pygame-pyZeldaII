
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
from maproom1 import *
from tree import *
from knightstatue1 import *
from dungeonwall import *
from koboldwizard import *
from dungeonstatue2 import *
from dungeonstatue3 import *
from dungeonentrance2 import *
from knight2 import *
from time import *

class Maproom6(Maproom):
    "Room with a (big) map"
    def __init__(self,x,y):
        Maproom.__init__(self,x,y)
        self.background = pygame.image.load('./pics/room-bg6.bmp').convert()
        self.gameobjects.append(Dungeonwall(0,0,300,40))
	self.gameobjects.append(Dungeonwall(0,260,40,300))
	self.gameobjects.append(Dungeonwall(0,0,40,300))
	self.gameobjects.append(Dungeonwall(0,260,300,40))
        self.gameobjects.append(Dungeonstatue2(100,76))
        self.gameobjects.append(Dungeonstatue3(160,76))
        self.gameobjects.append(Dungeonentrance2(130,0))
	#self.koboldwiz = KoboldWizard(100,60)
        #self.gameobjects.append(self.koboldwiz)
	self.knight = Knight2(50,50)
	self.gameobjects.append(self.knight)
        self.flag = 0
 
    def draw(self,screen):
        ###FIX numpy ### a = pygame.surfarray.pixels3d(pygame.display.get_surface())
        ###a = pygame.surfarray.array3d(pygame.display.get_surface())
	###a = pygame.display.get_surface().copy()
        #FIXif self.flag == 1:
        screen.blit(self.background, (0+self.relativex, 0+self.relativey))
        for i in self.gameobjects:
            if i != None:
                i.draw(screen,self)
        return
        
##	
##        for i in range(0,300):
##            for j in range(0,300):
##                ###c = a[j][i]
##                R = 255 >> 1
##                G = 0
##                B = 0
##                color = (R,G,B) ###(c[0],c[1],c[2])
##                
##                pygame.draw.line(pygame.display.get_surface(),color,(j,i),(j,i))
##        pygame.display.update()
##        sleep(.1)
##        for i in range(0,300):
##             for j in range(0,300):
##                ###c = a[j][i]
##                R = 255 >> 2
##                G = 0
##                B = 0
##                color = (R,G,B) ###(c[0],c[1],c[2])
##                
##                pygame.draw.line(pygame.display.get_surface(),color,(j,i),(j,i))
##        pygame.display.update()
##        sleep(.1)
##        for i in range(0,300):
##            for j in range(0,300):
##                ###c = a[j][i]
##                R = 255 >> 2
##                G = 0
##                B = 0
##                color = (R,G,B) ###(c[0],c[1],c[2])
##                
##                pygame.draw.line(pygame.display.get_surface(),color,(j,i),(j,i))
##        pygame.display.update()
##        sleep(.1)
##        for i in range(0,300):
##            for j in range(0,300):
##                ###c = a[j][i]
##                R = 0
##                G = 0
##                B = 0
##                color = (R,G,B) ###(c[0],c[1],c[2])
##                
##                pygame.draw.line(pygame.display.get_surface(),color,(j,i),(j,i))
##	self.flag = 1
	
    def collide(self, player):
	for i in self.gameobjects:
	    if i != None:
		i.update(self)	
	for i in self.gameobjects:
            if i != None:
                c = i.collide(self,player)
                ###FIX in all maproom collisions
		if c != 0:###FIXME put this in other room collides also
                    #print "->i=%s c=%s" % (i,c)
                    return c
		self.relativex = self.prevx
		self.relativey = self.prevy
	return 0

    def exit(self, game):
        if self.isroomupexit():
	    self.setxyfromup()	
	    return 7
	elif self.isroomdownexit():
	    self.setxyfromdown()	
	    return 5
##        if self.relativey > 100 and self.relativex > -10 and self.relativex < 20:
##	    game.setxy(0,80)
##	    return 4
##	elif self.relativey < -100 and self.relativex > -10 and self.relativex < 20:
##	    game.setxy(0,-25)
##	    return 1
##	if self.relativex < -100 and self.relativey > -10 and self.relativey < 20:
##	    game.setxy(0,0)
##	    return 7
	else:
	    return 0

	def talkto(self):#FIXME needs font
            print "talk to in maproom 6"
            ## return self.koboldwiz
            self.knight.talkcounter = 1
            return self.knight

##        def pickup(self, player):
##            for o in self.gameobjects:
##                if (o and o.collidepickup(self, player)):
##                    id = o.pickup(self)
##                    return id
##            return 0

    def removeobject(self, o):
        for i in self.gameobjects:
            if o:
                if o == i:
                    i = None##FIXME1

    def removeentrance2(self):
        self.gameobjects[6] = None
               
    def collidesword(self,room,player):
        for i in self.gameobjects:
	    if i!= None:
	    	c = i.collide(room,player)
		if c == 1:
			return i ## NOTE : returns collided entity (single)
		self.relativex = self.prevx
		self.relativey = self.prevy
	return None
