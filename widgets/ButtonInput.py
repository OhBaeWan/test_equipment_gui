import gui.widget as Widget
import gui.connection as connection
from imgui_bundle import imgui
from imgui_bundle import ImVec2
import time


class ButtonInput(Widget.Widget):
    def __init__(self, name="ButtonInput"):
        # This function will start the app
        super().__init__(name)
        self.value:int = 0
        self.type = connection.ConnectionType.EVENT
        self.allow_input = False

    def render(self):
        if imgui.button(f"{self.name}##{self.id}"):
            self.value += 1
            return True
        return False