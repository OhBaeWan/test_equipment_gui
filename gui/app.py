from imgui_bundle import imgui, ImVec2
import time


class App:
    def start(self, name=""):
        # Non unique descriptor for the app
        self.name:str = name
        # Unique descriptor for the app
        self.id:int = id(self)

        # app state
        self.running = False
        self.last_frame_hover = False
        self.running = True
        self.first_frame = True

    def update(self) -> bool:
        if not self.running:
            return False
        
        if self.first_frame:
            _, open = imgui.begin(f"{self.name}##{self.id}", True, imgui.WindowFlags_.always_auto_resize)
            self.first_frame = False
        else:
            _, open = imgui.begin(f"{self.name}##{self.id}", True, 0)


        if imgui.is_mouse_hovering_rect(ImVec2(imgui.get_window_pos().x, imgui.get_window_pos().y - imgui.get_frame_height_with_spacing()), imgui.get_window_pos() + imgui.get_window_size()):
            if not self.last_frame_hover:
                imgui.set_window_focus(f"{self.name}##{self.id}")
            self.last_frame_hover = True
        else:
            self.last_frame_hover = False

        if open:
            self.render()
            imgui.end()
        else:
            imgui.end()
            #print("Window closed")
            # If the window is closed, quit the app
            self.quit()
        
        return True

    def render(self):
        # This function will render the app

        pass

    def quit(self):
        # This function will quit the app
        self.running = False
        pass
