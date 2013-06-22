
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

class Demon(Gameobject):
    "Demon"
    def __init__(self,xx,yy):
	Gameobject.__init__(self, xx, yy)
        self.w = 36
        self.h = 36 
	self.stimlibleft = Stateimagelibrary()	
	self.stimlibright = Stateimagelibrary()
	self.stimlibup = Stateimagelibrary()	
	self.stimlibdown = Stateimagelibrary()	
        image = pygame.image.load('./pics/demon1-36x36.bmp').convert()
        image.set_colorkey((0,0,255)) 
	self.stimlibleft.addpicture(image)
	self.stimlibright.addpicture(image)
	self.stimlibup.addpicture(image)
	self.stimlibdown.addpicture(image)
	image = pygame.image.load('./pics/demon1-36x36.bmp').convert()
        image.set_colorkey((0,0,255)) 
	self.stimlibleft.addpicture(image)
	self.stimlibright.addpicture(image)
	self.stimlibup.addpicture(image)
	self.stimlibdown.addpicture(image)
	image = pygame.image.load('./pics/demon1-36x36.bmp').convert()
        image.set_colorkey((0,0,255)) 
	self.stimlibleft.addpicture(image)
	self.stimlibright.addpicture(image)
	self.stimlibup.addpicture(image)
	self.stimlibdown.addpicture(image)
	image = pygame.image.load('./pics/demon1-36x36.bmp').convert()
        image.set_colorkey((0,0,255)) 
	self.stimlibleft.addpicture(image)
	self.stimlibright.addpicture(image)
	self.stimlibup.addpicture(image)
	self.stimlibdown.addpicture(image)
	image = pygame.image.load('./pics/demon2-36x36.bmp').convert()
        image.set_colorkey((0,0,255)) 
	self.stimlibleft.addpicture(image)
	self.stimlibright.addpicture(image)
	self.stimlibup.addpicture(image)
	self.stimlibdown.addpicture(image)
	image = pygame.image.load('./pics/demon2-36x36.bmp').convert()
        image.set_colorkey((0,0,255)) 
	self.stimlibleft.addpicture(image)
	self.stimlibright.addpicture(image)
	self.stimlibup.addpicture(image)
	self.stimlibdown.addpicture(image)
	image = pygame.image.load('./pics/demon2-36x36.bmp').convert()
        image.set_colorkey((0,0,255)) 
	self.stimlibleft.addpicture(image)
	self.stimlibright.addpicture(image)
	self.stimlibup.addpicture(image)
	self.stimlibdown.addpicture(image)
	image = pygame.image.load('./pics/demon2-36x36.bmp').convert()
        image.set_colorkey((0,0,255)) 
	self.stimlibleft.addpicture(image)
	self.stimlibright.addpicture(image)
	self.stimlibup.addpicture(image)
	self.stimlibdown.addpicture(image)
	image = pygame.image.load('./pics/demon3-36x36.bmp').convert()
        image.set_colorkey((0,0,255)) 
	self.stimlibleft.addpicture(image)
	self.stimlibright.addpicture(image)
	self.stimlibup.addpicture(image)
	self.stimlibdown.addpicture(image)
	image = pygame.image.load('./pics/demon3-36x36.bmp').convert()
        image.set_colorkey((0,0,255)) 
	self.stimlibleft.addpicture(image)
	self.stimlibright.addpicture(image)
	self.stimlibup.addpicture(image)
	self.stimlibdown.addpicture(image)
	image = pygame.image.load('./pics/demon3-36x36.bmp').convert()
        image.set_colorkey((0,0,255)) 
	self.stimlibleft.addpicture(image)
	self.stimlibright.addpicture(image)
	self.stimlibup.addpicture(image)
	self.stimlibdown.addpicture(image)
	image = pygame.image.load('./pics/demon3-36x36.bmp').convert()
        image.set_colorkey((0,0,255)) 
	self.stimlibleft.addpicture(image)
	self.stimlibright.addpicture(image)
	self.stimlibup.addpicture(image)
	self.stimlibdown.addpicture(image)
	image = pygame.image.load('./pics/demon2-36x36.bmp').convert()
        image.set_colorkey((0,0,255)) 
	self.stimlibleft.addpicture(image)
	self.stimlibright.addpicture(image)
	self.stimlibup.addpicture(image)
	self.stimlibdown.addpicture(image)
	image = pygame.image.load('./pics/demon2-36x36.bmp').convert()
        image.set_colorkey((0,0,255)) 
	self.stimlibleft.addpicture(image)
	self.stimlibright.addpicture(image)
	self.stimlibup.addpicture(image)
	self.stimlibdown.addpicture(image)
	image = pygame.image.load('./pics/demon2-36x36.bmp').convert()
        image.set_colorkey((0,0,255)) 
	self.stimlibleft.addpicture(image)
	self.stimlibright.addpicture(image)
	self.stimlibup.addpicture(image)
	self.stimlibdown.addpicture(image)
	image = pygame.image.load('./pics/demon2-36x36.bmp').convert()
        image.set_colorkey((0,0,255)) 
	self.stimlibleft.addpicture(image)
	self.stimlibright.addpicture(image)
	self.stimlibup.addpicture(image)
	self.stimlibdown.addpicture(image)
	
        self.direction = "north"
        
    def draw(self, screen, room):
	if (self.direction == "left"):
            self.stimlibleft.draw(screen, self.x+room.relativex,self.y+room.relativey)
	elif (self.direction == "right"):
            self.stimlibright.draw(screen, self.x+room.relativex,self.y+room.relativey)
	elif (self.direction == "up"):
            self.stimlibup.draw(screen, self.x+room.relativex,self.y+room.relativey)
	elif (self.direction == "down"):
            self.stimlibright.draw(screen, self.x+room.relativex,self.y+room.relativey)
	    
	     
    def update(self,room):
        #FIXME elif
        sleep(.01)
	if (random.randint(0,5000) == 0):# and self.direction == "left"):
	   self.direction = "right"
	if (random.randint(0,5000) == 0):# and self.direction == "right"):
	   self.direction = "left"
        if (random.randint(0,5000) == 0):# and self.direction == "up"):
	   self.direction = "down"
	if (random.randint(0,5000) == 0):# and self.direction == "down"):
	   self.direction = "up"

	if (not self.collideobjectX(room)): 
	    if (self.direction == "left"):
	        self.x +=2
	        self.direction = "right" 
	    elif (self.direction == "right"):
	        self.x -=2
	        self.direction = "left"

        if (not self.collideobjectY(room)): 
	    if (self.direction == "up"):
	        self.y +=2
	        self.direction = "down" 
	    elif (self.direction == "down"):
	        self.y -=2
	        self.direction = "up"

	if (self.direction == "left"):
	    self.x -=1 
	elif (self.direction == "right"):
	    self.x +=1
	elif (self.direction == "up"):
	    self.y -=1
	elif (self.direction == "down"):
	    self.y +=1
