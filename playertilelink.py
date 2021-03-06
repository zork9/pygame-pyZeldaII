
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

class PlayerTileLink(PlayerBase):
    "Player"
    def __init__(self):
        PlayerBase.__init__(self,PlayerBase.DROW,PlayerBase.MAGICUSER,None)
        
        self.stimlib = Stateimagelibrary()	
        image = pygame.image.load('./pics/player-right-1-16x16.bmp').convert()
        image.set_colorkey((0,0,0))
	self.stimlib.addpicture(image)
        image = pygame.image.load('./pics/player-right-2-16x16.bmp').convert()
        image.set_colorkey((0,0,0))
	self.stimlib.addpicture(image)
        image = pygame.image.load('./pics/player-right-3-16x16.bmp').convert()
        image.set_colorkey((0,0,0))
	self.stimlib.addpicture(image)
        image = pygame.image.load('./pics/player-right-2-16x16.bmp').convert()
        image.set_colorkey((0,0,0))
	self.stimlib.addpicture(image)

        self.stimlibfight = Stateimagelibrary()	
        image = pygame.image.load('./pics/player-right-2-16x16.bmp').convert()
        image.set_colorkey((0,0,0))
        self.stimlibfight.addpicture(image)

        self.stimlibclimbing = Stateimagelibrary()	
        image = pygame.image.load('./pics/player-right-2-16x16.bmp').convert()
        image.set_colorkey((0,0,255))
        self.stimlibclimbing.addpicture(image)

        self.stimlibduck = Stateimagelibrary()	
        image = pygame.image.load('./pics/player-right-2-16x16.bmp').convert()
        image.set_colorkey((0,0,0))
        self.stimlibduck.addpicture(image)

        self.hitpoints = 50
        self.manapoints = 100
       	self.sword = BroadSword(0,0)
        self.duck = 0
        self.jumpcounter = 0
 
    def askclass(self):
        return "Assassin"

    def askrace(self):
        return "Drow"

    def askpicture(self):
        return './pics/taskbar-PC-drowmage.bmp'

    def collidewithenemyweapon(self,room,o):
        # FIXME NOTE
        for o in room.gameobjects:
            
            if o and o.collidewithsword(room,self):
                return self ## NOTE : returns collided entity (single)		
	return None

    def hitwithenemyweapon(self,damage):
	if damage > 0:
		print 'player is hit!'
        self.hitpoints -= damage
	### FIXself.lifemeter.set(self.hitpoints)

    def hitwithenemyweaponlow(self,damage):
	if damage > 0:
		print 'player is hit low!'
        self.hitpoints -= damage

    def pickup(self,room):
        n = room.pickup(self)
	return n

    def fightlow(self,room):
        self.fightcounter = 1
        
        o = room.collideswordlow(self)
        
        if o:
            print "LOW: fight scored hit on %s!" % o
            o.hitwithweapon(self.sword.roll())

    def fightmedium(self,room):
        self.fightcounter = 1
        
        o = room.collidesword(self)
        
        if o:
            print "MEDIUM-HIGH: fight scored hit on %s!" % o
            o.hitwithweapon(self.sword.roll())

    def jump(self, room):
        self.jumpcounter = 20
        self.direction = 'north'

    def update(self,room):
       if self.jumpcounter > 0 and self.jumpcounter < 200:
            ###FIXMENOTE room.relativey += 20
            room.yplus(10)
	    print "#############456> y=%d %s" % (room.relativey,room)
            self.jumpcounter += 15
       else:   
            self.jumpcounter = 0
            
    def setrubysword(self):
	self.sword = RubySword(0,0)
