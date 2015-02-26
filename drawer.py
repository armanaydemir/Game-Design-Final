#!/usr/bin/env python2.7-32
#actual game
#Arman Aydemir
#June 1st, 2014
import pygame
from pygame import *
import sys
from school import *
global colnum, color, lev, circlev, hnum

#writes save file for me
def writer():
	global hnum, levnum, colnum
	text_file = open('save.txt', 'w')
	text_file.write(str(colnum) + '\n')
	text_file.write(str(levnum) + '\n')
	if levnum > hnum:
		hnum = levnum
	text_file.write(str(hnum))
	text_file.close()
	
#sets up display
Width = 2880
Height = 1800
screen = display.set_mode((Width, Height), FULLSCREEN)

#checks for save file and either reads or makes a new one
try:
	s = [item.rstrip('\n') for item in open('save.txt','r').readlines()]
	colnum = int(s[0])
	levnum = int(s[1])
	hnum = int(s[1])
except:
	colnum = 0
	levnum = 0
	hnum = 0
	writer()
	
#color constants
colors = [Color('Light Blue',(0,150,255),False,(200,1000,400,160)), Color('Purple',(159,0,212),False,(200,800,400,160)), 
Color('Green',(45,199,14),False,(200,600,400,160)), Color('Navy',(0,61,173),False,(200,400,400,160)),
Color('Grey',(159,158,163),False,(200,1400,400,160)),Color('Nantucket Red',(255,105,105),False,(200,1200,400,160))]
color = colors[colnum].color
colors[colnum].chosen = True
	
#makes new lines of pointers
def addent(tell, adden):
	pointers = []
	for l in range(1,len(adden)):
		pointers.append((tell[0] + adden[l-1][0], tell[1] + adden[l-1][1]))
	return pointers

