#Possíveis testes

#01 - Teste com palavra "ifailuhkqq" deve retornar 3
#02 - Teste com palavra "ovo" deve retornar 2

import Questao03

def test_palavra_ifailihkqq():
    palavra = 'ifailuhqq'
    res = Questao03.ContagemDeAnagramas(palavra) 
    assert res == 3

def test_palavra_ovo():
    palavra = 'ovo'
    assert Questao03.ContagemDeAnagramas(palavra) == 2