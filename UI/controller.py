from logging import exception

import flet as ft
from UI.view import View
from model.model import Model


class Controller:
    def __init__(self, view: View, model: Model):
        self._view = view
        self._model = model

    def mostra_tratte(self, e):
        """
        Funzione che controlla prima se il valore del costo inserito sia valido (es. non deve essere una stringa) e poi
        popola "self._view.lista_visualizzazione" con le seguenti info
        * Numero di Hub presenti
        * Numero di Tratte
        * Lista di Tratte che superano il costo indicato come soglia
        """
        valore = self._view.guadagno_medio_minimo.value
        if valore.strip() is None:
            self._view.show_alert(" inserire valore valido")
            return
        try:
            valore= float(valore)
        except Exception as e:
            self._view.show_alert(" inserire valore valido")
            return
        num_nodi = self._model.get_num_nodes()
        num_archi = self._model.get_num_edges()


        self._model.costruisci_grafo(valore)
        edges = self._model.get_all_edges()
        #pulisco listview
        self._view.lista_visualizzazione.controls.clear()

        for edge_str in edges:
            self._view.lista_visualizzazione.controls.append(ft.Text(edge_str))

        self._view.update()
        # TODO

