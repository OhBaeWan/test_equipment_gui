import gui.widget as Widget
import gui.connection as connection
from imgui_bundle import imgui
from imgui_bundle import ImVec2
import time


class IntInput(Widget.Widget):
    def __init__(self, name="IntInput"):
        # This function will start the app
        super().__init__(name)
        self.value:int = 0
        self.type = connection.ConnectionType.INT
        #self.allow_input = False


    def render(self):
        changed, self.value = imgui.input_int("##self.id", self.value)
        if changed:
            return True
        return False
