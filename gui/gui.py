# the gui is a singleton class, it manages the GUI and the main loop
# it holds starts and manages the apps, and facilitates communication between them
# it is the main entry point for the GUI
# it is responsible for loading the config and setting up the GUI

from imgui_bundle import imgui, immapp, ImVec2
from imgui_bundle import glfw_utils

import time

import importlib
import sys
import os
# Add the parent directory to the sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

class GUIState:
    def __init__(self):
        self.apps = []
        self.maximize_apps = False


class GUI:
    # Singleton instance
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._init()
        return cls._instance

    def _init(self):
        print("Initializing GUI")
        self.state = GUIState()
        immapp.run(
            gui_function=self.update,  # The Gui function to run
            window_title="Test_Equipment_Gui",  # the window title
            window_size_auto=True,  # Auto size the application window given its widgets
            # Uncomment the next line to restore window position and size from previous run
            window_restore_previous_geometry=True,
            fps_idle=144,  # The maximum frame rate when the window is not active
        )
    

    def menue_bar(self):
        # menu bar
        imgui.begin_main_menu_bar()
        if imgui.begin_menu("File", True):
            if imgui.menu_item_simple("Exit", "E", False, True):
                print("Exit clicked")
                immapp.quit()
                pass
            imgui.end_menu()
        if imgui.begin_menu("Apps", True):
            # Discover all apps
            apps = self.discover_apps()
            for app in apps:
                if imgui.menu_item_simple(app, "", False, True):
                    print(f"App {app} clicked")
                    self.start_app(app)
            imgui.end_menu()
        imgui.end_main_menu_bar()


    def update(self):
        self.menue_bar()

        imgui.get_io().config_flags |= imgui.ConfigFlags_.docking_enable
        size = imgui.get_content_region_avail()
        size.y -= imgui.get_frame_height_with_spacing()
        imgui.set_next_window_pos(ImVec2(0, imgui.get_frame_height_with_spacing() - 3))
        imgui.begin("DockSpace", None ,imgui.WindowFlags_.no_title_bar | imgui.WindowFlags_.no_resize | imgui.WindowFlags_.no_move | imgui.WindowFlags_.no_scrollbar)
        imgui.set_window_size("DockSpace", (size.x - 1, size.y))
        imgui.dock_space(imgui.get_id("DockSpace"), size, imgui.DockNodeFlags_.passthru_central_node)
        for app in self.state.apps:
            if app is not None:
                app.update(size)
        imgui.end()
        

        
    # discover all apps in the apps directory
    def discover_apps(self):
        # This function will discover all apps in the apps directory
        # and return a list of app names
        apps = []
        for filename in os.listdir("apps"):
            if filename.endswith(".py") and filename != "__init__.py":
                app_name = filename[:-3]
                apps.append(app_name)
        return apps
    
    # load the app by name
    def load_app(self, app_name):
        # This function will load the app by name
        # and return the app instance
        try:
            module = importlib.import_module(f"apps.{app_name}")
            app = module.App()
            return app
        except ImportError as e:
            print(f"Error loading app {app_name}: {e}")
            return None
        
    # start the app
    def start_app(self, app_name):
        # This function will start the app by name
        # and return the app instance
        app = self.load_app(app_name)
        if app is not None:
            app.start()
            self.state.apps.append(app)
            return app
        else:
            print(f"Error starting app {app_name}")
            return None

if __name__ == "__main__":
    gui = GUI()