
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

    def talk(self, screen,font):
        self.talkcounter += 1
        if self.talkcounter == 0:
           return -1 
        elif self.talkcounter == 1:
            screen.blit(font.render("Listen to the mayor.", 8, (255,255,255)), (100,100))
	    talkflag = 1
	    while talkflag == 1:
                for event in pygame.event.get():
                    if event.type == QUIT:
        	        pygame.key.set_repeat(10,100)
                        talkflag = 0
                    elif event.type == KEYDOWN:
            	        if event.key == K_t:
        		    pygame.key.set_repeat(10,100)
                            talkflag = 0
        elif self.talkcounter == 2:
            # FIXME 
	    pygame.key.set_repeat(1000,1000)
            screen.blit(font.render("He is very wise.", 8, (255,255,255)), (100,100))
	    talkflag = 1
	    while talkflag == 1:
                for event in pygame.event.get():
                    if event.type == QUIT:
                        talkflag = 0
                    elif event.type == KEYDOWN:
            	        if event.key == K_t:
            		    pygame.key.set_repeat(10,100)
                            talkflag = 0
        elif self.talkcounter == 3:
            # FIXME 
	    pygame.key.set_repeat(1000,1000)
            screen.blit(font.render("Good luck upon your Quest.", 8, (255,255,255)), (100,100))
	    talkflag = 1
	    while talkflag == 1:
                for event in pygame.event.get():
                    if event.type == QUIT:
                        talkflag = 0
                    elif event.type == KEYDOWN:
            	        if event.key == K_t:
            		    pygame.key.set_repeat(10,100)
                            talkflag = 0
      	    ###self.talkcounter = -1
        return 1
 
