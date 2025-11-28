from database.DAO import DAO
import networkx as nx

class Model:
    def __init__(self):
        self._lista_fermate = []
        self._grafo = None

    def getAllFermate (self) :
        fermate = DAO.readAllFermate ()
        self._lista_fermate = fermate

    def creaGrafo (self) :

        # Primo metodo
        self._grafo = nx.MultiDiGraph ()
        for fermata in self._lista_fermate :
            self._grafo.add_node (fermata)

        for u in self._grafo : # Per ognuno dei 619 nodi
            for v in self._grafo : # Per ognuno dei possibili nodi connessi
                risultato = DAO.existsConnessioneTra (u, v)
                if len (risultato) > 0 :
                    self._grafo.add_edge (u, v)
                    print (f"Aggiunto arco tra {u} e {v}")


        # Secondo metodo
        """
        conta = 0
        for u in self._grafo :
            connessioniAVicini = DAO.searchViciniAFermata (u)
            for connessione in connessioniAVicini :
                fermataArrivo = self._dizionario_fermate [connessione.id_stazA]
                self._grafo.add_edge (u, fermataArrivo)
                print (f"Aggiunto arco tra {u} e {fermataArrivo}")
                print (len (self._grafo.edges))
        """

        # Terzo metodo
        """
        listaConnessioni = DAO.readAllConnessioni ()
        for c in listaConnessioni :
            u_nodo = self._dizionario_fermate [c.id_stazP]
            v_nodo = self._dizionario_fermate [c.id_stazA]
            self._grafo.add_edge (u_nodo, v_nodo)
            print (f"Aggiunto arco tra {u} e {v_nodo}")
        """

        # Quarto metodo
        listaConnessioni = DAO.readAllConnessioni ()
        for c in listaConnessioni :
            u_nodo = self._dizionario_fermate [c.id_stazP]
            v_nodo = self._dizionario_fermate [c.id_stazA]
            # print (f"{self.esiste_arco (u_nodo, v_nodo)}")

            if self._grafo.esiste_arco (u_nodo, v_nodo) :
                self._grafo [u_nodo] [v_nodo] ["peso"] += 1
            else :
                self._grafo.add_edge (u_nodo, v_nodo, peso = 1)

            self._grafo.add_edge (u_nodo, v_nodo, peso = peso_arco)
            print (f"Aggiunto arco tra {u} e {v_nodo}, peso: {peso_arco}")

    def esiste_arco (self, u, v) :
        return self._grafo [u] [v]
