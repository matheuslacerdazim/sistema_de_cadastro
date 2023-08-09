from validacoes import validar_nome, validar_cpf, validar_nascimento
from datetime import date

hoje = date.today()
dia_hoje = hoje.day  #Dia atual
mes_hoje = hoje.month  #Mês atual
ano_hoje = hoje.year  #Ano atual


def insere_cadastro(cadastros):
  """
  cadastros: lista que armazena todos os cadastros (list)
  Insere os dados do cadastro: nome + sobrenome, cpf e data de nascimento na lista cadastros.
  Retorna apenas mensagens de erro caso haja algo inválido, caso contrario apenas armazena o cadastro.
  """

  #Nome
  nome = input("\nPrimeiro nome: ").capitalize()
  sobrenome = input("Sobrenome: ").capitalize()

  if not validar_nome(nome) or not validar_nome(sobrenome):
    return "\nNome inválido."

  nome += " " + sobrenome

  #Cpf
  cpf = input("Cpf: 11 digitos (sem - ou .) : ")
  if not validar_cpf(cpf):
    return "\nCpf inválido"

  #Data de nascimento
  data_nasc = input("Data de nascimento (dd/mm/aa): ")
  if not validar_nascimento(data_nasc) is True:
    return validar_nascimento(data_nasc)

  def calcular_idade_em_dias(data_nasc):
    """
    data_nasc: data de nascimeto informada (str)
    Calcula a idade da pessoa em dias, levando em conta anos bissextos
    Retorna a idade em dias
    """
    #Armazenar quantos dias cada mês tem para armazenar os valores corretamente à <idade_dias>
    jan = 31
    fev = 28
    mar = 31
    abr = 30
    mai = 31
    jun = 30
    jul = 31
    ago = 31
    set = 30
    out = 31
    nov = 30
    dez = 31

    #Pegar a data de nascimento de cada usuário cadastrado e separar por dia mes e ano
    dia_nasc = int(data_nasc[:2])  #Dia de nascimento
    mes_nasc = int(data_nasc[3:5])  #Mês de nascimento
    ano_nasc = int(data_nasc[-4:])  #Ano de nascimento

    idade_dias = 0

    #Diferença de anos entre o ano atual e o ano de nascimento / +1 para iterar até o ano atual, pois sem +1 estava iterando somente até 2022
    dif_anos = (ano_hoje - ano_nasc) + 1

    #Lista <anos> com cada ano desde o nascimento até o ano atual
    ano = ano_nasc
    anos = []
    for i in range(dif_anos):
      anos.append(ano)
      ano += 1

    #Armazenar os dias à <idade_dias>

    #A - Se o ano de nascimento for o mesmo que o atual
    if dif_anos == 1:

      #Se o mês atual for:

      #Dezembro
      if mes_hoje == 12 and mes_nasc == 12:
        idade_dias = dia_hoje - dia_nasc
        return idade_dias

      elif mes_hoje == 12 and mes_nasc == 11:
        idade_dias = dia_hoje + (nov - dia_nasc)
        return idade_dias

      elif mes_hoje == 12 and mes_nasc == 10:
        idade_dias = dia_hoje + nov + (out - dia_nasc)
        return idade_dias

      elif mes_hoje == 12 and mes_nasc == 9:
        idade_dias = dia_hoje + nov + out + (set - dia_nasc)
        return idade_dias

      elif mes_hoje == 12 and mes_nasc == 8:
        idade_dias = dia_hoje + nov + out + set + (ago - dia_nasc)
        return idade_dias

      elif mes_hoje == 12 and mes_nasc == 7:
        idade_dias = dia_hoje + nov + out + set + ago + (jul - dia_nasc)
        return idade_dias

      elif mes_hoje == 12 and mes_nasc == 6:
        idade_dias = dia_hoje + nov + out + set + ago + jul + (jun - dia_nasc)
        return idade_dias

      elif mes_hoje == 12 and mes_nasc == 5:
        idade_dias = dia_hoje + nov + out + set + ago + jul + jun + (mai -
                                                                     dia_nasc)
        return idade_dias

      elif mes_hoje == 12 and mes_nasc == 4:
        idade_dias = dia_hoje + nov + out + set + ago + jul + jun + mai + (
          abr - dia_nasc)
        return idade_dias

      elif mes_hoje == 12 and mes_nasc == 3:
        idade_dias = dia_hoje + nov + out + set + ago + jul + jun + mai + abr + (
          mar - dia_nasc)
        return idade_dias

      elif mes_hoje == 12 and mes_nasc == 2:
        idade_dias = dia_hoje + nov + out + set + ago + jul + jun + mai + abr + mar + (
          fev - dia_nasc)
        return idade_dias

      elif mes_hoje == 12 and mes_nasc == 1:
        idade_dias = dia_hoje + nov + out + set + ago + jul + jun + mai + abr + mar + fev + (
          jan - dia_nasc)
        return idade_dias

      #Novembro
      if mes_hoje == 11 and mes_nasc == 11:
        idade_dias = dia_hoje - dia_nasc
        return idade_dias

      elif mes_hoje == 11 and mes_nasc == 10:
        idade_dias = dia_hoje + (out - dia_nasc)
        return idade_dias

      elif mes_hoje == 11 and mes_nasc == 9:
        idade_dias = dia_hoje + out + (set - dia_nasc)
        return idade_dias

      elif mes_hoje == 11 and mes_nasc == 8:
        idade_dias = dia_hoje + out + set + (ago - dia_nasc)
        return idade_dias

      elif mes_hoje == 11 and mes_nasc == 7:
        idade_dias = dia_hoje + out + set + ago + (jul - dia_nasc)
        return idade_dias

      elif mes_hoje == 11 and mes_nasc == 6:
        idade_dias = dia_hoje + out + set + ago + jul + (jun - dia_nasc)
        return idade_dias

      elif mes_hoje == 11 and mes_nasc == 5:
        idade_dias = dia_hoje + out + set + ago + jul + jun + (mai - dia_nasc)
        return idade_dias

      elif mes_hoje == 11 and mes_nasc == 4:
        idade_dias = dia_hoje + out + set + ago + jul + jun + mai + (abr -
                                                                     dia_nasc)
        return idade_dias

      elif mes_hoje == 11 and mes_nasc == 3:
        idade_dias = dia_hoje + out + set + ago + jul + jun + mai + abr + (
          mar - dia_nasc)
        return idade_dias

      elif mes_hoje == 11 and mes_nasc == 2:
        idade_dias = dia_hoje + out + set + ago + jul + jun + mai + abr + mar + (
          fev - dia_nasc)
        return idade_dias

      elif mes_hoje == 11 and mes_nasc == 1:
        idade_dias = dia_hoje + out + set + ago + jul + jun + mai + abr + mar + fev + (
          jan - dia_nasc)
        return idade_dias

      #Outubro
      if mes_hoje == 10 and mes_nasc == 10:
        idade_dias = dia_hoje - dia_nasc
        return idade_dias

      elif mes_hoje == 10 and mes_nasc == 9:
        idade_dias = dia_hoje + (set - dia_nasc)
        return idade_dias

      elif mes_hoje == 10 and mes_nasc == 8:
        idade_dias = dia_hoje + set + (ago - dia_nasc)
        return idade_dias

      elif mes_hoje == 10 and mes_nasc == 7:
        idade_dias = dia_hoje + set + ago + (jul - dia_nasc)
        return idade_dias

      elif mes_hoje == 10 and mes_nasc == 6:
        idade_dias = dia_hoje + set + ago + jul + (jun - dia_nasc)
        return idade_dias

      elif mes_hoje == 10 and mes_nasc == 5:
        idade_dias = dia_hoje + set + ago + jul + jun + (mai - dia_nasc)
        return idade_dias

      elif mes_hoje == 10 and mes_nasc == 4:
        idade_dias = dia_hoje + set + ago + jul + jun + mai + (abr - dia_nasc)
        return idade_dias

      elif mes_hoje == 10 and mes_nasc == 3:
        idade_dias = dia_hoje + set + ago + jul + jun + mai + abr + (mar -
                                                                     dia_nasc)
        return idade_dias

      elif mes_hoje == 10 and mes_nasc == 2:
        idade_dias = dia_hoje + set + ago + jul + jun + mai + abr + mar + (
          fev - dia_nasc)
        return idade_dias

      elif mes_hoje == 10 and mes_nasc == 1:
        idade_dias = dia_hoje + set + ago + jul + jun + mai + abr + mar + fev + (
          jan - dia_nasc)
        return idade_dias

      #Setembro
      if mes_hoje == 9 and mes_nasc == 9:
        idade_dias = dia_hoje - dia_nasc
        return idade_dias

      elif mes_hoje == 9 and mes_nasc == 8:
        idade_dias = dia_hoje + (ago - dia_nasc)
        return idade_dias

      elif mes_hoje == 9 and mes_nasc == 7:
        idade_dias = dia_hoje + ago + (jul - dia_nasc)
        return idade_dias

      elif mes_hoje == 9 and mes_nasc == 6:
        idade_dias = dia_hoje + ago + jul + (jun - dia_nasc)
        return idade_dias

      elif mes_hoje == 9 and mes_nasc == 5:
        idade_dias = dia_hoje + ago + jul + jun + (mai - dia_nasc)
        return idade_dias

      elif mes_hoje == 9 and mes_nasc == 4:
        idade_dias = dia_hoje + ago + jul + jun + mai + (abr - dia_nasc)
        return idade_dias

      elif mes_hoje == 9 and mes_nasc == 3:
        idade_dias = dia_hoje + ago + jul + jun + mai + abr + (mar - dia_nasc)
        return idade_dias

      elif mes_hoje == 9 and mes_nasc == 2:
        idade_dias = dia_hoje + ago + jul + jun + mai + abr + mar + (fev -
                                                                     dia_nasc)
        return idade_dias

      elif mes_hoje == 9 and mes_nasc == 1:
        idade_dias = dia_hoje + ago + jul + jun + mai + abr + mar + fev + (
          jan - dia_nasc)
        return idade_dias

      #Agosto
      if mes_hoje == 8 and mes_nasc == 8:
        idade_dias = dia_hoje - dia_nasc
        return idade_dias

      elif mes_hoje == 8 and mes_nasc == 7:
        idade_dias = dia_hoje + (jul - dia_nasc)
        return idade_dias

      elif mes_hoje == 8 and mes_nasc == 6:
        idade_dias = dia_hoje + jul + (jun - dia_nasc)
        return idade_dias

      elif mes_hoje == 8 and mes_nasc == 5:
        idade_dias = dia_hoje + jul + jun + (mai - dia_nasc)
        return idade_dias

      elif mes_hoje == 8 and mes_nasc == 4:
        idade_dias = dia_hoje + jul + jun + mai + (abr - dia_nasc)
        return idade_dias

      elif mes_hoje == 8 and mes_nasc == 3:
        idade_dias = dia_hoje + jul + jun + mai + abr + (mar - dia_nasc)
        return idade_dias

      elif mes_hoje == 8 and mes_nasc == 2:
        idade_dias = dia_hoje + jul + jun + mai + abr + mar + (fev - dia_nasc)
        return idade_dias

      elif mes_hoje == 8 and mes_nasc == 1:
        idade_dias = dia_hoje + jul + jun + mai + abr + mar + fev + (jan -
                                                                     dia_nasc)
        return idade_dias

      #Julho
      if mes_hoje == 7 and mes_nasc == 7:
        idade_dias = dia_hoje - dia_nasc
        return idade_dias

      elif mes_hoje == 7 and mes_nasc == 6:
        idade_dias = dia_hoje + (jun - dia_nasc)
        return idade_dias

      elif mes_hoje == 7 and mes_nasc == 5:
        idade_dias = dia_hoje + jun + (mai - dia_nasc)
        return idade_dias

      elif mes_hoje == 7 and mes_nasc == 4:
        idade_dias = dia_hoje + jun + mai + (abr - dia_nasc)
        return idade_dias

      elif mes_hoje == 7 and mes_nasc == 3:
        idade_dias = dia_hoje + jun + mai + abr + (mar - dia_nasc)
        return idade_dias

      elif mes_hoje == 7 and mes_nasc == 2:
        idade_dias = dia_hoje + jun + mai + abr + mar + (fev - dia_nasc)
        return idade_dias

      elif mes_hoje == 7 and mes_nasc == 1:
        idade_dias = dia_hoje + jun + mai + abr + mar + fev + (jan - dia_nasc)
        return idade_dias

      #Junho
      if mes_hoje == 6 and mes_nasc == 6:
        idade_dias = dia_hoje - dia_nasc
        return idade_dias

      elif mes_hoje == 6 and mes_nasc == 5:
        idade_dias = dia_hoje + (mai - dia_nasc)
        return idade_dias

      elif mes_hoje == 6 and mes_nasc == 4:
        idade_dias = dia_hoje + mai + (abr - dia_nasc)
        return idade_dias

      elif mes_hoje == 6 and mes_nasc == 3:
        idade_dias = dia_hoje + mai + abr + (mar - dia_nasc)
        return idade_dias

      elif mes_hoje == 6 and mes_nasc == 2:
        idade_dias = dia_hoje + mai + abr + mar + (fev - dia_nasc)
        return idade_dias

      elif mes_hoje == 6 and mes_nasc == 1:
        idade_dias = dia_hoje + mai + abr + mar + fev + (jan - dia_nasc)
        return idade_dias

      #Maio
      if mes_hoje == 5 and mes_nasc == 5:
        idade_dias = dia_hoje - dia_nasc
        return idade_dias

      elif mes_hoje == 5 and mes_nasc == 4:
        idade_dias = dia_hoje + (abr - dia_nasc)
        return idade_dias

      elif mes_hoje == 5 and mes_nasc == 3:
        idade_dias = dia_hoje + abr + (mar - dia_nasc)
        return idade_dias

      elif mes_hoje == 5 and mes_nasc == 2:
        idade_dias = dia_hoje + abr + mar + (fev - dia_nasc)
        return idade_dias

      elif mes_hoje == 5 and mes_nasc == 1:
        idade_dias = dia_hoje + abr + mar + fev + (jan - dia_nasc)
        return idade_dias

      #Abril
      if mes_hoje == 4 and mes_nasc == 4:
        idade_dias = dia_hoje - dia_nasc
        return idade_dias

      elif mes_hoje == 4 and mes_nasc == 3:
        idade_dias = dia_hoje + (mar - dia_nasc)
        return idade_dias

      elif mes_hoje == 4 and mes_nasc == 2:
        idade_dias = dia_hoje + mar + (fev - dia_nasc)
        return idade_dias

      elif mes_hoje == 4 and mes_nasc == 1:
        idade_dias = dia_hoje + mar + fev + (jan - dia_nasc)
        return idade_dias

      #Março
      if mes_hoje == 3 and mes_nasc == 3:
        idade_dias = dia_hoje - dia_nasc
        return idade_dias

      elif mes_hoje == 3 and mes_nasc == 2:
        idade_dias = dia_hoje + (fev - dia_nasc)
        return idade_dias

      elif mes_hoje == 3 and mes_nasc == 1:
        idade_dias = dia_hoje + fev + (jan - dia_nasc)
        return idade_dias

      #Fevereiro
      if mes_hoje == 2 and mes_nasc == 2:
        idade_dias = dia_hoje - dia_nasc
        return idade_dias

      elif mes_hoje == 2 and mes_nasc == 1:
        idade_dias = dia_hoje + (jan - dia_nasc)
        return idade_dias

      #Janeiro
      if mes_hoje == 1 and mes_nasc == 1:
        idade_dias = dia_hoje - dia_nasc
        return idade_dias

    #B - Se o ano de nascimento não for o mesmo que o atual
    elif dif_anos > 1:
      for j in range(dif_anos):
        #Divide o iterador em 3 partes :
        #1 - O primeiro ano : para saber quantos dias de idade o usuário tem desde a data do nascimento até o fim daquele ano
        #2 - Os anos entre o ano de nascimento e o ano atual : para somar 365 dias ou 366 caso seja ano bissexto
        #3 - O ano atual : para saber quantos dias de idade o usuário tem desde o começo do ano até a data atual

        #1 - Primeiro ano
        if j == range(dif_anos)[0]:

          #Janeiro
          if mes_nasc == 1:
            idade_dias += (
              jan - dia_nasc
            ) + fev + mar + abr + mai + jun + jul + ago + set + out + nov + dez

          #Fevereiro
          elif mes_nasc == 2:
            idade_dias += (
              fev - dia_nasc
            ) + mar + abr + mai + jun + jul + ago + set + out + nov + dez

          #Março
          elif mes_nasc == 3:
            idade_dias += (
              mar -
              dia_nasc) + abr + mai + jun + jul + ago + set + out + nov + dez

          #Abril
          elif mes_nasc == 4:
            idade_dias += (
              abr - dia_nasc) + mai + jun + jul + ago + set + out + nov + dez

          #Maio
          elif mes_nasc == 5:
            idade_dias += (mai -
                           dia_nasc) + jun + jul + ago + set + out + nov + dez

          #Junho
          elif mes_nasc == 6:
            idade_dias += (jun - dia_nasc) + jul + ago + set + out + nov + dez

          #Julho
          elif mes_nasc == 7:
            idade_dias += (jul - dia_nasc) + ago + set + out + nov + dez

          #Agosto
          elif mes_nasc == 8:
            idade_dias += (ago - dia_nasc) + set + out + nov + dez

          #Setembro
          elif mes_nasc == 9:
            idade_dias += (set - dia_nasc) + out + nov + dez

          #Outubro
          elif mes_nasc == 10:
            idade_dias += (out - dia_nasc) + nov + dez
          #Novembro
          elif mes_nasc == 11:
            idade_dias += (nov - dia_nasc) + dez

          #Dezembro
          elif mes_nasc == 12:
            idade_dias += dez - dia_nasc

          #Se o ano é bissexto e o nascimento foi antes de março, soma mais um
          if ((ano_nasc % 4 == 0 and ano_nasc % 100 != 0)
              or ano_nasc % 400 == 0) and mes_nasc < 3:
            idade_dias += 1

        #2 - Anos entre o ano de nascimento e o ano atual que sejam bissextos / Anos entre o ano de nascimento e o atual normais
        if j > range(dif_anos)[0] and j < range(dif_anos)[-1] and (
            anos[j] % 4 == 0 and anos[j] % 100 != 0) or anos[j] % 400 == 0:
          idade_dias += 366

        elif j > range(dif_anos)[0] and j < range(dif_anos)[-1]:
          idade_dias += 365

        #3 - Ano atual
        if j == range(dif_anos)[-1]:

          #Janeiro
          if mes_hoje == 1:
            idade_dias += dia_hoje

          #Fevereiro
          elif mes_hoje == 2:
            idade_dias += jan + dia_hoje

          #Março
          elif mes_hoje == 3:
            idade_dias += jan + fev + dia_hoje

          #Abril
          elif mes_hoje == 4:
            idade_dias += jan + fev + mar + dia_hoje

          #Maio
          elif mes_hoje == 5:
            idade_dias += jan + fev + mar + abr + dia_hoje

          #Junho
          elif mes_hoje == 6:
            idade_dias += jan + fev + mar + abr + mai + dia_hoje

          #Julho
          elif mes_hoje == 7:
            idade_dias += jan + fev + mar + abr + mai + jun + dia_hoje

          #Agosto
          elif mes_hoje == 8:
            idade_dias += jan + fev + mar + abr + mai + jun + jul + dia_hoje

          #Setembro
          elif mes_hoje == 9:
            idade_dias += jan + fev + mar + abr + mai + jun + jul + ago + dia_hoje

          #Outrubro
          elif mes_hoje == 10:
            idade_dias += jan + fev + mar + abr + mai + jun + jul + ago + set + dia_hoje

          #Novembro
          elif mes_hoje == 11:
            idade_dias += jan + fev + mar + abr + mai + jun + jul + ago + set + out + dia_hoje

          #Dezembro
          elif mes_hoje == 12:
            idade_dias += jan + fev + mar + abr + mai + jun + jul + ago + set + out + nov + dia_hoje

          if ((ano_hoje % 4 == 0 and ano_hoje % 100 != 0)
              or ano_hoje % 400 == 0) and mes_nasc > 2:
            idade_dias += 1
      return idade_dias

  idade_em_dias = calcular_idade_em_dias(data_nasc)

  cadastro = {
    "id": len(cadastros) + 1,
    "nome": nome,
    "cpf": cpf,
    "data_nasc": data_nasc,
    "idade_em_dias": f"{idade_em_dias} dias",
  }

  cadastros.append(cadastro)

  return "\nCadastro Completo."


