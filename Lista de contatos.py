#Função do item 1
def adicionar_contatos(contatos, nome_contato):
  contato = {"contato":nome_contato, "Favorito": False}
  contatos.append(contato)
  print(f"O contato {nome_contato} foi adicionado com sucesso!")
  return

#Função do item 2
def ver_contatos(contatos):
  print("\nLista de contatos: ")
  for indice, contato in enumerate(contatos, start=1):
    status = "⋆" if contato["Favorito"] else " "
    nome_contato = contato["contato"]
    print(f"{indice}. [{status}] {nome_contato}")
  return

#Função item 3
def editar_contato(contatos):
  ver_contatos(contatos)
  indice = int(input("\nDigite o número do contato que deseja editar: "))
  if 1 <= indice <= len(contatos):
    novo_nome = input("Digite o novo nome do contato: ")
    contatos[indice - 1]["contato"] = novo_nome
    print(f"O contato {indice} foi atualizado com sucesso para {novo_nome}!")

#Função item 4
def marcar_desamrcar_fav(contatos):

  return

#Função item 5
def contatos_fav():
  return

#Função item 6
def deletar_contato():
  return

contatos = []
while True: 
  print("\nMenu da lista de contatos")
  print("1. Adicionar um contato")
  print("2. Visualizar lista de contatos cadastrados")
  print("3. Editar um contato")
  print("4. Marcar ou desmarcar um contato como favorito")
  print("5. Ver lista de contatos favoritos")
  print("6. Deletar um contato")
  print("7. Sair")
  
  escolha = input("Digite sua escolha: ")
  if escolha == "1":
    nome_contato = input("Digite o nome do contato: ")
    adicionar_contatos(contatos, nome_contato)

  elif escolha == "2":
    ver_contatos(contatos)
  
  elif escolha == "3":
    editar_contato(contatos)

  elif escolha == "4":
    marcar_desamrcar_fav()

  elif escolha == "7":
   break
print("programa finalizado!")