def quick_sort(valores):
    # Se a lista tem 0 ou 1 item, não tem o que ordenar, então devolvo uma cópia
    if len(valores) <= 1:
        return list(valores)

    # Pego o item do meio como "pivô", que é a referência pra comparar os outros
    pivo = valores[len(valores) // 2]

    # Três listas vazias: uma pra cada grupo
    menores = []
    iguais = []
    maiores = []

    # Passo por cada número e mando pro grupo certo comparando com o pivô
    for numero in valores:
        if numero < pivo:
            menores.append(numero)
            continue
        if numero == pivo:
            iguais.append(numero)
            continue
        maiores.append(numero)

    # Os grupos de menores e maiores ainda estão bagunçados por dentro,
    # então chamo a própria função neles pra repetir o processo
    menores_ordenados = quick_sort(menores)
    maiores_ordenados = quick_sort(maiores)

    # Monto a lista final: menores já ordenados, depois os iguais ao pivô,
    # depois os maiores já ordenados
    return menores_ordenados + iguais + maiores_ordenados

print(quick_sort([7, 3, 9, 1, 5]))