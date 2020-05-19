import pygame 
import time
import random
import cx_Freeze
pygame.init()
WIDTH,HEIGHT = (800,600)
win = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Snake")

apple = pygame.transform.scale(pygame.image.load('apple2.png'),(20,20))
bg = pygame.transform.scale(pygame.image.load('background.jpg'),(WIDTH,HEIGHT))


def message_to_screen(msg,type):
	font = pygame.font.SysFont("comicsans",40)
	screen_text = font.render(msg,True,type)
	win.blit(screen_text,[WIDTH/2-screen_text.get_width()/2,HEIGHT/2-screen_text.get_height()/2])

def snake(rect_width,snakelist):
	for i in snakelist:
		pygame.draw.circle(win,(255,255,0),(int(i[0]+rect_width/2),int(i[1]+rect_width/2)),int(rect_width/2))

def Score(score):
	font = pygame.font.SysFont("comicsans",40)
	screen_text = font.render("Score : "+str(score),True,(0,0,0))
	win.blit(screen_text,[0,0])
def main():
	head = pygame.image.load('snakehead.png')
	rotate_img = pygame.transform.rotate(head,0)
	run = True
	gameover = False
	rect_width = 20
	lead_x = WIDTH/2
	lead_y = HEIGHT/2
	print(lead_x,lead_y)
	lead_x_change = 0
	lead_y_change = 0
	FPS = 60
	clock = pygame.time.Clock()
	AppleX = round(random.randrange(0,WIDTH-rect_width)/10.0)*10.0
	AppleY = round(random.randrange(0,HEIGHT-rect_width)/10.0)*10.0
	snakelist=[]
	snakelength = 1
	score = 0
	while run:
		clock.tick(FPS-30)
		pygame.time.delay(50)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
		keys = pygame.key.get_pressed()
		if keys[pygame.K_LEFT] and lead_x_change==0:
			lead_x_change= -rect_width
			lead_y_change=0
			rotate_img = pygame.transform.rotate(head,90)
		elif keys[pygame.K_RIGHT] and lead_x_change == 0:
			lead_x_change= rect_width
			lead_y_change=0
			rotate_img = pygame.transform.flip(pygame.transform.rotate(head,270),False,True)
		elif keys[pygame.K_UP] and lead_y_change==0:
			lead_y_change= -rect_width
			lead_x_change=0
			rotate_img = pygame.transform.rotate(head,0)
		elif keys[pygame.K_DOWN] and lead_y_change==0:
			lead_y_change= rect_width
			lead_x_change=0
			rotate_img = pygame.transform.rotate(head,180)
		lead_x+=lead_x_change
		lead_y+=lead_y_change
			
		if  0 >= lead_x or lead_x>= WIDTH or 0>= lead_y or lead_y>= HEIGHT or [lead_x,lead_y] in snakelist:	
			gameover = True
		elif AppleX + rect_width-10>= lead_x>= AppleX and (AppleY+rect_width-10>=lead_y>= AppleY or AppleY-10>=lead_y>= AppleY-rect_width):
			AppleX = round(random.randrange(0,WIDTH-rect_width)/20.0)*20.0
			AppleY = round(random.randrange(0,HEIGHT-rect_width)/20.0)*20.0
			snakelength +=1	
			score+=1
		win.fill((0,0,0))
		win.blit(bg, (0,0))
		win.blit(apple, (AppleX,AppleY))
		win.blit(rotate_img, (lead_x,lead_y))		
		snake(rect_width,snakelist)
		Score(score)
		pygame.display.update()
		snakehead=[]
		snakehead.append(lead_x)
		snakehead.append(lead_y)
		snakelist.append(snakehead)
		if len(snakelist) >= snakelength:
			del snakelist[0]

		if gameover == True:
			message_to_screen("You Loose",(0,0,0))
			pygame.display.update()
			time.sleep(2)
		
		while gameover == True:
			win.fill((255,255,255))
			win.blit(bg, (0,0))
			message_to_screen("Game Over press enter to play it again or 'q' to quit",(0,0,0))
			pygame.display.update()
			event = pygame.event.wait()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_q:
					gameover = False
					run = False
				else:
					main()		
	pygame.quit()		
main()