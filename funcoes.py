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
	#abre o arquivo agenda
	agenda = open("agendatelefonica.csv",'a')
	#recupera o nome digitado na tela
	nome = input("Nome do Contato:")
	#recupera o telefone digitado na tela
	telefone = input("Digite o telefone:")	
	clear()
	print("------------------------------------------")	
	print("CONTATO SALVO COM SUCESSO!")
	print("------------------------------------------")	
	print("Nome\t\t\tTelefone")
	print(nome, "\t\t\t", telefone)
	agenda.write(nome)
	agenda.write(",")
	agenda.write(telefone)
	agenda.write("\n")
	agenda.close()
	opcoes()
	bemvindo()
	
def listar():
	clear()
	print("------------------------------------------")
	print("Lista de Contatos")
	print("------------------------------------------")	
	
	agenda = open("agendatelefonica.csv")
	for linha in agenda:		
		arr = linha.replace('\n','').split(",")
		nome = arr[0]
		telefone = arr[1]
		print (nome, "\t\t\t", telefone)
	agenda.close()
	opcoes()

def opcoes():
	input("Pressione Enter para voltar as opcoes...")
	bemvindo()

def falha():
	print("Opcao Incorreta")
	opcoes()
