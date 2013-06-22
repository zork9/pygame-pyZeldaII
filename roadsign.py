
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
from time import *

class RoadSign(Gameobject):
    ""
    def __init__(self,xx,yy):
	Gameobject.__init__(self, xx, yy)
        self.w = 36
        self.h = 36 
        self.image = pygame.image.load('./pics/roadsign1-36x36.bmp').convert()
        self.image.set_colorkey((0,0,0)) 
        self.talkcounter = 0
        
    def draw(self, screen, room):
        screen.blit(self.image, (self.x+room.relativex,self.y+room.relativey))
	    
	     
    def update(self,room):
        1

    def collide(self, room, player):
	if (player.x > self.x+room.relativex  and 
	player.x < self.x+room.relativex+self.w and 
	player.y > self.y+room.relativey and 
	player.y < self.y+room.relativey + self.h):
	    print "collision with RoadSign!"
	    return 2 
	else:
	    return 0
		 
    def talk(self, screen,font):
        if self.talkcounter == 0:
            return
        
        if self.talkcounter > 1:
                self.talkcounter = 0
                return 
        talkover = 0
        while talkover == 0:
            pygame.display.update()
            if self.talkcounter == 1:
                screen.blit(font.render("", 6, (255,255,255)), (10,100))
            for event in pygame.event.get():
                if event.type == QUIT:
                    return
                elif event.type == KEYDOWN:
                    if event.key == K_z:
                        talkover = 1
                        self.talkcounter += 1
                
