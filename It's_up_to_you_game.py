##it's up to you.
#ask a question and it will answer you
import random
import PySimpleGUI as sg



class DecidaPormim:
    def __init__(self):
        self.respostas = [
            'Sim, você deve fazer isso',
            'Não sei, você que sabe',
            'Não faz isso não!',
            'Acho que está na hora certa',

        ]
    def Iniciar(self):
        #Layout
        layout = [
            [sg.Text("Faça uma pergunta")],
            [sg.Input()],
            [sg.Output(size=(50,20))],
            [sg.Button("Decida por mim")]
        ]
        #Janela
        self.janela = sg.Window("Decida por mim!", layout=layout)

        while True:

            # Ler os valores
            self.eventos, self.valores = self.janela.Read()
            # Fazer algo
            if self.eventos == "Decida por mim":

                print(random.choice(self.respostas))







decida = DecidaPormim()
decida.Iniciar()
