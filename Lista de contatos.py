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
def editar_contato(contatos, indice_contato, novo_nome):
  ver_contatos(contatos)
  if indice_contato_ajustado >= 0 and indice_contato_ajustado < len(contatos):
    indice_contato_ajustado = int(indice_contato) - 1
    contatos[indice_contato]["contato"] = novo_nome
  else:
    print("indíce de tarefa inválido.")
  return

#Função item 4
def marcar_desamrcar_fav(contatos, indice_contato):
  indice_contato_ajustado = int(indice_contato) - 1   
  if 0<=indice_contato_ajustado<len(contatos):
      contatos[indice_contato_ajustado]["Favorito"] = not contatos[indice_contato_ajustado]["Favorito"]
      print(f"contato {indice_contato} agora foi atualizado.")
  else: 
    print("indice do contato inválido")
  return

#Função item 5
def contatos_fav(status):
  if status == "⋆":
    
    
 

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
    indice_contato = input("digite o número do contato que voce quer editar: ")
    novo_nome = input("digite o novo nome:")
    editar_contato(contatos, indice_contato, novo_nome)
    print(f"O contato {indice_contato} foi atualizado com sucesso para {novo_nome}!")

  elif escolha == "4":
    ver_contatos(contatos)
    indice_contato = input("selecione o numero do contato que você quer favoritar ou desfavoritar: ")
    marcar_desamrcar_fav(contatos, indice_contato)

  elif escolha == "7":
   break
print("programa finalizado!")