from database.corso_DAO import CorsoDAO
from database.studente_DAO import StudenteDAO

class Model:
    def __init__(self):
        self._corsi = []   #?
        self._studenti = []   #?
        self._corsoDao = CorsoDAO()
        self._studenteDao = StudenteDAO()
        self.getCorsi()

    def getCorsi(self):
        allCorsi = self._corsoDao.getAllCorsi()
        for corso in allCorsi:
            self._corsi.append(corso)

    def getIscrittiCorso(self, codins):
        return self._studenteDao.getIscrittiCorso(codins)

    def cercaStudente(self, matricola):
        return self._studenteDao.cercaStudente(matricola)

    def cercaCorsiStudente(self, matricola):
        return self._corsoDao.cercaCorsiStudente(matricola)

    def iscrivi(self, codins, matricola):
       return self._studenteDao.iscrivi(codins, matricola)
