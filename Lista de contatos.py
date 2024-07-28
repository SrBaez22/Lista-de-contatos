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

  elif escolha == "7":
   break
print("programa finalizado!")