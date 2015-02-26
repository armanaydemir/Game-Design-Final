#!/usr/bin/env python2.7
#all classes used in drawer.py
#Arman Aydemir
#June 1st, 2014

import random
import math
import time
import pygame
from pygame import *

#class for constructing buttons
class PyButton:
	color = None
	shape = None
	screen = None
	
	#initializes variables
	def __init__(self, color, shape):
		pygame.init()
		self.color = color
		self.shape = shape	
		
	def contains_click(self, point):
		return self.shape.collidepoint(point)

#class for colors		
class Color:
	name = None
	color = None
	chosen = None
	place = None
	def __init__(self, name, color, chosen, block):
		self.name = name
		self.color = color
		self.chosen = chosen
		self.block = block
		
#class used as endpoints of a line
class Point:
	x = None
	y = None
	def __init__(self, t):
		self.x = t[0]
		self.y = t[1]
	
#class for creating lines
class Lines:
	p1 = None
	p2 = None
	forbid = None
	color = None
	
	def __init__(self, p1, p2, color, forbid, isRed):
		self.p1 = Point(p1)
		self.p2 = Point(p2)
		self.color = color
		self.forbid = forbid
		self.isRed = isRed
		
	def __str__(self):
		if self.isRed:
			return str((self.p1,self.p2)) + 'is Red'
		else:
			return str((self.p1,self.p2)) + 'is not Red'	
    	
    #checks if intersecting with another line (from http://bryceboe.com/2006/10/23/line-segment-intersection-algorithm/)
    #==========================
	def intersect(self, other):
		other = Lines(other[0],other[1], (0,0,0), False, False)
		return self.ccw(self.p1,other.p1,other.p2) != self.ccw(self.p2,other.p1,other.p2) and self.ccw(self.p1,self.p2,other.p1) != self.ccw(self.p1,self.p2,other.p2)
		
	def ccw(self,A,B,C):
		return (C.y-A.y)*(B.x-A.x) > (B.y-A.y)*(C.x-A.x)
	#=====================================================

#class for creating circles
class Circle:
	center = None
	radius = 0
	color = None
	
	def __init__(self, cen, rad, col):
		self.center = cen
		self.radius = rad
		self.color = col