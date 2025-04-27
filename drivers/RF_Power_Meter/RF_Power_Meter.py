import serial
from serial.tools import list_ports
import matplotlib.pyplot as plt
import numpy as np
import time
import threading


class RF_Power_Meter:
    def __init__(self, port=None, baudrate=115200):
        # if port is None, search for the correct port to use
        if port is None:
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
                        self.ser = serial.Serial(p.device, baudrate, exclusive=True)
                        # check if the output is correct
                        #wait for some data to arrive
                        time.sleep(0.1)
                        data = self.ser.read(self.ser.in_waiting).decode('utf-8')
                        # Split the data into individual readings, separated by '-'
                        readings = data.split('-')
                        for reading in readings:
                            if reading.endswith('u'):
                                # check the reading is the correct length 
                                if len(reading) == 9:
                                    # convert the reading to dBm
                                    power = -int(reading[:-1]) / 1000000
                                    # if we get here, the port is correct
                                    # print the power reading
                                    print(f"RF Power: {power:.1f} dBm")
                                    print(f"Connected to {p.device} at {baudrate} baud.")
                                    self.port = p.device
                                    break
                        if not hasattr(self, 'port'):
                            print(f"Port {p.device} has invalid data")
                            # close the port
                            self.ser.close()
                        else:
                            # if we get here, the port is correct
                            # break out of the loop
                            break
                    except Exception as e:
                        self.ser.close()
                        # if the port is not available, try the next one
                        print(f"Port {p.device} not available")
                        print(f"Error: {e}")
                        continue

                    
            # if we get here and self.port doesnt exist, no port was found
            # raise an exception
            if not hasattr(self, 'port'):
                print("No available ports found")
                raise Exception("No available ports found")
                      
        else:
            self.port = port
        self.baudrate = baudrate
        self.ser = None
        #
        self.x = []
        self.y = []
        self.connect()
        self.running = True
        self.thread = threading.Thread(target=self._read)
        self.thread.start()
        

    def connect(self):
        try:
            self.ser = serial.Serial(self.port, self.baudrate, exclusive=True)
            print(f"Connected to {self.port} at {self.baudrate} baud.")
        except serial.SerialException as e:
            print(f"Error: {e}")
            raise e
    
    def disconnect(self):
        self.running = False
        self.thread.join()
        self.ser.close()
        print(f"Power Meter disconnected from {self.port}.")
    
    def read (self):
        # check if the data is empty
        if len(self.x) == 0 or len(self.y) == 0:
            # if it is, return None
            return 0
        return self.y[-1]
        
    def _read(self):
        while self.running:
            try:
                if self.ser.in_waiting > 0:
                    power = -9999
                    # Read data from serial port, there are no newlines in the data stream so we need to use read() instead of readline()
                    data = self.ser.read(self.ser.in_waiting).decode('utf-8')
                    # Split the data into individual readings, separated by '-'
                    readings = data.split('-')
                    for reading in readings:
                        if reading.endswith('u'):
                            # check the reading is the correct length 
                            if len(reading) == 9:
                                # convert the reading to dBm
                                power = -int(reading[:-1]) / 1000000
                    #print(f"RF Power: {power:.1f} dBm")
                    self.x.append(time.time())
                    self.y.append(power)
                    time.sleep(0.1)
            except serial.SerialException as e:
                print(f"Error: {e}")

    



if __name__ == "__main__":
    # make a live plot of the data
    power_meter = RF_Power_Meter()
    try:
        plt.ion()
        fig, ax = plt.subplots()
        line, = ax.plot(power_meter.x, power_meter.y)
        ax.set_ylim(-100, 0)
        ax.set_xlabel('Time (s)')
        ax.set_ylabel('Power (dBm)')
        ax.set_title('RF Power Meter')
        while True:
            try:
                power = power_meter.read()
            except:
                print("Error reading power")
            line.set_xdata(power_meter.x)
            line.set_ydata(power_meter.y)
            ax.relim()
            ax.autoscale_view()
            plt.pause(0.1)
            fig.canvas.flush_events()
    except:
        power_meter.disconnect()
        plt.ioff()
        #plt.show()
        print("Exiting...")
