#Adventure game

import PySimpleGUI as sg


class Jogo_aventura:
    def __init__(self):
        self.pergunta1 = 'Você nasceu no norte ou no sul?   (N/S)' #norte - lado a e sul - lado b.
        self.pergunta2 = 'Você prefere a espada ou escudo? (espada/escudo)' #espada - ladoA e escudo LadoB
        self.pergunta3 = 'Qual é sua especialidade ?  (frente/tatico)' #Linha de frente - LadoA, taitoc ladoB
        self.finalHistoria1 = 'Você sera um heroi linha de frente'
        self.finalHistoria2 = 'Você sera um heroi protegendo todas as nossas tropas'
        self.finalHistoria3 = 'Você ira se sacrificar na batalha! '
        self.finalHistoria4 = 'Você não é capaz de lutar essa batalha!'



    def Iniciar(self):
        #Layout
        layout = [
            [sg.Text(" ### Jogo de aventura ### ", size=(20, 0))],
            [sg.Output(size=(45,0))],
            [sg.Input(size=(30,0), key='escolha')],
            [sg.Button('Iniciar'),sg.Button('Responder')],
        ]
        #Janela
        self.janela = sg.Window('Jogo de Aventura!', layout=layout)

        while True:
            # Ler dados

            self.LerValores()

            # Fazer algo
            if self.eventos == 'Iniciar':
                print(self.pergunta1)
                self.LerValores()

                if self.valores['escolha'] == 'N':
                    print(self.pergunta2)
                    self.LerValores()
                    if self.valores['escolha'] == 'espada':
                        print(self.finalHistoria1)
                    if self.valores['escolha'] == 'escudo':
                        print(self.finalHistoria2)

                if self.valores['escolha'] == 'S':

                    print(self.pergunta3)
                    self.LerValores()

                    if self.valores['escolha'] == 'frente':
                        print(self.finalHistoria3)

                    if self.valores['escolha'] == 'tatico':
                        print(self.finalHistoria4)

    def LerValores(self):
        self.eventos, self.valores = self.janela.Read()


jogo = Jogo_aventura()
jogo.Iniciar()