#main game function
def game(wait, firstry):
	global Width, Height, lev, levnum, hnum, circlev
	
	#defines levels
	#===============================================
	lev = [[Lines((576*2,257*2),(576*2,257*2+450),(235, 68, 42),False,True),Lines((576*3,257*3), (576*3,257*3+450),(235, 68, 42),False,True),Lines((576*4,257*4), (576*4,257*4+450),(235, 68, 42),False,True)],
		
		[Lines((1080,900),(1320,900),(235, 68, 42),False,True),Lines((1080+480,900),(1320+480,900),(235, 68, 42),False,True),Lines((1080+480+480,900),(1320+480+480,900),(235, 68, 42),False,True)],
		
		[Lines((960,600),(960*2,600),(235, 68, 42),False,True),Lines((960,1200),(960*2,1200),(235, 68, 42),False,True)],
		
		[Lines((720*2,360),(720*2,720),(235, 68, 42),False,True),Lines((720*3,360),(720*3,720),(235, 68, 42),False,True),Lines((720*2,360*3),(720*2,360*4),(235, 68, 42),False,True),Lines((720*3,360*3),(720*3,720*2),(235, 68, 42),False,True)],
		
		[Lines((1440,60),(1440,600-60),(235, 68, 42),False,True),Lines((1440,1200+60),(1440,1800-60),(235, 68, 42),False,True)],
	
		[Lines((1152,630),(1152,1170),(32,227,58),False,False), Lines((1728,630),(1728,1170),(32,227,58),False,False),Lines((2304,630),(2304,1170),(32,227,58),False,False),
		Lines((2304-60,570),(1728+60,570),(235, 68, 42),False,True), Lines((2304-60,1230),(1728+60,1230),(235, 68, 42),False,True), Lines((1152+60,570),(1728-60,570),(235, 68, 42),False,True), Lines((1728-60,1230),(1152+60,1230),(235, 68, 42),False,True)],
	
		[Lines((1800,570),(1800,1230),(32,227,58),False,False),Lines((1440,570),(1440,1270),(235, 68, 42),False,True),Lines((2160,630),(2160,1230),(235, 68, 42),False,True)],
	
		[Lines((576*2,360*2),(576*2+400,360*2),(32,227,58),False,False),Lines((576*2,360*2+100),(576*2+200,360*2+100),(235, 68, 42),False,True),Lines((576*3,360*3),(576*3+400,360*3),(32,227,58),False,False),Lines((576*3,360*3+100),(576*3+200,360*3+100),(235, 68, 42),False,True),Lines((576*4,360*4),(576*4+400,360*4),(32,227,58),False,False),Lines((576*4,360*4+100),(576*4+200,360*4+100),(235, 68, 42),False,True)],
		
		[Lines((1728,840),(1728,450),(235, 68, 42),False,True),Lines((2304,840),(2304,450),(235, 68, 42),False,True),Lines((1728,960),(1728,1350),(235, 68, 42),False,True),
		Lines((2304,960),(2304,1350),(235, 68, 42),False,True), Lines((1152+60,900),(1728-60,900),(32,227,58),False,False), Lines((1728+60,900),(2304-60,900),(32,227,58),False,False)],
		
		[Lines((480*3,300*2+35),(480*3,300*3-35),(235, 68, 42),False,True),Lines((480*2+35,300*3),(480*3-35,300*3),(235, 68, 42),False,True),Lines((480*3,300*4-35),(480*3,300*3+35),(235, 68, 42),False,True),Lines((480*4-35,300*3),(480*3+35,300*3),(235, 68, 42),False,True),
		Lines((480*4,300*3+35),(480*4,300*4-35),(235, 68, 42),False,True),Lines((480*4,300*5-35),(480*4,300*4+35),(235, 68, 42),False,True),Lines((480*3+35,300*4),(480*4-35,300*4),(235, 68, 42),False,True),Lines((480*5-35,300*4),(480*4+35,300*4),(235, 68, 42),False,True)]]
		
	circlev = [[Circle((576,257), 50, (0,0,0)),Circle((576,257+450), 50, (0,0,0)),Circle((576*2,257*2), 50, (0,0,0)),Circle((576*2,257*2+450), 50, (0,0,0)), Circle((576*3,257*3), 50, (0,0,0)),Circle((576*3,257*3+450), 50, (0,0,0)),Circle((576*4,257*4), 50, (0,0,0)),Circle((576*4,257*4+450), 50, (0,0,0))],
	
		[Circle((480,900), 50, (0,0,0)), Circle((960,900), 50, (0,0,0)), Circle((1440,900), 50, (0,0,0)), Circle((1920,900), 50, (0,0,0)), Circle((2400,900), 50, (0,0,0))],

		[Circle((2880-480,900), 50, (0,0,0)),Circle((480,900), 50, (0,0,0)),Circle((960,600), 50, (0,0,0)),Circle((960*2,600), 50, (0,0,0)), Circle((960,1200), 50, (0,0,0)), Circle((960*2,1200), 50, (0,0,0))],

		[Circle((720,360), 25, (0,0,0)),Circle((720,360*2), 25, (0,0,0)),Circle((720,360*3), 25, (0,0,0)),Circle((720,360*4), 25, (0,0,0)),Circle((720*2,360), 25, (0,0,0)),Circle((720*2,360*2), 25, (0,0,0)),Circle((720*2,360*3), 25, (0,0,0)),Circle((720*2,360*4), 25, (0,0,0)),Circle((720*3,360), 25, (0,0,0)),Circle((720*3,360*2), 25, (0,0,0)),Circle((720*3,360*3), 25, (0,0,0)),Circle((720*3,360*4), 25, (0,0,0))],

		[Circle((1440,0), 50, (0,0,0)), Circle((1440,600), 50, (0,0,0)),Circle((1440,1800), 50, (0,0,0)), Circle((1440,1200), 50, (0,0,0))],

		[Circle((576,570),50, (0,0,0)),Circle((576,1230),50, (0,0,0)), Circle((1152,570),50, (0,0,0)),Circle((1152,1230),50, (0,0,0)),Circle((1728,570),50, (0,0,0)),Circle((1728,1230),50, (0,0,0)),Circle((2304,570),50, (0,0,0)),Circle((2304,1230),50, (0,0,0))],

		[Circle((720,570),50, (0,0,0)),Circle((1440,1230),50, (0,0,0)),Circle((2160,570),50, (0,0,0))],
		
		[Circle((576,360),25, (0,0,0)),Circle((576+400,360),25, (0,0,0)),Circle((576,460),25, (0,0,0)),Circle((576+200,460),25, (0,0,0))],

		[Circle((576,900),50, (0,0,0)),Circle((1152,900),50, (0,0,0)),Circle((1728,900),50, (0,0,0)),Circle((2304,900),50, (0,0,0))],
		
		[Circle((480,300*2),25, (0,0,0)),Circle((480*2,300*2),25, (0,0,0)),Circle((480*2,300),25, (0,0,0)),Circle((480*2,300*3),25, (0,0,0)),Circle((480*3,300*2),25, (0,0,0)),Circle((480*3,300*3),25, (0,0,0)),Circle((480*3,300*4),25, (0,0,0)),Circle((480*4,300*3),25, (0,0,0)),Circle((480*4,300*4),25, (0,0,0)),Circle((480*4,300*5),25, (0,0,0)),Circle((480*5,300*4),25, (0,0,0))]]
	#===========================================
	
	#makes lines in each circle for intersection checking
	t = levnum
	for l in circlev[t]:
		lev[t].append(Lines((l.center[0] , l.center[1] - l.radius +1), (l.center[0], l.center[1] + l.radius -1), (0,0,0), True, False))
		lev[t].append(Lines((l.center[0] - l.radius +1, l.center[1]), (l.center[0] + l.radius -1, l.center[1]), (0,0,0), True, False))
	
	#makes menu, next, and pervious buttons
	menubtn = PyButton((255,255,255), Rect(0,0,288,100))
	nextbtn = PyButton((255,255,255), Rect(2880-288,1800-180,288,180))
	lastbtn = PyButton((255,255,255), Rect(0,1800-180,288,180))
	
	#defines variables
	running = True
	repeat = False
	adden = []
	stop = False
	ti = 2
	points = []
	cont = []
	pointers = []
	number = 0
	topple = False
	
	#list of strings for drawing notice on the screen
	drawlist = ['Drawing.', 'Drawing.', 'Drawing.', 'Drawing.', 
	'Drawing.', 'Drawing.','Drawing..','Drawing..', 'Drawing..','Drawing..','Drawing..', 'Drawing..','Drawing...','Drawing...','Drawing...','Drawing...','Drawing...','Drawing...']
	
	#waits for player to click
	while wait:
		screen.fill((255,255,255))
		event = pygame.event.poll()
		
		#if it is the first try on this level draws level number
		#==================
		if firstry:
			if levnum == 9:
				screen.blit(pygame.font.Font(None, 150).render('Level ' + str(levnum+1),1,(159,158,163)), (1200,150))
			else:
				screen.blit(pygame.font.Font(None, 150).render('Level ' + str(levnum+1),1,(159,158,163)), (1250,150))
		#===================
		
		#checks if mouse is over any of the buttons and if so draws what it does over it
		#========================================
		if menubtn.contains_click(pygame.mouse.get_pos()):
			screen.blit(pygame.font.Font(None, 65).render('Menu',1,(159,158,163)), (50,25))
		elif nextbtn.contains_click(pygame.mouse.get_pos()) and levnum != hnum:
			screen.blit(pygame.font.Font(None, 100).render('>',1,(159,158,163)), (2830,1700))
		elif lastbtn.contains_click(pygame.mouse.get_pos()) and levnum != 0:
			screen.blit(pygame.font.Font(None, 100).render('<',1,(159,158,163)), (50,1700))
		#========================================
			
		#checks if mouse is down and makes sure it is not clicking any of the button
		#===============
		if event.type == MOUSEBUTTONDOWN:
			if menubtn.contains_click(pygame.mouse.get_pos()):
				wait = False
				stop = True
				menu()
			elif nextbtn.contains_click(pygame.mouse.get_pos()) and levnum != hnum:
				wait = False
				stop = True
				levnum += 1
				game(True,True)
			elif lastbtn.contains_click(pygame.mouse.get_pos()) and levnum != 0:
				wait = False
				stop = True
				levnum -= 1
				game(True,True)
			else:
				points.append(pygame.mouse.get_pos())
				wait = False
		#============
		
		#quits if quit or escape button is pressed
		#=====================
		elif event.type == QUIT:
			pygame.quit()
			sys.exit()
		elif event.type == KEYDOWN:
			if event.key == K_ESCAPE:
				pygame.quit()
				sys.exit()
		#===========================
		
		#lets player go to next or last level with arrow keys
		#========================
			if event.key == 276 and levnum != 0:
				wait = False
				stop = True
				levnum -= 1
				game(True,True)
			elif event.key == 275 and levnum != hnum:
				wait = False
				stop = True
				levnum += 1
				game(True,True)
		#===================
		
		#draws every part of the level
		#======================
		for c in lev[levnum]:
			pygame.draw.line(screen, c.color, (c.p1.x,c.p1.y), (c.p2.x,c.p2.y), 7)
		for c in circlev[levnum]:
			pygame.draw.circle(screen, c.color, c.center, c.radius, 0)
		#=====================
		
		pygame.display.flip()
	
	#adds mouse position to necessary places and creates a few variables
	#=======================
	fpos = prevpos = pygame.mouse.get_pos()
	points.append(pygame.mouse.get_pos())
	popper = False
	u = 0
	h = 0
	#=======================
	
	#loops until either wins level or ends level and in loop it continues the line
	while running and not stop:
		
		#resets last and resets screen along with drawing 'drawing' on the screen and changing the amount of dots on drawing
		#============
		last = []
		screen.fill((255,255,255))
		screen.blit(pygame.font.Font(None, 55).render(drawlist[h],1,(159,158,163)), (2670,25))
		if h != len(drawlist)-1:
			h += 1
		else:
			h = 0
		event = pygame.event.poll()
		#==============
		
		#where it goes through if player has not complete the line yet
		if not repeat:
		
			#checks for quitting
			#==================
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
			elif event.type == KEYDOWN:
				if event.key == K_ESCAPE:
					pygame.quit()
					sys.exit()
			#====================
			
			#does not check for buttons while drawing line
			
			#checks for click and adds coordinates to list
			#=========================
			elif event.type == MOUSEBUTTONDOWN:
				repeat = True
				pointers = addent(tell, adden)
				popper = True
				fir = True
			elif event.type == MOUSEMOTION:
				(x, y) = event.pos
				points.append(event.pos)
				u += 1
				adden.append((x - fpos[0], y - fpos[1]))
			#========================
			
			#draws your line
			pygame.draw.lines(screen, color, False, points, 5)
			
			#part of complicated line drawing thing that i honestly don't remember how it works
			#=======================
			for l in points:
				last.append(l)
			prevpos = pygame.mouse.get_pos()
			adden.append((prevpos[0] - fpos[0], prevpos[1] - fpos[1]))
			tell = (fpos[0] + adden[len(adden) - 1][0], fpos[1] + adden[len(adden) - 1][1])
			#=====================
			
		#what it goes through if player has completed line
		else:
		
			#checks if mouse is over any of the buttons and if so draws what it does over it
			#========================================
			if menubtn.contains_click(pygame.mouse.get_pos()):
				screen.blit(pygame.font.Font(None, 65).render('Menu',1,(159,158,163)), (50,25))
			elif nextbtn.contains_click(pygame.mouse.get_pos()) and levnum != hnum:
				screen.blit(pygame.font.Font(None, 100).render('>',1,(159,158,163)), (2830,1700))
			elif lastbtn.contains_click(pygame.mouse.get_pos()) and levnum != 0:
				screen.blit(pygame.font.Font(None, 100).render('<',1,(159,158,163)), (50,1700))
			#========================================
			
			#checks if any of the buttons are clicked or if clicked to restart and checks for quitting
			#================================
			if event.type == MOUSEBUTTONDOWN:
				if menubtn.contains_click(pygame.mouse.get_pos()):
					wait = False
					stop = True
					menu()
				elif nextbtn.contains_click(pygame.mouse.get_pos()) and levnum != hnum:
					wait = False
					stop = True
					levnum += 1
					game(True, True)
				elif lastbtn.contains_click(pygame.mouse.get_pos()) and levnum != 0:
					wait = False
					stop = True
					levnum -= 1
					game(True, True)
				else:
					screen.fill((255,255,255))
					stop = True
					game(True, False)
			elif event.type == QUIT:
				pygame.quit()
				sys.exit()
			elif event.type == KEYDOWN:
				if event.key == K_ESCAPE:
					pygame.quit()
					sys.exit()
			#=========================
			
			#all part of the complicated line drawing thing that I still don't remember how it works... maybe i should start writing comments as I do it instead of doing it on saturday
			#=============================
			if u > 20:
				u = 20
			if len(points) >= 3:
				pygame.draw.lines(screen, color, False, points, 5)
				for l in points:
					last.append(l)
				points.pop(0)
				pygame.draw.lines(screen, color, False, pointers[0:ti:], 5)
				for l in pointers[0:ti:]:
					last.append(l)
			else:
				if fir:
					t = 1
					fir = False
				if u > 1:
					pygame.draw.lines(screen, color, False, pointers[ti:ti+u:], 5)
				for l in pointers[ti:ti+u:]:
					last.append(l)
			
			ti += 1
			if ti >= len(adden) - (u):
				points = pointers[ti:ti+u:]
				ti = 2
				tell = (tell[0] + adden[len(adden) - 1][0], tell[1] + adden[len(adden) - 1][1])
				pointers = addent(tell, adden)
				fir = True
		if len(points) + len(pointers) >= 20:
			popper = True
		if popper and len(points) > 3:
			points.pop(0)
		else:
			popper = False
		#=======================
			
		#checks if line is offscreen and also checks if line crossed anything
		#===============
		offscreen = True
		for c in lev[levnum]:
			for t in range(0,len(last)-1):
				if c.intersect([last[t],last[t+1]]):
					offscreen = False
					if (last[t],last[t+1]) not in cont:
						cont.append((last[t],last[t+1]))
						if c.forbid:
							screen.fill((255,255,255))
							stop = True
							game(True, False)
						else: 
							c.isRed = not c.isRed
							
							#if it does cross a line stops player from keeping on drawing
							repeat = True
							
							pointers = addent(tell, adden)
							popper = True
							fir = True
							if c.isRed:
								c.color = (235, 68, 42)
							else:
								c.color = (32,227,58)
				elif last[t][0] > 0 and last[t][1] > 0 and last[t][0] < 2880 and last[t][1] < 1800:
					offscreen = False
		if offscreen:	
			screen.fill((255,255,255))
			stop = True
			game(True, False)
		#================
			
		#checks if you beat it and beat the last level
		#========================
		if topple and levnum == 9:
			screen.fill((255,255,255))
			screen.blit(pygame.font.Font(None, 150).render('Congratulation! You beat the game!',1,(159,158,163)), (550,150))
			screen.blit(pygame.font.Font(None, 100).render('If you would like to go back and play any previous levels',1,(159,158,163)), (500,400))
			screen.blit(pygame.font.Font(None, 100).render('You can go to \'levels\' from the main menu',1,(159,158,163)), (650,550))
			screen.blit(pygame.font.Font(None, 200).render('Thanks For Playing!',1,(159,158,163)), (750,800))
			
			screen.blit(pygame.font.Font(None, 150).render('Click anywhere to go back to the main menu',1,(159,158,163)), (400,1200))
			pygame.display.flip()
			while True:
				event = pygame.event.poll()
				if event.type == MOUSEBUTTONDOWN:
					stop = True
					levnum = 0
					menu()
					break
		#=======================
		
		#checks if you won and draws the level
		#=======================
		elif topple:
			screen.fill((255,255,255))
			stop = True
			levnum += 1
			writer()
			game(True, True)
		
		win = True
		if not topple:
			for c in lev[levnum]:
				if c.isRed:
					win = False
				pygame.draw.line(screen, c.color, (c.p1.x,c.p1.y), (c.p2.x,c.p2.y), 7)
			for c in circlev[levnum]:
				pygame.draw.circle(screen, c.color, c.center, c.radius, 0)
		if win:
			win = False
			topple = True
		#=======================
		
		pygame.display.flip()

