# Add whatever it is needed to interface with the DB Table corso

from database.DB_connect import DBConnect
from model.corso import Corso
from model.studente import Studente


class CorsoDAO:

    def getAllCorsi(self):
        """
        Metodo che legge tutti i corsi nel db.
        :return: lista contenente i corsi nel db.
        """
        cnx = DBConnect.getConnection()
        cursor = cnx.cursor(dictionary=True)

        query = "select * from corso"
        cursor.execute(query)

        results = []
        for row in cursor:
            results.append(Corso(row['codins'], row['crediti'], row['nome'], row['pd']))

        cnx.close()

        return results

    def cercaCorsiStudente(self, matricola):
        """
        Funzione che data una matricola ricerca nel database i corsi frequentati.
        :param matricola: la matricola dello studente da ricercare.
        :return: una lista di corsi.
        """
        cnx = DBConnect.getConnection()
        cursor = cnx.cursor(dictionary=True)

        query = """SELECT corso.*
                   FROM corso, iscrizione
                   WHERE iscrizione.codins=corso.codins AND iscrizione.matricola=%s"""
        cursor.execute(query, (matricola, ))

        results =[]
        for row in cursor:
            results.append(Corso(row['codins'], row['crediti'], row['nome'], row['pd']))

        cnx.close()

        return results



if __name__ == '__main__':
    mydao = CorsoDAO()
    print(mydao.getAllCorsi())
