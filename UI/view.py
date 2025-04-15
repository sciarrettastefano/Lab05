import flet as ft


class View():
    def __init__(self, page: ft.Page):
        super().__init__()
        # page stuff
        self._page = page
        self._page.title = "Lab O5 - Segreteria Studenti"
        self._page.horizontal_alignment = 'CENTER'
        self._page.theme_mode = ft.ThemeMode.LIGHT
        # controller (it is not initialized. Must be initialized in the main, after the controller is created)
        self._controller = None
        # graphical elements
        self._title = None
        self.txt_name = None
        self.btn_hello = None
        self.txt_result = None
        self.txt_container = None

    def load_interface(self):
        """Function that loads the graphical elements of the view"""
        # title
        self._title = ft.Text("App Gestione Studenti", color="blue", size=24)
        self._page.add(self._title)

        # row1: dd per scegliere corso e bottone per cercare gli iscritti
        self._ddCorso = ft.Dropdown(
            label = "Corso",
            width = 600)
        self._controller.fillDDCorsi()

        self._btnCercaIscritti = ft.ElevatedButton("Cerca Iscritti",
                                                   on_click=self._controller.handleCercaIscritti)

        row1 = ft.Row([self._ddCorso, self._btnCercaIscritti],
                      alignment=ft.MainAxisAlignment.CENTER)

        # row2: textfields per inserire la matricola e visualizzare congome e nome
        self._txtInMatricola = ft.TextField(
            label="Matricola",
            hint_text="Inserisci il numero di matricola",
            width=160)

        self._txtInNome = ft.TextField(
            read_only=True,
            label="Nome",
            width=240)

        self._txtInCognome = ft.TextField(
            read_only=True,
            label="Cognome",
            width=240)

        row2 = ft.Row([self._txtInMatricola, self._txtInNome, self._txtInCognome],
                      alignment=ft.MainAxisAlignment.CENTER)

        # row3: bottoni per ricerca studenti, ricerca corsi, iscrizioni

        self._btnCercaStudente = ft.ElevatedButton(
            "Cerca Studente",
            on_click=self._controller.handleCercaStudente)

        self._btnCercaCorsi = ft.ElevatedButton(
            "Cerca Corsi",
            on_click=self._controller.handleCercaCorsi)

        self._btnIscrivi = ft.ElevatedButton(
            "Iscrivi",
            on_click=self._controller.handleIscrivi)

        row3 = ft.Row([self._btnCercaStudente, self._btnCercaCorsi, self._btnIscrivi],
                      alignment=ft.MainAxisAlignment.CENTER)

        # lv per visulaizzare risultati
        self._txtOut = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)

        self._page.add(row1, row2, row3, self._txtOut)

    @property
    def controller(self):
        return self._controller

    @controller.setter
    def controller(self, controller):
        self._controller = controller

    def set_controller(self, controller):
        self._controller = controller

    def create_alert(self, message):
        """Function that opens a popup alert window, displaying a message
        :param message: the message to be displayed"""
        dlg = ft.AlertDialog(title=ft.Text(message))
        self._page.dialog = dlg
        dlg.open = True
        self._page.update()

    def update_page(self):
        self._page.update()