#menu		
def menu():
	global colors, color, colnum, hnum, levnum
	
	#defines all buttons and variables
	blocks = []
	menubtn = PyButton((255,255,255), Rect(0,0,288,180))
	blocks.append(PyButton(color, Rect(200,160,800,300)))
	blocks.append(PyButton(color, Rect(200,620,400,160)))
	blocks.append(PyButton(color, Rect(200,820,400,160)))
	blocks.append(PyButton(color, Rect(200,1020,400,160)))
	free = False
	levels = False
	set = False
	tut = False
	
	#loop it goes through while waiting for click on button or quit
	while True:
		screen.fill((255,255,255))
		
		#if mouse over button draws what it does and draws everything
		#==============
		if menubtn.contains_click(pygame.mouse.get_pos()):
			screen.blit(pygame.font.Font(None, 65).render('Quit',1,(159,158,163)), (50,25))
		for btn in blocks:
			pygame.draw.rect(screen, btn.color, btn.shape)
		screen.blit(pygame.font.Font(None, 210).render('Play',1,(255,255,255)), (400, 250))
		screen.blit(pygame.font.Font(None, 90).render('Levels',1,(255,255,255)), (265, 680))
		screen.blit(pygame.font.Font(None, 90).render('Tutorial',1,(255,255,255)), (260, 880))
		screen.blit(pygame.font.Font(None, 90).render('Settings',1,(255,255,255)), (260, 1080))
		screen.blit(pygame.font.Font(None, 300).render('Woah',1,(0,0,0)), (2000,250))
		#===============
		
		#checks for quitting
		#==============
		event = pygame.event.poll()
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
		elif event.type == KEYDOWN:
			if event.key == K_ESCAPE:
				pygame.quit()
				sys.exit()
		#===============
		
		#checks if any of the buttons are clicked and does appropriate thing
		#=========================
		elif event.type == MOUSEBUTTONDOWN:
			if blocks[0].contains_click(pygame.mouse.get_pos()):
				free = True
			elif blocks[1].contains_click(pygame.mouse.get_pos()):
				levels = True
			elif blocks[2].contains_click(pygame.mouse.get_pos()):
				tut = True
			elif blocks[3].contains_click(pygame.mouse.get_pos()):
				set = True
			elif menubtn.contains_click(pygame.mouse.get_pos()):
				pygame.quit()
				sys.exit()
		#=================
				
		#breaks if any of the buttons are clicked
		if free or set or levels or tut:
			break
			
		pygame.display.flip()
	
	#goes to correct next function based off of variable that changed bc of the click
	#===================
	if free:
		game(True, True)
	elif levels:
		leve()
	elif set:
		settings()
	elif tut:
		tute(True,True,True,True)

