import gui.app as App
import gui.widget as Widget
import widgets.FloatInput as FloatInputWidget
import widgets.ButtonInput as ButtonInputWidget
from imgui_bundle import imgui
from imgui_bundle import ImVec2
import time

from drivers.HT008_Signal_Generator.HT008 import Ht008

class SignalGenerator(App.App):
    def start(self, name="SignalGenerator"):
        # This function will start the app
        super().start(name)
        self.freq_widget = FloatInputWidget.FloatInput(name="Frequency")
        self.freq_widget.allow_input = True
        self.freq_widget.allow_output = False
        self.freq_widget.value = 0.0

        self.but_widget = ButtonInputWidget.ButtonInput(name="Set Frequency")
        self.but_widget.allow_input = True
        self.but_widget.allow_output = False

        self.signal_generator = Ht008()
        self.signal_generator.connect()
        

    def render(self):
        imgui.text("Frequency (MHz):")
        self.freq_widget.update()

        imgui.text("Set Frequency:")
        if self.but_widget.update():
            self.signal_generator.set_single_point(self.freq_widget.value * 1e6, 0)

    def quit(self):
        self.signal_generator.disconnect()
        self.freq_widget.quit()
        super().quit()