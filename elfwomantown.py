
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

class ElfwomanTown(Gameobject):
    ""
    def __init__(self,xx,yy):
	Gameobject.__init__(self, xx, yy)
        self.w = 32 
        self.h = 96 
	self.stimlib = Stateimagelibrary()	
        image = pygame.image.load('./pics/elf-woman-1-32x96.bmp').convert()
        image.set_colorkey((255,255,255)) 
	self.stimlib.addpicture(image)
        self.talkcounter = 0

	self.direction = "left"

    def draw(self, screen, room):
        self.stimlib.draw(screen, self.x+room.relativex,self.y+room.relativey)    
    def update(self,room,player):
        1

    def collide(self, room, player):
	if (player.x > self.x+room.relativex  and 
	player.x < self.x+room.relativex+self.w and 
	player.y > self.y+room.relativey and 
            player.y < self.y+room.relativey + self.h):
            print "collision with Elf man in Town 1"
            return 2 ## NOTE 2 for talker
	else:
	    return 0

    def talk(self, screen,font):
        self.talkcounter += 1
        if self.talkcounter == 0:
           return -1 
        elif self.talkcounter == 1:
            screen.blit(font.render("I am Bomey.", 8, (255,255,255)), (100,100))
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
            screen.blit(font.render("There lives a wizard at the statue.", 8, (255,255,255)), (100,100))
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
            screen.blit(font.render("He can help you with magic.", 8, (255,255,255)), (100,100))
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
      	    ###self.talkcounter = -1
        return 1
 
##        screen.blit(font.render("Watch out for Gohma. He spits venom!",4, (255,255,255)), (10,100))
##        pygame.display.update()
##        sleep(1)
##        for event in pygame.event.get():
##            self.room.draw(screen) 
##           
##            pygame.display.update()
##            if event.type == QUIT:
##                return
##            elif event.type == KEYDOWN:
##                if event.key == K_z:
##                  break
