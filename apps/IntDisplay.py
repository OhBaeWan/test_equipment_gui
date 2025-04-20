import gui.app as App
import gui.widget as Widget
import widgets.IntDisplay as IntDisplayWidget 
from imgui_bundle import imgui
from imgui_bundle import ImVec2
import time

class IntDisplay(App.App):
    def start(self, name="IntDisplay"):
        # This function will start the app
        super().start(name)
        self.widget = IntDisplayWidget.IntDisplay(name="IntDisplay")
        self.value = 0
        self.widget.value = self.value
    
    def render(self):
        self.widget.update()
