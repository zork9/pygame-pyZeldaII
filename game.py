#!/usr/local/bin/python
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

from maproom1 import *
from maproomcatcastle1 import *
from maproom2 import *

from taskbar import *
from time import *
from inventory import *
from lifemeter import *
from manameter import *
from meter import *
from playerkattafighter import*
from playerlink import *

class Game:
    "Main function"
    def __init__(self):
        pygame.init()
        pygame.font.init()
        screen = pygame.display.set_mode((640, 480))
        font = pygame.font.SysFont("Times", 32)
        font2 = pygame.font.SysFont("Times", 12)
        gameover = 0

        askplayers = 0 # NOTE: 2 Player flag
        
        blankimage = pygame.image.load('./pics/blank.bmp').convert()
        ## There are several title screens in the ./pics/ directory
        titleimage = pygame.image.load('./pics/titlescreen-link2.bmp').convert()
        self.x = 0
        self.y = 0
        
        self.room = MaproomCatCastle1(0,0)
        ### self.room = Maproom1(0,0)
        lifemeter = LifeMeter(250,0)
        manameter = ManaMeter(0,0)
        player = PlayerLink(lifemeter,manameter)
##        selector = Selector(screen, font)
##
##        selector.select()
##        
##	heartmeter = Meter()
##	player = PlayerFighter(heartmeter)##default fighter class
##	if selector.askrace() == "Human":
##            if selector.askclass() == "Fighter":
##                player = PlayerHumanFighter(heartmeter)
##            elif selector.askclass() == "Magic User":
##                player = PlayerMagicUser(heartmeter)
##        if selector.askrace() == "Bugbear":
##            if selector.askclass() == "Fighter":
##                player = PlayerGnollFighter(heartmeter)
##        if selector.askrace() == "Katta":
##            if selector.askclass() == "Fighter":
##                player = PlayerKattaFighter(heartmeter)
##        if selector.askrace() == "Elven":
##            if selector.askclass() == "Fighter":
##                player = PlayerElfFighter(heartmeter)
##        if selector.askrace() == "Abeille":
##            if selector.askclass() == "Fighter":
##                player = PlayerAbeilleFighter(heartmeter)
##        
##        player2 = None
##
        pygame.key.set_repeat(10,100)
        self.keydown = 0
        self.inventoryitem = None
        self.inventorymasterkey = None
        self.inventorykey1 = None
        self.inventorykey2 = None
        self.inventoryrubysword = None
        
        self.taskbar = Taskbar(screen,font,player)
        self.talker = None
        gameflag = 0
        while gameover == 0:
            pygame.display.update()
            screen.blit(titleimage, (0,0))
            for event in pygame.event.get():
                if event.type == QUIT:
                    return
                elif event.type == KEYDOWN:
                    gameover = 1
                if event.type == pygame.MOUSEBUTTONDOWN:
                    gameover = 1

            
        gameover = 0
        while gameover == 0:
            player.h = 72 # NOTE: for ducking
            for event in pygame.event.get():
                if event.type == QUIT:
                    return
                elif event.type == KEYDOWN:
                    if event.key == K_z:
                        if self.keydown == 2 or player.duck:
                            player.fightlow(self.room)
                        else:
                            player.fightmedium(self.room)
                        break
                    # FIXME KLUDGE
            	    self.keydown = 1
                    # player 1 key controls
                    
                    if event.key == K_t:
                        if self.room.collide(player) == 4:
                            self.talker = self.room.talkto() # FIX
                            print "self.talker=%s" % self.talker
##			if self.talker == None:
##                       	id = player.pickup(self.room)
##				if id == 5:
##		                	self.taskbar.setrubysword()
##					player.setrubysword()
                    
##                    elif event.key == K_UP:
##                        self.room.movedown()    
                    if event.key == K_DOWN:
                        player.duck = 1
                        self.keydown = 2
                        #FIXME keydown = 2
                        #self.room.moveup()    
                    elif event.key == K_LEFT:
                        player.duck = 0
                        self.room.moveright()    
                    elif event.key == K_RIGHT:
                        player.duck = 0
                        self.room.moveleft()    
                    elif event.key == K_x:
                        if player.jumpcounter == 0:
                            player.jump(self.room)  
    
                    elif event.key == K_i:
