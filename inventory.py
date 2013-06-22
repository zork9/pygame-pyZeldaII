
# Copyright (C) Johan Ceuppens 2011
# Copyright (C) Johan Ceuppens 2010

# Copyright (C) Johan Ceuppens 2009 
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
from inventorybomb import *

class Inventory(object):
    def __init__(self):
        self.background = pygame.image.load('./pics/blank.bmp').convert()
        self.list = []
	self.ITEMWIDTH = 36 
	self.ITEMMAX = 7 
        self.list.append(Inventorybomb())

        self.rectimage = pygame.image.load('./pics/rectinventory-36x36.bmp').convert()
        self.rectimage.set_colorkey((0,0,0))
        self.selectioncounter = 0 

    def draw(self,screen):

        screen.blit(self.background, (0, 0))

        for i in range(0,len(self.list)):
            o = self.list[i]
            if o:
                o.draw(screen,40*(i%self.ITEMMAX),i/36)

	x = self.selectioncounter * self.ITEMWIDTH % self.ITEMMAX*self.ITEMWIDTH 
	y = self.selectioncounter / self.ITEMMAX * self.ITEMWIDTH
        self.drawrect(screen,x,y)

    def drawrect(self,screen,x,y):
        screen.blit(self.rectimage, (x, y))


    def moveleft(self):
        if self.selectioncounter > 0:
            self.selectioncounter -= 1

    def moveright(self):
        if self.selectioncounter < self.ITEMMAX * self.ITEMMAX:
            self.selectioncounter += 1

#    def setselection(self):
#        i = 
        
    def getitem(self,o):
#        for i in range(0,self.selectioncounter):
#            o = None
#            o = self.list.getlistobject(o)
	if len(self.list) > self.selectioncounter:
        	o = self.list[self.selectioncounter]
        	if o:
            		return o

        return None

    def additem(self,o):
        self.list.append(o)
