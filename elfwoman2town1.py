
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
from stateimagelibrary import *
import random
from elfwomantown import *

class Elfwoman2Town1(ElfwomanTown):
    ""
    def __init__(self,xx,yy):
	ElfwomanTown.__init__(self, xx, yy)
	self.stimlibleft = Stateimagelibrary()	
        image = pygame.image.load('./pics/elf-woman-2-32x96.bmp').convert()
        image.set_colorkey((255,255,255)) 
	self.stimlibleft.addpicture(image)
	self.stimlibright = Stateimagelibrary()	
        image = pygame.image.load('./pics/elf-woman-2-right-32x96.bmp').convert()
        image.set_colorkey((255,255,255)) 
	self.stimlibright.addpicture(image)
    
    def update(self,room,player):
	if self.x < 100:
		self.direction = "right"
	if self.x > 600:
		self.direction = "left"

	if self.direction == "left":
        	self.x -= 1 
	else:
		self.x += 1 

    def draw(self, screen, room):
	if self.direction == "left":
        	self.stimlibleft.draw(screen, self.x+room.relativex,self.y+room.relativey)    
	else:	
        	self.stimlibright.draw(screen, self.x+room.relativex,self.y+room.relativey)    



    def talk(self):
        self.talkcounter += 1
        if self.talkcounter == 0:
           return None 
        elif self.talkcounter == 1:
            return "Go listen to Error." 
        elif self.talkcounter == 2:
            return "Try to be friendly."
      	else:
    	    self.talkcounter = -1 
            return None
	return None 
 
 
