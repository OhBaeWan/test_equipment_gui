import serial
from serial.tools import list_ports
import time

def forward_pad_string_with_zeros(string, length):
        return "0" * (length - len(string)) + string


class Ht008: #'/dev/ttyUSB0'
    def __init__(self, port=None, baudrate=115200):
    
        self.port = port
        self.baudrate = baudrate
        self.ser = None
        #
        self.x = []
        self.y = []

        self.frequency = 100e6 # 100 MHz
        self.amplitude = 1.0 # dBm

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
                        cmd = "55 55 00 00 00 00 00 0D 0A" # 100 MHz
                        cmd = bytes.fromhex(cmd)
                        self.ser.write(cmd)
                        time.sleep(0.1)
                        # read the response
                        response = self.ser.read(self.ser.in_waiting)
                        # check the response
                        # if the response is correct, break out of the loop
                        # if it is not, try the next one
                        # check if the response is correct
                        if "OK" in response.decode('utf-8'):
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
    
    def disconnect(self):
        self.ser.close()

    # static

    
        
    def set_single_point(self, frequnecy, power):
        self.frequency = frequnecy
        

        #the first two bytes are the whole frequency in MHz
        #the third and fourth bytes are the decimal part of the frequency in MHz

        freq = int(frequnecy / 1e6)

        byte_1 = forward_pad_string_with_zeros(str(hex(freq)).replace("0x", ""), 4)[:2]
        byte_2 = forward_pad_string_with_zeros(str(hex(freq)).replace("0x", ""), 4)[2:]

        byte_3 = "00"

        byte_4 = "00"  
        

        # the fifth byte is amplitude which can be 0, 1, 2, or 3
        if power < 0:
            power = 0
        if power > 3:
            power = 3
        self.amplitude = power
        byte_5 = forward_pad_string_with_zeros(str(power), 2)

        print(byte_5)

        #cmd = "55 55 00 64 00 00 00 0D 0A" # 100 MHz
        cmd = "55 55 {} {} {} {} {} 0D 0A".format(byte_1, byte_2, byte_3, byte_4, byte_5)

        print(cmd)

        cmd = bytes.fromhex(cmd)
        self.ser.write(cmd)

    



if __name__ == "__main__":
    sg = Ht008()

    sg.connect()

    print("Setting single point")
    #sg.set_single_point(3207e6, 0)

    #time.sleep(5)

    print("Turning off")
    sg.set_single_point(0, 0)


    sg.disconnect()
    # sweep from 100 MHz to 800 MHz 1 MHz at a time with 0 dBm power
    '''
    for i in range(100, 5200, 10):
        sg.set_single_point(i * 1e6, 0)
        time.sleep(15)
'''
