import gui.app as App
import gui.widget as Widget
import widgets.FloatInput as FloatInputWidget
import widgets.ButtonInput as ButtonInputWidget
from imgui_bundle import imgui
from imgui_bundle import ImVec2
import time

from drivers.Digital_Step_Attenuator.ATT_6000 import ATT_6000

class DigitalStepAttenuator(App.App):
    def start(self, name="DigitalStepAttenuator"):
        # This function will start the app
        super().start(name)
        self.attenuation_widget = FloatInputWidget.FloatInput(name="Attenuation")
        self.attenuation_widget.allow_input = True
        self.attenuation_widget.allow_output = False
        self.attenuation_widget.value = 0.0

        self.but_widget = ButtonInputWidget.ButtonInput(name="Set Attenuation")
        self.but_widget.allow_input = True
        self.but_widget.allow_output = False

        self.digital_step_attenuator = ATT_6000()
        self.digital_step_attenuator.connect()
        self.digital_step_attenuator.set_attenuation(0)

    def render(self):
        imgui.text("Attenuation (dB):")
        self.attenuation_widget.update()

        imgui.text("Set Attenuation:")
        if self.but_widget.update():
            self.digital_step_attenuator.set_attenuation(self.attenuation_widget.value)
            self.attenuation_widget.value = self.digital_step_attenuator.get_current_attenuation()
            print(f"Set attenuation to {self.attenuation_widget.value} dB")

    def quit(self):
        self.digital_step_attenuator.disconnect()
        self.attenuation_widget.quit()
        super().quit()