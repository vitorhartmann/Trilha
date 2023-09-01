import pygame
import random

# Inicialização do Pygame
pygame.init()

# Definição das cores dos jogadores
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)

# Linhas do tabuleiro
AZUL = (0, 0, 255)
VERMELHO = (255, 0, 0)
AMARELO = (255, 255, 0)

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
ia_fez_jogada = False

posicoes = [
    # Posições do cubo externo
    (largura_tela // 2 - 300, altura_tela // 2 - 300),  # 0
    (largura_tela // 2, altura_tela // 2 - 300),  # 1
    (largura_tela // 2 + 300, altura_tela // 2 - 300),  # 2
    
    # Posições do cubo do meio
    (largura_tela // 2 - 200, altura_tela // 2 - 200),  # 3
    (largura_tela // 2, altura_tela // 2 - 200),  # 4
    (largura_tela // 2 + 200, altura_tela // 2 - 200),  # 5
    
    # Posições do cubo interno
    (largura_tela // 2 - 100, altura_tela // 2 - 100),  # 6
    (largura_tela // 2, altura_tela // 2 - 100),  # 7
    (largura_tela // 2 + 100, altura_tela // 2 - 100),  # 8
    
    (largura_tela // 2 - 300, altura_tela // 2),  # 9
    (largura_tela // 2 - 200, altura_tela // 2),  # 10
    (largura_tela // 2 - 100, altura_tela // 2),  # 11
    
    (largura_tela // 2 + 100, altura_tela // 2),  # 12
    (largura_tela // 2 + 200, altura_tela // 2),  # 13
    (largura_tela // 2 + 300, altura_tela // 2),  # 14
    
    (largura_tela // 2 - 100, altura_tela // 2 + 100), #15
    (largura_tela // 2, altura_tela // 2 +100), #16
    
    
    (largura_tela // 2 + 100, altura_tela // 2 + 100),  # 17
    
    (largura_tela // 2 - 200, altura_tela // 2 + 200),  # 18
    (largura_tela // 2, altura_tela // 2 + 200),  # 19
    (largura_tela // 2 + 200, altura_tela // 2 + 200),  # 20


    (largura_tela // 2 - 300, altura_tela // 2 + 300),  # 21
    (largura_tela // 2, altura_tela // 2 + 300),  # 22
    (largura_tela // 2 + 300, altura_tela // 2 + 300),  # 23
    
    
    
    
]




def desenhar_linhas_cubos():
    # Desenho do tabuleiro, segue a ordem em sentido horário

    
    # Linhas Horizontais

    pygame.draw.lines(tela, AZUL, True, [
                      posicoes[0], posicoes[1], posicoes[2]], 2) 
    pygame.draw.lines(tela, AZUL, True, [
                      posicoes[3], posicoes[4], posicoes[5]], 2) 
    pygame.draw.lines(tela, AZUL, True, [
                      posicoes[6], posicoes[7], posicoes[8]], 2)  
    pygame.draw.lines(tela, AZUL, True, [
                      posicoes[9], posicoes[10], posicoes[11]], 2)
    pygame.draw.lines(tela, AZUL, True, [
                      posicoes[12], posicoes[13], posicoes[14]], 2) 
    pygame.draw.lines(tela, AZUL, True, [
                      posicoes[15], posicoes[16], posicoes[17]], 2)
    pygame.draw.lines(tela, AZUL, True, [
                      posicoes[18], posicoes[19], posicoes[20]], 2)
    pygame.draw.lines(tela, AZUL, True, [
                      posicoes[21], posicoes[22], posicoes[23]], 2)


    # Linhas Verticais

    pygame.draw.lines(tela, AZUL, True, [
                      posicoes[0], posicoes[9], posicoes[21]], 2)   
    pygame.draw.lines(tela, AZUL, True, [
                      posicoes[3], posicoes[10], posicoes[18]], 2)  
    pygame.draw.lines(tela, AZUL, True, [
                      posicoes[6], posicoes[11], posicoes[15]], 2)  
    pygame.draw.lines(tela, AZUL, True, [
                      posicoes[1], posicoes[4], posicoes[7]], 2)   
    pygame.draw.lines(tela, AZUL, True, [
                      posicoes[16], posicoes[19], posicoes[22]], 2) 
    pygame.draw.lines(tela, AZUL, True, [
                      posicoes[8], posicoes[12], posicoes[17]], 2)  
    pygame.draw.lines(tela, AZUL, True, [
                      posicoes[5], posicoes[13], posicoes[20]], 2) 
    pygame.draw.lines(tela, AZUL, True, [
                      posicoes[2], posicoes[14], posicoes[23]], 2)      

    



# Função para exibir o tabuleiro
def exibir_tabuleiro():
    tela.fill(PRETO)
    desenhar_linhas_cubos()

    for i in range(24):
        pygame.draw.circle(tela, BRANCO, posicoes[i], 20)
        fonte = pygame.font.Font(None, 30)  # Reduzindo o tamanho da fonte para 30
        linha = i // 8
        coluna = i % 8

        # Substituir "B" por "X" e "P" por "O"
        texto = tabuleiro[linha][coluna]
        if texto == 'B':
            texto = 'X'
        elif texto == 'P':
            texto = 'O'

        texto_renderizado = fonte.render(texto, True, PRETO)
        tela.blit(texto_renderizado, (posicoes[i][0] - 12, posicoes[i][1] - 12))  # Reduzindo o deslocamento em 3 pixels

        # Mostrar o número da posição
       # texto_posicao = fonte.render(str(i), True, PRETO)
       # tela.blit(texto_posicao, (posicoes[i][0] - 7, posicoes[i][1] - 7))



    # Exibir mensagem de quem é a vez
    mensagem = f"Vez do jogador {jogador_atual}"
    fonte_mensagem = pygame.font.Font(None, 30)
    texto_mensagem = fonte_mensagem.render(mensagem, True, BRANCO)
    largura_texto = texto_mensagem.get_width()
    altura_texto = texto_mensagem.get_height()
    pos_x_mensagem = largura_tela // 2 - largura_texto // 2
    pos_y_mensagem = altura_tela // 2 - altura_texto // 2 - 50 - 350
    tela.blit(texto_mensagem, (pos_x_mensagem, pos_y_mensagem))

    # Exibir quantidade de peças disponíveis
    fonte_peca = pygame.font.Font(None, 30)
    texto_pecas = fonte_peca.render(
        f"P: {pecas_pretas_restantes}  B: {pecas_brancas_restantes}", True, BRANCO)
    tela.blit(texto_pecas, (10, 10))


def posicao_valida(linha, coluna):
    # Verifica se a posição está dentro dos limites do tabuleiro
    if linha < 0 or linha > 2 or coluna < 0 or coluna > 7:
        return False
    # Verifica se a posição está vazia
    if tabuleiro[linha][coluna] != ' ':
        return False
    # Verifica se a posição respeita as regras de colocação (unica regra atual, é quando tem alguma peça lá)
    # Adicione aqui as regras específicas do jogo

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


def obter_posicoes_disponiveis():
    posicoes_disponiveis = []
    for linha in range(len(tabuleiro)):
        for coluna in range(len(tabuleiro[linha])):
            if tabuleiro[linha][coluna] == ' ':
                posicoes_disponiveis.append((linha, coluna))
    return posicoes_disponiveis

def posicionar_pecas_pretas_aleatoriamente():
    global pecas_pretas_restantes

    while pecas_pretas_restantes > 0:
        linha, coluna = posicao_aleatoria()
        if tabuleiro[linha][coluna] == ' ':
            tabuleiro[linha][coluna] = 'P'
            pecas_pretas_restantes -= 1

def minimax(tabuleiro, profundidade, maximizando):
    if profundidade == 0 or pecas_brancas_restantes == 0 or pecas_pretas_restantes == 0:
        # Implementar aqui a função de avaliação da situação do jogo
        return 0  # Retorna a pontuação atual do tabuleiro

    if maximizando:
        melhor_pontuacao = float('-inf')
        for jogada in obter_posicoes_disponiveis():
            linha, coluna = jogada
            if posicao_valida(linha, coluna):
                tabuleiro[linha][coluna] = jogador_atual
                pontuacao = minimax(tabuleiro, profundidade - 1, False)
                tabuleiro[linha][coluna] = ' '  # Desfaz a jogada
                melhor_pontuacao = max(melhor_pontuacao, pontuacao)
        return melhor_pontuacao
    else:
        melhor_pontuacao = float('inf')
        for jogada in obter_posicoes_disponiveis():
            linha, coluna = jogada
            if posicao_valida(linha, coluna):
                tabuleiro[linha][coluna] = 'P' if jogador_atual == 'B' else 'B'
                pontuacao = minimax(tabuleiro, profundidade - 1, True)
                tabuleiro[linha][coluna] = ' '  # Desfaz a jogada
                melhor_pontuacao = min(melhor_pontuacao, pontuacao)
        return melhor_pontuacao


def escolher_melhor_jogada(tabuleiro, jogador):
    melhor_jogada = None
    melhor_pontuacao = float('-inf')

    for jogada in obter_posicoes_disponiveis():
        linha, coluna = jogada
        if posicao_valida(linha, coluna):
            tabuleiro[linha][coluna] = jogador
            pontuacao = minimax(tabuleiro, 3, False)
            tabuleiro[linha][coluna] = ' '  # Desfaz a jogada
            if pontuacao > melhor_pontuacao:
                melhor_jogada = jogada
                melhor_pontuacao = pontuacao

    return melhor_jogada


def tentar_colocar_peca(linha, coluna):
    if posicao_valida(linha, coluna):
        if tabuleiro[linha][coluna] == ' ':
            tabuleiro[linha][coluna] = jogador_atual
            return True
    return False


# Função principal do jogo
def jogar():
    global jogador_atual, pecas_brancas_restantes, pecas_pretas_restantes, ia_fez_jogada

    rodando = True

    while rodando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    rodando = False

        exibir_tabuleiro()
        pygame.display.flip()

        if pecas_brancas_restantes == 0 and pecas_pretas_restantes == 0:
            rodando = False
        elif jogador_atual == 'B':
            if pecas_brancas_restantes > 0:
                for evento in pygame.event.get():
                    if evento.type == pygame.MOUSEBUTTONDOWN:
                        x, y = evento.pos
                        for i in range(24):
                            pos_x, pos_y = posicoes[i]
                            if abs(x - pos_x) < 20 and abs(y - pos_y) < 20:
                                linha = i // 8
                                coluna = i % 8
                                if posicao_valida(linha, coluna):
                                    if tabuleiro[linha][coluna] == ' ':
                                        tabuleiro[linha][coluna] = jogador_atual
                                        pecas_brancas_restantes -= 1
                                        trocar_jogador()
                                        exibir_tabuleiro()
                                        pygame.display.flip()
                                        break
                # Marque que a IA ainda não fez sua jogada neste turno
                ia_fez_jogada = False
            else:
                jogador_atual = 'P'
        elif jogador_atual == 'P':
            if pecas_pretas_restantes > 0 and not ia_fez_jogada:
                # Posicione uma peça preta da IA aleatoriamente
                linha, coluna = posicao_aleatoria()
                if posicao_valida(linha, coluna):
                    tabuleiro[linha][coluna] = 'P'
                    pecas_pretas_restantes -= 1
                    trocar_jogador()
                    exibir_tabuleiro()
                    pygame.display.flip()
                    # Marque que a IA fez sua jogada neste turno
                    ia_fez_jogada = True
            else:
                jogador_atual = 'B'
                # Lógica para o jogador B ou outra lógica da IA
                # ...

    exibir_tabuleiro()
    pygame.display.flip()

    if pecas_brancas_restantes == 0 and pecas_pretas_restantes == 0:
        print("Fim do jogo. Ambos os jogadores colocaram todas as peças.")

    pygame.quit()



# Executar o jogo
jogar()
