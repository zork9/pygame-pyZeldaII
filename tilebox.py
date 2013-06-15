
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
from box import *

class Tilebox:
    "box full o tiles"
    
# example:    self.northwall1 = Tilebox(1,1,60,48,16,1,'./pics/walldungeon1-60x48.bmp')
#               draws 16 times the picture from left to right 1 high
    def __init__(self,x,y,w,h,nx,ny,imagefilename):
        # NOTE : self.w self.h is number of w and h tiles
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.nx = nx
        self.ny = ny
        self.image = pygame.image.load(imagefilename).convert()
	self.image.set_colorkey((0,0,255))
        
    def draw(self,screen,relx,rely):
        for j in range(0, self.ny):
            for i in range(0,self.nx):
                screen.blit(self.image,(self.x+self.w*i+relx,self.y+self.h*j+rely))

    # NOTE - player.h for fencepost errors
    def collide(self, room, player):
	if (player.x > self.x-room.relativex  and 
	 player.x < self.x-room.relativex + self.w*self.nx and 
	 player.y - player.h > self.y-room.relativey and 
	 player.y - player.h < self.y-room.relativey + self.h*self.ny):
	    print "collision in Tilebox!"	
	    return 1 
	else:
	    return 0


    def collidewithenemy(self, room, enemy):
	if (enemy.x > self.x  and 
	enemy.x < self.x+self.w*self.nx and 
	enemy.y - enemy.h > self.y and 
	enemy.y - enemy.h < self.y + self.h*self.ny):
	    #print "collision in Tilebox with enemy!"	
	    return 1 
	else:
	    return 0

