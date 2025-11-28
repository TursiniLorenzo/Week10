from database.DB_connect import DBConnect
from model.fermata import Fermata
from model.Connessione import Connessione

class DAO():
    pass

    @staticmethod
    def readAllFermate () :
        cnx = DBConnect.get_connection  ()
        result = []
        query = "SELECT * FROM fermata"
        cursor = cnx.cursor (dictionary = True)

        cursor.execute (query)

        for row in cursor :
            fermata = Fermata (row ["id_fermata"], row ["nome"], row ["coordX"], row ["coordY"])
            result.append (fermata)

        cursor.close ()
        cnx.close ()
        return result

    @staticmethod
    def existsConnessioneTra (u : Fermata, v : Fermata) : # Fermate
        # Verifica se esista una connessione tra nodo u e v
        cnx = DBConnect.get_connection  ()
        result = []
        query = ("SELECT * "
                 "FROM connessione c "
                 "WHERE c.id_stazP = %s "
                 "AND c.id_stazA = %s ")

        cursor = cnx.cursor (dictionary = True)

        cursor.execute (query, (u.id_fermata, v.id_fermata, ))

        for row in cursor :
            result.append (row)

        cursor.close ()
        cnx.close ()
        return result

    @staticmethod
    def searchViciniAFermata (u : Fermata ) :
        # Cerco le fermate collegate a quella passata come parametro
        cnx = DBConnect.get_connection()
        result = []
        query = ("SELECT * "
                 "FROM connessione c "
                 "WHERE c.id_stazP = %s ")

        cursor = cnx.cursor(dictionary=True)

        cursor.execute(query, (u.id_fermata, ))

        for row in cursor:
            connessione = Connessione (row ["id_connessione"], row ["id_linea"], row ["id_stazA"], row ["id_stazP"])
            result.append(connessione)


        cursor.close()
        cnx.close()
        return result


    @staticmethod
    def readAllConnessioni () :
        cnx = DBConnect.get_connection ()
        result = []


    @staticmethod
    def readVelocita () :
        cnx = DBConnect.get_connection ()
        result = []

        query = ("SELECT * FROM linea WHERE id_linea = %s ")

