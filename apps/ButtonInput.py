import gui.app as App
import gui.widget as Widget
import widgets.ButtonInput as ButtonInputWidget
from imgui_bundle import imgui
from imgui_bundle import ImVec2
import time


class ButtonInput(App.App):
    def start(self, name="ButtonInput"):
        # This function will start the app
        super().start(name)
        self.widget = ButtonInputWidget.ButtonInput(name="ButtonInput")


    def render(self):
        # This function will render the app
        self.widget.update()


    def quit(self):
        # This function will quit the app
        self.widget.quit()
        super().quit()