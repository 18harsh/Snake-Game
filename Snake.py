import pygame
import random
pygame.init()


class snake():
	def __init__(self):
		self.width = 500
		self.rows = 20
		self.win = pygame.display.set_mode((self.width,self.width))	
		self.flag = True
		self.xs = 25
		self.ys = 25
		self.lastkey = "down"
		self.xf = random.randrange(500-1)//25*25
		self.yf = random.randrange(500-1)//25*25
		self.dirnx = 0
		self.dirny = 1
		self.bodylen = [" "]
		self.snakepos= []
		self.xold = self.xs
		self.yold = self.ys
	def drawsnake(self):
		self.snakepos.insert(0,(self.xold,self.yold,25,25))
		pygame.draw.rect(self.win,(0,255,0),(self.xs,self.ys,25,25))
		pygame.draw.rect(self.win,(255,0,0),(self.xf,self.yf,25,25))
		for i in range(len(self.bodylen)-1):
			pygame.draw.rect(self.win,(0,255,0),self.snakepos[i])
		if len(self.bodylen) > len(self.snakepos):	
			pass
		else:
			self.snakepos.pop()	
	def move(self):
		self.xold = self.xs
		self.yold = self.ys
		self.xs+=self.dirnx*25
		self.ys+=self.dirny*25
		if self.xs<0:
			self.xs=475
		if self.xs > 475:
			self.xs = 0
		if self.ys < 0:
			self.ys = 475
		if self.ys > 475:
			self.ys = 0	
		if self.xs == self.xf and self.ys == self.yf:
			self.bodylen.append(" ")
			self.xf = random.randrange(500-1)//25*25
			self.yf = random.randrange(500-1)//25*25	
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
			keys = pygame.key.get_pressed()
			for key in keys:
				if keys[pygame.K_LEFT] and self.lastkey!="right":
					self.lastkey = "left"
					self.dirnx = -1
					self.dirny = 0
				elif keys[pygame.K_RIGHT] and self.lastkey!="left":
					self.lastkey = "right"
					self.dirnx = 1
					self.dirny = 0
					
				elif keys[pygame.K_UP] and self.lastkey != "down":
					self.lastkey = "up"
					self.dirnx = 0
					self.dirny = -1
					
				elif keys[pygame.K_DOWN] and self.lastkey!= "up":
					self.lastkey = "down"
					self.dirnx = 0
					self.dirny = 1	


	def drawgrid(self):
		spacedist = self.width//self.rows
		x = y = 0
		for _ in range(self.rows):
			x+=spacedist
			y+=spacedist
			pygame.draw.line(self.win,(255,255,255),(x,0),(x,self.width))
			pygame.draw.line(self.win,(255,255,255),(0,y),(self.width,y))
	def redrawWindow(self):
		self.win.fill((0,0,0))
		s.drawgrid()
		s.drawsnake()
		pygame.display.update()
		
	def main(self):
		clock = pygame.time.Clock()
		while self.flag:
			pygame.time.delay(50)
			clock.tick(10)
			s.redrawWindow()
			s.move()
			if (self.xs,self.ys,25,25) in self.snakepos:
				self.flag =False

s = snake()
s.main()			
