#Possíveis testes:

#01 - tamanho menor que 6
#02 - tamanho == 6 
#03 - tamanho > 6
#04 - Caractere especial inválido
#05 - Sem letra maiúscula
#06 - Com letra minúscula
#07 - Com número

import Questao02

def test_tamanho_menor_que_seis():
    senha = 'Ab3@'
    validacao = Questao02.validar_senha(senha)
    assert validacao["comprimento"] == 2

def test_tamanho_igual_a_seis():
    senha = 'Ab3@##'
    res = Questao02.validar_senha(senha)
    assert res["comprimento"] == 0
# python -m pytest

def test_tamanho_maior_que_seis():
    senha = 'Ab3@@##'
    assert Questao02.validar_senha(senha)["comprimento"] == 0

def test_simbolo_invalido():
    senha = 'Abc3><'
    res = Questao02.validar_senha(senha)
    assert not res["tem_caractere_especial"]
