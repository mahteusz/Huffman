import sys
import getopt
from No import No
from FilaPrioridade import FilaPrioridade

class Huffman():
    def __init__(self, texto):
        self.texto = texto
        self.dicionario = {}
        self.criarDicionario()
        self.arvore = self.criarArvore()
        self.dicBinarios = {}
        self.criarDicionarioDeBinarios()

    def criarDicionario(self):
        for char in self.texto:
            if char not in self.dicionario:
                self.dicionario[char]=1
            else:
                self.dicionario[char]+=1
    
    def criarFila(self):
        fila = FilaPrioridade()
        for key, value in self.dicionario.items():
            novo = No(key, value)
            fila.inserir(novo)
        return fila

    def criarArvore(self):
        fila = self.criarFila()
        while fila.getTamanho() != 1:
            esquerda = fila.removerMenor()
            direita = fila.removerMenor()
            novo = No(esquerda.char+direita.char, esquerda.freq+direita.freq, esquerda, direita)
            fila.inserir(novo, False)
        return fila.remover()
    
    def getBinario(self, raiz, procurado, dic):
        if not raiz:
            return ""
        if raiz.char == procurado:
            return raiz.char
        retorno = self.getBinario(raiz.esquerda, procurado, dic)
        if retorno:
            if procurado not in dic:
                dic[procurado] = "0"
            else:
                dic[procurado] += "0"
            return raiz.char + retorno
        retorno = self.getBinario(raiz.direita, procurado, dic)
        if retorno:
            if procurado not in dic:
                dic[procurado] = "1"
            else:
                dic[procurado] += "1"
            return raiz.char + retorno
        return ""

    def criarDicionarioDeBinarios(self):
        for key, item in self.dicionario.items():
            aux = self.arvore
            self.getBinario(aux, key, self.dicBinarios)
            revertida = ""
            if len(self.dicBinarios) > 1:
                for i in self.dicBinarios[key]:
                    revertida = i+revertida
            self.dicBinarios[key] = revertida
        ##print(dic)
    
    def padding(self, texto):
        paddingExtra = 8 - len(texto) % 8
        for i in range(paddingExtra):
            texto+="0"
        return texto
    
    def comprimir(self):
        resultado = ""
        for char in self.texto:
            resultado+=self.dicBinarios[char]
        print(resultado)
        ##resultado = self.padding(resultado)
        arrayDeBytes = bytearray()
        for i in range(0, len(self.texto), 8):
            byte = resultado[i:i+8]
            arrayDeBytes.append(int(byte, 2))

        arquivo = open('comprimido.bin', 'wb')
        arquivo.write(arrayDeBytes) 
        arquivo.close()   
        print(resultado)
        return resultado
    
    def descomprimir(self, arquivo, padding):
        arquivo = open(arquivo, 'rb')
        stringBits = ""
        resultado = ""
        byte = arquivo.read(1)
        contador = 0
        '''for byte in arquivo.read():
            print(byte)
            intByte = int.from_bytes(byte, byteorder='big')
            bits = bin(intByte)[2:].rjust(8, '0')
            resultado+=bits'''
        while byte != b"":
            byte = ord(byte)
            bits = bin(byte)[2:].rjust(8, '0')
            resultado+=bits
            byte = arquivo.read(1)
            contador+=1
        arquivo.close()
        print(resultado)
            
        stringBits = resultado
        stringBits = resultado[:len(resultado)-padding]
        print(stringBits)
        atual = self.arvore
        cont = 0
        while cont < len(stringBits):
            if len(atual.char) == 1:
                print(atual.char, end="")
                atual = self.arvore
            if not atual:
                atual = self.arvore
            
            if stringBits[cont] == '1':
                atual = atual.direita
            else:
                atual = atual.esquerda
            cont+=1
        print(atual.char)
    

def main():
    startDate = None
    endDate = None
    argv = sys.argv[1:]
    opts, args = getopt.getopt(argv, ["s:e"])


huff = Huffman("ab")
huff.comprimir()
huff.descomprimir("comprimido.bin", 2)
