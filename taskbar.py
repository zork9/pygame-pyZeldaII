
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

class Taskbar:
    "Taskbar"
    def __init__(self, screen, font, player):
        self.screen = screen	
        self.font = font
        self.player = player
        #self.foreground = pygame.image.load('./pics/taskbar01.bmp').convert()
        #self.foreground.set_colorkey((0,0,0)) 
##        self.pc = pygame.image.load(player.askpicture()).convert()
        #self.swordimage = pygame.image.load('./pics/taskbar-defaultsword1-32x32.bmp').convert()
        #self.swordimage.set_colorkey((0,0,255)) 
###        self.lifeimage = pygame.image.load('./pics/life1.bmp').convert()

##    def drawlife(self):
##	for i in range(0,self.player.hitpoints):
##		self.screen.blit(self.lifeimage, (10+i*2,10))

    def setswordimage(self, imagefilename,r,g,b):
        self.swordimage = pygame.image.load(imagefilename).convert()
        self.swordimage.set_colorkey((r,g,b)) 

    def draw(self):
        1#self.screen.blit(self.foreground, (0,0))
##        
##        self.screen.blit(self.pc, (10, 300))
##        self.screen.blit(self.font.render(self.player.askrace() + ' ' + self.player.askclass(), 6, (255,0,0)), (0+70,0+300))
###       	self.drawlife()
 
        #self.screen.blit(self.swordimage, (200, 10))

    def setrubysword(self):
        self.setswordimage('./pics/taskbar-rubysword1-32x32.bmp',0,0,255)
