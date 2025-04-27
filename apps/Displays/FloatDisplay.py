import gui.app as App
import gui.widget as Widget
import widgets.FloatDisplay as FloatDisplayWidget
from imgui_bundle import imgui
from imgui_bundle import ImVec2
import time

class FloatDisplay(App.App):
    def start(self, name="FloatDisplay"):
        # This function will start the app
        super().start(name)
        self.widget = FloatDisplayWidget.FloatDisplay(name="FloatDisplay")
        self.value = 0.0
        self.widget.value = self.value

    def render(self):
        self.widget.update()