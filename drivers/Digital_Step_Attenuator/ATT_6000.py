import serial
from serial.tools import list_ports
import time

class ATT_6000: # '/dev/ttyUSB1'
    def __init__(self, port=None, baudrate=115200):
        self.port = port
        self.baudrate = baudrate
        self.ser = None

        # Initialize the state of the attenuator
        self.current_attenuation = 0  # dB
        self.max_attenuation = 30      # dB

    def connect(self):
        if self.port is None:
            ports = list_ports.comports()
            for p in ports:
                if p.device is not None:
                    # check if the port is available
                    print(f"Trying port {p.device}...")
                    # try to open the port with the given baudrate
                    # if it fails, try the next one
                    # if it succeeds, check if the output is correct
                    # if it is, break out of the loop
                    # if it isn't, try the next one
                    try:
                        self.ser = serial.Serial(p.device, self.baudrate, exclusive=True)
                        print(f"Connected to {p.device} at {self.baudrate} baud.")
                        # send a command to the device to check if it is responding
                        cmd = "wv0" + self.convert_to_cmd_format(self.max_attenuation) + "\n"
                        self.ser.write(cmd.encode())
                        time.sleep(0.5)
                        # read the response 
                        response = self.ser.read(self.ser.in_waiting)
                        # check the response
                        # if the response is correct, break out of the loop
                        # if it is not, try the next one
                        # check if the response is correct
                        if "ok" in response.decode('utf-8'):
                            # if we get here, the port is correct
                            # print the power reading
                            print(f"Valid data from {p.device} at {self.baudrate} baud.")
                            self.port = p.device
                            break
                        else:
                            # if we get here, the port is correct
                            # print the power reading
                            print(response)
                            print(f"Port {p.device} has invalid data")
                            # close the port
                            self.ser.close()
                    except Exception as e:
                        print(f"Port {p.device} not available")
                        print(f"Error: {e}")
                        self.ser.close()
                        continue
            # if we get here and self.port doesnt exist, no port was found
            # raise an exception
            if self.port is None:
                print("No available ports found")
                raise Exception("No available ports found")
        else:
            try:
                self.ser = serial.Serial(self.port, self.baudrate, exclusive=True)
                print(f"Connected to {self.port} at {self.baudrate} baud.")
            except Exception as e:
                print(f"Port {self.port} not available")
                print(f"Error: {e}")
                raise Exception(f"Port {self.port} not available")
    
    def disconnect(self):
        if self.ser:
            self.ser.close()
            print("Disconnected.")

    def convert_to_cmd_format(self, value):
        # Convert the value to 4 digit number with leading zeros and the last two digits as decimal
        if value < 0:
            value = 0
        elif value > self.max_attenuation:
            value = self.max_attenuation
        # Convert to string and pad with leading zeros
        cmd_format = f"{int(value * 100):04d}"
        return cmd_format

    def set_attenuation(self, attenuation):
        if attenuation < 0:
            attenuation = 0
        elif attenuation > self.max_attenuation:
            attenuation = self.max_attenuation
            #raise ValueError(f"Attenuation must be between 0 and {self.max_attenuation} dB.")
        
        # Send command to set attenuation
        command = f"wv0{self.convert_to_cmd_format(attenuation)}\n"
        self.ser.write(command.encode())
        # print the readback
        readback = self.ser.read_until(b'\n').decode().strip()
        print(f"Readback: {readback}")
        
        
        # Update current attenuation
        self.current_attenuation = attenuation
        print(f"Set attenuation to {attenuation} dB.")
    
    def get_current_attenuation(self):
        return self.current_attenuation


if __name__ == "__main__":
    # Example usage
    attenuator = ATT_6000()
    try:
        attenuator.connect()
        attenuator.set_attenuation(10)  # Set to 10 dB
        time.sleep(1)
        #attenuator.set_attenuation(20)  # Set to 20 dB
    finally:
        attenuator.disconnect()