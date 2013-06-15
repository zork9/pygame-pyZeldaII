
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

class PlayerAbeilleFighter(PlayerBase):
    "player Fighter"
    def __init__(self,heartmeter):
        PlayerBase.__init__(self,heartmeter)

        self.stimlib = Stateimagelibrary()	
        image = pygame.image.load('./pics/playerabeillefighter1-48x48.bmp').convert()
        image.set_colorkey((0,0,255)) 
	self.stimlib.addpicture(image)	
        image = pygame.image.load('./pics/playerabeillefighter2-48x48.bmp').convert()
        image.set_colorkey((0,0,255)) 
	self.stimlib.addpicture(image)	
        image = pygame.image.load('./pics/playerabeillefighter3-48x48.bmp').convert()
        image.set_colorkey((0,0,255)) 
	self.stimlib.addpicture(image)	
        image = pygame.image.load('./pics/playerabeillefighter2-48x48.bmp').convert()
        image.set_colorkey((0,0,255)) 
	self.stimlib.addpicture(image)	
        image = pygame.image.load('./pics/playerabeillefighter1-48x48.bmp').convert()
        image.set_colorkey((0,0,255)) 
	self.stimlib.addpicture(image)	
        image = pygame.image.load('./pics/playerabeillefighter2-48x48.bmp').convert()
        image.set_colorkey((0,0,255)) 
	self.stimlib.addpicture(image)	
        image = pygame.image.load('./pics/playerabeillefighter3-48x48.bmp').convert()
        image.set_colorkey((0,0,255)) 
	self.stimlib.addpicture(image)	

        self.stimlibfight = Stateimagelibrary()	
        image = pygame.image.load('./pics/playerabeillefighterfight1-48x48.bmp').convert()
        image.set_colorkey((0,0,255))
        self.stimlibfight.addpicture(image)
        image = pygame.image.load('./pics/playerabeillefighterfight1-48x48.bmp').convert()
        image.set_colorkey((0,0,255))
        self.stimlibfight.addpicture(image)
        image = pygame.image.load('./pics/playerabeillefighterfight2-48x48.bmp').convert()
        image.set_colorkey((0,0,255))
        self.stimlibfight.addpicture(image)
        image = pygame.image.load('./pics/playerabeillefighterfight2-48x48.bmp').convert()
        image.set_colorkey((0,0,255))
        self.stimlibfight.addpicture(image)
        image = pygame.image.load('./pics/playerabeillefighterfight3-48x48.bmp').convert()
        image.set_colorkey((0,0,255))
        self.stimlibfight.addpicture(image)
        image = pygame.image.load('./pics/playerabeillefighterfight3-48x48.bmp').convert()
        image.set_colorkey((0,0,255))
        self.stimlibfight.addpicture(image)

    def draw(self, screen):
        # NOTE
        if self.fightcounter > 0:
            self.fightcounter += 1
            if self.fightcounter > 10:
                self.fightcounter = 0
            self.stimlibfight.draw(screen,self.x,self.y)
            return
        self.stimlib.draw(screen, self.x,self.y)

    def drawstatic(self,screen):
        self.draw(screen)
        
    def askclass(self):
        return "Fighter"

    def askrace(self):
        return "Abeille"

    def askpicture(self):
        return './pics/taskbar-PC-abeillefighter.bmp'
