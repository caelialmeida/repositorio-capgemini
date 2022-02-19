#Para testar, digite no terminal: python -m pytest

#Possíveis testes:
#01 - se o input numero for uma letra em vez de algarismo, retornar erro. Mensagem: Você deve adicionar um número.

import Questao01

def test_input_letras():
    numero = 3
    escadinha = Questao01.escadinha(numero)

    expeted_chars = ((numero * 2) + 1) * numero

    assert len(escadinha) == expeted_chars