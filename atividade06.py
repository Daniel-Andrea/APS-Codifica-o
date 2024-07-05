#Atividade A
print('Atividade letra A')
fixo = 50
hora = 18
total = 0
def ganhoSemanal(total,hora, fixo):
    total = (4*hora)*5+fixo
    return total
    
salario = ganhoSemanal(total,hora,fixo)
print(salario)
print('\n')

#atividade b
print('Atividade letra B')

def orçamento1(diárias):
  return 220 + 129 * diárias

def orçamento2(diárias):
  return 173 + 162 * diárias

diárias = int(input("Informe o número de diárias: "))

if orçamento1(diárias) < orçamento2(diárias):
  print("O orçamento 1 é mais barato.")
elif orçamento1(diárias) > orçamento2(diárias):
  print("O orçamento 2 é mais barato.")
else:
  print("Os dois orçamentos são iguais.")
print('\n')

#atividade C
print('Atividade letra c')
def juros(valor, meses):
  return valor * (1 + 0.03) ** meses
print("Valor com juros após 1 mês:", juros(134, 1))
print("Valor com juros após 3 meses:", juros(134, 3))

meses = 0
while juros(134, meses) < 160:
  meses += 1
print("A conta ultrapassará R$ 160,00 em", meses, "meses.")

meses = 0
while juros(134, meses) < 268:
  meses += 1
print("O valor dobrará em", meses, "meses.")
print('\n')

#atividade D
print('Atividade letra D')
def liquido(bruto):
  if bruto <= 1100:
    inss = bruto * 0.075
  elif bruto <= 2203.48:
    inss = bruto * 0.09
  elif bruto <= 3305.22:
    inss = bruto * 0.12
  elif bruto <= 6433.57:
    inss = bruto * 0.14
  else:
    inss = bruto * 0.15

  if bruto <= 1903.98:
    ir = 0
  elif bruto <= 2826.65:
    ir = (bruto - 1903.98) * 0.075
  elif bruto <= 3751.05:
    ir = (bruto - 2826.65) * 0.15
  elif bruto <= 4664.68:
    ir = (bruto - 3751.05) * 0.225
  else:
    ir = (bruto - 4664.68) * 0.275

  liquido = bruto - inss - ir

  return liquido
bruto = float(input("Informe o salário bruto: "))
print("O salário líquido é de R$", liquido(bruto))
print('\n')

#atividade E
print('Atividade letra E')

    