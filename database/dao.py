from database.DB_connect import DBConnect
from model.hub import Hub
from model.spedizione import Spedizione


class DAO:
    """
    Implementare tutte le funzioni necessarie a interrogare il database.
    """
    # TODO
    @staticmethod
    def get_all_hub():
        conn = DBConnect.get_connection()
        result = []
        query = "select * from hub"
        cursor = conn.cursor(dictionary=True)
        cursor.execute(query)
        for row in cursor :
            #print(row)
            hub = Hub(row["id"], row["codice"], row["nome"],row["citta"],
                      row["stato"], row["longitudine"], row["latitudine"])
            result.append(hub)
        return result

    @staticmethod
    def get_num_nodes():
        conn = DBConnect.get_connection()

        query = "select count(*) from hub"
        cursor = conn.cursor()
        cursor.execute(query)
        (result,) = cursor.fetchone()
        cursor.close()
        conn.close()

        return result

    @staticmethod
    def existsConnessioneTra(u:Hub,v:Hub,threshold:float):
        conn = DBConnect.get_connection()
        spedizioni =[]
        query = """select * from spedizione s 
                 where s.id_hub_origine =%s and s.id_hub_destinazione= %s 
                 """
        cursor = conn.cursor(dictionary=True)
        cursor.execute(query,(u.id,v.id))
        for row in cursor :
            spedizione = Spedizione(row["id"],row["id_compagnia"],row["numero_tracking"],
                                    row["id_hub_origine"], row["id_hub_destinazione"],
                                    row["data_ritiro_programmata"], row["distanza"],
                                    row["data_consegna"], row["valore_merce"]
                                    )

            spedizioni.append(spedizione)
           # print(spedizione)
        cursor.close()
        conn.close()
        #verifico threshold
        somma = float(0)
        if not spedizioni:
            return[]
        for s in spedizioni:
            somma += s.valore_merce
        if somma/ float(len(spedizioni))>= threshold:
            return spedizioni
        else:
            return []
    @staticmethod
    def get_num_edges():
        conn = DBConnect.get_connection()

        query = """ SELECT COUNT(*) AS num_edges
                    FROM (SELECT DISTINCT id_hub_origine, id_hub_destinazione
                            FROM spedizione) AS t """
        cursor = conn.cursor()
        cursor.execute(query)
        (result,) = cursor.fetchone()
        cursor.close()
        conn.close()
        return result
