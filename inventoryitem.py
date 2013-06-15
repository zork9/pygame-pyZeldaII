
# Copyright (C) Johan Ceuppens 2011
# Copyright (C) Johan Ceuppens 2010

# Copyright (C) Johan Ceuppens 2009 
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


class Inventoryitem(object):
    def __init__(self,imagefilename):
        self.image = pygame.image.load(imagefilename).convert()
        self.image.set_colorkey((0,0,0))#FIXME rgb transdparency

    def draw(self,screen,x,y):
        screen.blit(self.image, (x, y))

    def addtolist(self,list):
        list.addobject(self)


#NOTE There s no fallthrough for item usage
