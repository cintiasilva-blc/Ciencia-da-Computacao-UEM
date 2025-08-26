def OrdenacaoSelecao(arranjo: list) -> list:
    '''Recebe uma lista de números e ordena do menor para o maior
    Exemplos:
    >>> OrdenacaoSelecao([3, 4, 9, 2, 10, 5, 8, 1, 7, 6])
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    >>> OrdenacaoSelecao([5,4,3,2,1])
    [1, 2, 3, 4, 5]
    '''

    n = len(arranjo)
    for i in range(n):
        min = i
        for j in range(i + 1, n):
            if arranjo[min] > arranjo[j]:
                min = j
        aux = arranjo[i]
        arranjo[i] = arranjo[min]
        arranjo[min] = aux
    
    return arranjo


def OrdenacaoInsercao(arranjo: list) -> list:
    '''Recebe uma lista de números e ordena do menor para o maior
    Exemplos:
    >>> OrdenacaoInsercao([3,4,9,2,10,5,8,1,7,6])
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    >>> OrdenacaoInsercao([5,4,3,2,1])
    [1, 2, 3, 4, 5]
    '''

    for i in range(1, len(arranjo)):
        pivo = arranjo[i]
        j = i - 1
        while j >= 0 and pivo < arranjo[j]:
            arranjo[j + 1] = arranjo[j]
            j = j - 1
        arranjo[j + 1] = pivo

    return arranjo


def OrdenacaoBubbleSort(arranjo: list) -> list:
    '''Recebe uma lista de números e ordena do menor para o maior
    Exemplos:
    >>> OrdenacaoBubbleSort([3,4,9,2,10,5,8,1,7,6])
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    >>> OrdenacaoBubbleSort([5,4,3,2,1])
    [1, 2, 3, 4, 5]
    '''
     
    n = len(arranjo)
    for i in range(n):
        for j in range(0, n-i-1):
            if arranjo[j] > arranjo[j + 1]:
                aux: int = arranjo[j]
                arranjo[j] = arranjo[j + 1]
                arranjo[j + 1] = aux

    return arranjo
    