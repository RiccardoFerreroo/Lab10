from database.DB_connect import DBConnect
from model.hub import Hub


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
            print(row)
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
