from imgui_bundle import imgui, ImVec2
import time


class App:
    def start(self):
        # This function will start the app
        # and return the app instance
        self.name = "App"
        self.id = f"{self.name}.{time.time()}" 
        self.running = True
        self.last_frame_hover = False

    def update(self, size):
        if not self.running:
            return False
        
        _, open = imgui.begin(f"{self.name}##{self.id}", True, 0)


        if imgui.is_mouse_hovering_rect(ImVec2(imgui.get_window_pos().x, imgui.get_window_pos().y - imgui.get_frame_height_with_spacing()), imgui.get_window_pos() + imgui.get_window_size()):
            if not self.last_frame_hover:
                imgui.set_window_focus(f"{self.name}##{self.id}")
            self.last_frame_hover = True
        else:
            self.last_frame_hover = False

        if open:
            self.render()
            imgui.text(f"Docked: {imgui.is_window_docked()}")
            imgui.text(f"Focused: {imgui.is_window_focused()}")
            imgui.text(f"Hovered: {self.last_frame_hover}")
            imgui.end()
        else:
            imgui.end()
            print("Window closed")
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
