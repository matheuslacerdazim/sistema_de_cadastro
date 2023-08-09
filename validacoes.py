from datetime import date

hoje = date.today()
dia_hoje = hoje.day  #Dia atual
mes_hoje = hoje.month  #Mês atual
ano_hoje = hoje.year  #Ano atual


def validar_nome(nome):
  """
  sobrenome: sobrenome a ser validado (str)
  Verifica se a str sobrenome tem apenas um sobrenome
  Retorna False se tiver mais que um sobrenome e True se tiver apenas um
  """

  return nome.isalpha()


def validar_cpf(cpf):
  """
  cpf: cpf a ser validado (str)
  Verificar se os dois digitos verificadores são válidos
  Retorna False se não forem válidos e True caso sejam válidos
  """

  if cpf == "":
    return False

  else:
    #1 - Verificação do primeiro digito verificador (penúltimo número)
    #Multiplica-se o primeiro número do cpf por 10, o segundo por 9 e assim por diante, até chegar no 9º número * 2
    #Depois soma-se todos os resultados
    conta1 = (int(cpf[0]) * 10) + \
             (int(cpf[1]) * 9) + \
             (int(cpf[2]) * 8) + \
             (int(cpf[3]) * 7) + \
             (int(cpf[4]) * 6) + \
             (int(cpf[5]) * 5) + \
             (int(cpf[6]) * 4) + \
             (int(cpf[7]) * 3) + \
             (int(cpf[8]) * 2)

    #Divide-se o resultado dessa soma por 11 para obter o resto
    resto1 = conta1 % 11

    #Se o resto for menor que 2 (0 ou 1) o primeiro digito verificador(10º número) deve ser 0
    if resto1 < 2 and cpf[9] != "0":
      return False

    #Se o resto for maior ou igual a 2, o primeiro digito verificador(10º número) deve ser 11 menos o resto
    elif resto1 >= 2 and cpf[9] != str(11 - resto1):
      return False

    else:      
      #2 - Verificação do segundo digito verificador (último número)
      #Multiplica-se o primeiro número do cpf por 11, o segundo por 10 e assim por diante, até chegar no 10º número *2
      conta2 = (int(cpf[0]) * 11) + \
               (int(cpf[1]) * 10) + \
               (int(cpf[2]) * 9) + \
               (int(cpf[3]) * 8) + \
               (int(cpf[4]) * 7) + \
               (int(cpf[5]) * 6) + \
               (int(cpf[6]) * 5) + \
               (int(cpf[7]) * 4) + \
               (int(cpf[8]) * 3) + \
               (int(cpf[9]) * 2)

      #Divide-se o resultado dessa soma por 11 para obter o resto
      resto2 = conta2 % 11

      #Se o resto for menor que 2 (0 ou 1) o primeiro digito verificador(10º número) deve ser 0
      if resto2 < 2 and cpf[10] != "0":
        return False

      #Se o resto for maior ou igual a 2, o segundo digito verificador(11º número) deve ser 11 menos o resto
      elif resto2 >= 2 and cpf[10] != str(11 - resto2):
        return False

      else:
        return True

        
def validar_nascimento(data_nasc):
  """
  data_nasc: data de nascimento a ser validada (str)
  Verificar se a data é valida, verificando se o mês informado tem o dia informado, e se a data não passa do dia atual
  Retorna a declaração de invalidade da data, caso essa exista, caso não  retorna True
  """

  #Caso nada seja inserido
  if data_nasc == "":
    return "\nNenhuma data inserida, repita a operação e insira uma data válida"

  #Caso tenha sido inserido algo, e esse algo for diferente de números nos campos de dia,mês e ano a operação sera encerada
  elif not data_nasc[:2].isdecimal() or not data_nasc[3:5].isdecimal(
  ) or not data_nasc[-4:].isdecimal():
    return "\nA data deve ser inserida no formato dd/mm/aaaa e deve conter apenas números \nRepita a operação e insira uma data válida"

  #Verificar se o mês informado possui o dia informado ou não

  #Janeiro
  elif int(data_nasc[3:5]) == 1 and int(data_nasc[:2]) > 31:
    return "Janeiro só vai até dia 31, repita a operação"

  #Fevereiro(ano bissexto)
  elif (int(data_nasc[3:5]) == 2) and (
    (int(data_nasc[-4:]) % 4 == 0 and int(data_nasc[-4:]) % 100 != 0)
      or int(data_nasc[-4:]) % 400 == 0) and (int(data_nasc[:2]) > 29):
    return "Em anos bissextos Fevereiro vai só até o dia 29, repita a operação"

  #Fevereiro(ano normal)
  elif int(data_nasc[3:5]) == 2 and int(data_nasc[:2]) > 28:
    return "Fevereiro só vai até o dia 28, repita a operação"

  #Março
  elif int(data_nasc[3:5]) == 3 and int(data_nasc[:2]) > 31:
    return "Março só vai até o dia 31, repita a operação"

  #Abril
  elif int(data_nasc[3:5]) == 4 and int(data_nasc[:2]) > 30:
    return "Abril só vai até o dia 30, repita a operação"

  #Maio
  elif int(data_nasc[3:5]) == 5 and int(data_nasc[:2]) > 31:
    return "Maio só vai até o dia 31, repita a operação"

  #Junho
  elif int(data_nasc[3:5]) == 6 and int(data_nasc[:2]) > 30:
    return "Junho só vai até o dia 30, repita a operação"

  #Julho
  elif int(data_nasc[3:5]) == 7 and int(data_nasc[:2]) > 31:
    return "Julho só vai até o dia 31, repita a operação"

  #Agosto
  elif int(data_nasc[3:5]) == 8 and int(data_nasc[:2]) > 31:
    return "Agosto só vai até o dia 31, repita a operação"

  #Setembro
  elif int(data_nasc[3:5]) == 9 and int(data_nasc[:2]) > 30:
    return "Setembro só vai até o dia 30, repita a operação"

  #Outubro
  elif int(data_nasc[3:5]) == 10 and int(data_nasc[:2]) > 31:
    return "Outubro só vai até o dia 31, repita a operação"

  #Novembro
  elif int(data_nasc[3:5]) == 11 and int(data_nasc[:2]) > 30:
    return "Novembro só vai até o dia 30, repita a operação"

  #Dezembro
  elif int(data_nasc[3:5]) == 12 and int(data_nasc[:2]) > 31:
    return "Dezembro só vai até o dia 31, repita a operação"

  #Verificar se há datas futuras

  #Se o ano for posterior ao ano atual
  elif int(data_nasc[-4:]) > ano_hoje:
    return "\nNão estamos aceitando cadastros de viajantes do tempo no momento"

  #Se o ano for o atual mas o mês for posterior ao mês atual
  elif int(data_nasc[-4:]) == ano_hoje and int(data_nasc[3:5]) > mes_hoje:
    return "\nNão estamos aceitando cadastros de viajantes do tempo no momento"

  #Se o ano for o atual e o mês também, será válido somente se o dia do nascimento for menor que o dia atual
  elif int(data_nasc[-4:]) == ano_hoje and int(
      data_nasc[3:5]) == mes_hoje and dia_hoje < int(data_nasc[:2]):
    return "\nNão estamos aceitando cadastros de viajantes do tempo no momento"

  else:
    return True
