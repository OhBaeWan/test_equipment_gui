import gui.app as App
import gui.widget as Widget
import widgets.TextInput as TextInputWidget
from imgui_bundle import imgui
from imgui_bundle import ImVec2
import time


class TextInput(App.App):
    def start(self, name="TextInput"):
        # This function will start the app
        super().start(name)
        self.text = ""
        self.widget = TextInputWidget.TextInput(name="TextInput")



    def render(self):
        # This function will render the app
        imgui.text("Text Input")
        imgui.separator()
        imgui.text("Enter text:")
        if self.widget.update():
            self.text = self.widget.value


    def quit(self):
        # This function will quit the app
        self.widget.quit()
        super().quit()