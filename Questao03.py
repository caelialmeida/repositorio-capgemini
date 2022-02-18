"""
Duas palavras podem ser consideradas anagramas de si mesmas se as letras de uma palavra podem ser realocadas para formar a outra palavra. 
Dada uma string qualquer, desenvolva um algoritmo que encontre o número de pares de substrings que são anagramas.

- Passo 01 - input palavra (variável)
- Passo 02 - separar substrings
	#Com um loop para ir do início até o fim da string, e ir adicionando uma letra a cada loop.
	#Guardar as substrings em um dicionário para poder consultar no próximo passo e evitar repetições ou muita demora.
- Passo 03 - comparar substrings 
    #Poderia organizar as letras das palavras em ordem alfabética para facilitar a verificação de anagramas
- Passo 04 - guardar anagramas (adicionando um contador)
- Passo 05 - contar a quantidade (variável)
- Passo 06 - entregar a quantidade

Os anagramas nas substrings não precisam ser com substrings até o final da strings, mas precisa encontrar letras repetidas na string.
Ex. ifa - fai (a letra "i" se repete após o "a") O contador vai até a próxima letra repetida, não significa que vai dividir a palavra em substrings de tamanhos iguais.
"""
# palavra = str(input('Sua palavra:'))
def ContagemDeAnagramas(string):
    n = len(string)
    map = dict()

    for i in range(n): #loop pra contar o tamanho das substrings
        substring = ''
        for j in range(i, n):
            substring = ''.join(sorted(substring + string[j]))
            map[substring] = map.get(substring, 0)

            map[substring] += 1 #contagem de substrings 

    anagramas = 0

    for k, v in map.items(): #loop pelo dicionário de substrings 
        anagramas += (v*(v-1))//2 #fórmula de combinações possíveis
    return anagramas

# print(ContagemDeAnagramas(palavra))