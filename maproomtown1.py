
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
from elfwoman1town1 import *
from elfwoman2town1 import *

class MaproomTown1(MaproomDungeon):
    "Room with a (big) map"
    def __init__(self,x,y):
        MaproomDungeon.__init__(self,x,y)
        self.background = pygame.image.load('./pics/bg-town-1-2000x600.bmp').convert()
	# ground level
        self.gameobjects.append(Box(0,440,2000,400))
        self.gameobjects.append(Elfwoman1Town1(800,332))
        self.gameobjects.append(Elfwoman2Town1(400,332))
	self.changeroomnumber = 0
 
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
	if self.relativex  < -2000+460:
		return 1
	return 0

    def setxyfromup(self):
        self.relativex = -640 
	self.relativey = -640

    def exit(self, game):
	if self.isroomupexit():
		self.setxyfromup()
		return 1.1 
	return 0 


    def collideup(self, player):
	return 0
  
    def collidesword(self,player):
        for i in self.gameobjects:
	    if i!= None:
	    	id = i.collidewithsword(self,player)
		#self.relativex = self.prevx
		#self.relativey = self.prevy
		return i ## NOTE : returns collided entity (single)
	return None

    def talkto(self,player):
	for i in self.gameobjects:
		print "i=%s" % i
		if i.collide(self,player):
        		return i 
	return None

	### NOTE town 1 collides for going inside houses
    def MOVEDOWN(self,room,player):

	print "DOWN> %d %d" % (room.relativex,player.x)

	if room.relativex < -700 + player.x and room.relativex > -750 + player.x:
		room.changeroomnumber = 3.1 
	if room.relativex < -1110 + player.x and room.relativex > -1160 + player.x:
		room.changeroomnumber = 3.2



    def removeobject(self, o):
        for i in range(0,len(self.gameobjects)):
            if self.gameobjects[i] == o:
                self.gameobjects[i] = None