#                        self.level.gameover = 1
                      #FIXME  pygame.event.flush()
                        flag = 0
                        inventory = Inventory()
		
			##if Scrollinvisibility(0,0,0,0,"1","1").readkeys(None):
                        ##    inventory.additem(Inventoryscrollinvisibility())

			if self.inventorymasterkey == 1:
                       		1###FIX for key in inventory.additem(Inventorymasterkey())
                        if self.inventorykey1 == 1:
                       		1###FIX for key in inventory.additem(Inventorykey1())
                       	if self.inventorykey2 == 1:
                       		1###FIX for key in inventory
			while flag == 0:#NOTE1
                            for event in pygame.event.get():
                                if event.type == QUIT:
                                    return

                                elif event.type == KEYDOWN:
                                    if event.key == K_LEFT:
                                        inventory.moveleft()
                                    elif event.key == K_RIGHT:
                                        inventory.moveright()
                                    elif event.key == K_z:
                                        self.inventoryitem = inventory.getitem(self.inventoryitem)

                                        flag = 1


                                inventory.draw(screen)
                                pygame.display.update()
 
#	    pickupid = self.room.pickup(player)
#	    if pickupid:
#		if pickupid == 1: # NOTE : masterkey id
#		    self.inventorymasterkey = 1
#		elif pickupid == 2: ## NOTE: dungeonentrance 2 id opens with key 1
 #                   if self.inventorykey1 == 1:
#                        self.room.removeentrance2()
#                elif pickupid == 3: # NOTE dungeon key 1 id
#                    self.inventorykey1 = 1
#                elif pickupid == 4: # NOTE dungeon key 2 id
#                    self.inventorykey2 = 1
#                elif pickupid == 5: # NOTE ruby sword id
#                    self.inventoryrubysword = 1
#                    self.taskbar.setrubysword()
                    
            if self.room.collide(player) == 1 or player.hitpoints <= 0: # NOTE: return 1 after player lifemeter runs out (player.hit)
        	endingimage = pygame.image.load('./pics/endingscreen2.bmp').convert()
        	while gameover == 0:
	            	pygame.display.update()
        	    	screen.blit(endingimage, (0,0))
            		for event in pygame.event.get():
                		if event.type == QUIT:
                    			return
                		elif event.type == KEYDOWN:
                    			gameover = 1
					return
                		if event.type == pygame.MOUSEBUTTONDOWN:
                    			gameover = 1
					return
				    
            if self.room.collide(player) == 3 or self.room.collide(player) == 2:###Dungeon wall
                ###self.room.undomove() ### FIXME for rebound on enemies
                f = self.room.fall(player)
                if not f == 2:
                    self.room.movedown()#FIXME
            f = self.room.fall(player)
            if f == 2:
                gameflag = 0
            elif f == 0:
                1#gameflag = 1
            if self.room.collideup(player) == 2:
		self.room.moveup()
		self.room.moveup()
		self.room.moveup()
		self.room.moveup()
                         
            if self.room.collidewithropes(player) == 2:
                
                while gameflag == 0:

                    for event in pygame.event.get():
                        if event.type == QUIT:
                            return
                        elif event.type == KEYDOWN:
            	    
                            # player 1 key controls
                            ##player.draw(screen)
                            ##if event.key == K_z:
                             ##   player.fight(self.room)  
                            if event.key == K_UP:
                                if self.room.collidewithropes(player) == 2:
                                    self.room.movedown()   
                            elif event.key == K_DOWN:
