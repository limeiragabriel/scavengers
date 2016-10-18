#scavengers

página: https://limeiragabriel.github.io/scavengers/
repositório: https://github.com/limeiragabriel/scavengers

## descrição
mini-projeto de pygame da disciplina de P1 - desenvolvimento em python

* A ideia:

Scavengers é um Rogue-Like baseado no game original feito na unity em C# e distribuido na asset store gratuitamente para estudo. Agora "reinventado" em pygame como projeto da disciplina de Programação 1.

* Sobre o gênero do jogo:

Roguelike é um subgênero de jogos RPG, caracterizado pela geração de level aleatória durante a partida, mapa baseado em tile e permanent death. Jogos deste gênero são descendentes do jogo original Rogue, de 1980, particularmente espelhando-se no quesito de gráficos ASCII ou Sprite, gameplay baseado em turnos, e narrativa high fantasy.

mais sobre o gênero: https://pt.wikipedia.org/wiki/Roguelike

* A história:

Vocẽ está na pele de um sobrevivente do apocalipse zumbi em um mundo totalmente devastado e com escassez de recursos, onde o objetivo é sobreviver o máximo de dias possiveis enquanro coleta recursos para isso e escapa dos monstros.


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

### 08/09/2016

* melhora na organização e comentarios no código
* melhora na eficiencia do codigo (chegando a dobrar o desempenho em fps em relação a versões anteriores)
* sistema de dano ao se aproximar do inimigo
* melhora na identificação da posição dos zumbis para colisao

### 09/09/2016

* Movimentação dos zumbis pelo cenario
* tiles com passagem bloqueada para o player quando o zumbi estiver
* movimentação baseada em turnos implementada
* coreeção dos seguintes bugs:
  * tiles onde os zumbis passaram permanecem invalidos mesmo vazios
  * depois de levar o primeiro hit do zumbi o player não gasta mais energia ao andar pelo cenario
  * zumbis atravessam player e vice-versa
  * zumbis se atravessam
  
### 18/10/2016

* versão final (1.0)
