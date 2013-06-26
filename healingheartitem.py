
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

class HealingheartItem(Gameobject):
    ""
    def __init__(self, xx,yy):
        Gameobject.__init__(self,xx,yy)
        self.w = 32
        self.h = 32
	self.stimlib = Stateimagelibrary()
        image = pygame.image.load('./pics/healingheart-32x32.bmp').convert()
        image.set_colorkey((0,0,0)) 
	self.stimlib.addpicture(image)		
   	self.counter = 0 


    def update(self,room,player):
	1	

    def draw(self,screen,room):
            self.stimlib.draw(screen, self.x+room.relativex,self.y+room.relativey)

    def collide(self, room, player):
	c = None
	if (player.x-room.relativex > self.x - self.w  and 
	player.x-room.relativex < self.x and 
	player.y-room.relativey > self.y - self.h and 
	player.y-room.relativey < self.y + self.h):
	    c = 1 
	else:
	    c = 0 ## for game self.talker
	if c == 1:	  
		print "collision with Healing heart!"
		player.changeplayer("heart")
		## remove item from map :
		room.gameobjects.remove(self)
		return 2
	else:
	    return 0 ## for game self.talker

