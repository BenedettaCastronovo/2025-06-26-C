import copy

import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self._grafo = nx.Graph()
        self._nodi = DAO.getAll()
        self._grafo.add_nodes_from(self._nodi)
        self._mappaC={}
        for n in self._nodi:
            self._mappaC[n.constructorId] = n
        self.best = {}
        self.max = 0

        pass

    def getY(self):
        return DAO.getY()

    def creaGrafo(self, minimo, maximo):
        self._grafo.clear()
        for n in self._nodi:
            n.piaz = DAO.getP(n.constructorId, minimo, maximo)
        self._archi = DAO.getA(self._mappaC, minimo, maximo)
        for a in self._archi:
            self._grafo.add_edge(a.c1, a.c2, weight=a.peso)

    def getN(self):
        return len(self._nodi)

    def getA(self):
        return len(self._archi)

    def ComP(self):
        self._comp = list(nx.connected_components(self._grafo))
        self.magg = max(self._comp, key=len)
        co = self._grafo.subgraph(self.magg).copy()
        lista = []
        for n in co.nodes():
            edges = list(co.edges(n, data=True)) #per ogni nodo guardo tutti i nodi
            if len(edges) == 0:
                continue
            mas = max(edges, key=lambda x: x[2]["weight"]) #tra tutti i nodi prendo quello maggiore
            lista.append((n, mas[2]["weight"])) #tupla
        self.listaa = sorted(lista, key=lambda x: x[1], reverse=True)
        return self.magg, self.listaa

    def getMaxImp(self, k, m):
        self.best = {}
        self.max = 0
        comp = self.magg
        print(f"totale nodi in comp: {len(comp)}")
        nodi_validi = [n for n in comp if self.is_valid(n, comp, m)]
        print(f"nodi validi con m={m}: {len(nodi_validi)}")
        self.ric([], nodi_validi, k, m)
        print(f"best: {self.best}, max: {self.max}")
        return self.best, self.max

    def ric(self, parziale, comp, k, m):
        if len(parziale) == k: #condizione terminale
            if self.costo(parziale) > self.max:
                self.best = copy.deepcopy(parziale)
                self.max = self.costo(parziale)
            return

        for n in comp:
            if n not in parziale and self.is_valid(n, comp, m):
                parziale.append(n)
                self.ric(parziale, comp, k, m)
                parziale.pop()

    def is_valid(self, n, comp, m):
        if n in comp and len(n.piaz) >= m:
            return True
        return False

    def costo(self, parziale):
        i = 0
        somma = 0
        for c in parziale:
            np = 0
            npTot = 0
            for t in c.piaz.values():
                for p in t:  # p è la singola Posizione
                    npTot += 1
                    if p.position is not None:
                        np += 1
            if npTot > 0:
                i = 1 - np / npTot
            else:
                i = 0
            somma += i
        return somma












