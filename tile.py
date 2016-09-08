import pygame, text, os
import random

Tileset_ = ['invalid01.png','invalid02.png','invalid03.png','invalid04.png',
			'invalid05.png','invalid06.png','invalid07.png','invalid08.png',
			'invalid09.png','invalid10.png','invalid11.png',
			'path01.png','path02.png','path03.png','path04.png',
			'path05.png','path06.png','path07.png','path08.png']

procedurais = (43,44,45,47,48,49,51,52,53,55,56,
				63,64,65,67,68,69,71,72,73,75,76,
				83,84,85,87,88,89,91,92,93,95,96,97,
				123,124,125,127,128,129,131,132,133,135,136,137,138,
				143,144,145,147,148,149,151,152,153,155,156,157,158,
				163,164,165,167,168,169,171,172,173,175,176,177,178,
				203,204,205,207,208,209,211,212,213,215,216,217,218,
				225,227,228,229,231,232,233,235,236,237,238,
				245,247,248,249,251,252,253,255,256,257,258)


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
		self.idTilePath = random.randint(11,17)
		self.tipo_ = random.randint(0,1)
		# ...

		Tile.total_tiles += 1

		if Type == 'vazio':
			self.walkable = True
		else:
			self.walkable = False


		pygame.Rect.__init__(self, (x,y), (Tile.largura, Tile.altura))

		Tile.Lista.append(self)

	@staticmethod
	def RecarregarAleatorios():
		for tile in Tile.Lista:

			if tile.number in procedurais:
				if tile.tipo_ == 0:
					tile.Type = 'vazio'
					tile.walkable = True
				else:
					tile.Type = 'solido'
					tile.walkable = False

	@staticmethod
	def refresh():
		for tile in Tile.Lista:
			tile.idTileInv = random.randint(0,10)
			tile.idTilePath = random.randint(11,17)
			tile.tipo_ = random.randint(0,1)

	@staticmethod
	def get_tile(number):
		for tile in Tile.Lista:
			if tile.number == number:
				return tile

	@staticmethod
	def draw_tiles(tela):

		for tile in Tile.Lista:

			if tile.Type != 'vazio':

				caminho = os.path.join("tileset", Tileset_[tile.idTileInv])
				tileInv = pygame.image.load(caminho).convert_alpha()

				tela.blit(tileInv,tile)

			elif tile.number == 39:

				caminho3 = os.path.join("tileset","exit.png")
				exit_ = pygame.image.load(caminho3).convert_alpha()

				tela.blit(exit_,tile)

			elif tile.Type == 'vazio':

				caminho2 = os.path.join("tileset",Tileset_[tile.idTilePath])
				tilePath = pygame.image.load(caminho2).convert_alpha()

				tela.blit(tilePath,tile)

			#text.ExibirTexto(tela,tile.number, tile.x, tile.y)

