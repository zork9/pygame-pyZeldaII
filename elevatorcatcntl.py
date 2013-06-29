
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

class Elevatorcatcntl(Gameobject):
    ""
    def __init__(self, xx,yy,ww,hh):
        Gameobject.__init__(self,xx,yy)
	self.startx = xx
	self.starty = yy	
	self.roomstarty = yy	
        self.w = ww
        self.h = hh
        self.hitpoints = 999999999 #FIX else wall/floor disappears
        self.image = pygame.image.load('./pics/elevator-1-48x96.bmp').convert()
        self.image.set_colorkey((0,0,0)) 
	self.moveflag = 0

	# NOTE that updates must propagate without falling (staying on e.g. 
	# a box or boxcat
    def update(self, room, player):
	### move down with elevator:
	## print "123> DOWN = starty=%d y=%d playery=%d" % (self.roomstarty,room.relativey,player.y)
	if self.moveflag == 2:
		if room.relativey < - self.roomstarty:
			### player.y += 10
			self.y += 10
			room.yplus(-10) ### elevator down move
		else:
			room.yplus(-10) ### elevator down move
			room.yplus(-10) ### elevator down move, hack for fallcollide
	
		self.y += 10	
		if room.relativey < - self.roomstarty - 480 + 80:
			### print "123> STOP"
			self.moveflag = 0
	### move up with elevator
	### FIX
	elif self.moveflag == 1:
		if self.y > self.starty: ##NOTE default room height, ascend no more or less:
			player.y -= 10 ### fall even with obstruction 
			self.y -= 10	
			if room.fall(player) == 0: ### no obstruction
				1
			elif room.fall(player) == 2:	### obstruction	
				room.yplus(10) ### elevator down move
		if self.y >= self.starty + 480:
			self.moveflag = 0
			self.y -= 10
	### no move
	else:
		1
		## KLU
		room.yplus(10)	
		room.yplus(10)	
    def draw(self, screen, room):
	if self.moveflag == 0:
        	screen.blit(self.image, (self.x+room.relativex, self.y+room.relativey))
	else:	
		### NOTE self.y !
        	screen.blit(self.image, (self.x+room.relativex, self.y+room.relativey))
			
    def collide(self, room, player):
	#if self.moveflag == 0:
	if (player.x-room.relativex > self.x - self.w and
	player.x-room.relativex < self.x+self.w and 
	player.y-room.relativey > self.y - self.h  and #FIX
	player.y-room.relativey < self.y + self.h):
	    ### print "collision in elevator catcntl!"
	    ### self.moveflag = 1
	    ### room.yplus(-10) ### elevator down move
	    return 2 
	else:
	    return 0
	#return 0
	### for in room.roofs list
    def collideup(self, room, player):
		return 0 

    def fallcollide(self, room, player):
        # FIX BUG
        #print 'gameobject x=%d y=%d player x=%d y=%d' % (self.x,self.y,player.x-room.relativex,player.y-room.relativey)
	if (player.x-room.relativex > self.x  and 
	player.x-room.relativex < self.x+self.w and 
	player.y-room.relativey+player.h > self.y and 
	player.y-room.relativey < self.y + self.h):
	    #print "collision with Game Object!"
	    return 1 
	else:
		return 0 
