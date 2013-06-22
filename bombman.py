
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

class Bombman(Gameobject):
    "Bombman"
    def __init__(self,xx,yy):
	Gameobject.__init__(self, xx, yy)
        self.w = 36
        self.h = 36 

	self.stimlibburning = Stateimagelibrary()
	for i in range(0,15):	
        	image = pygame.image.load('./pics/bombburning1-24x24.bmp').convert()
        	image.set_colorkey((255,255,255)) 
		self.stimlibburning.addpicture(image)	
	for i in range(0,15):	
        	image = pygame.image.load('./pics/bombburning2-24x24.bmp').convert()
        	image.set_colorkey((255,255,255)) 
		self.stimlibburning.addpicture(image)	
	for i in range(0,15):	
        	image = pygame.image.load('./pics/bombburning3-24x24.bmp').convert()
        	image.set_colorkey((255,255,255)) 
		self.stimlibburning.addpicture(image)	
	for i in range(0,15):	
        	image = pygame.image.load('./pics/bomb1-24x24.bmp').convert()
        	image.set_colorkey((255,255,255)) 
		self.stimlibburning.addpicture(image)
	for i in range(0,5):	
        	image = pygame.image.load('./pics/bombred1-24x24.bmp').convert()
        	image.set_colorkey((255,255,255)) 
		self.stimlibburning.addpicture(image)
	for i in range(0,5):	
        	image = pygame.image.load('./pics/bomb1-24x24.bmp').convert()
        	image.set_colorkey((255,255,255)) 
		self.stimlibburning.addpicture(image)
	for i in range(0,5):	
        	image = pygame.image.load('./pics/bombred1-24x24.bmp').convert()
        	image.set_colorkey((255,255,255)) 
		self.stimlibburning.addpicture(image)
	for i in range(0,5):	
        	image = pygame.image.load('./pics/bomb1-24x24.bmp').convert()
        	image.set_colorkey((255,255,255)) 
		self.stimlibburning.addpicture(image)
	for i in range(0,5):	
        	image = pygame.image.load('./pics/bombred1-24x24.bmp').convert()
        	image.set_colorkey((255,255,255)) 
		self.stimlibburning.addpicture(image)
	for i in range(0,5):	
        	image = pygame.image.load('./pics/bomb1-24x24.bmp').convert()
        	image.set_colorkey((255,255,255)) 
		self.stimlibburning.addpicture(image)
	self.stimlibleft = Stateimagelibrary()	
	self.stimlibright = Stateimagelibrary()	
        image = pygame.image.load('./pics/bombmanleft1-36x36.bmp').convert()
        image.set_colorkey((0,0,0)) 
	self.stimlibleft.addpicture(image)	
        image = pygame.image.load('./pics/bombmanleft1-36x36.bmp').convert()
        image.set_colorkey((0,0,0)) 
	self.stimlibleft.addpicture(image)	
        image = pygame.image.load('./pics/bombmanleft1-36x36.bmp').convert()
        image.set_colorkey((0,0,0)) 
	self.stimlibleft.addpicture(image)	
        image = pygame.image.load('./pics/bombmanleft2-36x36.bmp').convert()
        image.set_colorkey((0,0,0)) 
	self.stimlibleft.addpicture(image)	
        image = pygame.image.load('./pics/bombmanleft2-36x36.bmp').convert()
        image.set_colorkey((0,0,0)) 
	self.stimlibleft.addpicture(image)	
        image = pygame.image.load('./pics/bombmanleft2-36x36.bmp').convert()
        image.set_colorkey((0,0,0)) 
	self.stimlibleft.addpicture(image)	
        image = pygame.image.load('./pics/bombmanleft3-36x36.bmp').convert()
        image.set_colorkey((0,0,0)) 
	self.stimlibleft.addpicture(image)	
        image = pygame.image.load('./pics/bombmanleft3-36x36.bmp').convert()
        image.set_colorkey((0,0,0)) 
	self.stimlibleft.addpicture(image)	
        image = pygame.image.load('./pics/bombmanleft3-36x36.bmp').convert()
        image.set_colorkey((0,0,0)) 
	self.stimlibleft.addpicture(image)	
        image = pygame.image.load('./pics/bombmanleft2-36x36.bmp').convert()
        image.set_colorkey((0,0,0)) 
	self.stimlibleft.addpicture(image)	
        image = pygame.image.load('./pics/bombmanleft2-36x36.bmp').convert()
        image.set_colorkey((0,0,0)) 
	self.stimlibleft.addpicture(image)	
        image = pygame.image.load('./pics/bombmanleft2-36x36.bmp').convert()
        image.set_colorkey((0,0,0)) 
	self.stimlibleft.addpicture(image)	

        image = pygame.image.load('./pics/bombman1-36x36.bmp').convert()
        image.set_colorkey((0,0,0)) 
	self.stimlibright.addpicture(image)	
        image = pygame.image.load('./pics/bombman1-36x36.bmp').convert()
        image.set_colorkey((0,0,0)) 
	self.stimlibright.addpicture(image)	
        image = pygame.image.load('./pics/bombman1-36x36.bmp').convert()
        image.set_colorkey((0,0,0)) 
	self.stimlibright.addpicture(image)	
        image = pygame.image.load('./pics/bombman2-36x36.bmp').convert()
        image.set_colorkey((0,0,0)) 
	self.stimlibright.addpicture(image)	
        image = pygame.image.load('./pics/bombman2-36x36.bmp').convert()
        image.set_colorkey((0,0,0)) 
	self.stimlibright.addpicture(image)	
        image = pygame.image.load('./pics/bombman2-36x36.bmp').convert()
        image.set_colorkey((0,0,0)) 
	self.stimlibright.addpicture(image)	
        image = pygame.image.load('./pics/bombman3-36x36.bmp').convert()
        image.set_colorkey((0,0,0)) 
	self.stimlibright.addpicture(image)	
        image = pygame.image.load('./pics/bombman3-36x36.bmp').convert()
        image.set_colorkey((0,0,0)) 
	self.stimlibright.addpicture(image)	
        image = pygame.image.load('./pics/bombman3-36x36.bmp').convert()
        image.set_colorkey((0,0,0)) 
	self.stimlibright.addpicture(image)	
        image = pygame.image.load('./pics/bombman2-36x36.bmp').convert()
        image.set_colorkey((0,0,0)) 
	self.stimlibright.addpicture(image)	

	self.direction = "left"

    def draw(self, screen, room):
	###print "self.direction=%s" % self.direction
	if (self.direction == "left"):
            self.stimlibleft.draw(screen, self.x+room.relativex,self.y+room.relativey)
	elif (self.direction == "right"):
            self.stimlibright.draw(screen, self.x+room.relativex,self.y+room.relativey)
	elif (self.direction == "burning"):    
            self.stimlibburning.draw(screen, self.x+room.relativex,self.y+room.relativey)
	    if self.stimlibburning.index >= self.stimlibburning.max:
	    	room.removeobject(self)
	    
	     
    def update(self,room):
	#print "self.direction=%s" % self.direction
	
	if self.direction == "burning":
		return

	if (random.randint(0,100) == 0 and self.direction == "left"):
	   self.direction = "right"
	elif (random.randint(0,100) == 0 and self.direction == "right"):
	   self.direction = "left"

	if (not self.collideobjectX(room)): 
	    if (self.direction == "left"):
	        self.x +=2
	        self.direction = "right" 
	    elif (self.direction == "right"):
	        self.x -=2
	        self.direction = "left"


	if (self.direction == "left"):
	        self.x -=1 
	elif (self.direction == "right"):
	        self.x +=1

    def collide(self, room, player):
	if (player.x > self.x+room.relativex  and 
	player.x < self.x+room.relativex+self.w and 
	player.y > self.y+room.relativey and 
	player.y < self.y+room.relativey + self.h):
		print "collision with Bombman!"
	    ###if player.hit():## FIX player needs descending hearts in meter
       		self.direction = "burning"
	return 0 
	    #else:
	    #	return 2 
	#else:
	 #   return 0

		 