def altera_cpf(cadastros):
  """
  cadastros: lista que armazena todos os cadastros(list)
  Pega o id do cadastro a ser alterado e altera o cpf
  Retorna as situações de invalidade do id e do cpf,caso sejam inválidos, caso contrario altera o cpf e retorna a mensagem de sucesso na alteração 
  """

  #Verificação do id, se existe ou não nos cadastros
  id = int(input("\nId do cadastro que deseja efetuar a alteração: "))
  if id > len(cadastros):
    return "\nInsira um id válido"
  
  else:
    novo_cpf = input("Insira o novo Cpf: 11 digitos (sem - ou .) : ")

    if not validar_cpf(novo_cpf):
      return "\n Cpf inválido."

    else:
      cadastros[id - 1]["cpf"] = novo_cpf
      return "\nCpf alterado com sucesso."

      
def troca_sobrenomes(cadastros):
  """
  cadastros: lista que armazena todos os cadastros (list)
  Pega os ids dos dois cadastros desejados e troca os sobrenomes entre eles
  Retorna a mensagem de invalidade do id caso algum dos ids não existe, caso contrario retorna a mensagem de sucesso na alteração
  """
  
  id1 = int(input("\nInsira o id que possui o primeiro sobrenome desejado: "))
  id2 = int(input("Insira o id que possui o segundo sobrenome desejado: "))

  if id1 > len(cadastros) or id2 > len(cadastros):
    return "\nAlgum dos ids é inválido, escolha um id correspondente a um cadastro existente."

  else:
    #Procura os espaços em branco que simbolizam o meio do nome e usa-os para dividir entre nome e sobrenome
    
    meio1 = cadastros[id1 - 1]["nome"].find(" ")
    nome1 = cadastros[id1 - 1]["nome"][:meio1]
    sobrenome1 = cadastros[id1 - 1]["nome"][meio1 + 1:]

    meio2 = cadastros[id2 - 1]["nome"].find(" ")
    nome2 = cadastros[id2 - 1]["nome"][:meio2]
    sobrenome2 = cadastros[id2 - 1]["nome"][meio2 + 1:]

    cadastros[id1 - 1]["nome"] = nome1 + " " + sobrenome2
    cadastros[id2 - 1]["nome"] = nome2 + " " + sobrenome1

    return "\nSobrenomes alterados com sucesso."


def remove_cadastro(cadastros):
  """
  cadastros: lista que armazena todos os cadastros (list)
  Pega o id do cadastro que se deseja remover e remove-o da lista de cadastros
  Retorna a mensagem de invalidade de id caso o id seja invalido, caso contrario retorna a mensagem de sucesso na remoção
  """

  id = int(input("\nInsira o id do cadastro que deseja remover."))
  if id > len(cadastros):
    return "\nid inválido, escolha um id correspondente a um cadastro existente."

  else:
    cadastros.remove(cadastros[id - 1])

    #loop para reorganizar os ids da lista de cadastros, visto que removido um cadastro havera uma lacuna
    novo_id = 1
    for cadastro in cadastros:
      cadastro["id"] = novo_id
      novo_id += 1

    return "\nCadastro removido com sucesso."


def exibe_cadastros(cadastros):
  """
  cadastros: lista que armazena todos os cadastros (list)
  Apenas exibe cada cadastro, um por um
  """

  for cadastro in cadastros:
    for chave, valor in cadastro.items():
      print(f"{chave}: {valor}")
    print()
