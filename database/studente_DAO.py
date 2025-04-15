# Add whatever it is needed to interface with the DB Table studente

from database.DB_connect import DBConnect
from model.studente import Studente

class StudenteDAO:

    def cercaStudente(self, matricola):
        """
        Metodo che cerca uno studente nel db dat la sua matricola.
        :param matricola: str da far diventare int che rappresenta la matricola dello studente da ricercare.
        :return: istanza dello studente se trovato (valore None se non trovato).
        """
        cnx = DBConnect.getConnection()
        cursor = cnx.cursor(dictionary=True)

        query = "SELECT * FROM studente WHERE matricola = %s"
        cursor.execute(query, (int(matricola), ))

        result = None
        row = cursor.fetchone()
        if row is not None:
            result = Studente(row['matricola'], row['cognome'], row['nome'], row['CDS'])

        cnx.close()

        return result

    def getIscrittiCorso(self, codins):
        """Funzione che recupera una lista con tutti gli studenti iscritti al corso selezionato.
        :param codins: il corso di cui recuperare gli iscritti.
        :return: una lista con tutti gli studenti iscritti."""
        cnx = DBConnect.getConnection()
        cursor = cnx.cursor(dictionary=True)

        query = ("""SELECT studente.*
                    FROM iscrizione, studente
                    WHERE iscrizione.matricola=studente.matricola AND iscrizione.codins=%s""")
        cursor.execute(query, (codins, ))

        results = []
        for row in cursor:
            results.append(Studente(row['matricola'], row['cognome'], row['nome'], row['CDS']))

        cnx.close()

        return results

    def iscrivi(self, codins, matricola):
        """
        Il metodo crea una relazione non ancora presente tra uno studente ed un corso
        che sono già presenti nel db.
        :param codins: str rappresentante codice dell'insegnamento in questione.
        :param matricola: int rappresentante matricola dello studente in questione.
        :return: None
        """
        cnx = DBConnect.getConnection()
        if cnx is not None:
            cursor = cnx.cursor(dictionary=True)

            query = """INSERT INTO iscrizione (codins, matricola) values (%s, %s)"""
            cursor.execute(query, (codins, matricola))

            cnx.commit()
            cnx.close()
            return True
        else:
            return False

if __name__ == '__main__':
    mydao = StudenteDAO()
    print(mydao.cercaStudente("161245"))