##                              if at the end of the rope, have to jump off  
                                if self.room.collidewithropes(player) == 2:
                                    self.room.moveup()
                            elif event.key == K_RIGHT:
                                self.room.moveleft()
                                gameflag = 1    
                            elif event.key == K_LEFT:
                                self.room.moveright()
                                gameflag = 1
                            elif event.key == K_x:
                                gameflag = 1
                            elif event.key == K_z:
                                gameflag = 1
                    self.room.draw(screen,player)
                    player.update(self.room)
                    player.drawclimbing(screen)
                    self.taskbar.draw()
                    lifemeter.draw(screen) 
                    manameter.draw(screen,font2) 
                    pygame.display.update()
                    screen.blit(blankimage, (0,0))
                    
            
                
            self.room.draw(screen,player)
            player.update(self.room)
            if self.keydown == 1:
                self.keydown = 0
                player.draw(screen)
            elif self.keydown == 2:
                self.keydown = 2
                player.drawduck(screen)
                player.h = 32
            else:
                player.drawstatic(screen)
            
            #player.draw(screen)
	    sleep(0.05)
            # fight for enemies
            # remove dead game objects
		# FIX put in mana meter
	    manameter.index = player.manapoints

            for o in self.room.gameobjects:
                if o:
                    o.fight(self.room,player,self.keydown)
                    if o.hitpoints <= 0:
                        self.room.removeobject(o)

            if self.talker != None:
                if self.talker.talk(screen,font) < 0:
			self.talker = None

            self.taskbar.draw()
            lifemeter.draw(screen,font2)
            manameter.draw(screen,font2)
            
            pygame.display.update()
            screen.blit(blankimage, (0,0))
            roomnumber = self.room.exit(self)
            self.chooseroom(roomnumber,font)


    def sethitf(self, hitf):
        for i in self.room.gameobjects:
            i.hitf = hitf

    def setxy(self,xx,yy):
        self.x = xx
        self.y = yy

    def chooseroom(self, roomnumber,font):
        if (roomnumber == 0):
            return
        # NOTE: 1_X  woods around haunted castle
        if (roomnumber == 1):
            self.talker = None
            self.room = Maproom1(self.x,self.y)
        elif (roomnumber == 1.1):
            self.talker = None
            self.room = Maproom1_1(self.x,self.y)
        elif (roomnumber == 1.2):
            self.talker = None
            self.room = Maproom1_2(self.x,self.y)
        elif (roomnumber == 1.3):
            self.talker = None
            self.room = Maproominn1_3(self.x,self.y)
        elif (roomnumber == 1.4):
            self.talker = None
            self.room = Maproominn1_4(self.x,self.y)
        elif (roomnumber == 1.5):
            self.talker = None
            self.room = Maproominn1_5(self.x,self.y)
        elif (roomnumber == 1.6):
            self.talker = None
            self.room = Maproominn1_6(self.x,self.y)
        # NOTE left woods of haunted castle
        elif (roomnumber == "1.1.1"):
            self.talker = None
            self.room = Maproom1_1_1(self.x,self.y)
        # rooms of haunted castle    
        elif (roomnumber == 2):
            self.talker = None
            self.room = Maproom2(self.x,self.y)
        elif (roomnumber == 3):
            self.talker = None
            self.room = Maproom3(self.x,self.y)
        elif (roomnumber == 4):
            self.talker = None
            self.room = Maproom4(self.x,self.y)
        elif (roomnumber == 5):
            self.talker = None
            self.room = Maproom5(self.x,self.y)
        elif (roomnumber == 6):
            self.talker = None
            self.room = Maproom6(self.x,self.y)
        elif (roomnumber == 7):
            self.talker = None
            self.room = Maproom7(self.x,self.y)
        elif (roomnumber == 8):
            self.talker = None
            self.room = Maproom8(self.x,self.y)
        elif (roomnumber == 9):
            self.talker = None
            self.room = Maproom9(self.x,self.y)
        elif (roomnumber == 10):
            self.talker = None
            self.room = Maproom10(self.x,self.y)
        elif (roomnumber == 11):
            self.talker = None
            self.room = Maproom11(self.x,self.y)
        elif (roomnumber == 12):
            self.talker = None
            self.room = Maproom12(self.x,self.y)
        elif (roomnumber == 13):
            self.talker = None
            self.room = Maproom13(self.x,self.y)
        elif (roomnumber == 14):
            self.talker = None
            self.room = Maproom14(self.x,self.y)
        # set sword parameters
        if self.inventoryrubysword:
            self.sethitf(self.room.gameobjects.hit2)
            
if __name__ == "__main__":
    foo = Game()



