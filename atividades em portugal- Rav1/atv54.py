'''Há um detalhe importante:
 Python não possui passagem de parâmetros por referência
da mesma forma que C++ ou Pascal.'''
#passei o codigo de Python para Portugol<<<<

algoritmo "entrega"

procedimento entrega3dias(var valor: real)
inicio
   valor <- valor + 25
fimprocedimento

procedimento entrega5dias(var valor: real)
inicio
   valor <- valor + 20
fimprocedimento

procedimento entrega7dias(var valor: real)
inicio
   valor <- valor + 15
fimprocedimento

procedimento entrega10dias(var valor: real)
inicio
   valor <- valor + 10
fimprocedimento

var
   valor: real
   opcao: inteiro

inicio

   escreva("Informe o valor da compra: ")
   leia(valor)

   escreval("Prazo de entrega")
   escreval("1 - 3 dias úteis")
   escreval("2 - 5 dias úteis")
   escreval("3 - 7 dias úteis")
   escreval("4 - 10 dias úteis")

   escreva("Escolha uma opção: ")
   leia(opcao)

   escolha opcao

      caso 1
         entrega3dias(valor)

      caso 2
         entrega5dias(valor)

      caso 3
         entrega7dias(valor)

      caso 4
         entrega10dias(valor)

      outrocaso
         escreval("Opção inválida")

   fimescolha

   escreval("Valor final: R$ ", valor)

fimalgoritmo