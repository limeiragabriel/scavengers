import pygame, sys
from tile import Tile


def MovePlayer(tela, survivor, zombie):
	# ... fechar a janela
	for event in pygame.event.get():

		if event.type == pygame.KEYDOWN:
			
			zombieTile = zombie.get_number()

			if event.key == pygame.K_w:
				proxTile = survivor.get_number() - Tile.V
			
				if Tile.get_tile(proxTile).walkable and proxTile != zombieTile:
					survivor.y -= survivor.altura

			elif event.key == pygame.K_s:
				proxTile = survivor.get_number() + Tile.V

				if Tile.get_tile(proxTile).walkable and proxTile != zombieTile:
					survivor.y += survivor.altura
			
			elif event.key == pygame.K_a:
				proxTile = survivor.get_number() - Tile.H

				if Tile.get_tile(proxTile).walkable and proxTile != zombieTile:
					survivor.x -= survivor.largura

			elif event.key == pygame.K_d:
				proxTile = survivor.get_number() + Tile.H

				if Tile.get_tile(proxTile).walkable and proxTile != zombieTile:
					survivor.x += survivor.largura