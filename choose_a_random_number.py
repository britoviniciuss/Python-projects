import random
import PySimpleGUI as sg


class ChuteOnumero:
    def __init__(self):
        self.valor_aleatorio = 0
        self.valormax = 100
        self.valormin = 1
        self.tentar_novamente = True


    def Iniciar(self):

        #Layout da janela
        layout = [
            [sg.Text("Seu chute!", size=(20,0))],
            [sg.Input(size=(18,0), key="ValorChute")],
            [sg.Button("Chutar!")],
            [sg.Output(size=(50,10))]
        ]

        #Janela

        self.janela = sg.Window("Chute um numero!", layout=layout)

        self.GerarNumeroAleatorio()

        try:
            while True:

                #Recebe os valores
                self.evento, self.valores = self.janela.Read()



                # Fazer algo
                if self.evento == "Chutar!":
                    self.valor_do_chute = self.valores['ValorChute']
                    while self.tentar_novamente == True:

                        if int(self.valor_do_chute) > self.valor_aleatorio:
                            print("Chute um valor mais baixo!")

                            break
                        elif int(self.valor_do_chute) < self.valor_aleatorio:
                            print("Chute um valor mais alto!")

                            break
                        if int(self.valor_do_chute) == self.valor_aleatorio:
                            self.tentar_novamente = False
                            print("Voce acertou o numero!!")
                            break

        except:

            print("Favor digitar apenas numeros!!")
            self.Iniciar()



    def GerarNumeroAleatorio(self):
        self.valor_aleatorio = random.randint(self.valormin, self.valormax)



print("## Programa de chutar um numero ##")
chute = ChuteOnumero()
chute.Iniciar()
