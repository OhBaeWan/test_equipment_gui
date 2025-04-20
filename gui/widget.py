import time
from imgui_bundle import imgui, ImVec2
import gui.GUI as GUI
import gui.connection as connection

class Widget:
    def __init__(self, name: str):
        self.name:str = name
        self.id:int = id(self)

        self.value = None

        self.in_conn = None
        self.in_conn_id = None

        self.out_conn = {}

        self.allow_input = True
        self.allow_output = True

        self.type = connection.ConnectionType.EVENT

        GUI.GUI().state.widgets[self.id] = self



    def update(self) -> bool:
        # This function will update the widget
        if self.allow_input:
            imgui.button(f"Input##{self.id}")
            if imgui.begin_drag_drop_target():
                payload = imgui.accept_drag_drop_payload_py_id("widget")
                if payload:
                    # Handle the payload here
                    print(f"Received payload: {payload.data_id}")
                    # create a connection between the sender and receiver
                    sender = GUI.GUI().state.widgets[payload.data_id]
                    # remove the previous connection if it exists
                    if self.in_conn != None:
                        try:
                            GUI.GUI().state.connections.pop(self.in_conn.id, None)
                            # remove the connection from the previous senders out_conn
                            GUI.GUI().state.widgets[self.in_conn.id].out_conn.pop(self.id, None)
                        except Exception as e:
                            print(f"Error removing connection: {e}")
                            

                    self.in_conn = connection.Connection(sender, self, self.type)
                    self.in_conn_id = self.in_conn.id
                    # add the connection to the senders out_conn
                    sender.out_conn[self.id] = self.in_conn

                imgui.end_drag_drop_target()
        
            imgui.same_line()

        r = self.render()

        if self.allow_output:
            imgui.same_line()
            imgui.button(f"Output##{self.id}")
            if imgui.begin_drag_drop_source():
                imgui.set_drag_drop_payload_py_id("widget", self.id)
                imgui.button(f"{self.name}##{self.id}")
                imgui.end_drag_drop_source()
        return r

    def render(self) -> bool:
        # This function will render the widget
        return False
    
    def quit(self):
        # This function will quit the widget
        GUI.GUI().state.widgets.pop(self.id, None)
        if self.in_conn != None:
            GUI.GUI().state.connections.pop(self.in_conn.id, None)
        # remove the connection for all the connections in the out_conn
        for conn in self.out_conn.values():
            GUI.GUI().state.connections.pop(conn.id, None)
    def __del__(self):
        # This function will quit the widget
        GUI.GUI().state.widgets.pop(self.id, None)
        if self.in_conn != None:
            GUI.GUI().state.connections.pop(self.in_conn.id, None)
        pass