import pygame, sys, random, text
from tile import Tile
from colors import Color
from charactersC import Zombie

# =============== tiles ao redor do cenario =======================
laterais = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,
			21,40,41,60,61,80,81,100,101,120,121,140,141,160,
			161,180,181,200,201,220,221,240,241,260,261,280,
			281,282,283,284,285,286,287,288,289,290,291,292,293,
			294,295,296,297,298,299,300)
# ==================================================================

# ============== fechar a janela do game pelo "x" ===================
def CloseWindow():
	close = pygame.event.get(pygame.QUIT)
	if close:
		pygame.quit()
		sys.exit()
# ====================================================================

# ===================== gera o proximo nivel =========================
def nextLevel(tela,survivor,LevelAtual):

	tempo = 0
	clock = pygame.time.Clock()

	while tempo < 60:
		clock.tick(30)
		tela.fill([0,0,0])
		text.ExibirTexto(tela,'Day '+str(LevelAtual),100,250,50)
		tempo += 1
		pygame.display.flip()

	Tile.refresh()
	#Tile.RecarregarAleatorios()
# ========================================================================

# ========== tela de fim de jogo ao acabar a energia do player ===========
def GameOver(tela,LevelAtual):
	clock = pygame.time.Clock()

	if LevelAtual > 1:
		texto = ' Days You Starved.'
	else:
		texto = ' Day You Starved.'

	while True:
		CloseWindow()
		clock.tick(30)
		tela.fill([0,0,0])
		text.ExibirTexto(tela,'After ' +str(LevelAtual) + texto,100,250,15)
		pygame.display.flip()
# ==========================================================================

# ============== invalidos ao redor do cenario ==============================
def TilesLaterais(tela):
	for y in range(0, tela.get_height(), 40):
		for x in range(0, tela.get_width(), 40):
			if Tile.total_tiles in laterais:
				Tile(x, y, 'solido')
			else:
				Tile(x, y, 'vazio')
# ===========================================================================

# ================= exibe a quantidade de energia do player ===================
class PlayerHealth():

	healthAmount = 100

	def displayHealth(self,tela):
		text.ExibirTexto(tela,'Food:',320,10,15)
		text.ExibirTexto(tela,str(self.healthAmount),400,10,15, Color.DarkRed)
# ============================================================================

# =================== Tiles onde estao os zumbis ==============================
def zombieTile():

	currentTiles = [] # posicao atual de cada zumbi

	# ================== torna a posicao do zumbi inacessivel ao player ========
	for zombie in Zombie.Lista:
		for tile in Tile.Lista:
			if tile.number == zombie.get_number():
				tile.walkable = False
				currentTiles.append(tile)

	# ================= verifica se o zumbi ainda esta no msm tile ============
	for tile in currentTiles:
		if tile.number not in Zombie.Lista:
			tile.walkable = True     # torna o tile acessivel caso nao haja mais zumbis
# =============================================================================
