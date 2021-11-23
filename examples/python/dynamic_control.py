"""
Example script to control eV-Technologies FEM "EVT-AFEM-30GHz"
Date 19/11/2021
Licence MIT
"""

import serial
import time

# First connect the device to the computer
# You can list available ports the the following command: "python -m serial.tools.list_ports"
# The default configuration is: 9600, 8, N, 1,no timeout, we could specify but configuring the baudrate is enough
fem = serial.Serial('COM13', 100000)

# Demo function that switch all modes for 5 seconds
def demo_mode():
    for band in range (1,8): # Python range end with the -1 index
        band_str = str(band)
        data_to_send = 'C' + band_str
        # Variable to be sent has to be an ASCII string
        fem.write(data_to_send.encode('ascii'))
        print("Command sent: ", data_to_send)
        # Delay in seconds
        time.sleep(5)

fem.close()
