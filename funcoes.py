import os
import sys

#Sai do programa
def sair():
	exit()

#Limpa a tela
def clear():	
	os.system('cls')

def bemvindo():	
	#Limpa a tela
	clear()	
	print("BEM VINDO A AGENDA")
	print("------------------------------------------")
	print("Selecione uma opcao")
	print("------------------------------------------")	
	#Opcoes do Usuario
	print("1 - Adicionar um novo contato")
	print("2 - Listar os contatos")
	print("3 - Sair")
	#Recupera a opcao selecionada
	opcao = int(input())	
	#Estrutura de controle
	if opcao == 1:
		adicionar()
	elif opcao == 2:
		listar()
	elif opcao == 3:
		sair()
	else:
		falha()

#Funcoes do processo
def adicionar():
	#limpa a tela
	clear()
	#escreve o cabecalho
	print("------------------------------------------")
	print("Adicionar um Contato")
	print("------------------------------------------")	
	#abre o arquivo agenda para escrita
	agenda = open("agendatelefonica.csv",'a')
	#recupera o nome digitado na tela
	nome = input("Nome do Contato:")
	#recupera o telefone digitado na tela
	telefone = input("Digite o telefone:")	
	#limpa a tela
	clear()
	#escreve o header de sucesso
	print("------------------------------------------")	
	print("CONTATO SALVO COM SUCESSO!")
	print("------------------------------------------")	
	#printo o nome e o telefone, com tabulacao
	#esse e um ponto que pode ser melhorado, porque a tabulacao nao fica alinhada
	print("Nome\t\t\tTelefone")
	print(nome, "\t\t\t", telefone)
	#escrevo no arquivo o nome do contato
	agenda.write(nome)
	#acrescento uma vírgula, para separar os dados
	agenda.write(",")
	#adiciono o telefone
	agenda.write(telefone)
	#quero uma linha
	agenda.write("\n")
	#fecho o arquivo
	agenda.close()
	#exibo a mensagem para pressionar enter para ir para opcoes
	opcoes()	
	
def listar():
	#limpa a tela
	clear()
	#escreve o header
	print("------------------------------------------")
	print("Lista de Contatos")
	print("------------------------------------------")	
	#abre o arquivo agenda somente leitura
	agenda = open("agendatelefonica.csv")
	#para cada linha do arquivo
	for linha in agenda:
		#eu separo o nome do telefone pelo caractere ','
		arr = linha.replace('\n','').split(",")
		#pego o nome
		nome = arr[0]
		#pego o telefone
		telefone = arr[1]
		#e printo na tela o nome e o telefone, com tabulacao
		print (nome, "\t\t\t", telefone)
	#fecha o arquivo
	agenda.close()
	#exibo a mensagem para pressionar enter para ir para opcoes
	opcoes()

def opcoes():
	input("Pressione Enter para voltar as opcoes...")
	#se apertar, ele exibe o menu
	bemvindo()

def falha():
	#exibe a mensagem de opcao incorreta
	print("Opcao Incorreta")
	opcoes()
