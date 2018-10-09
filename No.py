class No():
    def __init__(self, char, freq, esquerda=None, direita=None):
        self.char = char
        self.freq = freq
        self.esquerda = esquerda
        self.direita = direita

    def printar(self):
        if self.esquerda:
            self.esquerda.printar()
        print(self.char)
        if self.direita:
            self.direita.printar()