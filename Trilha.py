import pygame
import random

# Inicialização do Pygame
pygame.init()

# Definição das cores
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
AZUL = (0, 0, 255)
VERMELHO =(255,0,0)
AMARELO =(255,255,0)

# Dimensões da tela
largura_tela = 900            
altura_tela = 900

# Criando a tela
tela = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption("Trilha")

# Variáveis do jogo
tabuleiro = [[' ']*8 for _ in range(7)]

jogador_atual = 'X'
posicoes = [
    # Posições do cubo interno
    (largura_tela // 2 - 100, altura_tela // 2 - 100),
    (largura_tela // 2, altura_tela // 2 - 100),
    (largura_tela // 2 + 100, altura_tela // 2 - 100),
    (largura_tela // 2 - 100, altura_tela // 2),
    (largura_tela // 2 + 100, altura_tela // 2),
    (largura_tela // 2 - 100, altura_tela // 2 + 100),
    (largura_tela // 2, altura_tela // 2 + 100),
    (largura_tela // 2 + 100, altura_tela // 2 + 100),

    # Posições do cubo do meio
    (largura_tela // 2 - 200, altura_tela // 2 - 200),
    (largura_tela // 2, altura_tela // 2 - 200),
    (largura_tela // 2 + 200, altura_tela // 2 - 200),
    (largura_tela // 2 - 200, altura_tela // 2),
    (largura_tela // 2 + 200, altura_tela // 2),
    (largura_tela // 2 - 200, altura_tela // 2 + 200),
    (largura_tela // 2, altura_tela // 2 + 200),
    (largura_tela // 2 + 200, altura_tela // 2 + 200),

    # Posições do cubo externo
    (largura_tela // 2 - 300, altura_tela // 2 - 300),
    (largura_tela // 2, altura_tela // 2 - 300),
    (largura_tela // 2 + 300, altura_tela // 2 - 300),
    (largura_tela // 2 - 300, altura_tela // 2),
    (largura_tela // 2 + 300, altura_tela // 2),
    (largura_tela // 2 - 300, altura_tela // 2 + 300),
    (largura_tela // 2, altura_tela // 2 + 300),
    (largura_tela // 2 + 300, altura_tela // 2 + 300)
]


fase_colocacao = True
pecas_brancas = 9
pecas_pretas = 9
fase_movimento = False
pecas_selecionadas = []

def desenhar_linhas_cubos():
    # Cubo vermelho (Menor)
    pygame.draw.lines(tela, VERMELHO, True, [posicoes[0], posicoes[1], posicoes[2]], 2) 
    pygame.draw.lines(tela, VERMELHO, True, [posicoes[2], posicoes[4], posicoes[7]], 2)
    pygame.draw.lines(tela, VERMELHO, True, [posicoes[0], posicoes[3], posicoes[5]], 2)
    pygame.draw.lines(tela, VERMELHO, True, [posicoes[5], posicoes[6], posicoes[7]], 2)

    # Cubo azul (Do meio)
    pygame.draw.lines(tela, AZUL, True, [posicoes[8], posicoes[9], posicoes[10]], 2) 
    pygame.draw.lines(tela, AZUL, True, [posicoes[8], posicoes[11], posicoes[13]], 2)
    pygame.draw.lines(tela, AZUL, True, [posicoes[10], posicoes[12], posicoes[15]], 2)
    pygame.draw.lines(tela, AZUL, True, [posicoes[13], posicoes[14], posicoes[15]], 2)


    # Cubo Vermelho (Maior)
    pygame.draw.lines(tela, BRANCO, True, [posicoes[16], posicoes[17], posicoes[18]], 2) 
    pygame.draw.lines(tela, BRANCO, True, [posicoes[16], posicoes[19], posicoes[21]], 2)
    pygame.draw.lines(tela, BRANCO, True, [posicoes[18], posicoes[20], posicoes[23]], 2)
    pygame.draw.lines(tela, BRANCO, True, [posicoes[23], posicoes[22], posicoes[21]], 2)

    # Linhas de Ligamento (Em amarelo)
    pygame.draw.lines(tela, AMARELO, True, [posicoes[19], posicoes[11], posicoes[3]], 2)
    pygame.draw.lines(tela, AMARELO, True, [posicoes[1], posicoes[9], posicoes[17]], 2)
    pygame.draw.lines(tela, AMARELO, True, [posicoes[4], posicoes[12], posicoes[20]], 2)
    pygame.draw.lines(tela, AMARELO, True, [posicoes[6], posicoes[14], posicoes[22]], 2)


# Função para exibir o tabuleiro
def exibir_tabuleiro():
    tela.fill(PRETO)
    desenhar_linhas_cubos()  # Chama a função para desenhar as linhas dos cubos

    for i in range(24):
        pygame.draw.circle(tela, BRANCO, posicoes[i], 20)
        fonte = pygame.font.Font(None, 50)
        linha = i // 8
        coluna = i % 8
        texto = fonte.render(tabuleiro[linha][coluna], True, PRETO)
        tela.blit(texto, (posicoes[i][0] - 15, posicoes[i][1] - 15))


# Função para verificar se a posição é válida
def posicao_valida(linha, coluna):
    if linha < 0 or linha > 6 or coluna < 0 or coluna > 7:
        return False
    if tabuleiro[linha][coluna] != ' ':
        return False
    return True

# Função para fazer uma jogada
def fazer_jogada(linha, coluna):
    global fase_colocacao, pecas_brancas, pecas_pretas, fase_movimento, jogador_atual

    if fase_colocacao:
        if posicao_valida(linha, coluna):
            tabuleiro[linha][coluna] = jogador_atual
            if jogador_atual == 'X':
                pecas_brancas -= 1
            else:
                pecas_pretas -= 1

            # Verificar se há um moinho
            if verificar_moinho(linha, coluna):
                fase_movimento = True
                pecas_selecionadas.clear()

            # Trocar de jogador
            if pecas_brancas == 0 and pecas_pretas == 0:
                fase_colocacao = False
                jogador_atual = 'X'  # Reiniciar com as peças pretas
            else:
                if jogador_atual == 'X':
                    jogador_atual = 'O'
                else:
                    jogador_atual = 'X'
           
    elif fase_movimento:
            if tabuleiro[linha][coluna] == jogador_atual and verificar_moinho(linha, coluna):
                return
    
            if tabuleiro[linha][coluna] == jogador_atual:
                pecas_selecionadas.append((linha, coluna))
    
                if len(pecas_selecionadas) == 2:
                    linha_origem, coluna_origem = pecas_selecionadas[0]
                    linha_destino, coluna_destino = pecas_selecionadas[1]
    
                    if movimento_valido(linha_origem, coluna_origem, linha_destino, coluna_destino):
                        tabuleiro[linha_destino][coluna_destino] = jogador_atual
                        tabuleiro[linha_origem][coluna_origem] = ' '
                        pecas_selecionadas.clear()
    
                        if verificar_moinho(linha_destino, coluna_destino):
                            fase_remocao = True
    
                        # Trocar de jogador
                        if jogador_atual == 'X':
                            jogador_atual = 'O'
                        else:
                            jogador_atual = 'X'
            else:
                pecas_selecionadas.clear()

# Função para verificar se há um moinho
def verificar_moinho(linha, coluna):
    peca = tabuleiro[linha][coluna]
    # Verificar linha
    if tabuleiro[linha][0] == tabuleiro[linha][1] == tabuleiro[linha][2] == peca:
        return True
    # Verificar coluna
    if tabuleiro[0][coluna] == tabuleiro[1][coluna] == tabuleiro[2][coluna] == peca:
        return True
    # Verificar diagonais
    if (linha, coluna) in [(0, 0), (0, 2), (1, 1), (2, 0), (2, 2)]:
        if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] == peca:
            return True
        if tabuleiro[2][0] == tabuleiro[1][1] == tabuleiro[0][2] == peca:
            return True
    return False

# Função para verificar se um movimento é válido
def movimento_valido(linha_origem, coluna_origem, linha_destino, coluna_destino):
    if tabuleiro[linha_origem][coluna_origem] == jogador_atual and tabuleiro[linha_destino][coluna_destino] == ' ':
        # Movimento vertical
        if coluna_origem == coluna_destino and abs(linha_origem - linha_destino) == 1:
            return True
        # Movimento horizontal
        if linha_origem == linha_destino and abs(coluna_origem - coluna_destino) == 1:
            return True
        # Movimento diagonal
        if (linha_origem, coluna_origem) in [(0, 0), (0, 2), (2, 0), (2, 2)] and (linha_destino, coluna_destino) == (1, 1):
            return True
        if (linha_origem, coluna_origem) == (1, 1) and (linha_destino, coluna_destino) in [(0, 0), (0, 2), (2, 0), (2, 2)]:
            return True
    return False


# Função principal do jogo
def jogar():
    global jogador_atual

    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                return

            if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
                pos = pygame.mouse.get_pos()
                coluna = (pos[0] - 100) // 200
                linha = (pos[1] - 100) // 200

                if 0 <= linha < 7 and 0 <= coluna < 8:
                    fazer_jogada(linha, coluna)

        exibir_tabuleiro()
        pygame.display.flip()

# Executar o jogo
jogar()
