import random

def jogar():
    print('********************************')
    print('Bem vindo ao jogo de adivinhação')
    print('********************************')

    numero_secreto = random.randrange(1,101)
    total_de_tentativas = 0
    pontos = 1000

    print('Qual nível de dificuldade?')
    print('(1) Fácil (2) Médio (3) Difícil')

    nivel = int(input("Define o nível do jogo: "))

    if (nivel == 1):
        total_de_tentativas = 20
    elif (nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    for rodada in range(1, total_de_tentativas + 1):
        print("Tentativa {} de {}".format(rodada, total_de_tentativas))
        chute_str = input('Digite um número entre 1 e 100: ')
        print('Você digitou ', chute_str)
        chute = int(chute_str)

        if (chute < 1 or chute > 100):
            print('Você deve digitar um número entre 1 e 100')
            continue


        acertou = chute == numero_secreto
        maior   = chute >  numero_secreto
        menor   = chute <  numero_secreto

        if(acertou):
            print('Você acertou e fez {} pontos!'.format(pontos))
            break
        else:
            if (maior):
                print('Você errou! O seu chute foi o maior do que o número secreto')
            elif (menor):
                print("Você errou! O seu chute foi menor do que o número secreto" )
                
            ponto_perdidos = abs(numero_secreto - chute)
            pontos = pontos - ponto_perdidos

        total_de_tentativas = total_de_tentativas
        rodada = rodada + 1
            
            
    print(f'Fim de jogo! O número secreto era {numero_secreto}')

if(__name__=="__main__"):
    jogar()

