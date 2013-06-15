
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

class Digdogger(Gameobject):
    "Flying Eye"
    def __init__(self,xx,yy):
	Gameobject.__init__(self, xx, yy)
        self.w = 32
        self.h = 32
        self.PI = 3.14182829
        self.hitpoints = 1
        
		
        self.headimage = pygame.image.load('./pics/digdogger1.bmp').convert()
        self.headimage.set_colorkey((0,0,255)) 
		
        #self.bodyimage = pygame.image.load('./pics/snakebody1-48x48.bmp').convert()
        #self.bodyimage.set_colorkey((0,0,0)) 
	
	self.talkcounter = 0
	self.direction = "down"

        self.angle = sqrt(2)/2

    def draw(self, screen, room):
        if self.hitpoints <= 0:
            for i in range(0,len(room.gameobjects)):
                if room.gameobjects[i] == self:
                    room.gameobjects[i] = None
                    return
##        sleep(.1) # FIX goblin sleep
        self.angle += self.PI/8
        self.x -= 2
##        self.y = sin(self.angle)*20
##        screen.blit(self.bodyimage, (self.x+room.relativex,self.y+room.relativey))
##        self.angle += self.PI/8
##        self.y = sin(self.angle)*20
##        screen.blit(self.bodyimage, (self.x-10+room.relativex,self.y+room.relativey))
##        self.angle += self.PI/8
##        self.y = sin(self.angle)*20
##        screen.blit(self.bodyimage, (self.x-20+room.relativex,self.y+room.relativey))
##        self.angle += self.PI/8
##        self.y = sin(self.angle)*20
##        screen.blit(self.bodyimage, (self.x-30+room.relativex,self.y+room.relativey))

        self.angle += self.PI/8
        self.x -= 10
        self.yy = sin(self.angle)*20
        screen.blit(self.headimage, (self.x-40+room.relativex,self.yy+self.y+room.relativey))
##        self.angle -= self.PI/8
##        self.angle -= self.PI/8
##        self.angle -= self.PI/8
	     
    def update(self,room,player):
        1
        

    def collide(self, room, player):
        # FIX BUG
        #print 'gameobject x=%d y=%d player x=%d y=%d' % (self.x,self.y,player.x-room.relativex,player.y-room.relativey)
	if (player.x-room.relativex > self.x-self.w  and 
	player.x-room.relativex < self.x+self.w+self.w and 
	player.y-room.relativey > self.y-self.h and 
	player.y-room.relativey < self.y + self.h +self.h):
	    print "collision with Digdogger!"
	    return 1 
	else:
	    return 0 ## for game self.talker


    def collidewithsword(self, room, player):
        print 'Digdogger x=%d y=%d player x=%d y=%d' % (self.x,self.y,player.x-room.relativex,player.y-room.relativey)
	if (player.x-room.relativex > self.x -self.w  and 
	player.x-room.relativex < self.x+self.w and 
	player.y-room.relativey > self.y -self.h and 
	player.y-room.relativey < self.y + self.h):
	    print "collision with Sword Digdogger!"
	    return 1 
	else:
	    return 0

    def fight(self,room,player,keydown = -1):
        self.fightcounter = 1
        o = player.collidewithenemyweapon(room,self)
        if o:
            player.hitwithenemyweapon(RNG().rollgoblinknife())
