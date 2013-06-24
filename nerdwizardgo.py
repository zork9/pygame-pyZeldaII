
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
from commongo import *
from stateimagelibrary import *

class NerdWizardGO(CommonGO):
    "Game object"
    def __init__(self, xx,yy):
	CommonGO.__init__(self,xx,yy)	

	self.x = xx 
        self.y = yy
	# default width and height 
        self.w = 24 
        self.h = 24
        image = pygame.image.load('./pics/nerd-left-1-24x24.bmp').convert()
        image.set_colorkey((255,255,255)) 
	self.stimlib.addpicture(image)
        image = pygame.image.load('./pics/nerd-left-1-24x24.bmp').convert()
        image.set_colorkey((255,255,255)) 
	self.stimlib.addpicture(image)
        image = pygame.image.load('./pics/nerd-left-1-24x24.bmp').convert()
        image.set_colorkey((255,255,255)) 
	self.stimlib.addpicture(image)
        image = pygame.image.load('./pics/nerd-left-1-24x24.bmp').convert()
        image.set_colorkey((255,255,255)) 
	self.stimlib.addpicture(image)
        image = pygame.image.load('./pics/nerd-right-1-24x24.bmp').convert()
        image.set_colorkey((255,255,255)) 
	self.stimlib.addpicture(image)
        image = pygame.image.load('./pics/nerd-right-1-24x24.bmp').convert()
        image.set_colorkey((255,255,255)) 
	self.stimlib.addpicture(image)
        image = pygame.image.load('./pics/nerd-right-1-24x24.bmp').convert()
        image.set_colorkey((255,255,255)) 
	self.stimlib.addpicture(image)
        image = pygame.image.load('./pics/nerd-right-1-24x24.bmp').convert()
        image.set_colorkey((255,255,255)) 
	self.stimlib.addpicture(image)
        self.hitpoints = 1000000000
        # NOTE : decrease 1 hitpoint with default sword
        self.hitf = self.hit1
        
