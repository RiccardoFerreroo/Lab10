from database.dao import DAO
import networkx as nx

class Model:
    def __init__(self):
        self._nodes = None
        self._edges = None
        self.G = nx.Graph()
        self.lista_nodes = []
        self.lista_edges = []

    def costruisci_grafo(self, threshold):
        """
        Costruisce il grafo (self.G) inserendo tutti gli Hub (i nodi) presenti e filtrando le Tratte con
        guadagno medio per spedizione >= threshold (euro)
        """
        self.lista_nodes= DAO.get_all_hub()
        #print("lista_nodes: ", self.lista_nodes)
        for hub in self.lista_nodes:
            self.G.add_node(hub)
        for u in self.lista_nodes:
            for v in self.lista_nodes:
                risultato = DAO.existsConnessioneTra(u,v)
                if (len(risultato)>0):# esiste almeno una connessione
                    self.G.add_edge(u,v)# creo arco
                    print(f"aggiunto arco tra {u}e {v}")



        # TODO

    def get_num_edges(self):
        """
        Restituisce il numero di Tratte (edges) del grafo
        :return: numero di edges del grafo
        """

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
        # TODO

