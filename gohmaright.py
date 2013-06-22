
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
from venomspit import *

class GohmaRight(Gameobject):
    "Gohma enemy"
    def __init__(self,xx,yy):
	Gameobject.__init__(self, xx, yy)
        self.w = 64
        self.h = 64 
	self.stimlibleft = Stateimagelibrary()	
	self.stimlibright = Stateimagelibrary()	
        image = pygame.image.load('./pics/gohmaright1.bmp').convert()
        image.set_colorkey((0,0,255)) 
	self.stimlibleft.addpicture(image)
	image = pygame.image.load('./pics/gohmaright1.bmp').convert()
        image.set_colorkey((0,0,255)) 
	self.stimlibleft.addpicture(image)
	image = pygame.image.load('./pics/gohmaright1.bmp').convert()
        image.set_colorkey((0,0,255)) 
	self.stimlibleft.addpicture(image)
	image = pygame.image.load('./pics/gohmaright1.bmp').convert()
        image.set_colorkey((0,0,255)) 
	self.stimlibleft.addpicture(image)
        image = pygame.image.load('./pics/gohmaright2.bmp').convert()
        image.set_colorkey((0,0,255)) 
	self.stimlibleft.addpicture(image)
	image = pygame.image.load('./pics/gohmaright2.bmp').convert()
        image.set_colorkey((0,0,255)) 
	self.stimlibleft.addpicture(image)
	image = pygame.image.load('./pics/gohmaright2.bmp').convert()
        image.set_colorkey((0,0,255)) 
	self.stimlibleft.addpicture(image)
	image = pygame.image.load('./pics/gohmaright2.bmp').convert()
        image.set_colorkey((0,0,255)) 
	self.stimlibleft.addpicture(image)
        image = pygame.image.load('./pics/gohmaright3.bmp').convert()
        image.set_colorkey((0,0,255)) 
	self.stimlibleft.addpicture(image)
	image = pygame.image.load('./pics/gohmaright3.bmp').convert()
        image.set_colorkey((0,0,255)) 
	self.stimlibleft.addpicture(image)
	image = pygame.image.load('./pics/gohmaright3.bmp').convert()
        image.set_colorkey((0,0,255)) 
	self.stimlibleft.addpicture(image)
	image = pygame.image.load('./pics/gohmaright3.bmp').convert()
        image.set_colorkey((0,0,255)) 
	self.stimlibleft.addpicture(image)
	image = pygame.image.load('./pics/gohmaright4.bmp').convert()
        image.set_colorkey((0,0,255)) 
	self.stimlibleft.addpicture(image)
	image = pygame.image.load('./pics/gohmaright4.bmp').convert()
        image.set_colorkey((0,0,255)) 
	self.stimlibleft.addpicture(image)
	image = pygame.image.load('./pics/gohmaright4.bmp').convert()
        image.set_colorkey((0,0,255)) 
	self.stimlibleft.addpicture(image)
	image = pygame.image.load('./pics/gohmaright4.bmp').convert()
        image.set_colorkey((0,0,255)) 
	self.stimlibleft.addpicture(image)

        image = pygame.image.load('./pics/gohmaright1.bmp').convert()
        image.set_colorkey((0,0,255)) 
	self.stimlibright.addpicture(image)
	image = pygame.image.load('./pics/gohmaright1.bmp').convert()
        image.set_colorkey((0,0,255)) 
	self.stimlibright.addpicture(image)
	image = pygame.image.load('./pics/gohmaright1.bmp').convert()
        image.set_colorkey((0,0,255)) 
	self.stimlibright.addpicture(image)
	image = pygame.image.load('./pics/gohmaright1.bmp').convert()
        image.set_colorkey((0,0,255)) 
	self.stimlibright.addpicture(image)
        image = pygame.image.load('./pics/gohmaright2.bmp').convert()
        image.set_colorkey((0,0,255)) 
	self.stimlibright.addpicture(image)
	image = pygame.image.load('./pics/gohmaright2.bmp').convert()
        image.set_colorkey((0,0,255)) 
	self.stimlibright.addpicture(image)
	image = pygame.image.load('./pics/gohmaright2.bmp').convert()
        image.set_colorkey((0,0,255)) 
	self.stimlibright.addpicture(image)
	image = pygame.image.load('./pics/gohmaright2.bmp').convert()
        image.set_colorkey((0,0,255)) 
	self.stimlibright.addpicture(image)
        image = pygame.image.load('./pics/gohmaright3.bmp').convert()
        image.set_colorkey((0,0,255)) 
	self.stimlibright.addpicture(image)
	image = pygame.image.load('./pics/gohmaright3.bmp').convert()
        image.set_colorkey((0,0,255)) 
	self.stimlibright.addpicture(image)
	image = pygame.image.load('./pics/gohmaright3.bmp').convert()
        image.set_colorkey((0,0,255)) 
	self.stimlibright.addpicture(image)
	image = pygame.image.load('./pics/gohmaright3.bmp').convert()
        image.set_colorkey((0,0,255)) 
	self.stimlibright.addpicture(image)
	image = pygame.image.load('./pics/gohmaright4.bmp').convert()
        image.set_colorkey((0,0,255)) 
	self.stimlibright.addpicture(image)
	image = pygame.image.load('./pics/gohmaright4.bmp').convert()
        image.set_colorkey((0,0,255)) 
	self.stimlibright.addpicture(image)
	image = pygame.image.load('./pics/gohmaright4.bmp').convert()
        image.set_colorkey((0,0,255)) 
	self.stimlibright.addpicture(image)
	image = pygame.image.load('./pics/gohmaright4.bmp').convert()
        image.set_colorkey((0,0,255)) 
	self.stimlibright.addpicture(image)

	self.direction = "down"

    def draw(self, screen, room):
	if (self.direction == "down"):
            self.stimlibleft.draw(screen, self.x+room.relativex,self.y+room.relativey)
	elif (self.direction == "up"):
            self.stimlibright.draw(screen, self.x+room.relativex,self.y+room.relativey)
	    
	     
    def update(self,room):
        sleep(.01) # FIX darkknight sleep
##	if (random.randint(0,100) == 0 and self.direction == "up"):
##	   self.direction = "down"
##	elif (random.randint(0,100) == 0 and self.direction == "down"):
##	   self.direction = "up"

	if (self.collideobjectXY(room)): 
	    if (self.direction == "up"):
	        self.y +=2
	        self.direction = "down" 
	    elif (self.direction == "down"):
	        self.y -=2
	        self.direction = "up"


	if (self.direction == "up"):
	        self.y -=1 
	elif (self.direction == "down"):
	        self.y +=1

        #FIX gohma down spit venom if random.randint(0,300) == 0:
        #    room.gameobjects.append(Venomspit(self.x+self.w/2,self.y+self.h))

    def collide(self, room, player):
	if (player.x > self.x+room.relativex  and 
	player.x < self.x+room.relativex+self.w and 
	player.y > self.y+room.relativey and 
	player.y < self.y+room.relativey + self.h):
	    print "collision with gohmadown!"
	    if player.hit():
		return 1 
	    else:
	    	return 2 
	else:
	    return 0

		 
