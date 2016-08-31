import pygame
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

class Zombie(Character):

	Lista = []

	def __init__(self, x, y):
		Character.__init__(self,x,y)
		Zombie.Lista.append(self)

	def draw(self,tela):
		for zombie in Zombie.Lista:
			zombie = pygame.image.load("zombie1.png").convert_alpha()
			tela.blit(zombie,(self.x, self.y))

class Survivor(Character):

	def __init__(self,x,y):
		Character.__init__(self, x, y)

	def draw(self,tela):
		character = pygame.image.load("survivor.png").convert_alpha()
		tela.blit(character,(self.x, self.y))