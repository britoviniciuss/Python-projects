import random


class ChuteOnumero:
    def __init__(self):
        self.valor_aleatorio = 0
        self.valormax = 5
        self.valormin = 1
        self.tentar_novamente = True

    def Iniciar(self):
        self.GerarNumeroAleatorio()
        self.PedirValorAleatorio()

        try:
            while self.tentar_novamente == True:

                if int(self.valor_do_chute) > self.valor_aleatorio:
                    print("Chute um valor mais baixo!")
                    self.PedirValorAleatorio()
                elif int(self.valor_do_chute) < self.valor_aleatorio:
                    print("Chute um valor mais alto!")
                    self.PedirValorAleatorio()
                if int(self.valor_do_chute) == self.valor_aleatorio:
                    self.tentar_novamente = False
                    print("Voce acertou o numero!!")
        except:
            print("Favor digitar apenas numeros!!")
            self.Iniciar()



    def PedirValorAleatorio(self):

        self.valor_do_chute = input("Chute um valor : ")


    def GerarNumeroAleatorio(self):
        self.valor_aleatorio = random.randint(self.valormin, self.valormax)


print("## Programa de chutar um numero ##")
chute = ChuteOnumero()
chute.Iniciar()
