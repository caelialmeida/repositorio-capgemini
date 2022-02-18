""" QUESTÃO 02 - DESAFIO ACADEMIA CAPGEMINI - 2022
Débora se inscreveu em uma rede social para se manter em contato com seus amigos. A página de cadastro exigia o preenchimento dos campos de nome e senha, porém a senha precisa ser forte. O site considera uma senha forte quando ela satisfaz os seguintes critérios:
- Possui no mínimo 6 caracteres.
- Contém no mínimo 1 digito.
- Contém no mínimo 1 letra em minúsculo.
- Contém no mínimo 1 letra em maiúsculo.
- Contém no mínimo 1 caractere especial. Os caracteres especiais são: !@#$%^&*()-+
Débora digitou uma string aleatória no campo de senha, porém ela não tem certeza se é uma senha forte. 
Para ajudar Débora, construa um algoritmo que informe qual é o número mínimo de caracteres que devem ser adicionados para uma string qualquer ser considerada segura.

**** PASSO A PASSO ****
Passo 01 - Inserir senha
Passo 02 - Verificar tamanho da senha
Passo 03 - Retornar quantidade de caracteres que faltam para completar 6 dígitos.
"""

#senha precisa ter 6 dígitos. 
#saída é a quantidade de dígitos que faltam para completar 6 dígitos.

#Essa questão me deixou bem confusa. Eu deveria retornar apenas a quantidade de dígitos que faltam para a senha atingir o tamanho mínimo? 
#Por via das dúvidas, decidi fazer a questão de uma maneira MAIS completa e deixar o código disponível para consulta.

senha = input('Digite sua senha:')
if (len(senha)) < 6: #condição para verificar se o tamanho da senha corresponde ao mínimo exigido

    faltam = 6 - len(senha) #cálculo para verificar o tamanho da senha

    print ("Falta(m) " + str(faltam) + "caracter(es)")

"""
Antes, eu tinha colocado a operação da variável "faltam" diretamente no "print".
No editor online dava erro. Imprimia tudo que tinha no print. ("Faltam 6 - len senha caracteres") Mas no VSCode dava certo.
Por isso, decidi adicionar uma nova variável, "faltam" para fazer a operação e verificar quantos caracteres faltavam.
"""

"""
#Outros critérios para a senha ser consderada forte:
"""
#Validando a senha dada
def validar_senha(senha):
#Símbolos disponíveis para uso
	simbolos =['$', '@', '#', '%', '&', '*', '+', '-', '!']
	val = True
#Verifica o tamanho da senha e quantos caracteres faltam
	if len(senha) < 6:
		print('Sua senha deve ter no mínimo 6 dígitos. Faltam', 6-len(senha), 'caracteres.')
		val = False
#Verifica se a senha contém um numeral	
	if not any(char.isdigit() for char in senha):
		print('Sua senha deve ter ao menos um número.')
		val = False
#Verifica se a senha contém uma letra maiúscula
	if not any(char.isupper() for char in senha):
		print('Sua senha deve ter ao menos uma letra maiúscula.')
		val = False
#Verifica se a senha contém uma letra minúscula		
	if not any(char.islower() for char in senha):
		print('Sua senha deve ter ao menos uma letra minúscula.')
		val = False
#Verifica se a senha contém algum símbolo		
	if not any(char in simbolos for char in senha):
		print('Sua senha deve ter ao menos um desses símbolos: $ @ # % & * + - !')
		val = False
	if val:
		return val

def main():
	
	if (validar_senha(senha)):
		print("Sua senha é válida!")
	else:
		print("Senha inválida!")
			
if __name__ == '__main__':
	main()