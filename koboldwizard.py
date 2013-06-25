
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

class KoboldWizard(Gameobject):
    ""
    def __init__(self,xx,yy):
	Gameobject.__init__(self, xx, yy)
        self.w = 50
        self.h = 50 
	self.stimlibleft = Stateimagelibrary()	
	self.stimlibright = Stateimagelibrary()	
        image = pygame.image.load('./pics/koboldwizard-50x50.bmp').convert()
        image.set_colorkey((255,255,255)) 
	self.stimlibleft.addpicture(image)
        self.talkcounter = 0

    def draw(self, screen, room):
        self.stimlibleft.draw(screen, self.x+room.relativex,self.y+room.relativey)    
	     
    def update(self,room,player):
        1

    def collide(self, room, player):
	if (player.x > self.x+room.relativex  and 
	player.x < self.x+room.relativex+self.w and 
	player.y > self.y+room.relativey and 
            player.y < self.y+room.relativey + self.h):
            print "collision with Kobold Wizard!"
            return 2 ## NOTE 2 for talker
	else:
	    return 0

    def talk(self):
        self.talkcounter += 1
        if self.talkcounter == 0:
           return None 
        elif self.talkcounter == 1:
            return "My brother fought for the Angel Legion." 
        elif self.talkcounter == 2:
            return "As I did." 
        elif self.talkcounter == 3:
            return "It happened long ago."
        elif self.talkcounter == 3:
            return "We were defeated."
        elif self.talkcounter == 3:
            return "As a reprisal I was changed into a kobold."
      	else:
    	    self.talkcounter = -1 
            return None
	return None 
 
