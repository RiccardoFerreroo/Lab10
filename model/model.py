from database.dao import DAO
import networkx as nx

class Model:
    def __init__(self):
        self._nodes = None
        self._edges = None
        self.G = nx.Graph() #grafo semplice non orientato ( consegna )
        self.lista_nodes = []
        self.lista_edges = []

    def costruisci_grafo(self, threshold):
        """
        Costruisce il grafo (self.G) inserendo tutti gli Hub (i nodi) presenti e filtrando le Tratte con
        guadagno medio per spedizione >= threshold (euro)
        """
        self.G.clear()

        self.lista_nodes= DAO.get_all_hub()
        #print("lista_nodes: ", self.lista_nodes)
        for hub in self.lista_nodes:
            self.G.add_node(hub)

        for u in self.lista_nodes:
            for v in self.lista_nodes:
                if u == v:
                    continue

                risultato = DAO.existsConnessioneTra(u,v,threshold)
                if len(risultato)>0:# esiste almeno una connessione
                    cifra = 0
                    for elemento in risultato:
                        cifra +=elemento.valore_merce

                    peso = cifra / len(risultato)
                    self.G.add_edge(u,v, weight=peso)# creo arco
                    #print(f"aggiunto arco tra {u}e {v} "
                        #  f"con valore medio {peso}")
        #print(self.G)
        return self.G


        # TODO

    def get_num_edges(self):
        """
        Restituisce il numero di Tratte (edges) del grafo
        :return: numero di edges del grafo
        """

        num_edges = DAO.get_num_edges()
        return num_edges
        # TODO

    def get_num_nodes(self):
        """
        Restituisce il numero di Hub (nodi) del grafo
        :return: numero di nodi del grafo
        """
        num_nodes = DAO.get_num_nodes()
        #print(num_nodes)
        return num_nodes

    def get_all_edges(self):
        """
        Restituisce tutte le Tratte (gli edges) con i corrispondenti pesi
        :return: gli edges del grafo con gli attributi (il weight)
        """
        edges_info = []
        for edge in self.G.edges(data=True):
            u = edge[0]
            v = edge[1]
            data = edge[2]#dizionario con tutti gli attributi dell'arco
            edges_info.append(f"{u.nome} -> {v.nome} -- Guadagno Medio"
                              f" Per Spedizione: {data['weight']}")
        return edges_info

        # TODO

