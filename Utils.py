from random import randint
from tabulate import tabulate

class RangeDict(dict):
    def __getitem__(self, item):
        if not isinstance(item, range):
            for key in self:
                if item in key:
                    return self[key]
            raise KeyError(item)
        else:
            return super().__getitem__(item)

def quadroParaValores(quadro):
    d = dict()
    i = 1
    for t in quadro:
        a = int(t[1]*100 + i)
        d[range(i,a)] = t[0]
        i = a
    
    return RangeDict(d)


class Chegada():
    def __init__(self):
        self.intervaloChegadas = []
        self.horarioChegadas = []

    def preencheEntrada(self, intervaloChegadas, numeroDeUsuarios):
        for i in range(numeroDeUsuarios):
            if i == 0:
                self.intervaloChegadas.append(0)
                self.horarioChegadas.append(0)
            else:
                self.intervaloChegadas.append(intervaloChegadas[randint(1,100)])
                self.horarioChegadas.append(self.horarioChegadas[i-1] + self.intervaloChegadas[i])
        
        
class Fila():
    def __init__(self):
        self.tempo = []


class Atendimento():
    def __init__(self):
        self.entrada = []
        self.tempo = []
        self.saida = []

    def defineTempoAtendimento(self, tempoDeAtendimento, numeroDeUsuarios):
        for _ in range(numeroDeUsuarios):
            self.tempo.append(tempoDeAtendimento[randint(1,100)])


class Sistema():
    def __init__(self, quadroDeChegada, quadroDeAtendimento, numeroDeUsuarios):
        self.chegada = Chegada()
        self.fila = Fila()
        self.atendimento = Atendimento()
        self.tempoDeChegada = quadroParaValores(quadroDeChegada)
        self.tempoDeAtendimento = quadroParaValores(quadroDeAtendimento)
        self.numeroDeUsuarios = numeroDeUsuarios

    def primeirosValores(self):
        self.chegada.preencheEntrada(self.tempoDeChegada, self.numeroDeUsuarios)
        self.atendimento.defineTempoAtendimento(self.tempoDeAtendimento, self.numeroDeUsuarios)

        self.fila.tempo.append(0)
        self.atendimento.entrada.append(0)
        self.atendimento.saida.append(self.atendimento.tempo[0])

    def calcular(self):
        self.primeirosValores()

        for i in range(1, self.numeroDeUsuarios, 1):
            self.atendimento.entrada.append(max(self.chegada.horarioChegadas[i], self.atendimento.saida[i-1]))
            self.fila.tempo.append(self.atendimento.entrada[i] - self.chegada.horarioChegadas[i])
            self.atendimento.saida.append(self.atendimento.entrada[i]+self.atendimento.tempo[i])


    def mostrarTabela(self):
        result = [(i+1, self.chegada.horarioChegadas[i], self.fila.tempo[i], self.atendimento.entrada[i], self.atendimento.tempo[i],self.atendimento.saida[i], self.atendimento.saida[i] - self.chegada.horarioChegadas[i]) for i in range(self.numeroDeUsuarios)]
        print(tabulate(result, headers=["Pessoas","Chegada","Tempo de fila","Entrada atendimento","Tempo de atendimento", "Saida atendimento","Tempo de sistema"], tablefmt="fancy_grid",numalign="center"))