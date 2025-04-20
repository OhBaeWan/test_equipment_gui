import gui.widget as Widget
import gui.connection as connection
from imgui_bundle import imgui
from imgui_bundle import ImVec2
import time

class FloatDisplay(Widget.Widget):
    def __init__(self, name="FloatDisplay"):
        # This function will start the app
        super().__init__(name)
        self.value:float = 0.0
        self.type = connection.ConnectionType.FLOAT
        self.allow_output = False

    def render(self):
        imgui.text(f"{self.value:.3f}")
        return False