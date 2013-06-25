
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
###from maproomdungeonwall import *

# each wall has its own pic, for dithered and changed images
class MaproomWestDungeonWall:
    ""
    def __init__(self,x,y,w,h):
        self.x = x
        self.y = y
        self.w = w 
        self.h = h 
        self.wallimage = pygame.image.load('./pics/walldungeon1-60x48.bmp')
        
    def collide(self, room, player):
	if (player.x > self.x+room.relativex  and 
	player.x < self.x+room.relativex+self.w and 
	player.y > self.y+room.relativey and 
	player.y < self.y+room.relativey + self.h):
	    print "collision in Dungeon Wall!"	
	    return 2 
	else:
	    return 0

        
    def draw(self,screen,room):
	##print "x=%d" % self.relativex 
        screen.blit(self.wallimage, (self.x+room.relativex, self.y+room.relativey))
