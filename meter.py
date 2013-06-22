
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

class Heart:
	def __init__(self):
        	self.image = pygame.image.load('./pics/heart.bmp').convert()
        	self.image.set_colorkey((0,0,0))
        	#self.imagemax = pygame.image.load('./pics/life1.bmp').convert()
        	#self.imagemax.set_colorkey((0,0,0))
		

class Meter:
    "life or mana meter"
    def __init__(self):
	self.max = 50 
	self.index = 50
	self.hearts = []
	for i in range(0,3):
		self.hearts.append(Heart())
 
    def draw(self,screen):
	# KLUDGY
	j = 0
	for i in range(0,self.index/10):
        	screen.blit(self.hearts[0].image, (17+j*12, 26))
		j += 1