#settings	
def settings():
	
	#global and variable statements
	global color, colnum
	stop = False
	
	#loop
	while not stop:
		
		#creates and draws all buttons
		#========================
		menubtn = PyButton((255,255,255), Rect(0,0,288,180))
		blocks = []
		screen.fill((255,255,255))
		screen.blit(pygame.font.Font(None, 210).render('Choose Color',1,(0,0,0)), (1440,250))
		for t in colors:
			if t.chosen == True:
				blocks.append(PyButton((0,0,0), Rect(t.block[0]-15,t.block[1]-15,t.block[2]+30,t.block[3]+30)))
		for t in colors:
			blocks.append(PyButton(t.color, Rect(t.block)))
		for btn in blocks:
			pygame.draw.rect(screen, btn.color, btn.shape)
		#=========================
		
		#checks if mouse is over menu button, if mouse clicks menu button, and if quit
		#====================
		event = pygame.event.poll()
		if menubtn.contains_click(pygame.mouse.get_pos()):
			screen.blit(pygame.font.Font(None, 65).render('Menu',1,(159,158,163)), (50,25))
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
		elif event.type == KEYDOWN:
			if event.key == K_ESCAPE:
				pygame.quit()
				sys.exit()
		elif event.type == MOUSEBUTTONDOWN:
			colors[colnum].chosen = False
			if menubtn.contains_click(pygame.mouse.get_pos()):
				stop = True
				menu()
				break
			#=======================
			
			#checks if any buttons are clicked and selects the correct color as the color and saves it as the color
			#=============
			elif blocks[1].contains_click(pygame.mouse.get_pos()):
				colnum = 0
			elif blocks[2].contains_click(pygame.mouse.get_pos()):
				colnum = 1
			elif blocks[3].contains_click(pygame.mouse.get_pos()):
				colnum = 2
			elif blocks[4].contains_click(pygame.mouse.get_pos()):
				colnum = 3
			elif blocks[5].contains_click(pygame.mouse.get_pos()):
				colnum = 4
			elif blocks[6].contains_click(pygame.mouse.get_pos()):
				colnum = 5
			colors[colnum].chosen = True
			color = colors[colnum].color
			writer()
			#==============
			
		pygame.display.flip()

