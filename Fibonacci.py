from time import sleep

class Fibonacci:
    def __init__(self):
        self.fibo_list = []

    def fibo(self, n):
        if n == 1:
            return 0
        elif n == 2:
            return 1
        else:
            return self.fibo(n - 1) + self.fibo(n - 2)

    def limite(self, nro_escolhido):
        n = 1
        while self.fibo(n) <= nro_escolhido:
            self.fibo_list.append(self.fibo(n))
            n += 1

    def verificar_numero(self, nro_escolhido):
        self.fibo_list = []
        self.limite(nro_escolhido)

        if nro_escolhido in self.fibo_list:
            index_lista = [n for n, x in enumerate(self.fibo_list) if x == nro_escolhido]
            index = int(index_lista[0] + 1)
            print(f"\nO número {nro_escolhido} está na sequência de Fibonacci, e é o {index}° número\n")
            sleep(1)
            continua_solicitacao = input(str("\nSe deseja verificar outro número digite [S]\n"
                                            "se quiser parar, digite [X]\n").strip().lower())
            if continua_solicitacao == "x":
                print("Fechando o Programa...")
                exit()
        else:
            print(f"\nO número {nro_escolhido} não está na sequência de Fibonacci")
            sleep(1)
            continua_solicitacao = input(str("\nSe deseja verificar outro número digite [S]\n"
                                            "se quiser parar, digite [X]\n").strip().lower())
            if continua_solicitacao == "x":
                print("Fechando o Programa...")
                exit()


if __name__ == '__main__':
    fibo = Fibonacci()

    print("\nA Sequência de Fibonacci se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores\n"
          "(exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...)\n")
    print("Deseja descobrir se algum número pertence à sequencia?\n"
          "\nSe sim, digite [S]\n"
          "Se deseja sair, digite [X]")

    while True:
        escolha_usuario = input().strip().lower()

        if escolha_usuario == "x":
            break

        while True:
            nro_escolhido = 0

            while True:
                try:
                    nro_escolhido = int(input("\nNúmero que deseja verificar: "))
                    if not 0 <= nro_escolhido <= 500000:
                        raise ValueError("Por favor, pode digitar um número menor que 500000?")
                except ValueError as e:
                    print("Valor inválido:", e)
                else:
                    break

            fibo.verificar_numero(nro_escolhido)
            