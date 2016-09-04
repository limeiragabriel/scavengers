import pygame, text, os
import random

invalidTile = ['invalid01.png','invalid02.png','invalid03.png','invalid04.png',
				'invalid05.png','invalid06.png','invalid07.png','invalid08.png',
				'invalid09.png','invalid10.png','invalid11.png']

pathTile = ['path01.png','path02.png','path03.png','path04.png',
			'path05.png','path06.png','path07.png','path08.png']


class Tile(pygame.Rect):

	Lista = []
	largura, altura = 40, 40
	total_tiles = 1
	H,V = 1, 20

	def __init__(self, x, y, Type):

		self.Type = Type
		self.number = Tile.total_tiles
		
		# Atribuindo um identificador aleatorio para definir o sprite de cada tile...
		self.idTileInv = random.randint(0,10)
		self.idTilePath = random.randint(0,7)
		# ...

		Tile.total_tiles += 1

		if Type == 'vazio':
			self.walkable = True
		else:
			self.walkable = False


		pygame.Rect.__init__(self, (x,y), (Tile.largura, Tile.altura))

		Tile.Lista.append(self)

	@staticmethod
	def refresh():
		for tile in Tile.Lista:
			tile.idTileInv = random.randint(0,10)
			tile.idTilePath = random.randint(0,7)

	@staticmethod
	def get_tile(number):
		for tile in Tile.Lista:
			if tile.number == number:
				return tile

	@staticmethod
	def draw_tiles(tela):

		for tile in Tile.Lista:

			caminho = os.path.join("tileset", invalidTile[tile.idTileInv])
			tileInv = pygame.image.load(caminho).convert_alpha()

			caminho2 = os.path.join("tileset",pathTile[tile.idTilePath])
			tilePath = pygame.image.load(caminho2).convert_alpha()

			caminho3 = os.path.join("tileset","exit.png")
			exit_ = pygame.image.load(caminho3).convert_alpha()

			if tile.Type != 'vazio':
				tela.blit(tileInv,tile)

			elif tile.number == 39:
				tela.blit(exit_,tile)

			elif tile.Type == 'vazio':
				tela.blit(tilePath,tile)

			#text.ExibirTexto(tela,tile.number, tile.x, tile.y)

