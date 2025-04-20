import gui.app as App
import gui.widget as Widget
import widgets.FloatInput as FloatInputWidget
from imgui_bundle import imgui
from imgui_bundle import ImVec2
import time

class FloatInput(App.App):
    def start(self, name="FloatInput"):
        # This function will start the app
        super().start(name)
        self.widget = FloatInputWidget.FloatInput(name="FloatInput")
        self.value = 0.0
    
    def render(self):
        # This function will render the app
        imgui.text("Float Input")
        imgui.separator()
        imgui.text("Enter float:")
        if self.widget.update():
            self.value = self.widget.value
    
    def quit(self):
        # This function will quit the app
        self.widget.quit()
        super().quit()