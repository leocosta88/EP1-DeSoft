# -*- coding: utf-8 -*-
"""
Created on Thu Oct  4 17:55:21 2018

@author: leo72
"""
import json





try:
    with open('cardapio.txt','r') as cardapio:
        cardapio = json.loads(cardapio.read())
    with open('comanda.txt','r') as comanda:
        comanda = json.loads(comanda.read())
    
except: 
    FileNotFoundError

cardapio = {}
mesa = {}


while0 = True
while while0:
   print('0 - Sair')
   print('1 - Cardapio')
   print('2 - Comanda')
   y = int(input('Faça a sua Escolha:'))
   if y == 0:
       print("Até Mais!")
       while0 = False
       break
   elif y == 1:
       card = True
       while card:
        print('Cardapio Eletronica')
        print('0 - Voltar')
        print('1 - Imprimir Cardapio')
        print('2 - Adicionar Item')
        print('3 - Remover Item')
        x = int(input('Faça sua Escolha: '))
        while2 = True
        while while2:
            if x == 0:
                card = False
                break
            elif x == 1:            
                for produto,preço in cardapio.items():
                    print('{0} : R${1:.2f}'.format(produto,preço))
                    print()
                break
            elif x == 2:
                prod = input('Nome do Produto: ')
                preç = float(input("Preço Desejado: "))
                if preç > 0:     
                    if prod not in cardapio:
                        cardapio[prod] = preç
                    else:
                        cardapio[prod] += preç
                else:
                    print('Não é possível adicionar preço negativa.')
                break
            elif x == 3:
                nomezin = input('Nome do Produto: ')
                precin = float(input('Preço desejado a retirar: '))
                if nomezin not in cardapio:
                    print('Não é possível retirar um item não existente.')
                else:
                    if cardapio[nomezin] - precin <= 0:
                        del cardapio[nomezin]
                    else:
                        cardapio[nomezin] -= precin
                break
   elif y == 2:
     primeiro = True
     while primeiro:
         num = int(input('Digite o numero da sua mesa:'))
         if num > 0:
             comanda = {}
             if num in mesa:
                 mesa[num] = comanda
                 while1 = True
                 while while1:
                     print('Comanda Eletronica')
                     print('0 - Voltar')
                     print('1 - Adicionar Item')
                     print('2 - Remover Item')
                     print('3 - Imprimir Comanda')
                     x = int(input('Faça sua Escolha: '))
                     while2 = True
                     while while2:
                         if x == 0:
                             while1 = False
                             primeiro = False
                             break
                         elif x == 1:
                             prod = input('Nome do Produto: ')
                             if prod in cardapio:
                                 pedidos = int(input("Quantidade Desejada: ")) 
                                 if pedidos > 0:     
                                     if prod not in comanda:
                                         comanda[prod] = pedidos
                                     else:
                                         comanda[prod] += pedidos
                                 else:
                                     print('Não é possível adicionar quantidade negativa')
                             else:
                                 print('Produto não está no cardápio')
                             break
                         elif x == 2:
                             nomezin = input('Nome do Produto: ')
                             quantidadezin = int(input('Quantidade desejada a retirar: '))      
                             if nomezin not in comanda:
                                 print('Não é possível retirar um item não existente')
                             else:
                                 if comanda[nomezin] - quantidadezin <= 0:
                                     del comanda[nomezin]
                                 else:
                                     comanda[nomezin] -= quantidadezin
                                 break
                         elif x == 3:
                             total = 0
                             conta = 0
                             print('Mesa {0}:'.format(num))
                             print()
                             for e in comanda:
                                 total += cardapio[e]*comanda[e]
                                 print('{0}: Preço Unitário: R${1:.2f}; Preço Total: R${2:.2f}'.format(e,cardapio[e],cardapio[e]*comanda[e]))
                             conta = total*1.1
                             print('Valor total com 10% de taxa de serviço: R${0:.2f}'.format(conta))
                             break         
             else:
                 print('Número de mesa inválido')

                            
                            
                
atualizacao = json.dumps(cardapio, sort_keys = True)
with open('cardapio.txt','w') as cardapio: 
    cardapio.write(atualizacao)
    
atualizacao2 = json.dumps(comanda, sort_keys = True) 
with open('comanda.txt','w') as comanda: 
    comanda.write(atualizacao)