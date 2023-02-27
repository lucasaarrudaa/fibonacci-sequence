from time import sleep
import re

print("\nA Sequência de Fibonacci se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores\n"
      "(exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...)\n")
print("Deseja descobrir se algum número pertence à sequencia?\n"
      "Se sim, digite [S]\n"
      "Se deseja sair, digite [X]")

escolha_usuario = str(input().strip().upper())
while escolha_usuario == "S":

    #executando
    while True:
        fibo_list = []
        nro_escolhido = 0
        while True:
            try:
                nro_escolhido = int(input("Número que deseja verificar: \n"))
                if not 0 <= nro_escolhido <= 500000:
                    raise ValueError("Por favor, pode digitar um número menor que 500000?")
            except ValueError as e:
                print("Valor inválido:", e)
            else:
                break

        # definindo a fórmula:
        def fibo(n):
            if n == 1:
                return 0
            elif n == 2:
                return 1
            else:
                return fibo(n - 1) + fibo(n - 2)

        # define um limite para a sequencia
        def limite():
            n = 35
            for val in range(1, n + 1):
                fibo_list.append(fibo(val))

        while True:
            print("********************************************")
            print("Aguarde um momento enquanto estou calculando")
            print("********************************************\n")
            sleep(2)
            limite()

            # Se o número estiver na sequência, mostra a posição.
            if nro_escolhido in fibo_list:
                index_lista = [n for n, x in enumerate(fibo_list) if x== nro_escolhido]
                index = int(index_lista[0] + 2)

                #tranformando a lista em string
                print(f"O número {nro_escolhido} está na sequência de Fibonacci, é o {index}° número\n")

                # Pergunta se o usuário deseja seguir
                continua_solicitacao = input(str("Se deseja verificar outro número digite [S]\n "
                                                "se quiser parar, digite [X]").strip())
                sleep(1)
                if continua_solicitacao == "S":
                    continue
                elif continua_solicitacao == "X":
                    break
        break

    # se não, manda mensagem que não encontrou.
    else:
        print(f" O número {nro_escolhido} não está na sequência de Fibonacci")
        break

    # Se o usuário escolher sair, para o programa
    if escolha_usuario == "X":
        break
