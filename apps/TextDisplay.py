import gui.app as App
import gui.widget as Widget
import widgets.TextDisplay as TextDisplayWidget
from imgui_bundle import imgui
from imgui_bundle import ImVec2
import time

class TextDisplay(App.App):
    def start(self, name="TextDisplay"):
        # This function will start the app
        super().start(name)
        self.widget = TextDisplayWidget.TextDisplay(name="TextDisplay")
        self.text = ""
        self.widget.value = self.text
    
    def render(self):
         self.widget.update()