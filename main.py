import pygame
import time
import random

snake_speed = 15

window_x = 720
window_y = 480

black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)

pygame.init()

pygame.display.set_caption('Snake igrica')
game_window = pygame.display.set_mode((window_x, window_y))

fps = pygame.time.Clock()

snake_position = [100, 50]

#definisanje prva 4 bloka tela zmijice
snake_body = [[100,50],
			  [90,50],
			  [80,50],
			  [70,50]
			]

voce_position = [random.randrange(1, (window_x//10)) * 10,
				 random.randrange(1, (window_y//10)) * 10]

voce_spawn = True

#pocetna putanja zmije
direction = 'RIGHT'
promeni = direction


rezultat = 0

#funkcija rezultata
def pokazi_rezultat(choice, color, font, size):
	#font rezultata
	rezultat_font = pygame.font.SysFont(font, size)

	#prikazi rezultat
	rezultat_surface = rezultat_font.render('Rezultat je: ' + str(rezultat), True, color)

	#objekat za tekst
	rezultat_rect = rezultat_surface.get_rect()

	#prikaz teksta
	game_window.blit(rezultat_surface, rezultat_rect)


#funkcija gameover
def game_over():

	font = pygame.font.SysFont('times new roman', 50)

	#podloga za tekst
	game_over_surface = font.render('Tvoj rezultat je: ' + str(rezultat), True, red)

	game_over_rect = game_over_surface.get_rect()

	#pozicija za tekst
	game_over_rect.midtop = (window_x/2, window_y/4)

	#blit za preslikavanje
	game_window.blit(game_over_surface, game_over_rect)
	pygame.display.flip()

	#ugasi igricu
	time.sleep(2)

	pygame.quit()
	quit()


while True:
	for event in pygame.event.get():
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_UP:
				promeni = 'UP'
			if event.key == pygame.K_DOWN:
				promeni = 'DOWN'
			if event.key == pygame.K_RIGHT:
				promeni = 'RIGHT'
			if event.key == pygame.K_LEFT:
				promeni = 'LEFT'

	#ukolio su kliknuta dva dugmeta odjedared
	if promeni == 'UP' and promeni != 'DOWN':
		promeni = 'UP'
	if promeni == 'DOWN' and promeni != 'UP':
		promeni = 'DOWN'
	if promeni == 'LEFT' and promeni != 'RIGHT':
		promeni = 'LEFT'
	if promeni == 'RIGHT' and promeni != 'LEFT':
		promeni = 'RIGHT'

	#pomeranje zmijice
	if promeni == 'UP':
		snake_position[1] -= 10
	if promeni == 'DOWN':
		snake_position[1] += 10
	if promeni == 'LEFT':
		snake_position[0] -= 10
	if promeni == 'RIGHT':
		snake_position[0] += 10

	#rast zmijice prilikom prikupljanja vockica
	#sudar zmijice
	snake_body.insert(0, list(snake_position))
	if snake_position[0] == voce_position[0] and snake_position[1] == voce_position[1]:
		rezultat += 20
		voce_spawn = False
	else:
		snake_body.pop()

	if not voce_spawn:
		voce_position = [random.randrange(1, (window_x//10)) * 10, 
                         random.randrange(1, (window_y//10)) * 10]
	voce_spawn = True
	game_window.fill(black)
	
	for pos in snake_body:
		pygame.draw.rect(game_window, green, pygame.Rect(pos[0], pos[1], 10, 10))
		pygame.draw.rect(game_window, white, pygame.Rect(voce_position[0], voce_position[1], 10, 10))

    #gameover uslovi
	if snake_position[0] < 0 or snake_position[0] > window_x-10:
		game_over()
	if snake_position[1] < 0 or snake_position[1] > window_y-10:
		game_over()


   	# ????? 
	for block in snake_body[1:]:
		if snake_position[0] == block[0] and snake_position[1] == block[1]:
			game_over()

   	#prikaz konstantnog rezultata
	pokazi_rezultat(1, white, 'times new roman', 20)

   	# osvezi ekran
	pygame.display.update()

   	#fps
	fps.tick(snake_speed)

