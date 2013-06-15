
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
from koboldwizard import *
from time import *
from maproom import *

# each wall has its own pic, for dithered and changed images
class MaproomDungeonWall:
    "Room with a (big) map"
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.wallimage = pygame.image.load('./pics/walldungeon1-60x48.bmp')
        
        
##    def draw(self,screen,self.relativex,self.relativey):
##	##print "x=%d" % self.relativex 
##        screen.blit(self.wallimage, (relativex+self.x, relativey+self.y))

    def collide(self, room, player):
	if (player.x > self.x+room.relativex  and 
	player.x < self.x+room.relativex+self.w and 
	player.y > self.y+room.relativey and 
	player.y < self.y+room.relativey + self.h):
	    print "collision in Dungeon Wall!"	
	    return 1 
	else:
	    return 0

    def collidepickup(self, room, player):
	if (player.x > self.x+room.relativex-self.w  and 
	player.x < self.x+room.relativex+self.w and 
	player.y > self.y+room.relativey-self.h and 
	player.y < self.y+room.relativey + self.h):
	    #print "collision!"	
	    return 1 
	else:
	    return 0 
    
    def collideobjectX(self, room):
	for i in room.gameobjects:
	    if i != None:	
	        if (self.x > i.x  and 
		    self.x < i.x+i.w):
	            return 1 
	return 0

    def collideobjectY(self, room):
	for i in room.gameobjects:
	    if i != None:	
	        if (self.y > i.y  and 
		    self.y < i.y+i.h):
	            return 1 
	return 0
 
    def collideobjectXY(self, room):
	for i in room.gameobjects:
	    if i:		
	        if (self.x > i.x  and 
	 	    self.x < i.x+i.w and 
	            self.y > i.y and 
	            self.y < i.y+i.h):
	            return 1 
	return 0 
