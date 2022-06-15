import pygame
import sys
import random
import time
from pygame.locals import *

def draw_floor():
	screen.blit(floor,(floor_x_pos,650))
	screen.blit(floor,(floor_x_pos+432,650))


def create_pipe():
	random_pipe_pos = random.choice(pipe_height)
	bottom_pipe = pipe_surface.get_rect(midtop =(750,random_pipe_pos))
	top_pipe = pipe_surface.get_rect(midtop =(750,random_pipe_pos-800))
	return bottom_pipe, top_pipe


def move_pipe(pipes):
	for pipe in pipes :
		pipe.centerx -= 3
	return pipes


def draw_pipe(pipes):
	for pipe in pipes:
		if pipe.bottom >= 600 : 
			screen.blit(pipe_surface,pipe)
		else:
			flip_pipe = pygame.transform.flip(pipe_surface,False,True)
			screen.blit(flip_pipe,pipe)


def check_collision(pipes):
	for pipe in pipes:
		if bird_rect.colliderect(pipe) or bird_rect.colliderect(knife_2_rect):
			hit_sound.play()
			return False
	if bird_rect.top <= -75 or bird_rect.bottom >= 650:
			return False
	return True 


def rotate_bird(bird1):
	new_bird = pygame.transform.rotozoom(bird1,-bird_movement*3,1)
	return new_bird


def bird_animation():
	new_bird = bird_list[bird_index]
	new_bird_rect = new_bird.get_rect(center = (100,bird_rect.centery))
	return new_bird, new_bird_rect


def score_display(game_state):
	if game_state == 'main game':
		score_surface = game_font.render(str(int(score)),True,(random.randint(0,255),random.randint(0,255),random.randint(0,255)))
		score_rect = score_surface.get_rect(center = (600,100))
		screen.blit(score_surface,score_rect)
	if game_state == 'game_over':
		score_surface = game_font.render(f'Score: {int(score)}',True,(color1,color2,color3))
		score_rect = score_surface.get_rect(center = (216,100))
		screen.blit(score_surface,score_rect)

		high_score_surface = game_font.render(f'High Score: {int(high_score)}',True,(255,255,255))
		high_score_rect = high_score_surface.get_rect(center = (216,630))
		screen.blit(high_score_surface,high_score_rect)


def update_score(score,high_score):
	if score > high_score:
		high_score = score
	return high_score

def move_acquy():
	acquy_rect.centerx -= 0
	screen.blit(acquy_1, (acquy_rect.centerx,20))

def move_knife():
	knife_2_rect.centerx -= 3
	knife_2_rect.centery += 1
	screen.blit(knife_2, (knife_2_rect.centerx,knife_2_rect.centery))


color1 = random.randint(0,120)
color2 = random.randint(0,255)
color3 = random.randint(0,255)

pygame.mixer.pre_init(frequency=44100, size=-16, channels=2, buffer=512)
pygame.init()
screen= pygame.display.set_mode((732,412))
clock = pygame.time.Clock()
game_font = pygame.font.Font('04B_19.ttf',35)


gravity = 0.18
bird_movement = 0
game_active = True
score = 0
high_score = 0


acquy_1 = pygame.image.load('../assets/acquy_2a.png').convert_alpha()
acquy_2 = pygame.image.load('../assets/acquy_2a.png').convert_alpha()
acquy_3 = pygame.image.load('../assets/acquy_2a.png').convert_alpha()
ácquy = pygame.image.load('../assets/ácquy.png').convert_alpha()
knife_2 = pygame.image.load('../assets/knife_2.png').convert_alpha()
acquy_rect = acquy_1.get_rect(center = (600,80))
knife_2_rect = acquy_1.get_rect(center = (590,80))
acquy_surface = pygame.Surface((600,80))


