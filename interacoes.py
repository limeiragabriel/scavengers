import pygame, sys
from tile import Tile


def Interacoes(tela, survivor):
	canmove = True
	# ... fechar a janela
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
	# ... .... .... .... ...

		if event.type == pygame.KEYDOWN and canmove:
			
			if event.key == pygame.K_w:
				proxTile = survivor.get_number() - Tile.V

				if Tile.get_tile(proxTile).walkable:
					survivor.y -= survivor.altura

			if event.key == pygame.K_s:
				proxTile = survivor.get_number() + Tile.V

				if Tile.get_tile(proxTile).walkable:
					survivor.y += survivor.altura
			
			if event.key == pygame.K_a:
				proxTile = survivor.get_number() - Tile.H

				if Tile.get_tile(proxTile).walkable:
					survivor.x -= survivor.largura

			if event.key == pygame.K_d:
				proxTile = survivor.get_number() + Tile.H

				if Tile.get_tile(proxTile).walkable:
					survivor.x += survivor.largura