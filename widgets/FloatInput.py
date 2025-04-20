import gui.widget as Widget
import gui.connection as connection
from imgui_bundle import imgui
from imgui_bundle import ImVec2
import time


class FloatInput(Widget.Widget):
    def __init__(self, name="FloatInput"):
        # This function will start the app
        super().__init__(name)
        self.value:float = 0.0
        self.type = connection.ConnectionType.FLOAT
        #self.allow_input = False

    def render(self):
        changed, self.value = imgui.input_float("##self.id", self.value)
        if changed:
            return True
        return False