backgr_files = "quangduongtouchinggod.jpg"
# bg = pygame.image.load(f'../assets/{backgr_files}').convert()
# bg = pygame.transform.scale2x(bg)
backgr_files = "colen_gau_2.jpg"
bg_2 = pygame.image.load(f'../assets/{backgr_files}').convert()
# bg_2 = pygame.transform.scale2x(bg_2)
backgr_files = "another_acquy_2.jpg"
bg_3 = pygame.image.load(f'../assets/{backgr_files}').convert()
bg_3 = pygame.transform.scale2x(bg_3)
backgr_files = "colen_dai.png"
bg_4 = pygame.image.load(f'../assets/{backgr_files}').convert()
bg_4 = pygame.transform.scale2x(bg_4)
# backgr_files = "backgr_acquy.jpg"
# bg_5 = pygame.image.load(f'../assets/{backgr_files}').convert()
# bg_5 = pygame.transform.scale2x(bg_5)
bg_list = []
bg_list.append(bg_4)
bg_list.append(bg_4)
bg_list.append(bg_2)
bg_list.append(bg_3)
bg_list.append(bg_3)


floor = pygame.image.load('../assets/floor.png').convert()
floor = pygame.transform.scale2x(floor)
floor_x_pos = 0


bird_down = pygame.transform.scale2x(pygame.image.load('../assets/downflap.png').convert_alpha())
bird_mid = pygame.transform.scale2x(pygame.image.load('../assets/midflap.png').convert_alpha())
bird_up = pygame.transform.scale2x(pygame.image.load('../assets/upflap.png').convert_alpha())
bird_list= [bird_down,bird_mid,bird_up] #0 1 2
bird_index = 0
bird = bird_list[bird_index]

bird_rect = bird.get_rect(center = (100,384))

birdflap = pygame.USEREVENT + 1
pygame.time.set_timer(birdflap,200)


pipe_surface = pygame.image.load('../assets/pipe-green.png').convert()
pipe_surface = pygame.transform.scale2x(pipe_surface)
pipe_list =[]



spawnpipe= pygame.USEREVENT
pygame.time.set_timer(spawnpipe, 1200)
pipe_height = [200,300,350,400]

game_over_surface = pygame.transform.scale2x(pygame.image.load('../assets/banlanhat.png').convert_alpha())
game_over_rect = game_over_surface.get_rect(center=(500,200))


flap_sound = pygame.mixer.Sound('../sound/ớ (mp3cut.net).wav')
hit_sound = pygame.mixer.Sound('../sound/banlanhat.wav')
# score_sound = pygame.mixer.Sound('sound/sfx_point.wav')


second = 0
dem_bg = 0
bg_index = 0
key_space = 0

while True:
	dem_bg += 1

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_SPACE and game_active:
				bird_movement = 0
				bird_movement =-7
				key_space += 1
				flap_sound.play()
			if event.key == pygame.K_SPACE and game_active==False:
				game_active = True 
				pipe_list.clear()
				bird_rect.center = (100,384)
				bird_movement = 0 
				score = 0

		if event.type == spawnpipe:
			pipe_list.extend(create_pipe())

		if event.type == birdflap:
			if bird_index < 2:
				bird_index += 1
			else:
				bird_index =0 
			bird, bird_rect = bird_animation()    


	if score > 15 and score < 30:
		bg_index = 1

	elif score > 30 and score < 35:
		bg_index = 2

	elif score > 35 and score < 45:
		bg_index = 3

	elif score > 45:
		bg_index = 4

	bg = bg_list[bg_index]

	screen.blit(bg,(0,0))
	
	# if key_space >= 5 and key_space <= 15:



	# if key_space >= 10 and key_space <= 15:
	# 	move_acquy()
	# 	move_knife()



	if game_active:
		bird_movement += gravity
		rotated_bird = rotate_bird(bird)       
		bird_rect.centery += bird_movement
		screen.blit(rotated_bird,bird_rect)
		game_active= check_collision(pipe_list)
		pipe_list = move_pipe(pipe_list)
		draw_pipe(pipe_list)
		score += 0.007
		score_display('main game')

	else:
		screen.blit(game_over_surface,game_over_rect)
		high_score = update_score(score,high_score)
		score_display('game_over')
		screen.blit(ácquy, (100,150))
		key_space = 0 
		bg_index = 0

	floor_x_pos -= 0.05
	draw_floor()
	if floor_x_pos <= -432:
		floor_x_pos =0
	
	pygame.display.update()
	clock.tick(120)
