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
    pygame.draw.lines(tela, VERMELHO, True, [
                      posicoes[0], posicoes[1], posicoes[2]], 2)  # Linha superior
    pygame.draw.lines(tela, VERMELHO, True, [
                      posicoes[2], posicoes[4], posicoes[7]], 2)  # Linha direita
    pygame.draw.lines(tela, VERMELHO, True, [
                      posicoes[7], posicoes[6], posicoes[5]], 2)  # Linha inferior
    pygame.draw.lines(tela, VERMELHO, True, [
                      posicoes[5], posicoes[3], posicoes[0]], 2)  # Linha esquerda

    # Cubo azul (Do meio)
    pygame.draw.lines(tela, AZUL, True, [
                      posicoes[8], posicoes[9], posicoes[10]], 2)  # Linha superior
    pygame.draw.lines(tela, AZUL, True, [
                      posicoes[10], posicoes[12], posicoes[15]], 2)  # Linha direita
    pygame.draw.lines(tela, AZUL, True, [
                      posicoes[15], posicoes[14], posicoes[13]], 2)  # Linha inferior
    pygame.draw.lines(tela, AZUL, True, [
                      posicoes[13], posicoes[11], posicoes[8]], 2)  # Linha esquerda

    # Cubo Vermelho (Maior)
    pygame.draw.lines(tela, BRANCO, True, [
                      posicoes[16], posicoes[17], posicoes[18]], 2)  # Linha superior
    pygame.draw.lines(tela, BRANCO, True, [
                      posicoes[18], posicoes[20], posicoes[23]], 2)  # Linha direita
    pygame.draw.lines(tela, BRANCO, True, [
                      posicoes[23], posicoes[22], posicoes[21]], 2)  # Linha inferior
    pygame.draw.lines(tela, BRANCO, True, [
                      posicoes[21], posicoes[19], posicoes[16]], 2)  # Linha esquerda

    # Linhas de Ligamento (Em amarelo)
    pygame.draw.lines(tela, AMARELO, True, [
                      posicoes[17], posicoes[9], posicoes[1]], 2)  # Linha superior
    pygame.draw.lines(tela, AMARELO, True, [
                      posicoes[20], posicoes[12], posicoes[4]], 2)  # Linha direita
    pygame.draw.lines(tela, AMARELO, True, [
                      posicoes[22], posicoes[14], posicoes[6]], 2)  # Linha inferior
    pygame.draw.lines(tela, AMARELO, True, [
                      posicoes[19], posicoes[11], posicoes[3]], 2)  # Linha esquerda


# Função para exibir o tabuleiro
def exibir_tabuleiro():
    tela.fill(PRETO)
    desenhar_linhas_cubos()  # Chama a função para desenhar as linhas dos cubos

    for i in range(24):
        pygame.draw.circle(tela, BRANCO, posicoes[i], 20)
        fonte = pygame.font.Font(None, 50)
        linha = i // 8
        coluna = i % 8

        # Substituir "B" por "X" e "P" por "O"
        texto = tabuleiro[linha][coluna]
        if texto == 'B':
            texto = 'X'
        elif texto == 'P':
            texto = 'O'

        texto_renderizado = fonte.render(texto, True, PRETO)
        tela.blit(texto_renderizado,
                  (posicoes[i][0] - 15, posicoes[i][1] - 15))

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


def obter_posicoes_disponiveis():
    posicoes_disponiveis = []
    for linha in range(len(tabuleiro)):
        for coluna in range(len(tabuleiro[linha])):
            if tabuleiro[linha][coluna] == ' ':
                posicoes_disponiveis.append((linha, coluna))
    return posicoes_disponiveis


def minimax(tabuleiro, profundidade, maximizando):
    if profundidade == 0 or pecas_brancas_restantes == 0 or pecas_pretas_restantes == 0:
        # Aqui você deve implementar a função de avaliação da situação do jogo
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
    global jogador_atual, pecas_brancas_restantes, pecas_pretas_restantes

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
            else:
                jogador_atual = 'P'
        elif jogador_atual == 'P':
            if pecas_pretas_restantes > 0:
                jogada = escolher_melhor_jogada(tabuleiro, jogador_atual)
                if jogada is not None:
                    linha, coluna = jogada
                    if tentar_colocar_peca(linha, coluna):
                        pecas_pretas_restantes -= 1
                        trocar_jogador()
                    else:
                        print("IA: Jogada inválida. Tentando nova jogada...")
                        jogada_valida = False
                        while not jogada_valida:
                            nova_jogada = escolher_melhor_jogada(
                                tabuleiro, jogador_atual)
                            if nova_jogada is not None:
                                nova_linha, nova_coluna = nova_jogada
                                if tentar_colocar_peca(nova_linha, nova_coluna):
                                    jogada_valida = True
                                    pecas_pretas_restantes -= 1
                                    trocar_jogador()
                                    print(
                                        f"IA: Jogada válida na posição ({nova_linha}, {nova_coluna})")
                            else:
                                jogada_valida = True
                                print(
                                    "IA: Não foi possível realizar uma jogada válida.")
                                trocar_jogador()
                    exibir_tabuleiro()
                    pygame.display.flip()
                else:
                    print("IA: Não foi possível realizar uma jogada válida.")
                    jogador_atual = 'B'
            else:
                jogador_atual = 'B'
                jogada = escolher_melhor_jogada(tabuleiro, jogador_atual)
                if jogada is not None:
                    linha, coluna = jogada
                    if tentar_colocar_peca(linha, coluna):
                        pecas_brancas_restantes -= 1
                    exibir_tabuleiro()
                    pygame.display.flip()

    exibir_tabuleiro()
    pygame.display.flip()

    if pecas_brancas_restantes == 0 and pecas_pretas_restantes == 0:
        print("Fim do jogo. Ambos os jogadores colocaram todas as peças.")

    pygame.quit()


# Executar o jogo
jogar()
