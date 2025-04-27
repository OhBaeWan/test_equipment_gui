import gui.app as App
import gui.widget as Widget
import widgets.FloatDisplay as FloatDisplayWidget
from imgui_bundle import imgui
from imgui_bundle import ImVec2
import time

from drivers.RF_Power_Meter.RF_Power_Meter import RF_Power_Meter

class PowerMeter(App.App):
    def start(self, name="PowerMeter"):
        # This function will start the app
        super().start(name)
        self.widget = FloatDisplayWidget.FloatDisplay(name="PowerMeter")
        self.widget.allow_input = False
        self.widget.allow_output = True
        self.value = 0.0
        self.widget.value = self.value
        self.power_meter = RF_Power_Meter()
        

    def render(self):
        self.value = self.power_meter.read()
        self.widget.value = self.value
        self.widget.update()

    def quit(self):
        self.power_meter.disconnect()
        self.widget.quit()
        super().quit()