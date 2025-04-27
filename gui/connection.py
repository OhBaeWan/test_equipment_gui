# An enum to represent the type of connection
from enum import Enum
import gui.GUI as GUI
import threading

class ConnectionType(Enum):
    FLOAT = 1
    INT = 2
    STRING = 3
    BOOL = 4
    EVENT = 5



class Connection:
    def __init__(self, sender, receiver, type:ConnectionType):
        self.sender = sender
        self.receiver = receiver
        self.type = type
        self.id:int = id(self)

        g = GUI.GUI()
        g.state.connections[id(self)] = self

        self.val = None
        self.lock = threading.Lock()

    def get_value(self):
        with self.lock:
            return self.val
        
    def set_value(self, value):
        with self.lock:
            # check that the value is of the same type as the connection
            if self.type == ConnectionType.FLOAT:
                if isinstance(value, float):
                    self.val = value
                else:
                    raise ValueError("Value is not of type float")
            elif self.type == ConnectionType.INT:
                if isinstance(value, int):
                    self.val = value
                else:
                    raise ValueError("Value is not of type int")
            elif self.type == ConnectionType.STRING:
                if isinstance(value, str):
                    self.val = value
                else:
                    raise ValueError("Value is not of type str")
            elif self.type == ConnectionType.BOOL:
                if isinstance(value, bool):
                    self.val = value
                else:
                    raise ValueError("Value is not of type bool")
            elif self.type == ConnectionType.EVENT:
                if isinstance(value, int):
                    self.val = value
                else:
                    raise ValueError("Value is not of type int")
            else:
                raise ValueError("Invalid value type")


        
    def update(self):
        # This function will update the connection
        # and return True if the connection is valid
        if self.sender.value is not None and self.receiver.value is not None:
            if self.type == ConnectionType.FLOAT:
                if isinstance(self.sender.value, float) and isinstance(self.receiver.value, float):
                    self.receiver.value = self.sender.value
                    return True
            elif self.type == ConnectionType.INT:
                if isinstance(self.sender.value, int) and isinstance(self.receiver.value, int):
                    self.receiver.value = self.sender.value
                    return True
            elif self.type == ConnectionType.STRING:
                if isinstance(self.sender.value, str) and isinstance(self.receiver.value, str):
                    self.receiver.value = self.sender.value
                    return True
            elif self.type == ConnectionType.BOOL:
                if isinstance(self.sender.value, bool) and isinstance(self.receiver.value, bool):
                    self.receiver.value = self.sender.value
                    return True
            elif self.type == ConnectionType.EVENT:
                if isinstance(self.sender.value, int) and isinstance(self.receiver.value, int):
                    self.receiver.value = self.sender.value
                    return True
        return False     