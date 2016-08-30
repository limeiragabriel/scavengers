import pygame, text

class Tile(pygame.Rect):

	Lista = []
	largura, altura = 40, 40
	total_tiles = 1
	H,V = 1, 18

	def __init__(self, x, y, Type):

		self.type = Type
		self.number = Tile.total_tiles
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

			if tile.type != 'vazio':
				pygame.draw.rect(tela, [40,40,40], tile)

			text.ExibirTexto(tela,tile.number, tile.x, tile.y)