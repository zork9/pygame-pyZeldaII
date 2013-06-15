
# Copyright (C) Johan Ceuppens 2011
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
from math import *
from time import *

class Ghostcircling(Gameobject):
    "ghostcircling"
    def __init__(self,xx,yy):
	Gameobject.__init__(self, xx, yy)
	self.i = 0 ## / medridians, / paralells
	self.j = 0###-2*3.14 ## / medridians, / paralells
        self.w = 36
        self.h = 36 
	self.stimlibleft = Stateimagelibrary()	
	self.stimlibright = Stateimagelibrary()	
        image = pygame.image.load('./pics/ghostwanderingleft2-36x36.bmp').convert()
        image.set_colorkey((0,0,0)) 
	self.stimlibleft.addpicture(image)	
        image = pygame.image.load('./pics/ghostwanderingleft2-36x36.bmp').convert()
        image.set_colorkey((0,0,0)) 
	self.stimlibleft.addpicture(image)	
        image = pygame.image.load('./pics/ghostwanderingleft2-36x36.bmp').convert()
        image.set_colorkey((0,0,0)) 
	self.stimlibleft.addpicture(image)	
        image = pygame.image.load('./pics/ghostwanderingleft2-36x36.bmp').convert()
        image.set_colorkey((0,0,0)) 
	self.stimlibleft.addpicture(image)	
        image = pygame.image.load('./pics/ghostwanderingleft2-36x36.bmp').convert()
        image.set_colorkey((0,0,0)) 
	self.stimlibleft.addpicture(image)	
        image = pygame.image.load('./pics/ghostwanderingleft2-36x36.bmp').convert()
        image.set_colorkey((0,0,0)) 
	self.stimlibleft.addpicture(image)	
        image = pygame.image.load('./pics/ghostwanderingleft2-36x36.bmp').convert()
        image.set_colorkey((0,0,0)) 
	self.stimlibleft.addpicture(image)	
        image = pygame.image.load('./pics/ghostwanderingleft2-36x36.bmp').convert()
        image.set_colorkey((0,0,0)) 
	self.stimlibleft.addpicture(image)	

        image = pygame.image.load('./pics/ghostwandering2-36x36.bmp').convert()
        image.set_colorkey((0,0,0)) 
	self.stimlibright.addpicture(image)	
        image = pygame.image.load('./pics/ghostwandering2-36x36.bmp').convert()
        image.set_colorkey((0,0,0)) 
	self.stimlibright.addpicture(image)	
        image = pygame.image.load('./pics/ghostwandering2-36x36.bmp').convert()
        image.set_colorkey((0,0,0)) 
	self.stimlibright.addpicture(image)	
        image = pygame.image.load('./pics/ghostwandering2-36x36.bmp').convert()
        image.set_colorkey((0,0,0)) 
	self.stimlibright.addpicture(image)	
        image.set_colorkey((0,0,0)) 
	self.stimlibright.addpicture(image)	
        image = pygame.image.load('./pics/ghostwandering2-36x36.bmp').convert()
        image.set_colorkey((0,0,0)) 
	self.stimlibright.addpicture(image)	
        image = pygame.image.load('./pics/ghostwandering2-36x36.bmp').convert()
        image.set_colorkey((0,0,0)) 
	self.stimlibright.addpicture(image)	
        image = pygame.image.load('./pics/ghostwandering2-36x36.bmp').convert()
        image.set_colorkey((0,0,0)) 
	self.stimlibright.addpicture(image)	
        image = pygame.image.load('./pics/ghostwandering2-36x36.bmp').convert()
        image.set_colorkey((0,0,0)) 
	self.stimlibright.addpicture(image)	

	self.direction = "left"

###    def draw(self, screen, room):
###	if (self.direction == "left"):
###            self.stimlibleft.draw(screen, self.x+room.relativex,self.y+room.relativey)
###	elif (self.direction == "right"):
###            self.stimlibright.draw(screen, self.x+room.relativex,self.y+room.relativey)
	    
	     
    def update(self,room):
	1

    def collide(self, room, player):
	if (player.x > self.x+room.relativex  and 
	player.x < self.x+room.relativex+self.w and 
	player.y > self.y+room.relativey and 
	player.y < self.y+room.relativey + self.h):
	    print "collision with ghostwandering2!"
	    if player.hit():
		return 1 
	    else:
	    	return 2 
	else:
	    return 0

    def draw(self,screen,room):
	color = (255,0,0)
	self.PI = 3.14152829
	self.cx = 150
	self.cy = 60 
	self.cz = 100
	self.n = 100
	self.r = 100
	if self.j < self.n / 2:
		self.theta1 = self.j*2*self.PI / self.n - self.PI
		self.theta2 = (self.j+1)*2*self.PI / self.n - self.PI
		if self.i < self.n:
			self.theta3 = self.i * 2*self.PI / self.n
			x = cos(self.theta2)*cos(self.theta3) 
			y = sin(self.theta2)*sin(self.theta3)
			z = sin(self.theta2)
			self.x = x * self.r
			self.y = y * self.r
			###self.z *= self.r
		        self.stimlibleft.draw(screen, self.cx+self.x+room.relativex,self.cy+self.y+room.relativey)
                        sleep(.05) # FIX ghost2 sleep
			###pygame.draw.line(pygame.display.get_surface(),color, (self.cx+self.x,self.cy+self.y),(self.cx+self.x,self.cy+self.y))
			self.i += .5 # FIX .001 
		else:
			self.i = 0
		self.j += .1
	else:
		self.j = 0

		 
