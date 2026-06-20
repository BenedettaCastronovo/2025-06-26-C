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

        pass

    def getY(self):
        return DAO.getY()

    def creaGrafo(self, minimo, maximo):
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
        magg = max(self._comp, key=len)
        co = self._grafo.subgraph(magg).copy()
        lista = []
        for n in co.nodes():
            edges = list(co.edges(n, data=True)) #per ogni nodo guardo tutti i nodi
            if len(edges) == 0:
                continue
            mas = max(edges, key=lambda x: x[2]["weight"]) #tra tutti i nodi prendo quello maggiore
            lista.append((n, mas[2]["weight"])) #tupla
        self.listaa = sorted(lista, key=lambda x: x[1], reverse=True)
        return magg, self.listaa