#levels
def leve():

	#global statements and variable creation
	global colors, color, colnum, hnum, levnum
	stop = False
	
	#loop
	while not stop:
	
		#draws and blits and creates everything on screen
		#==================
		menubtn = PyButton((255,255,255), Rect(0,0,288,180))
		blocks = []
		screen.fill((255,255,255))
		screen.blit(pygame.font.Font(None, 180).render('Select Level',1,(0,0,0)), (1040,200))
		xpl = 480
		ypl = 800
		for t in range(0,hnum+1):
			blocks.append(PyButton(color, Rect(xpl-80, ypl, 160,160)))
			pygame.draw.rect(screen, blocks[len(blocks)-1].color,  blocks[len(blocks)-1].shape)
			if t != 9:
				screen.blit(pygame.font.Font(None, 100).render(str(t+1),1,(255,255,255)), (xpl-20,ypl+50))
			else:
				screen.blit(pygame.font.Font(None, 100).render(str(t+1),1,(255,255,255)), (xpl-40,ypl+50))
			xpl += 480
			if xpl == 2880:
				xpl = 480
				ypl = 1300
		for t in range(hnum+1, 10):	
			locked = (PyButton((0,0,0), (xpl-80, ypl, 160,160)))
			pygame.draw.rect(screen, locked.color,  locked.shape)
			if t != 9:
				screen.blit(pygame.font.Font(None, 100).render(str(t+1),1,(255,255,255)), (xpl-20,ypl+50))
			else:
				screen.blit(pygame.font.Font(None, 100).render(str(t+1),1,(255,255,255)), (xpl-40,ypl+50))
			xpl += 480
			if xpl == 2880:
				xpl = 480
				ypl = 1300
		#====================
		
		#checks menubutton and quitting
		#===================
		event = pygame.event.poll()
		if menubtn.contains_click(pygame.mouse.get_pos()):
			screen.blit(pygame.font.Font(None, 65).render('Menu',1,(159,158,163)), (50,25))
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
		elif event.type == KEYDOWN:
			if event.key == K_ESCAPE:
				pygame.quit()
				sys.exit()
		elif event.type == MOUSEBUTTONDOWN:
			if menubtn.contains_click(pygame.mouse.get_pos()):
				stop = True
				menu()
				break
			#==============
			
			#checks if clicking on level button and if so goes to that level
			#===============
			else:
				for t in range(0,len(blocks)):
					if blocks[t].contains_click(pygame.mouse.get_pos()):
						levnum = t
						stop = True
						game(True, True)
						break
			#==============
			
		pygame.display.flip()

