# Simulador de dado
# Simula o uso de um dado.
import random
import PySimpleGUI as sg


class SimuladorDeDado:
    def __init__(self):
        self.valor_min = 1
        self.valor_max = 6
        ## Layout
        self.layout = [
            [sg.Text("Jogar o dado?")],
            [sg.Button("sim"), sg.Button("Não")]
        ]

    def Iniciar(self):

        ## Janela
        self.janela = sg.Window("Simulador de Dado", layout=self.layout)
        ## ler os valores da tela
        self.eventos, self.valores = self.janela.Read()
        ## fazer algo com esses valor

        try:
            if self.eventos == "sim" or self.eventos == "s":
                self.GerarValorDoDado()
            elif self.eventos == "Não" or self.eventos == "n":
                print("Agredecemos a sua participação")
            else:
                print("Digite sim ou não")
        except:
            print("error.")

    def GerarValorDoDado(self):
        print(random.randint(self.valor_min, self.valor_max))


simulador = SimuladorDeDado()
simulador.Iniciar()
