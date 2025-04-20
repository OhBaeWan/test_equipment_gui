import gui.widget as Widget
import gui.connection as connection
from imgui_bundle import imgui
from imgui_bundle import ImVec2
import time


class TextDisplay(Widget.Widget):
    def __init__(self, name="TextDisplay"):
        # This function will start the app
        super().__init__(name)
        self.value:str = ""
        self.type = connection.ConnectionType.STRING
        self.allow_output = False

    def render(self):
        imgui.text(self.value)