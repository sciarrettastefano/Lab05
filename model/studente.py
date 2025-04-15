from dataclasses import dataclass

from model.corso import Corso


@dataclass(order=True)
class Studente:
    matricola: str
    cognome: str
    nome: str
    CDS: str

    def __str__(self):
        return f"{self.nome.upper()}, {self.cognome.upper()} ({self.matricola})"

    def __eq__(self, other):
        return self.matricola == other.matricola

    def __hash__(self):
        return hash(self.matricola)