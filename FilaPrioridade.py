class FilaPrioridade():
	'''Será uma implementação de uma fila de prioridade que será organizada
	   de forma decrescente'''
	def __init__(self):
		self.elementos = []
	
	def inserir(self, elemento, organizar=True):
		self.elementos.append(elemento)
		if organizar:
			self.organizar()
	
	def organizar(self):
		tamanho = self.getTamanho()
		contador = 0
		while contador <= tamanho:
			for i in range(tamanho-1, 0, -1):
				if self.elementos[i].freq > self.elementos[i-1].freq:
					self.elementos[i], self.elementos[i-1] = self.elementos[i-1], self.elementos[i]
			contador+=1
           

	def remover(self):
		return self.elementos.pop()

	def removerMenor(self):
		menor = self.elementos[0].freq
		escolhido = 0
		for i in range(self.getTamanho()):
			if self.elementos[i].freq < menor:
				menor = self.elementos[i].freq
				escolhido = i
		retorno = self.elementos[escolhido]
		del self.elementos[escolhido]
		return retorno

	def getTamanho(self):
		return len(self.elementos)
	
	def printar(self):
		for i in range(self.getTamanho()):
			print(self.elementos[i].char, self.elementos[i].freq)