import pygame, sys
from pygame.locals import *

import colorama
from colorama import Fore, Style, init
from colorama import init as colorama_init
import time
import sys
from termcolor import cprint 
from pyfiglet import figlet_format

WINDOWWIDTH = 800
WINDOWHEIGHT = 500 

WHITE = (255, 255, 255)
RED   = (255,   0,   0)
GREEN = (  0, 255,   0)
ORANGE = '#F9AE57'
ORANGE_2 = '#D99700'
GREY = '#4F565E'
pygame.init()

FPS = 100
fpsClock = pygame.time.Clock()

DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
pygame.display.set_caption('DedNine')

# a1_x, a1_y = 30,80
# a2_x, a2_y = a1_x - 15, a1_y
# a3_x, a3_y = 80, a1_y
# a4_x, a4_y = a3_x - 15, a1_y
# i1_x, i1_y, r1 = a1_x - 7, a1_y + 5, 15
# i2_x, i2_y, r2 = a3_x - 7, a3_y + 5, 15

# carSurface = pygame.Surface((100, 100), SRCALPHA)
# pygame.draw.polygon(carSurface, ORANGE, ((a1_x,a1_y), (a2_x, a2_y), (35, 0), (55, 0), (a3_x, a3_y), (a4_x, a4_y), (45, 20),(30,80)))
# pygame.draw.circle(carSurface, ORANGE_2, (i1_x, i1_y), r1)
# pygame.draw.circle(carSurface, ORANGE_2, (i2_x, i2_y), r2)
# pygame.draw.circle(carSurface, GREEN, ())

def rotate(surface_1, surface_2, angle, x):
	rotated_surface_1 = pygame.transform.rotozoom(surface_1,angle,1)
	rotated_rect_1 = rotated_surface_1.get_rect(center = (x,400))
	rotated_surface_2 = pygame.transform.rotozoom(surface_2,angle,1)
	rotated_rect_2 = rotated_surface_2.get_rect(center = (x+125,400))
	return rotated_surface_1, rotated_rect_1, rotated_surface_2, rotated_rect_2

def draw_bg():
	DISPLAYSURF.blit(bg_1, (bg_x_pos+800,0))
	DISPLAYSURF.blit(bg_1, (bg_x_pos,0))
def draw_floor():
	DISPLAYSURF.blit(floor, (floor_x_pos+800,350))
	DISPLAYSURF.blit(floor, (floor_x_pos,350))

car_x = 800
xe_dai = pygame.image.load('C:\\Users\\DucPhan\\Downloads\\xegau.png')

banh_xe_dai = pygame.image.load('C:\\Users\\DucPhan\\Downloads\\banhxegau.png')
banh_xe_dai_rect = banh_xe_dai.get_rect(center = (120,372))

bg_1 = pygame.image.load('C:\\Users\\DucPhan\\Downloads\\E760357F-DDBF-40DE-B975-3D28514E595B.jpg')
ds = pygame.image.load('C:\\Users\\DucPhan\\Downloads\\danhsach1.png').convert_alpha()

banh_xe_dai_2 = pygame.image.load('C:\\Users\\DucPhan\\Downloads\\banhxegau.png')
banh_xe_dai_rect_2 = banh_xe_dai_2.get_rect(center = (277,372))

net_bo_sound = pygame.mixer.Sound('C:\\Users\\DucPhan\\Downloads\\tiếngnetbo (mp3cut.net).mp3')

floor = pygame.image.load('C:\\Users\\DucPhan\\Downloads\\E760357F-DDBF-40DE-B975-3D28514E595B (1).jpg')
# floor = pygame.transform.scale2x(floor)
font = pygame.font.Font('freesansbold.ttf', 32)
text = font.render('DedNine', True, '#303841')
textRect = text.get_rect()
textRect.center = (400,300)
wheel_x = 745
angle = 0
a=0
# net_bo_sound.play()
# bg_index = 0
bg_list = [bg_1]
# times = 0
bg_x_pos = 0
floor_x_pos = 0
while True:
	a+= 1
	# bg_x_pos += 1
	floor_x_pos += 1
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
	if car_x == -150:
		# print('jjj')
		with open("..\\.txt\\dednine.txt") as f:
			content = f.read()
		for line in content.splitlines():
			print(line)
			time.sleep(0.03)
	angle += 1
	wheel_x -= 0.5
	car_x -= 0.5

	DISPLAYSURF.blit(bg_1, (bg_x_pos,0))
	if car_x <= 400 :
		# DISPLAYSURF.blit(text,textRect)
		DISPLAYSURF.blit(ds,(250,20))




	xe_dai_rect = xe_dai.get_rect(center = (car_x,327))

	draw_floor()


	if floor_x_pos >= 0:
		floor_x_pos = -800

	DISPLAYSURF.blit(xe_dai,xe_dai_rect)
	banh_xe_rotated, banh_xe_rotated_rect, banh_xe_rotated_2, banh_xe_rotated_rect_2 = rotate(banh_xe_dai,banh_xe_dai_2, angle, wheel_x)

	DISPLAYSURF.blit(banh_xe_rotated,banh_xe_rotated_rect)
	DISPLAYSURF.blit(banh_xe_rotated_2,banh_xe_rotated_rect_2)
	pygame.display.update()
	fpsClock.tick(FPS)