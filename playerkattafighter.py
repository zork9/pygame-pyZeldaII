
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
from stateimagelibrary import *
from playerbase import *
from rng import *
from broadsword import *
from rubysword import *

class PlayerKattaFighter(PlayerBase):
    "Player Katta Fighter"
    def __init__(self,heartmeter):
        PlayerBase.__init__(self,PlayerBase.KATTA,PlayerBase.FIGHTER,heartmeter)
        
        self.stimlib = Stateimagelibrary()	
        image = pygame.image.load('./pics/playerkattafighter1-48x48.bmp').convert()
        image.set_colorkey((0,0,0)) 
	self.stimlib.addpicture(image)	
        image = pygame.image.load('./pics/playerkattafighter2-48x48.bmp').convert()
        image.set_colorkey((0,0,0)) 
	self.stimlib.addpicture(image)	
        image = pygame.image.load('./pics/playerkattafighter3-48x48.bmp').convert()
        image.set_colorkey((0,0,0)) 
	self.stimlib.addpicture(image)	
        image = pygame.image.load('./pics/playerkattafighter2-48x48.bmp').convert()
        image.set_colorkey((0,0,0)) 
	self.stimlib.addpicture(image)	
        image = pygame.image.load('./pics/playerkattafighter1-48x48.bmp').convert()
        image.set_colorkey((0,0,0)) 
	self.stimlib.addpicture(image)	
        image = pygame.image.load('./pics/playerkattafighter2-48x48.bmp').convert()
        image.set_colorkey((0,0,0)) 
	self.stimlib.addpicture(image)	
        image = pygame.image.load('./pics/playerkattafighter3-48x48.bmp').convert()
        image.set_colorkey((0,0,0)) 
	self.stimlib.addpicture(image)	

        self.stimlibfight = Stateimagelibrary()	
        image = pygame.image.load('./pics/playerkattafighterfight1-48x48.bmp').convert()
        image.set_colorkey((0,0,0))
        self.stimlibfight.addpicture(image)
        image = pygame.image.load('./pics/playerkattafighterfight1-48x48.bmp').convert()
        image.set_colorkey((0,0,0))
        self.stimlibfight.addpicture(image)
        image = pygame.image.load('./pics/playerkattafighterfight2-48x48.bmp').convert()
        image.set_colorkey((0,0,0))
        self.stimlibfight.addpicture(image)
        image = pygame.image.load('./pics/playerkattafighterfight2-48x48.bmp').convert()
        image.set_colorkey((0,0,0))
        self.stimlibfight.addpicture(image)
        image = pygame.image.load('./pics/playerkattafighterfight3-48x48.bmp').convert()
        image.set_colorkey((0,0,0))
        self.stimlibfight.addpicture(image)
        image = pygame.image.load('./pics/playerkattafighterfight3-48x48.bmp').convert()
        image.set_colorkey((0,0,0))
        self.stimlibfight.addpicture(image)

        self.hitpoints = 50
       	self.sword = BroadSword(0,0)
 
    def askclass(self):
        return "Fighter"

    def askrace(self):
        return "Katta"

    def askpicture(self):
        return './pics/taskbar-PC-kattafighter.bmp'

    def collidewithenemyweapon(self,room,o):
        if o.collide(room,self):
		return self ## NOTE : returns collided entity (single)
		
	return None

    def hitwithenemyweapon(self,damage):
	if damage > 0:
		print 'player is hit!'
        self.hitpoints -= damage

    def pickup(self,room):
        n = room.pickup(self)
	return n

    def fight(self,room):
        self.fightcounter = 1
        o = room.collidesword(self)
        if o:
            o.hitwithweapon(self.sword.roll())
       
    def setrubysword(self):
	self.sword = RubySword(0,0)
