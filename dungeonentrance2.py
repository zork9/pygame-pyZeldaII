
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

class Dungeonentrance2(Gameobject):
    "Dungeon entrance 1"
    def __init__(self, xx,yy):
	Gameobject.__init__(self,xx,yy)	
	self.w = 70
        self.h = 70 
        self.image = pygame.image.load('./pics/dungeon-entrance2-48x48.bmp').convert()
        self.image.set_colorkey((0,0,0)) 

    def collide(self, room, player):
	if (player.x > self.x+room.relativex  and 
	player.x < self.x+room.relativex+self.w and 
	player.y > self.y+room.relativey and 
	player.y < self.y+room.relativey + self.h):
	    print "collision with Dungeon Entrance 2! x=%d y=%d" % (room.relativex,room.relativey) 
	    ###if player.hit():
	    return 3 ###NOTE 3 for dungeon walls and entrances bounc back ## 4 ?
	return 0

    ### NOTE: dungeon master key gets checked in game.py and this opens with return 2
    def pickup(self, room):
        ###room.removeobject(self)
	return 2
