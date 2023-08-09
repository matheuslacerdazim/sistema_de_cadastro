from funcionalidades import insere_cadastro, altera_cpf, troca_sobrenomes, remove_cadastro, exibe_cadastros

def menu() :
  
  print("""
  Escolha a opção desejada: 
  1 - Realizar cadastro
  2 - Alterar CPF
  3 - Trocar sobrenomes
  4 - Remover cadastro
  5 - Listar cadastros
  6 - Encerrar  
  """)

  return input("-> ")

cadastros = []

while True:
  
  opcao = menu()
  
  if opcao == "1" :
    print(insere_cadastro(cadastros))
          
  elif opcao == "2" :
    print(altera_cpf(cadastros))

  elif opcao == "3" :
    print(troca_sobrenomes(cadastros))

  elif opcao == "4" :
    print(remove_cadastro(cadastros))

  elif opcao == "5" :
    exibe_cadastros(cadastros)
    
  elif opcao == '6': # Encerrar    
    print('\nAté logo!')
    break
    
  else:  # Opção inexistente
    print('\nOpção inválida') 
