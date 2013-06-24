
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
from box import *

class TilemapBox(Box):
    "Box"
    def __init__(self, xx,yy,ww,hh):
        Box.__init__(self,xx,yy,ww,hh)
        self.w = ww
        self.h = hh
        self.hitpoints = 999999999 #FIX else wall/floor disappears
	self.changeroomnumber = 0 

    def collidego(self, room, player):
	if (player.x-room.relativex > self.x  and 
	player.x-room.relativex < self.x+self.w and 
	player.y-room.relativey > self.y and 
	player.y-room.relativey < self.y + self.h):
	    print "collision with TilemapBox (collidego)"
	    room.changeroom(self.changeroomnumber)
	    return 1 
	else:
	    return 0 ## for game self.talker
