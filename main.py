import pygame, sys, text
from tile import *
from charactersC import *
from interacoes import *
from gameManager import *

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
som = pygame.mixer.Sound('scavengers_music.aif')
audio = False
# ========================================================================

# ======================== dia atual e energia ===========================
LevelAtual = 1
playerHealth = PlayerHealth()
# ========================================================================

# mostrar o primeiro dia /// tirar quando implementar o menu
nextLevel(tela,survivor,LevelAtual)

# ============================== loop principal ===========================
while True:

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

	CloseWindow()

	if GetHit(survivor):
		playerHealth.healthAmount -= 10

	

	MovePlayer(survivor)

	MoveZombie()

	tela.fill((0,0,0))
	
	tela.blit(ground,(0,0))

	Tile.draw_tiles(tela)
	zombieTile()

	# ======================== HUD =========================================
	text.ExibirTexto(tela,'Day '+str(LevelAtual),20,10,15)
	playerHealth.displayHealth(tela)
	# ======================================================================

	survivor.draw(tela)
	zombie1.draw(tela)

	zombie2.draw(tela)

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