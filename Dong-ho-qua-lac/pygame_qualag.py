import pygame,sys
from pygame.locals import *

#khai báo lặt vặt
WINDOWWIDTH = 800
WINDOWHEIGHT = 500 

WHITE = (255, 255, 255)
RED   = (255,   0,   0)
GREEN = (  0, 255,   0)
ORANGE = '#F9AE57'
ORANGE_2 = '#D99700'
GREY   = '#4F565E'
color1 = '#2B2B2B'	#xám
color2 = '#C695C6'	#hồng
color3 = '#AC4042'	#đỏ đô
color4 = '#832E0F'	#đỏ nâu
pygame.init()

FPS = 100
fpsClock = pygame.time.Clock()

DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
pygame.display.set_caption('D E D N I N E')
icon = pygame.image.load('C:\\Users\\DucPhan\\Downloads\\logo_2.png')			#kim giây
pygame.display.set_icon(icon)

x_clock = 250
x_digital_logo = 550
y_digital = 180

def rotate(surface_1,surface_2, angel):
	rotated_surface_1 = pygame.transform.rotozoom(surface_1,angel,1)			#kim giây
	rotated_rect_1    = rotated_surface_1.get_rect(center = (x_clock,138))

	rotated_surface_2 = pygame.transform.rotozoom(surface_2,angel/60,1)			#kim phút
	rotated_rect_2    = rotated_surface_2.get_rect(center = (x_clock,139.5))

	# rotated_surface_3 = pygame.transform.rotozoom(surface_3,angel/3600,1)		#kim giờ
	# rotated_rect_3 = rotated_surface_3.get_rect(center = (x_clock,201.5))

	return rotated_surface_1, rotated_rect_1, rotated_surface_2, rotated_rect_2

def qua_lag(surface_4, angel):
	rotated_surface_4 = pygame.transform.rotozoom(surface_4,angel,1)		#quả lag
	rotated_rect_4 = rotated_surface_4.get_rect(center = (x_clock,230))
	return rotated_surface_4,rotated_rect_4 

kim_giay  = pygame.image.load('C:\\Users\\DucPhan\\Downloads\\kím (1)_cp.png'				).convert_alpha()		#kim giây
kim_phut  = pygame.image.load('C:\\Users\\DucPhan\\Downloads\\kim.png'       				).convert_alpha()		#kim phút
qualag 	  = pygame.image.load('C:\\Users\\DucPhan\\Downloads\\lag_4_cp.png'	 				).convert_alpha()		#quả lag
clock     = pygame.image.load('C:\\Users\\DucPhan\\Downloads\\clock_face_cp.png'			).convert_alpha()		#mặt che quả lag
clock_all = pygame.image.load('C:\\Users\\DucPhan\\Downloads\\clock3_cp.png'				).convert_alpha()		#cả đồng hồ
digital   = pygame.image.load('C:\\Users\\DucPhan\\Downloads\\digital_clock_1.png'			).convert_alpha()		#khung điện tử
logo      = pygame.image.load('C:\\Users\\DucPhan\\Downloads\\dednine1 (1)_rotated2_cp.png' ).convert_alpha()		#logo

clock_rect 	   = clock.get_rect(center = (x_clock,300))
clock_all_rect = clock_all.get_rect(center = (x_clock,300))
digital_rect   = digital.get_rect(center = (x_digital_logo,y_digital))
logo_rect      = logo.get_rect(center = (x_digital_logo,330))
bg_1           = pygame.image.load('C:\\Users\\DucPhan\\Downloads\\bg_lag1_cp.jpg')	#background

def show_time(time):
	gio  = str(int(time)//3600)
	h1   = int(time)%3600
	phut = str(h1//60)
	giay = str(h1%60)
	font = pygame.font.SysFont('DS-Digital', 80)
	text = font.render(f"{phut.zfill(2)}:{giay.zfill(2)}", True, color4)
	textRect = text.get_rect(center = (x_digital_logo,y_digital))
	return text, textRect, giay, phut,gio

angel = 0
angel_lag = 0
time = 0
angel_max = 18
run = True
a = True

while run:
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()

	if a:
		angel_lag += 0.5
	else: 
		angel_lag -= 0.5

	if angel_lag == angel_max or angel_lag == -angel_max:
		a = not a

	
	DISPLAYSURF.blit(bg_1, (0,0))		# blit background

	time  += 0.01
	angel -= 0.06

	text_surface, text_rect , giay, phut, gio = show_time(time)

	kimgiay_rotated , kimgiay_rotated_rect, kimphut_rotated , kimphut_rotated_rect= rotate(kim_giay,kim_phut, angel)
	lag_surface, lag_rect = qua_lag(qualag, angel_lag)

	DISPLAYSURF.blit(clock_all,clock_all_rect)				#cả thân đồng hồ
	DISPLAYSURF.blit(lag_surface,lag_rect)					#vẽ mặt che quả lag
	DISPLAYSURF.blit(clock,clock_rect)						#mặt đồng hồ
	DISPLAYSURF.blit(digital,digital_rect)					#vẽ khung điện tử
	DISPLAYSURF.blit(logo,logo_rect)						#vẽ logo
	DISPLAYSURF.blit(text_surface,text_rect)				#vẽ thời gian
	DISPLAYSURF.blit(kimgiay_rotated,kimgiay_rotated_rect)	#vẽ kim giây
	DISPLAYSURF.blit(kimphut_rotated,kimphut_rotated_rect)	#vẽ kim phút



	pygame.display.update()
	fpsClock.tick(FPS)












