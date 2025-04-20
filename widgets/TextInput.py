import gui.widget as Widget
import gui.connection as connection
from imgui_bundle import imgui
from imgui_bundle import ImVec2
import time


class TextInput(Widget.Widget):
    def __init__(self, name="TextInput"):
        # This function will start the app
        super().__init__(name)
        self.value:str = ""
        self.type = connection.ConnectionType.STRING
        #self.allow_input = False

    def render(self):
        changed, self.value = imgui.input_text("##self.id", self.value)
        if changed:
            return True
        return False