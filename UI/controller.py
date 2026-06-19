import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        self._year1 = None
        self._year2 = None


    def fillY(self):
        self._years = self._model.getY()
        for y in self._years:
            self._view._ddYear1.options.append(ft.dropdown.Option(y))
            self._view._ddYear2.options.append(ft.dropdown.Option(y))

        self._view.update_page()

    def handleBuildGraph(self, e):
        self._year1 = self._view._ddYear1.value
        self._year2 = self._view._ddYear2.value
        if self._year1 is None or self._year2 is None:
            self._view._txt_result.controls.clear()
            self._view._txt_result.controls.append(ft.Text("seleziona un anno"))
        if self._view._ddYear1.value > self._view._ddYear2.value:
            self._view._txt_result.controls.clear()
            self._view._txt_result.controls.append(ft.Text("seleziona gli anni nell'ordine corretto"))
            return

        self._model.creaGrafo(self._year1, self._year2)
        nodi = self._model.getNodi()
        archi = self._model.getArchi()
        self._view._txt_result.controls.clear()
        self._view._txt_result.controls.append(ft.Text("grafo creato correttamente"))
        self._view.update_page()


    def handlePrintDetails(self, e):
        self._view._txt_result.controls.clear()
        self._view._txt_result.controls.append(ft.Text(f"nodi: {nodi}, archi: {archi}"))
        self._view.update_page()

    def handleCercaTeamSfortunati(self, e):
        pass
