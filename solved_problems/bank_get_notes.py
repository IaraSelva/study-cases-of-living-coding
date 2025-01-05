# Dado um valor (o quanto se quer sacar)
# e um dicionário de notas (a quantidade e o valor das notas que o caixa eletrônico possui)
# encontrar a combinação de notas possíveis para o valor que se quer sacar

# Deve-se testar todos as combinações possíveis para chegar no valor a ser sacado, por isso precisa-se usar recursão.
# Para cada nota testamos se ela é menor que o valor que queremos sacar e, se sim, chamamos a função novamente com o valor atualizado sendo o valor originar menos o valor da nota que está sendo testada
# Temos ainda um set de valores não possíveis que terá um valor adicionado sempre que sair do for, ou seja, não tiver encontrado uma resposta possível
# E ainda um array que contém as notas que já foram testadas até então (e que foram possíveis) mais a nota encontrada atualmente
# Retorna-se a resposta apenas se o retorno da recursão não tiver sido None
# O retorno será None caso: 1) o valor já esteja na lista de not_possible 2) saia do for, ou seja, o valor já tenha sido testado para todas as notas sem sucesso
# A quantidade de notas deve ser diminuída em 1 sempre antes de chamar a recursão e, caso ans retorne None, signofica que não encontrei uma combinação possível para aquela nota então o dicionário é atualizado novamente, dessa vez aumentando em 1


def get_notes(value, notes, not_possible = set(), notes_until_here = []):
    if value in not_possible:
        return None
    if value in notes:
        return notes_until_here + [value]
    for note in notes:
        if note < value and notes[note] > 0:
            notes[note] = notes[note] - 1
            ans = get_notes(value - note, notes, not_possible, notes_until_here + [note])
            if ans:
                return ans
            notes[note] = notes[note] + 1

    not_possible.add(value)
    return None