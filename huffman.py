import sys
class Huffman():
	'''Classe para representar o Algoritmo de Huffman em si, onde será
	   criada todas as estruturas necessárias e será realizada a compressão
	   e descompressão dos dados'''
	def __init__(self, arquivo):
		self.arquivo = arquivo
		self.dicionarioDeFrequencia = {}
		self.raiz = None

	def criarDicionario(self):
		f = open(self.arquivo, "r")
		for char in f.read():
			if char not in self.dicionarioDeFrequencia:
				self.dicionarioDeFrequencia[char]=1
			else:
				self.dicionarioDeFrequencia[char]+=1
		f.close()

	def criarFilaDePrioridade(self):
		pass
	def criarArvore(self):
		pass
	def getBinario(self, raiz, procurado):
		pass
	def criarDicionarioDeBinarios(self):
		pass
	def comprimir(self):
		pass
	def descomprimir(self):
		pass
	def calcularEstatisticas(self):
		pass

arquivo = sys.argv[1]
huff = Huffman(arquivo)
huff.criarDicionario()
print(huff.dicionarioDeFrequencia)