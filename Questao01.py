"""
Escreva um algoritmo que mostre na tela uma escada de tamanho n utilizando o caractere * e espaços. 
A base e altura da escada devem ser iguais ao valor de n. 
A última linha não deve conter nenhum espaço.

Passo 01 - Entrar com número
Passo 02 - Loop para criar as linhas
Passo 03 - Calcular os números de espaços vazios e de estrelas a cada linha
Passo 04 - Usar a função print para "quebrar" a linha
"""
# numero = 2
# numero = int(input('Digite um numero:'))
# print(numero)
# espaco = 2 * numero - 2 #espaços vazios entre cada asteriscos
#Para cada linha há um número diferente de espaços vazios. 
#Esse é o loop que contabiliza esses espaços vazios.


def escadinha(numero):
    espaco = 2 * numero - 2
    
    _escadinha = ""
    for i in range(0, numero):
        # print(len(_escadinha))
        #Conta para saber o número de asteriscos * que vão aparecer a cada linha
        for j in range(0, espaco):
            _escadinha += " "
        
        espaco = espaco - 2

        #Loop para imprimir a quantidade de asteriscos a cada linha
        for j in range(0, i + 1):  
            _escadinha += "* " #Você pode alterar o símbolo impresso, basta trocar o sinal "*"

        _escadinha += "\n"

    return _escadinha
"""
num = 6


    * \
  * * \n
* * * \n

print(((num * 2) + 1) * num)
res = escadinha(num)
print(len(res))

"""


