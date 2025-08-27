from enum import Enum


class Dia(Enum):
    '''
    Um dia da semana.
    '''
    DOM = False 
    SEG = True
    TER = True * 2
    QUA = True * 3
    QUI = True * 4
    SEX = True * 5
    SAB = True * 6

class Dias:
    '''
    Um conjunto de dias da semana que um evento deve se repetir.
    '''

    dias: list[Dia]

    def __init__(self) -> None:
        '''
        Cria um novo conjunto vazio de dias.

        Exemplos
        >>> c = Dias()
        >>> c.lista()
        []
        '''

        self.dias = []

    def alterna(self, d: Dia) -> None:
        '''
        Alterna a pertinencia do dia *d* em *self*, isto é, se *d* está em
        *self*, *d* é removido. Se *d* não está em *self*, *d* é adicionado.

        Exemplos
        >>> c = Dias()
        >>> c.alterna(Dia.SEX)
        >>> c.lista()
        ['SEX']
        >>> c.alterna(Dia.SEG)
        >>> c.lista()
        ['SEG', 'SEX']
        >>> c.alterna(Dia.SEX)
        >>> c.lista()
        ['SEG']
        '''

        nova_lista = []

        if d in self.dias:
            for i in self.dias:
                if i != d:
                    nova_lista.append(i)
                    self.dias = nova_lista
        else:
            self.dias.append(d)


    def lista(self) -> list[str]:
        '''
        Devolve uma lista com os dias (abreviações) em ordem da semana que
        estão em *self*.

        Exemplos
        >>> c = Dias()
        >>> c.lista()
        []
        >>> c.alterna(Dia.TER)
        >>> c.lista()
        ['TER']
        >>> c.alterna(Dia.DOM)
        >>> c.lista()
        ['DOM', 'TER']
        >>> c.alterna(Dia.QUI)
        >>> c.alterna(Dia.SEG)
        >>> c.alterna(Dia.SAB)
        >>> c.alterna(Dia.QUA)
        >>> c.alterna(Dia.SEX)
        >>> c.lista()
        ['DOM', 'SEG', 'TER', 'QUA', 'QUI', 'SEX', 'SAB']
        '''

        nomes = []
        for i in self.dias:
            nomes.append(i.name)
            nomes = self.dias
        return self.dias
