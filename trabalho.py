
class Aresta:

	def __init__(self, vertice = 0, peso = 0):
		self.vertice = vertice # vertice em que a aresta conecta
		self.peso = peso # peso da aresta
	
	# faz com que a aresta seja eliminada da lista
	# de arestas possiveis
	def elimina(self):
		self.peso = -1

class Grafo:

	def __init__(self,vertices = [],lista = []):
		self.vertices = vertices# lista de vertices do grafo
		self.lista = lista# lista de lista de arestas do grafo
	
	# coloca um novo vertice no grafo
	def add(self,lista):
		self.lista.append(lista)
	
	#retorna o custo da bifloresta de menor custo
	def bifloresta(self):
		
		#lista dos vertices percorridos
		# 0 se nao foi percorrido e 1 se foi 
		vertices = [0 for i in self.lista]
		#comeca no primeiro vertice
		vertices[0] = 1
		
		#custo total
		custo = 0
		#maior aresta
		maior = -1
		
		for h in range(len(vertices)-1):
			# acha a menor aresta 
			achou = 0
			# verifica a lista ate achar a aresta de menor peso nao conectada na arvore 
			while(achou == 0):
				# peso da menor aresta disponivel, e indice dela na lista de arestas do vertice e o vertice que tem essa aresta na lista
				menor = 1001
				indice = 0
				vertice_menor = 0
				for i in self.vertices:
					# se valor eh diferente de zero vertice nao esta na arvore logo nao precisa verificar ele
					if (vertices[i] != 0):
						k = 0
						for j in self.lista[i]:
							# se eh menor atualiza os valores
							if (j.peso < menor and j.peso != -1):
								menor = j.peso
								indice = k
								vertice_menor = i
							k += 1
				
				# verifica se ja passou pelo vertice da menor aresta 
				if (vertices[self.lista[vertice_menor][indice].vertice] != 1):
					custo += menor 
					if (menor > maior):
						maior = menor 
					vertices[self.lista[vertice_menor][indice].vertice] = 1
					self.lista[vertice_menor][indice].elimina()
					achou = 1
				else:
					self.lista[vertice_menor][indice].elimina()
	
		return custo - maior 
	
	
def main():
	
	#lista com vertices do grafo
	vertices = range(int(input()))
	
	grafo = Grafo(vertices)
	
	#loop para ler as entradas
	for i in vertices:
		# le a entrada  e transforma em lista de strings
		string = input()
		linha = string.split()
		# para cada elemento diferente de -1 na lista adiciona como uma aresta na lista de arestas do vertice i
		grafo.add([Aresta(j,int(linha[j])) for j in vertices if int(linha[j]) != -1])

	#imprime o custo da bifloresta de menor custo	
	print(grafo.bifloresta())
	

#inicia a aplicacao
main()
