
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
from roadsign import *
from stateimagelibrary import *
import random
from time import *

class RoadSignInn(RoadSign):
    ""
    def __init__(self,xx,yy):
	Gameobject.__init__(self, xx, yy)
        self.image = pygame.image.load('./pics/roadsign2-36x36.bmp').convert()
        self.image.set_colorkey((0,0,0)) 
      
    def talk(self, screen,font):
        if self.talkcounter == 0:
            return
        
        if self.talkcounter > 1:
                self.talkcounter = 0
                return 
        talkover = 0
        while talkover == 0:
            pygame.display.update()
            if self.talkcounter == 1:
                screen.blit(font.render("Friendly Arm Inn", 6, (255,255,255)), (10,100))
            for event in pygame.event.get():
                if event.type == QUIT:
                    return
                elif event.type == KEYDOWN:
                    if event.key == K_z:
                        talkover = 1
                        self.talkcounter += 1
                
