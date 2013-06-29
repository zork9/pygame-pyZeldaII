
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

class Elfwoman1Town1(ElfwomanTown):
    ""
    def __init__(self,xx,yy):
	ElfwomanTown.__init__(self, xx, yy)
    
    def update(self,room,player):
	if self.x < 100:
		self.direction = "right"
	if self.x > 600:
		self.direction = "left"

	if self.direction == "left":
        	self.x -= 1 
	else:
		self.x += 1 

    def talk(self):
        self.talkcounter += 1
        if self.talkcounter == 0:
           return None 
        elif self.talkcounter == 1:
            return "Some adivce" 
        elif self.talkcounter == 2:
            return "Go listen to Error." 
        elif self.talkcounter == 3:
            return "He is an archelf and very wise."
      	else:
    	    self.talkcounter = -1 
            return None
	return None 
 
