import gui.widget as Widget
import gui.connection as connection
from imgui_bundle import imgui
from imgui_bundle import ImVec2
import time

class IntDisplay(Widget.Widget):
    def __init__(self, name="IntDisplay"):
        # This function will start the app
        super().__init__(name)
        self.value:int = 0
        self.type = connection.ConnectionType.INT
        self.allow_output = False
    
    def render(self):
        imgui.text(f"{self.value}")
        return False