
# Copyright (C) Johan Ceuppens 2010-2014
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
from enemy import *
from stateimagelibrary import *
import random
from time import *
from math import *
from rng import *

class EnemyFlyer(Enemy):
    "e.g. DigDogger"
    def __init__(self,xx,yy,ww,hh,hp):
	Enemy.__init__(self, xx,yy,ww,hh,hp)
        self.realw = self.w 
        self.realh = self.h 
        self.duckh = self.h/2 

        self.stimlibleft = Stateimagelibrary()
        self.stimlibright = Stateimagelibrary()
        image = pygame.image.load('./pics/nopicture.bmp').convert()
        image.set_colorkey((0,0,255))
        self.stimlibleft.addpicture(image)
        image = pygame.image.load('./pics/nopicture.bmp').convert()
        image.set_colorkey((0,0,255))
        self.stimlibright.addpicture(image)
        
	self.talkcounter = 0
	self.direction = "left"

	self.stun = 0


    def draw(self, screen, room):
        if (self.direction == "left"):
            self.stimlibleft.draw(screen, self.x+room.relativex,self.y+room.relativey)
        elif (self.direction == "right"):
            self.stimlibright.draw(screen, self.x+room.relativex,self.y+room.relativey)
                
    def update(self,room,player):
	if not self.stun:
		if player.x+48 < self.x:
		    self.direction = "left"
		elif player.x-48 > self.x:
		    self.direction = "right"
		if self.direction == "left":
		    self.x -= 5
		if self.direction == "right":
		    self.x += 5
                            
    def collide(self, room, player):
        # FIX BUG
        #print 'gameobject x=%d y=%d player x=%d y=%d' % (self.x,self.y,player.x-room.relativex,player.y-room.relativey)
	if (player.x-room.relativex > self.x-player.w/2  and 
	player.x-room.relativex < self.x+self.w and 
	player.y-room.relativey > self.y-player.h/2 and 
	player.y-room.relativey < self.y + self.h):
	    print "collide() with Daira!"
	    return 1 
	else:
	    return 0 ## for game self.talker


    def collidewithswordmedium(self, room, player):
        ### print 'gameobject x=%d y=%d player x=%d y=%d' % (self.x,self.y,player.x-room.relativex,player.y-room.relativey)
	if (player.x-room.relativex > self.x-self.w and 
	player.x-room.relativex < self.x+self.w+self.w and 
	player.y-room.relativey >= self.y - self.h/2 and 
	player.y-room.relativey <= self.y + self.h):
	    print "collidewithswordmedium() with Daira!"
	    return self 
	else:
	    return None

    def collidewithswordlow(self, room, player):
        ### print 'gameobject x=%d y=%d player x=%d y=%d' % (self.x,self.y,player.x-room.relativex,player.y-room.relativey)
	if (player.x-room.relativex > self.x-self.w and 
	player.x-room.relativex < self.x+self.w+self.w and 
	player.y-room.relativey+player.duckh >= self.y - self.duckh and 
	player.y-room.relativey <= self.y + self.h):
	    print "collidewithswordlow() with Daira!"
	    return self 
	else:
	    return None

    def collideup(self, room, player):
	return 0
  
    def hitwithweapon(self,damage):
	if damage > 0:
            print 'Daira is hit!'
            self.stun = 40
        self.hitpoints -= damage
	if self.direction == "left":
		self.x += 10
	if self.direction == "right":
		self.x -= 10

    def fight(self,room,player,keydown = -1):
        self.fightcounter = 1
        o = player.collidewithenemyweapon(room,self)
        if o:
            player.hitwithenemyweapon(RNG().rollgoblinknife())
        
