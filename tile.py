import pygame, text, os,sys
import random

laterais = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,
			21,40,41,60,61,80,81,100,101,120,121,140,141,160,
			161,180,181,200,201,220,221,240,241,260,261,280,
			281,282,283,284,285,286,287,288,289,290,291,292,293,
			294,295,296,297,298,299,300)

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

def cancelDrawAndQuit():
	close = pygame.event.get(pygame.QUIT)
	if close:
		pygame.quit()
		sys.exit()

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
		#self.idTilePath = random.randint(11,17)
		self.tipo_ = random.randint(0,1)
		# ...
		self.isItemSpawn = False
		self.itemType = 0

		Tile.total_tiles += 1

		if Type == 'vazio':
			self.walkable = True   # tiles onde se pode andar
		else:
			self.walkable = False  # tiles onde NAO	se pode andar


		pygame.Rect.__init__(self, (x,y), (Tile.largura, Tile.altura))

		Tile.Lista.append(self)

	# ======= "recarrega" os tiles para gerar um novo cenario aleatorio ==========
	@staticmethod
	def refresh():
		for tile in Tile.Lista:
			tile.idTileInv = random.randint(0,10)
			#tile.idTilePath = random.randint(11,17)
			tile.tipo_ = random.randint(0,1)

			if tile.number in procedurais:
				if tile.tipo_ == 0:
					tile.Type = 'vazio'
					tile.walkable = True
				else:
					tile.Type = 'solido'
					tile.walkable = False
	# ============================================================================

	# ===== retorna o numero do tile de acordo com sua posicao na tela ===========
	@staticmethod
	def get_tile(number):
		for tile in Tile.Lista:
			if tile.number == number:
				return tile
	# ============================================================================

	# ====================== desenha os tiles do cenario =========================
	@staticmethod
	def draw_tiles(tela):

		for tile in Tile.Lista:

			cancelDrawAndQuit()

			if tile.Type != 'vazio' and tile.number not in laterais:

				caminho = os.path.join("tileset", Tileset_[tile.idTileInv])
				tileInv = pygame.image.load(caminho).convert_alpha()

				tela.blit(tileInv,tile)
				tile.walkable = False
