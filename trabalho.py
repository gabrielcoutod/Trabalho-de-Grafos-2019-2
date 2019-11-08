
class Aresta:

	def __init__(self, vertice = 0, peso = 0):
		self.vertice = vertice
		self.peso = peso 
	
	def zera(self):
		self.peso = -1



class Grafo:

	def __init__(self,lista = []):
		self.lista = lista
	
	def add(self,lista):
		self.lista.append(lista)
		
	def bifloresta(self):
		
		#lista dos vertices percorridos
		# 0 se nao foi percorrido e 1 se foi 
		vertices = [0 for i in range(len(self.lista))]
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
				for i in range(len(vertices)):
					# se valor eh diferente de zero vertice nao esta na arvore logo nao precisa verificar ele
					if (vertices[i] != 0):
						for j in range(len(self.lista[i])):
							# se eh menor atualiza os valores
							if (self.lista[i][j].peso < menor and self.lista[i][j].peso != -1):
								menor = self.lista[i][j].peso
								indice = j
								vertice_menor = i
				
				# verifica se ja passou pelo vertice da menor aresta 
				if (vertices[self.lista[vertice_menor][indice].vertice] != 1):
					custo += menor 
					if (menor > maior):
						maior = menor 
					vertices[self.lista[vertice_menor][indice].vertice] = 1
					self.lista[vertice_menor][indice].peso = -1
					achou = 1
				else:
					self.lista[vertice_menor][indice].peso = -1
	
		return custo - maior 
	
	
def main():
	
	num_vertices = int(input())
	
	grafo = Grafo()
	
	for i in range(num_vertices):
		string = input()
		linha = string.split()
		grafo.add([Aresta(i,int(linha[i])) for i in range(len(linha)) if int(linha[i]) != -1])
		
	print(grafo.bifloresta())
	
	
main()
