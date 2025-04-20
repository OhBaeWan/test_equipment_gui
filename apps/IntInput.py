import gui.app as App
import gui.widget as Widget
import widgets.IntInput as IntInputWidget
from imgui_bundle import imgui
from imgui_bundle import ImVec2
import time

class IntInput(App.App):
    def start(self, name="IntInput"):
        # This function will start the app
        super().start(name)
        self.widget = IntInputWidget.IntInput(name="IntInput")
        self.value = 0

    def render(self):
        # This function will render the app
        imgui.text("Int Input")
        imgui.separator()
        imgui.text("Enter integer:")
        if self.widget.update():
            self.value = self.widget.value

    def quit(self):
        # This function will quit the app
        self.widget.quit()
        super().quit()