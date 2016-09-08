import pygame, sys, text
from tile import Tile
from gameManager import PlayerHealth

# ================= movimentacao do personagem =======================
def MovePlayer(tela, survivor, zombie):
	
	# =============== posicao do zumbi ================================
	zombieTile = zombie.get_number()
	# =================================================================

	# ============ eventos do teclado =================================
	for event in pygame.event.get():

		if event.type == pygame.KEYDOWN:

			# ======================= tecla W ==========================
			if event.key == pygame.K_w:
				proxTile = survivor.get_number() - Tile.V
				# ========== descontar energia pelo movimento =============
				PlayerHealth.healthAmount -= 1
				# ================== mover para cima ========================= 
				if Tile.get_tile(proxTile).walkable and proxTile != zombieTile:
					survivor.y -= survivor.altura
			# ============================================================

			# ======================= tecla S ==========================
			elif event.key == pygame.K_s:
				proxTile = survivor.get_number() + Tile.V
				# ========== descontar energia pelo movimento =============
				PlayerHealth.healthAmount -= 1
				# ================== mover para baixo =========================
				if Tile.get_tile(proxTile).walkable and proxTile != zombieTile:
					survivor.y += survivor.altura
				# ============================================================

			# ======================= tecla A ==========================
			elif event.key == pygame.K_a:
				proxTile = survivor.get_number() - Tile.H
				# ========== descontar energia pelo movimento =============
				PlayerHealth.healthAmount -= 1
				# ================== mover para besquerda ====================
				if Tile.get_tile(proxTile).walkable and proxTile != zombieTile:
					survivor.x -= survivor.largura
				# ============================================================

			# ======================= tecla D ==========================
			elif event.key == pygame.K_d:
				proxTile = survivor.get_number() + Tile.H
				# ========== descontar energia pelo movimento =============
				PlayerHealth.healthAmount -= 1
				# ================== mover para direita ====================
				if Tile.get_tile(proxTile).walkable and proxTile != zombieTile:
					survivor.x += survivor.largura
				# ============================================================
	# ============================================================================
