
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

class ManaBlock: 
	def __init__(self):
        	self.image = pygame.image.load('./pics/mana-17x14.bmp').convert()
        	self.image.set_colorkey((0,0,0))
        	#self.imagemax = pygame.image.load('./pics/life1.bmp').convert()
        	#self.imagemax.set_colorkey((0,0,0))
		
class ManaHalfBlock: 
	def __init__(self):
        	self.image = pygame.image.load('./pics/mana-half-17x14.bmp').convert()
        	self.image.set_colorkey((0,0,0))
        	#self.imagemax = pygame.image.load('./pics/life1.bmp').convert()
        	#self.imagemax.set_colorkey((0,0,0))
		
class ManaEmptyBlock: 
	def __init__(self):
        	self.image = pygame.image.load('./pics/mana-empty-17x14.bmp').convert()
        	self.image.set_colorkey((0,0,0))
        	#self.imagemax = pygame.image.load('./pics/life1.bmp').convert()
        	#self.imagemax.set_colorkey((0,0,0))
		

class ManaMeter:
    "mana meter"
    def __init__(self,xx,yy):
	self.max = 50 
	self.index = 50
	self.hearts = []
	self.div = 10
	self.x = xx
	self.y = yy 

	for i in range(0,self.index/self.div):
		self.hearts.append(ManaBlock())

    def set(self, hp):
	self.index = hp	
	for i in range(self.index/self.div, self.max/self.div):
		if i:
			self.hearts[i] = ManaEmptyBlock() 

    def draw(self,screen,font):
	lifestr = "mana - %d" % (self.max/self.div); 	
        screen.blit(font.render(lifestr, 8, (255,255,255)), (17+self.x,3+self.y))
	j = 0
	for i in self.hearts:
		#if i != None:
        	screen.blit(i.image, (self.x+17+j*17, self.y+26))
		j += 1
