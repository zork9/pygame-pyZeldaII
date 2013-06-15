
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

class Selector:
    "Class and Race Selector"
    def __init__(self, screen, font):
        self.screen = screen
        self.font = font
        self.background = pygame.image.load('./pics/blank.bmp').convert()
        self.klass = "Fighter"
        self.race = "Human"
        # fighters
        self.humanfighterimage = pygame.image.load('./pics/taskbar-PC.bmp').convert()
        self.gnollfighterimage = pygame.image.load('./pics/taskbar-PC-gnoll.bmp').convert()
        self.kattafighterimage = pygame.image.load('./pics/taskbar-PC-kattafighter.bmp').convert()
        self.elffighterimage = pygame.image.load('./pics/taskbar-PC-elffighter.bmp').convert()
        self.abeillefighterimage = pygame.image.load('./pics/taskbar-PC-abeillefighter.bmp').convert()
        # magic users
       
        # thieves
         
    def draw(self):
        # fighters
        self.screen.blit(self.background, (0, 300))       
        self.screen.blit(self.humanfighterimage, (0,0))
        self.screen.blit(self.gnollfighterimage, (50,0))
        self.screen.blit(self.kattafighterimage, (100,0))
        self.screen.blit(self.elffighterimage, (150,0))
        self.screen.blit(self.abeillefighterimage, (200,0))
        # magic users
        

    def select(self):
        while 1:
                self.draw()
                pygame.display.update()
                for event in pygame.event.get():
                    if event.type == QUIT:
                        return
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        position = pygame.mouse.get_pos()
                        mousex = position[0]
                        mousey = position[1]
                        
                        if mousex > 0 and mousex < 50 and mousey > 0 and mousey < 50:
                            self.race = "Human"    
                            self.klass = "Fighter"
                            return
                        elif mousex > 50 and mousex < 100 and mousey > 0 and mousey < 50:
                            self.race = "Bugbear"    
                            self.klass = "Fighter"
                            return
                        elif mousex > 100 and mousex < 150 and mousey > 0 and mousey < 50:
                            self.race = "Katta"    
                            self.klass = "Fighter"
                            return
                        elif mousex > 150 and mousex < 200 and mousey > 0 and mousey < 50:
                            self.race = "Elven"    
                            self.klass = "Fighter"
                            return
                        elif mousex > 200 and mousex < 250 and mousey > 0 and mousey < 50:
                            self.race = "Abeille"    
                            self.klass = "Fighter"
                            return

    def askrace(self):
        return self.race

    def askclass(self):
        return self.klass
