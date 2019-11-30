#Trabalho de Grafos 

# Eduardo Eugenio Kussler
# Gabriel Couto Domingues
# Thiago Sotoriva Lermen

#Algoritmo: calcula-se o peso da arvore geradora minima 
# 			com o algoritmo de prim e subtrai do valor 
#			o peso da aresta de maior peso da AGM

class Aresta:

	def __init__(self, vertice = 0, peso = 0):
		self.vertice = vertice # uma das pontas da aresta(outra ponta implicita)
		self.peso = peso # peso da aresta
	
	# faz com que a aresta seja eliminada da lista de arestas possiveis
	# colocando valor 1001
	def elimina(self):
		self.peso = 1001

class Grafo:

	def __init__(self,vertices = [],lista = []):
		self.vertices = vertices# lista de vertices do grafo
		self.lista = lista# lista que contem listas de arestas incidentes a vertices do grafo
	
	# coloca a lista de arestas incidentes sobre um vertice no grafo
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
		
		# for para pegar as arestas para arvore
		for h in range(len(vertices)-1):

			menor = 1001 # peso da aresta de menor peso disponivel
			indice = 0 # indice dela na lista de arestas do vertice
			vertice_menor = 0 # vertice que tem essa aresta na lista

			# verifica as arestas ate achar a aresta para conectar na arvore 
			for i in self.vertices:
				# se valor eh diferente de zero vertice nao esta na arvore logo nao precisa verificar ele
				if (vertices[i] != 0):
					k = 0  #indice da aresta
					# percorre listas de arestas incidentes
					for j in self.lista[i]:
						# se eh menor atualiza os valores
						if (j.peso < menor):
							#verifica se essa aresta conecta em um vertice que nao esta na arvore
							if (vertices[self.lista[i][k].vertice] != 1):
								# se nao estiver salva os valores
								menor = j.peso
								indice = k
								vertice_menor = i
							else:
								# se estiver na arvore elimina essa aresta da lista
								self.lista[i][k].elimina()
						k += 1
			
			# atualiza custo, maior aresta, coloca o vertice na lista de vertices, elimina a aresta 
			custo += menor 
			if (menor > maior):
				maior = menor 
			vertices[self.lista[vertice_menor][indice].vertice] = 1
			self.lista[vertice_menor][indice].elimina()
	
		return custo - maior 
	
	
def main():
	
	#lista com vertices do grafo
	vertices = range(int(input()))
	
	#grafo
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
