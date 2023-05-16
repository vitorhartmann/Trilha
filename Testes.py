import pygame
import random

# Inicialização do Pygame
pygame.init()

# Definição das cores dos jogadores
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)


#Linhas do tabuleiro
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
pecas_brancas_restantes = 9
pecas_pretas_restantes = 9
jogador_atual = 'B'  # Começa com as peças brancas




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


def desenhar_linhas_cubos():
    # Desenho do tabuleiro, segue a ordem em sentido horário

    # Cubo vermelho (Menor)
    pygame.draw.lines(tela, VERMELHO, True, [posicoes[0], posicoes[1], posicoes[2]], 2) # Linha superior
    pygame.draw.lines(tela, VERMELHO, True, [posicoes[2], posicoes[4], posicoes[7]], 2) # Linha direita
    pygame.draw.lines(tela, VERMELHO, True, [posicoes[7], posicoes[6], posicoes[5]], 2) # Linha inferior
    pygame.draw.lines(tela, VERMELHO, True, [posicoes[5], posicoes[3], posicoes[0]], 2) # Linha esquerda

    # Cubo azul (Do meio)
    pygame.draw.lines(tela, AZUL, True, [posicoes[8], posicoes[9], posicoes[10]], 2) # Linha superior
    pygame.draw.lines(tela, AZUL, True, [posicoes[10], posicoes[12], posicoes[15]], 2) # Linha direita
    pygame.draw.lines(tela, AZUL, True, [posicoes[15], posicoes[14], posicoes[13]], 2) # Linha inferior
    pygame.draw.lines(tela, AZUL, True, [posicoes[13], posicoes[11], posicoes[8]], 2) # Linha esquerda


    # Cubo Vermelho (Maior)
    pygame.draw.lines(tela, BRANCO, True, [posicoes[16], posicoes[17], posicoes[18]], 2) # Linha superior
    pygame.draw.lines(tela, BRANCO, True, [posicoes[18], posicoes[20], posicoes[23]], 2) # Linha direita
    pygame.draw.lines(tela, BRANCO, True, [posicoes[23], posicoes[22], posicoes[21]], 2) # Linha inferior
    pygame.draw.lines(tela, BRANCO, True, [posicoes[21], posicoes[19], posicoes[16]], 2) # Linha esquerda

    # Linhas de Ligamento (Em amarelo)
    pygame.draw.lines(tela, AMARELO, True, [posicoes[17], posicoes[9], posicoes[1]], 2) # Linha superior
    pygame.draw.lines(tela, AMARELO, True, [posicoes[20], posicoes[12], posicoes[4]], 2) # Linha direita
    pygame.draw.lines(tela, AMARELO, True, [posicoes[22], posicoes[14], posicoes[6]], 2) # Linha inferior
    pygame.draw.lines(tela, AMARELO, True, [posicoes[19], posicoes[11], posicoes[3]], 2) # Linha esquerda



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

    # Exibir mensagem de quem é a vez
    mensagem = f"Vez do jogador {jogador_atual}"
    fonte_mensagem = pygame.font.Font(None, 30)
    texto_mensagem = fonte_mensagem.render(mensagem, True, BRANCO)
    largura_texto = texto_mensagem.get_width()
    altura_texto = texto_mensagem.get_height()
    pos_x_mensagem = largura_tela // 2 - largura_texto // 2
    pos_y_mensagem = altura_tela // 2 - altura_texto // 2 - 50 - 350
    tela.blit(texto_mensagem, (pos_x_mensagem, pos_y_mensagem))

    
    # Exibir mensagem de quem é a vez
    mensagem = f"Vez do jogador {jogador_atual}"
    fonte_mensagem = pygame.font.Font(None, 30)
    texto_mensagem = fonte_mensagem.render(mensagem, True, BRANCO)
    largura_texto = texto_mensagem.get_width()
    altura_texto = texto_mensagem.get_height()
    pos_x_mensagem = largura_tela // 2 - largura_texto // 2
    pos_y_mensagem = altura_tela // 2 - altura_texto // 2 - 50 - 350
    tela.blit(texto_mensagem, (pos_x_mensagem, pos_y_mensagem))



def posicao_valida(linha, coluna):
    # Verifica se a posição está dentro dos limites do tabuleiro
    if linha < 0 or linha >= len(tabuleiro) or coluna < 0 or coluna >= len(tabuleiro[0]):
        return False
    # Verifica se a posição está vazia
    if tabuleiro[linha][coluna] != ' ':
        return False
    # Verifica se a posição respeita as regras de colocação (por exemplo, não está na linha externa do tabuleiro)
    # Adicione aqui as regras específicas do seu jogo
    # ...
    return True

def posicao_aleatoria():
    linha = random.randint(0, len(tabuleiro) - 1)
    coluna = random.randint(0, len(tabuleiro[0]) - 1)
    while not posicao_valida(linha, coluna):
        linha = random.randint(0, len(tabuleiro) - 1)
        coluna = random.randint(0, len(tabuleiro[0]) - 1)
    return linha, coluna


def trocar_jogador():
    global jogador_atual
    if jogador_atual == 'B':
        jogador_atual = 'P'
    else:
        jogador_atual = 'B'





# Função principal do jogo
def jogar():
    global jogador_atual, pecas_brancas_restantes, pecas_pretas_restantes

    colocando_peca = True  # Variável para controlar se o jogador está colocando uma peça

    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                return

            if evento.type == pygame.MOUSEBUTTONDOWN and colocando_peca:
                x, y = evento.pos
                for i in range(24):
                    pos_x, pos_y = posicoes[i]
                    if abs(x - pos_x) < 20 and abs(y - pos_y) < 20:
                        linha = i // 8
                        coluna = i % 8
                        if posicao_valida(linha, coluna):
                            if tabuleiro[linha][coluna] == ' ':
                                tabuleiro[linha][coluna] = jogador_atual
                                if jogador_atual == 'B':
                                    pecas_brancas_restantes -= 1
                                else:
                                    pecas_pretas_restantes -= 1
                                colocando_peca = False
                                trocar_jogador()
                                break

        exibir_tabuleiro()
        pygame.display.flip()

        if pecas_brancas_restantes == 0 and pecas_pretas_restantes == 0:
            # Ambos os jogadores colocaram todas as peças, passa para a próxima fase do jogo
            break

    # Continuar com a lógica original do jogo
    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                return

        if jogador_atual == 'B':
            if pecas_brancas_restantes > 0:
                colocando_peca = True  # Permite que o jogador humano coloque a próxima peça
            else:
                jogador_atual = 'P'  # Passa para o próximo jogador se não há mais peças brancas

        elif jogador_atual == 'P':
            if pecas_pretas_restantes > 0:
                linha, coluna = posicao_aleatoria()
                if posicao_valida(linha, coluna):
                    if tabuleiro[linha][coluna] == ' ':
                        tabuleiro[linha][coluna] = 'P'
                        pecas_pretas_restantes -= 1
                        trocar_jogador()
            else:
                jogador_atual = 'B'  # Passa para o próximo jogador se não há mais peças pretas

        exibir_tabuleiro()
        pygame.display.flip()



# Executar
jogar()
