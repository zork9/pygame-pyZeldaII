
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
from gameobject import *

class Boxcat(Gameobject):
    "Box"
    def __init__(self, xx,yy,ww,hh):
        Gameobject.__init__(self,xx,yy)
        self.w = ww
        self.h = hh
        self.hitpoints = 999999999 #FIX else wall/floor disappears
        #FIX is in base class self.image = pygame.image.load('./pics/.bmp').convert()
        #self.image.set_colorkey((0,0,0)) 

    def setimage(self, imagefilename,r,g,b):
        self.image = pygame.image.load(imagefilename).convert()
        self.image.set_colorkey((r,g,b)) 

    def collide(self, room, player):
	if (player.x > self.x+room.relativex  and 
	player.x < self.x+room.relativex+self.w and 
	player.y > self.y+room.relativey and #FIXED +self.h
	player.y < self.y+room.relativey + self.h):
	    print "collision in catbox!"	
	    return 2 
	else:
	    return 0

	### for in room.roofs list
    def collideup(self, room, player):
            ###print 'collideup gameobject x=%d y=%d player x=%d y=%d' % (self.x,self.y,player.x-room.relativex,player.y-room.relativey)
	    return 0


    def fallcollide(self, room, player):
        # FIX BUG
        ### print 'fallcollide gameobject x=%d y=%d player x=%d y=%d' % (self.x,self.y,player.x-room.relativex,player.y-room.relativey)
	if (player.x-room.relativex > self.x  and 
	player.x-room.relativex < self.x+self.w and 
	player.y-room.relativey+player.h > self.y and 
	player.y-room.relativey < self.y + self.h):
	    print "collision with Boxcat!"
	    return 1 
	else:
	    return 0 ## for game self.talker
