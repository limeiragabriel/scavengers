import pygame, text, os
import random

invalidTile = ['invalid01.png','invalid02.png','invalid03.png','invalid04.png',
				'invalid05.png','invalid06.png','invalid07.png','invalid08.png',
				'invalid09.png','invalid10.png','invalid11.png']

tileId = random.randint(0,10)


class Tile(pygame.Rect):

	Lista = []
	largura, altura = 40, 40
	total_tiles = 1
	H,V = 1, 20

	def __init__(self, x, y, Type):

		self.Type = Type
		self.number = Tile.total_tiles
		# ...
		self.idTile = random.randint(0,10)
		# ...
		Tile.total_tiles += 1

		if Type == 'vazio':
			self.walkable = True
		else:
			self.walkable = False


		pygame.Rect.__init__(self, (x,y), (Tile.largura, Tile.altura))

		Tile.Lista.append(self)

	@staticmethod
	def get_tile(number):
		for tile in Tile.Lista:
			if tile.number == number:
				return tile

	@staticmethod
	def draw_tiles(tela):

		for tile in Tile.Lista:

			caminho = os.path.join("tileset", invalidTile[tile.idTile])
			tileInv = pygame.image.load(caminho).convert_alpha()

			if tile.Type != 'vazio':
				tela.blit(tileInv,tile)

			text.ExibirTexto(tela,tile.number, tile.x, tile.y)

