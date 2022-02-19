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

#Essa questão me deixou bem confusa. Eu deveria retornar apenas a quantidade de dígitos que faltam para a senha atingir o tamanho mínimo ou consultar todos os critérios? 
#Por via das dúvidas, decidi fazer a questão de uma maneira MAIS completa.

#Validando a senha dada
def validar_senha(senha):
	#Símbolos disponíveis para uso
	erros = {
		"comprimento": 0,
		"tem_numero": True,
		"tem_letra_maiuscula": True,
		"tem_letra_minuscula": True,
		"tem_caractere_especial": True
	}
	simbolos = ['$', '@', '#', '%', '&', '*', '+', '-', '!']
	#Verifica o tamanho da senha e quantos caracteres faltam
	if len(senha) < 6:
		erros["comprimento"] = 6-len(senha) 
	#Verifica se a senha contém um numeral	
	if not any(char.isdigit() for char in senha):
		erros["tem_numero"] = False
	#Verifica se a senha contém uma letra maiúscula
	if not any(char.isupper() for char in senha):
		erros["tem_letra_maiuscula"] = False
	#Verifica se a senha contém uma letra minúscula		
	if not any(char.islower() for char in senha):
		erros["tem_letra_minuscula"] = False
	#Verifica se a senha contém algum símbolo		
	if not any(char in simbolos for char in senha):
		erros["tem_caractere_especial"] = False
	
	return erros 

# senha = input('Digite sua senha:')
# print(validar_senha(senha))