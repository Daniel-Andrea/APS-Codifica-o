#atividade A
print('Atividade letra A')
numero = 16
def dobro(numero):
    return numero * 2
def triplo(numero):
    return numero * 3
def quadruplo(numero):
    return numero * 4
def quintuplo(numero):
    return numero * 5
def resultados():
    nmr_dobro = dobro(numero)
    nmr_triplo= triplo(numero )
    nmr_quadrado = quadruplo(numero)
    nmr_quintuplo = quintuplo(numero)
    print(f'dobro: {nmr_dobro}')
    print(f'triplo: {nmr_triplo}')
    print(f'quadruplo: {nmr_quadrado}')
    print(f'quintuplo: {nmr_quintuplo}')
resultados()
print('\n')

#atividade B
print('Atividade letra B')
def aplicar_desconto(preco, desconto):
  return preco - (preco * desconto / 100)

def verificação():
  precos = [10.0, 20.0, 30.0, 40.0, 50.0, 60.0]
  descontos = [3.0, 3.5, 4.2, 4.75, 5.12, 5.23]

  for preco, desconto in zip(precos, descontos):
    preco_desconto = aplicar_desconto(preco, desconto)
    print(f"O preço do item com desconto é R${preco_desconto:.2f}")
verificação()
print('\n')


#atividade c
print('Atividade letra C')
ano = 2019
def calcular_idade(nascimento):
    idade = ano - nascimento
    return idade

def verificarIdade(idade):
    if idade < 18:
        print('A idade é menor que 18')
    elif idade <= 30:
        print('A idade é menor ou igual a 30')
    elif idade <= 50:
        print('A idade é menor ou igual a 50')
    elif idade <= 80:
        print('A idade é menor ou igual a 80')

while (True):
    nascimento= int(input("Digite o ano que nasceu, se desejar para é só digitar 0000:   "))
    if nascimento == 0000:
        break
    idade = calcular_idade(nascimento)
    verificarIdade(idade)
print('\n')

#atividade D
print('Atividade letra D')
def operacao():
    resultado = 1-2+3-4+5-6+7-8+9-10
    return print(resultado)
operacao()
print('\n')

#atividade E
print('Ativdade letra E')
def operacao2():
    resultado2 = (1/10) - (1/9) + (1/7) + (1/6) - (1/5) + (1/4) - (1/3) + (1/2) - (1/1)
    return print(resultado2)
operacao2()
print('\n')

#atividade F
print('Atividade letra F')
def operacao3():
    resultado3 = 1/10 - 2/9 + 3/8 - 4/7 + 5/6 - 6/5 + 7/4 - 8/3 + 9/2 - 10/1

    return print(resultado3)
operacao3()
print('\n')

#atividade G
print('Atividade letra G')










    