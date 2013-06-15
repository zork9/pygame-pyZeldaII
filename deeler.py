
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
from math import *
from rng import *

class Deeler(Gameobject):
    "Spider"
    def __init__(self,xx,yy):
	Gameobject.__init__(self, xx, yy)
        self.w = 32
        self.h = 32
        self.hitpoints = 2
        
        self.yy = yy
    
        self.image = pygame.image.load('./pics/dealer1-48x48.bmp').convert()
        self.image.set_colorkey((0,0,255))
        self.image2 = pygame.image.load('./pics/dealerup1-48x48.bmp').convert()
        self.image2.set_colorkey((0,0,255)) 
	self.silkimage = pygame.image.load('./pics/silk-2x2.bmp').convert()
        self.silkimage.set_colorkey((0,0,255))
        
	self.talkcounter = 0
	self.direction = "down"

        self.crawling = 1
        self.up = 0

    def draw(self, screen, room):
        if self.crawling == 0:
            # Draw spider silk cord
            for i in range(self.yy,self.y-48):
                screen.blit(self.silkimage, (self.x-self.w/2+room.relativex,i))
	    
            screen.blit(self.image, (self.x-40+room.relativex,self.y+room.relativey))
	else:
            screen.blit(self.image2, (self.x-40+room.relativex,self.y+room.relativey))
	    
    def update(self,room,player):
        if abs(player.x-self.x+room.relativex) < 5:
            self.crawling = 0

        # movement in trees towards player
        if self.crawling:
            if player.x <= self.x-room.relativex:
                self.x -= 6
            elif player.x > self.x-room.relativex:
                self.x += 6
            return
        # lowering to bite
        else:
            if self.up:
                self.y -= 6
                if self.y <= self.yy:
                    self.up = 0
                    self.crawling = 1
                return
            if self.y < 300:
                self.y += 6
            elif self.y >= 300:
                self.up = 1
                    
    def collide(self, room, player):
        # FIX BUG
        #print 'gameobject x=%d y=%d player x=%d y=%d' % (self.x,self.y,player.x-room.relativex,player.y-room.relativey)
	if (player.x-room.relativex > self.x-self.w  and 
	player.x-room.relativex < self.x+self.w+self.w and 
	player.y-room.relativey > self.y-self.h and 
	player.y-room.relativey < self.y + self.h +self.h):
	    print "collision with Deeler!"
	    return 1 
	else:
	    return 0 ## for game self.talker


    def collidewithsword(self, room, player):
        print 'Digdogger x=%d y=%d player x=%d y=%d' % (self.x,self.y,player.x-room.relativex,player.y-room.relativey)
	if (player.x-room.relativex > self.x -self.w  and 
	player.x-room.relativex < self.x+self.w and 
	player.y-room.relativey > self.y -self.h and 
	player.y-room.relativey < self.y + self.h):
	    print "collision with Sword Dealer!"
	    return 1 
	else:
	    return 0

    def fight(self,room,player,keydown = -1):
        1
