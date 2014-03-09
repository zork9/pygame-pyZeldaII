
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
from enemyflyer import *
from stateimagelibrary import *
import random
from time import *
from math import *
from rng import *

class Digdogger(EnemyFlyer):
    "Flying Eye"
    def __init__(self,xx,yy,ww,hh,hp):
	EnemyFlyer.__init__(self, xx, yy,ww,hh,hp)
        self.PI = 3.14152829
		
        self.headimage = pygame.image.load('./pics/digdogger1.bmp').convert()
        self.headimage.set_colorkey((0,0,255)) 
		
	self.talkcounter = 0
	self.direction = "down"

        self.angle = sqrt(2)/2

    def draw(self, screen, room):
        if self.hitpoints <= 0:
            for i in range(0,len(room.gameobjects)):
                if room.gameobjects[i] == self:
                    room.gameobjects[i] = None
                    return
        self.angle += self.PI/8
        self.x -= 2
        self.angle += self.PI/8
        self.x -= 10
        self.yy = sin(self.angle)*20
        screen.blit(self.headimage, (self.x-40+room.relativex,self.yy+self.y+room.relativey))
	     
    def update(self,room,player):
        1
        
    def fight(self,room,player,keydown = -1):
        self.fightcounter = 1
        o = player.collidewithenemyweapon(room,self)
        if o:
            player.hitwithenemyweapon(RNG().rollgoblinknife())
