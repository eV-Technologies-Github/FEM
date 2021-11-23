"""
Example script to control eV-Technologies FEM "EVT-AFEM-30GHz"
Date 19/11/2021
Licence MIT
"""

import serial

# First connect the device to the computer
# You can list available ports the the following command: "python -m serial.tools.list_ports"
# The default configuration is: 9600, 8, N, 1,no timeout, we could specify but configuring the baudrate is enough
fem = serial.Serial('COM13', 100000)

# Send the command "C1" to choose the frequency band 10MHz - 30GHz
fem.write(b"\C1")
# Send the command "C6" to choose the frequency band 2GHz - 5GHz
fem.write(b"\C6")
# Send the command "D00" to set the digital attenuator to 0
fem.write(b"\D00")
# Send the command "V2100" to set the attenuator 2 to 100
fem.write(b"\V2100")
# Send the command "F2351" to set the filter to 235 and bank 1
fem.write(b"\F2351")

# Close the connection
fem.close()
