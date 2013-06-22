
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
class MaproomNorthDungeonWall:
    "Room with a (big) map"
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.w = 60
        self.h = 48
        self.wallimage = pygame.image.load('./pics/walldungeon1-60x48.bmp')
        
        
    def draw(self,screen,relativex,relativey):
	##print "x=%d" % self.relativex 
        screen.blit(self.wallimage, (self.x+relativex, self.y+relativey))
