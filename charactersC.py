import pygame, os
from tile import Tile

class Character(pygame.Rect):

	largura, altura = 40,40

	# ... construtor de objetos ...
	def __init__(self,x,y):
		pygame.Rect.__init__(self, x, y, Character.largura, Character.altura)

	def __str__(self):
		return str(self.get_number())


	def get_number(self):
		return ((self.x / self.largura)+ Tile.H) + ((self.y / self.altura)* Tile.V)

	def get_tile(self):
		return Tile.get_tile(self.get_number)

## "controles" para quadros da animacao dos sprites
a = 0
b = 0
largura = 40
altura = 40
frame = 0.0
##=========================

class Zombie(Character):

	Lista = []

	def __init__(self, x, y):
		Character.__init__(self,x,y)
		Zombie.Lista.append(self)

	def draw(self,tela):

		global a,b,largura,altura,frame

		caminho = os.path.join('tileset','zombie_idle.png')

		if frame >= 1.0:
			a += 40
			frame = 0.0

		frame += 0.1

		if a >= (40 * 6):
			a = 0

		for zombie in Zombie.Lista:
			zombie = pygame.image.load(caminho).convert_alpha()
			tela.blit(zombie,(self.x, self.y),(a,b,largura,altura))

class Survivor(Character):

	def __init__(self,x,y):
		Character.__init__(self, x, y)

	def draw(self,tela):
		global a,b,largura,altura,frame

		if frame >= 1.0:
			a += 40
			frame = 0.0

		frame += 0.1

		if a >= (40 * 6):
			a = 0

		caminho = os.path.join('tileset','player_idle.png')
		character = pygame.image.load(caminho).convert_alpha()

		tela.blit(character,(self.x, self.y),(a,b,largura,altura))