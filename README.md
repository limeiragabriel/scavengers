#scavengers
mini-projeto de pygame da disciplina de P1

##implementações

- python 2.7
- pygame

### 29/08/2016 até 07/09/2016

* inicio do projeto
* basico
  * display
  * inicio do game
  * fechar jogo
* Classe Tiles (definindo cada 'célula' correspondente dentro da tela)
* Classes sobrevivente e zumbi
* Movimentação do player de Tile à Tile
* adicionados sprites do cenario e dos personagens
* inimigo basico (ainda sem comportamento, apenas testes de colisão)
* "trilha sonora"
* identificadores nos Tiles para definir sprites de areas "validas e invalidas"
* Todos os cenários já são gerados de maneira aleatória
* Mudança de cenario ao chegar na saida ("Exit")
* exibição de informações na tela (textos como dia atual, vida e de transição)
* Tela de transição entre cenários com contador de "dias" passados no game
* Vida/Fome do player descontada a cada movimento
* adicionado Game Over ao alcançar 0 de energia
* alteração na função draw_tiles para melhorar desenpenho do jogo
* implementação da classe Color para facilitar codificação
* animação de Idle do player e do zumbi adicionadas
