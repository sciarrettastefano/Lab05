import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handleCercaIscritti(self, e):
        """
        Metodo che abilita la ricerca degli iscritti al corso selezionato
        alla pressione del rispettivo bottone.
        """
        codins = self._view._ddCorso.value

        if codins is None:
            self._view.create_alert("Selezionare un corso!")
            return

        iscritti = self._model.getIscrittiCorso(codins)

        self._view._txtOut.controls.clear()
        if len(iscritti) == 0:
            self._view._txtOut.controls.append(ft.Text("Non ci sono iscritti al corso"))
        else:
            self._view._txtOut.controls.append(ft.Text(f"Ci sono {len(iscritti)} iscritti al corso:"))
            for iscritto in iscritti:
                self._view._txtOut.controls.append(ft.Text(f"{iscritto}"))
            self._view.update_page()

    def handleCercaStudente(self, e):
        """
        Metodo che permette la ricerca di uno studente nel db tramite
        la sua matricola alla pressiuone del corrispettivo pulsante.
        """
        matricola = self._view._txtInMatricola.value
        if matricola == "":
            self._view.create_alert("Inserire una matricola!")
            self._view._txtInCognome.value = ""
            self._view._txtInNome.value = ""
            self._view.update_page()
            return

        studente = self._model.cercaStudente(matricola)
        if studente is None:
            self._view.create_alert("Matricola non presente nel database!")
            self._view._txtInCognome.value = ""
            self._view._txtInNome.value = ""
            self._view.update_page()
            return

        self._view._txtInCognome.value = studente.cognome
        self._view._txtInNome.value = studente.nome
        self._view._txtOut.controls.clear()
        self._view._txtOut.controls.append(ft.Text("Ricerca completata correttamente",
                                                   color="green"))
        self._view.update_page()

    def handleCercaCorsi(self, e):
        """
        Metodo che permette la ricerca dei corsi di uno studente
        tramite la sua matricola (se presente nel db).
        """
        matricola = self._view._txtInMatricola.value
        if matricola == "":
            self._view.create_alert("Inserire una matricola!")
            self._view._txtInCognome.value = ""
            self._view._txtInNome.value = ""
            self._view.update_page()
            return

        studente = self._model.cercaStudente(matricola)
        if studente is None:
            self._view.create_alert("Matricola non presente nel database!")
            self._view._txtInCognome.value = ""
            self._view._txtInNome.value = ""
            self._view.update_page()
            return

        self._view._txtOut.controls.clear()

        corsi = self._model.cercaCorsiStudente(matricola)
        if len(corsi) == 0:
            self._view._txtInCognome.value = studente.cognome
            self._view._txtInNome.value = studente.nome
            self._view._txtOut.controls.append(ft.Text(f"Nessun corso seguito dallo studente {studente}.",
                                                       style=ft.TextStyle(decoration=ft.TextDecoration.UNDERLINE)))
            self._view.update_page()
            return
        else:
            self._view._txtInCognome.value = studente.cognome
            self._view._txtInNome.value = studente.nome
            self._view._txtOut.controls.append(ft.Text(f"Corsi seguiti dallo studente {studente}:",
                                                       style=ft.TextStyle(decoration=ft.TextDecoration.UNDERLINE)))
            for corso in corsi:
                self._view._txtOut.controls.append(ft.Text(f"{corso}"))
            self._view.update_page()
            return

    def handleIscrivi(self, e):
        """
        Il metodo permette all'utente di aggiungere una relazione tra
        uno studente ed un corso all'interno del db.
        """
        matricola = self._view._txtInMatricola.value
        if matricola == "":
            self._view.create_alert("Inserire una matricola!")
            self._view._txtInCognome.value = ""
            self._view._txtInNome.value = ""
            self._view.update_page()
            return

        studente = self._model.cercaStudente(matricola)
        if studente is None:
            self._view.create_alert("Matricola non presente nel database!")
            self._view._txtInCognome.value = ""
            self._view._txtInNome.value = ""
            self._view.update_page()
            return

        codins = self._view._ddCorso.value
        if codins == "":
            self._view.create_alert("Selezionare un corso!")
            self._view.update_page()
            return

        result = self._model.iscrivi(codins, matricola)

        self._view._txtOut.controls.clear()
        if result:
            self._view._txtOut.controls.append(ft.Text("Iscrizione avvenuta con successo.",
                                                      color="green"))
        else:
            self._view._txtOut.controls.append(ft.Text("Iscrizione fallita.",
                                                          color="red"))
        self._view.update_page()




    def fillDDCorsi(self):
        for corso in self._model._corsi:
            self._view._ddCorso.options.append(ft.dropdown.Option(key=corso.codins, text=corso))
        self._view.update_page()