#tutorial
#all of the comments necessary in this one should be in the other functions as all the loops are 99% copy and pasted
def tute(inc,inc2,inc3,inc4):
	global colors, color, colnum, hnum, levnum, lev, circlev
	nonmenu = False
	while inc:
		blocks = []
		menubtn = PyButton((0,0,0), Rect(0,0,240,130))
		blocks.append(PyButton(color, Rect(200,160,800,300)))
		blocks.append(PyButton(color, Rect(200,620,400,160)))
		blocks.append(PyButton(color, Rect(200,820,400,160)))
		blocks.append(PyButton(color, Rect(200,1020,400,160)))
		blocks.append(PyButton((255,255,255), Rect(10,10,220,110)))
		while True:
			colors[colnum].chosen = True
			color = colors[colnum].color
			event = pygame.event.poll()
			screen.fill((255,255,255))
			screen.blit(pygame.font.Font(None, 65).render('Quit',1,(159,158,163)), (50,25))
			pygame.draw.rect(screen, menubtn.color, menubtn.shape)
			for btn in blocks:
				pygame.draw.rect(screen, btn.color, btn.shape)
			screen.blit(pygame.font.Font(None, 210).render('Play',1,(255,255,255)), (400, 250))
			screen.blit(pygame.font.Font(None, 90).render('Levels',1,(255,255,255)), (265, 680))
			screen.blit(pygame.font.Font(None, 90).render('Tutorial',1,(255,255,255)), (260, 880))
			screen.blit(pygame.font.Font(None, 90).render('Settings',1,(255,255,255)), (260, 1080))
			screen.blit(pygame.font.Font(None, 70).render('You can always go back to the last screen that you were on by clicking on the top left corner of the screen.',1,color), (200, 1600))
			screen.blit(pygame.font.Font(None, 60).render('Press Space to Continue or Escape to Quit the Tutorial',1,color), (900, 1700))
			screen.blit(pygame.font.Font(None, 65).render('Quit',1,(159,158,163)), (50,25))

			screen.blit(pygame.font.Font(None, 300).render('Woah',1,(0,0,0)), (2000,250))
			pygame.display.flip()
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
			elif event.type == KEYDOWN:
				if event.key == K_ESCAPE:
					inc = False
					inc2 = False
					inc3 = False
					inc4 = False
					menu()
				elif event.key == 32:
					inc = False
					break
			pygame.display.flip()
	while inc2:
		menubtn = PyButton((255,255,255), Rect(0,0,288,180))
		blocks = []
		screen.fill((255,255,255))
		screen.blit(pygame.font.Font(None, 210).render('Choose Color',1,(0,0,0)), (1440,250))
		screen.blit(pygame.font.Font(None, 55).render('This is the settings page. You can get to this page by selecting \'settings\' from the menu. From here you can change the color scheme of the game.',1,color), (100, 1600))
		screen.blit(pygame.font.Font(None, 55).render('Press Space to Continue or Escape to Quit the Tutorial',1,color), (900, 1700))
		for t in colors:
			if t.chosen == True:
				blocks.append(PyButton((0,0,0), Rect(t.block[0]-15,t.block[1]-15,t.block[2]+30,t.block[3]+30)))
		for t in colors:
			blocks.append(PyButton(t.color, Rect(t.block)))
		for btn in blocks:
			pygame.draw.rect(screen, btn.color, btn.shape)
		event = pygame.event.poll()
		if menubtn.contains_click(pygame.mouse.get_pos()):
			screen.blit(pygame.font.Font(None, 65).render('Menu',1,(159,158,163)), (50,25))
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
		elif event.type == KEYDOWN:
			if event.key == K_ESCAPE:
				inc = False
				inc2 = False
				inc3 = False
				inc4 = False
				menu()
			elif event.key == 276:
				inc = False
				inc2 = False
				inc3 = False
				inc4 = False
				tute(True,True,True,True)
			elif event.key == 32:
					inc2 = False
					break
		elif event.type == MOUSEBUTTONDOWN:
			colors[colnum].chosen = False
			if blocks[1].contains_click(pygame.mouse.get_pos()):
				colnum = 0
			elif blocks[2].contains_click(pygame.mouse.get_pos()):
				colnum = 1
			elif blocks[3].contains_click(pygame.mouse.get_pos()):
				colnum = 2
			elif blocks[4].contains_click(pygame.mouse.get_pos()):
				colnum = 3
			elif blocks[5].contains_click(pygame.mouse.get_pos()):
				colnum = 4
			elif blocks[6].contains_click(pygame.mouse.get_pos()):
				colnum = 5
			colors[colnum].chosen = True
			color = colors[colnum].color
			writer()
		pygame.display.flip()
	while inc3:
		menubtn = PyButton((255,255,255), Rect(0,0,288,180))
		blocks = []
		screen.fill((255,255,255))
		screen.blit(pygame.font.Font(None, 180).render('Select Level',1,(0,0,0)), (1040,200))
		xpl = 480
		ypl = 800
		for t in range(0,hnum+1):
			blocks.append(PyButton(color, Rect(xpl-80, ypl, 160,160)))
			pygame.draw.rect(screen, blocks[len(blocks)-1].color,  blocks[len(blocks)-1].shape)
			if t != 9:
				screen.blit(pygame.font.Font(None, 100).render(str(t+1),1,(255,255,255)), (xpl-20,ypl+50))
			else:
				screen.blit(pygame.font.Font(None, 100).render(str(t+1),1,(255,255,255)), (xpl-40,ypl+50))
			xpl += 480
			if xpl == 2880:
				xpl = 480
				ypl = 1300
		for t in range(hnum+1, 10):	
			locked = (PyButton((0,0,0), (xpl-80, ypl, 160,160)))
			pygame.draw.rect(screen, locked.color,  locked.shape)
			if t != 9:
				screen.blit(pygame.font.Font(None, 100).render(str(t+1),1,(255,255,255)), (xpl-20,ypl+50))
			else:
				screen.blit(pygame.font.Font(None, 100).render(str(t+1),1,(255,255,255)), (xpl-40,ypl+50))
			xpl += 480
			if xpl == 2880:
				xpl = 480
				ypl = 1300
		event = pygame.event.poll()
		if menubtn.contains_click(pygame.mouse.get_pos()):
			screen.blit(pygame.font.Font(None, 65).render('Menu',1,(159,158,163)), (50,25))
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
		elif event.type == KEYDOWN:
			if event.key == K_ESCAPE:
				inc = False
				inc2 = False
				inc3 = False
				inc4 = False
				menu()
			elif event.key == 276:
				inc = False
				inc2 = False
				inc3 = False
				inc4 = False
				tute(False,True,True,True)
		elif event.type == MOUSEBUTTONDOWN:
			if blocks[0].contains_click(pygame.mouse.get_pos()):
				inc3 = False
				inc4 = True
				levnum = 0
				break	
		screen.blit(pygame.font.Font(None, 50).render('This is the levels page. You can get to this page by selecting \'levels\' from the menu. From here you can see and select to play all of the of the levels that you have unlocked.',1,(color)), (30, 1600))
		screen.blit(pygame.font.Font(None, 60).render('Select the first level in order to continue or Press Escape to Quit the Tutorial',1,color), (700, 1700))
		pygame.display.flip()
	while inc4:
		lev = [[Lines((576*2,257*2),(576*2,257*2+450),(235, 68, 42),False,True),Lines((576*3,257*3), (576*3,257*3+450),(235, 68, 42),False,True),Lines((576*4,257*4), (576*4,257*4+450),(235, 68, 42),False,True)]]
		circlev = [[Circle((576,257), 50, (0,0,0)),Circle((576,257+450), 50, (0,0,0)),Circle((576*2,257*2), 50, (0,0,0)),Circle((576*2,257*2+450), 50, (0,0,0)), Circle((576*3,257*3), 50, (0,0,0)),Circle((576*3,257*3+450), 50, (0,0,0)),Circle((576*4,257*4), 50, (0,0,0)),Circle((576*4,257*4+450), 50, (0,0,0))]]
		for t in range(0,len(circlev)):
			for l in circlev[t]:
				lev[t].append(Lines((l.center[0] , l.center[1] - l.radius +1), (l.center[0], l.center[1] + l.radius -1), (0,0,0), True, False))
				lev[t].append(Lines((l.center[0] - l.radius +1, l.center[1]), (l.center[0] + l.radius -1, l.center[1]), (0,0,0), True, False))
		ti = 2
		points = []
		cont = []
		pointers = []
		number = 0
		cont = 0
		while cont != 5:
			screen.fill((255,255,255))
			event = pygame.event.poll()
			if levnum == 9:
				screen.blit(pygame.font.Font(None, 150).render('Level ' + str(levnum+1),1,(159,158,163)), (1200,150))
			else:
				screen.blit(pygame.font.Font(None, 150).render('Level ' + str(levnum+1),1,(159,158,163)), (1250,150))
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
			elif event.type == KEYDOWN:
				if event.key == K_ESCAPE:
					inc = False
					inc2 = False
					inc3 = False
					inc4 = False
					menu()
					break
				elif event.key == 276:
					if cont != 0:
						cont -= 1
					else:
						inc = False
						inc2 = False
						inc3 = False
						inc4 = False
						tute(False,False,True,True)
				elif event.key == 32:
					cont += 1 
			for c in lev[levnum]:
				pygame.draw.line(screen, c.color, (c.p1.x,c.p1.y), (c.p2.x,c.p2.y), 7)
			for c in circlev[levnum]:
				pygame.draw.circle(screen, c.color, c.center, c.radius, 0)
			if cont == 0:
				screen.blit(pygame.font.Font(None, 50).render('This is the actual game. You can get to the last level you played through the menu by selecting \'play\' or you can select a specific level by going into the levels page.',1,(color)), (90, 1600))
				screen.blit(pygame.font.Font(None, 60).render('Press Space to Continue or Press Escape to Quit the Tutorial',1,color), (900, 1700))
			elif cont == 1:
				screen.blit(pygame.font.Font(None, 50).render('The goal of the game is to turn all of the lines green without hitting the black circles.',1,(color)), (50, 1500)) 
				screen.blit(pygame.font.Font(None, 50).render('The lines flip colors from green to red or vice versa every time that your line crosses over them',1,(color)), (50, 1600))
				screen.blit(pygame.font.Font(None, 60).render('Press Space to Continue or Press Escape to Quit the Tutorial',1,color), (900, 1700))
			elif cont == 2:
				screen.blit(pygame.font.Font(None, 50).render('You draw the line by clicking once, then end it either by crossing a line or by clicking a second time.',1,(color)), (300, 1600))
				screen.blit(pygame.font.Font(None, 60).render('Press Space to Continue or Press Escape to Quit the Tutorial',1,color), (900, 1700))
			elif cont == 3:
				screen.blit(pygame.font.Font(None, 50).render('Once you finish drawing the line the game automatically repeats the pattern until it either turns all of the lines green or you click again to stop it and try again',1,(color)), (100, 1600))
				screen.blit(pygame.font.Font(None, 60).render('Press Space to Continue or Press Escape to Quit the Tutorial',1,color), (900, 1700))	
			elif cont == 4:
				screen.blit(pygame.font.Font(None, 50).render('The best way to truly understand it is to play it and experiment with it. Beware it can glitch and skip over a line, if it does this just try the same line again',1,(color)), (100, 1500))
				screen.blit(pygame.font.Font(None, 50).render('So how about you give it a try! Also you can tell if it is drawing by looking in the top right corner',1,(color)), (500, 1600))
				screen.blit(pygame.font.Font(None, 60).render('Press Space to Play Level 1 or Press Escape to Go to the Menu',1,color), (900, 1700))
			pygame.display.flip()	
		if inc4:
			game(True,False)
			break
		else:
			nonmenu = True
	if nonmenu:
		menu()

menu()