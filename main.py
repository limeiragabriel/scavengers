import pygame, sys, text,os
from tile import *
from charactersC import *
from interacoes import *
from gameManager import *
from menu import Menu

pygame.init()
pygame.mixer.init()


# ====================== Resolucao ======================================
LARGURA,ALTURA = 800, 600
tela = pygame.display.set_mode((LARGURA,ALTURA))
# =======================================================================

# ==================== taxa de atualizacao ===============================
clock = pygame.time.Clock()
FPS = 30
total_frames = 0
# ========================================================================

# ================ tiles invalidos pelo cenario ==========================
TilesLaterais(tela)
#Tile.RecarregarAleatorios()
# ========================================================================

# ========= tiles do Back ground =========================================
caminho = os.path.join("tileset", "DirtGround.png")
ground = pygame.image.load(caminho).convert_alpha()
# ========================================================================

# =================== personagens ========================================
zombie1 = Zombie(Tile.get_tile(126).x,Tile.get_tile(126).y)

zombie2 = Zombie(Tile.get_tile(146).x,Tile.get_tile(146).y)

survivor = Survivor(40,520)
# ========================================================================

# ======================= musica de fundo ================================
trilha = os.path.join('sounds','scavengers_music.aif')
som = pygame.mixer.Sound(trilha)
som.set_volume(1)
audio = False
# ========================================================================

# ======================== dia atual e energia ===========================
LevelAtual = 1
playerHealth = PlayerHealth()
tonalidade = Color.LimeGreen
# ========================================================================

Manager = Gerenciador() #classe do gamemanager

listaDeTiles = [] # armazenar posicoes dos zumbis

# ============================== loop principal ===========================
while True:

	# ================ fechar janela
	CloseWindow()
	# ==============================

	# ========================== menu principal ==============================
	while Manager.onMenu:
		Menu(tela)
	# ========================================================================

	#============= mostrar o primeiro dia ao sair do menu ================
	if Manager.primeiroDia:
		Intro(tela)
		nextLevel(tela,survivor,LevelAtual)
		Manager.primeiroDia = False #torna falso para nao exibir dia 1 mais de uma vez
	# ======================================================================

	# ======================= Game Over ===================================
	if playerHealth.healthAmount <= 0:
		som.stop()
		GameOver(tela,LevelAtual)
	# =====================================================================

	# ========== checa se o player alcancou o fim da fase =================
	if survivor.get_number() == 39:
		LevelAtual += 1
		nextLevel(tela,survivor,LevelAtual)
		survivor = Survivor(40,520)
	# =====================================================================

	# ================ torna nao andavel lugar onde tem zumbi ================
	PosicaoDeZumbi(listaDeTiles)
	# ======================================================================

	#tela.fill((0,0,0))

	tela.blit(ground,(0,0)) # fundo (terreno)

	Tile.draw_tiles(tela)   # desenha os tiles do cenario

	# ================== sistema de trurnos ==================================
	if Manager.playerTurn:
		MovePlayer(survivor)
	else:
		#GetHit(survivor,tela)
		MoveZombie(survivor)
		GetHit(survivor,tela)
	# =========================================================================

	# =============== zera as posicoes para atualiza-las =====================
	AttPosicaoDeZumbi(listaDeTiles)
	listaDeTiles = []
	# =========================================================================

	# ======================== HUD =========================================
	if playerHealth.healthAmount >= 75:
		tonalidade = Color.LimeGreen
	elif playerHealth.healthAmount >= 50:
		tonalidade = Color.DarkOrange
	else:
		tonalidade = Color.Red

	text.ExibirTexto(tela,'Day '+str(LevelAtual),20,10,15)
	playerHealth.displayHealth(tela,tonalidade)
	# ======================================================================

	survivor.draw(tela) # desenha o sobrevivente

	# zumbis =========================
	zombie1.draw(tela)

	zombie2.draw(tela)
	# ===================
	# ================================

	# ====================== inicia a musica de fundo ======================
	if audio == False:
		som.play(-1)
		audio = True
	# ======================================================================

	# fps counter ===============
	pygame.display.set_caption('FPS %.2f' %(clock.get_fps()) )
	# ===========================

	pygame.display.flip() #update screen
	clock.tick(FPS)
	total_frames += 1
