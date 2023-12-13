# Radar_Breathing_detection
Radar Breathing Detection: CS 437

This system is designed to detect breathing using radar to measure stomach micro-movements using the phase obtained from the phase Doppler profile. To operate the system, either collect raw ADC data or use one of the four preexisting files within this repository. In BreathSensing.ipynb, you can graphically display the processed phase information, get the breathing rate, and identify inhale/exhale peaks. The paths must be changed accordingly to the correct path throughout the code. Additionally, multiple data files and their ground truth breathing rates can be compared in the last cell of this notebook.

breathing.py and not_breathing.py are files run in a Raspberry Pi environment. breathing is used to simply play back the inhale-exhale periods in red/blue increments on the LED matrix while not_breathing also will send a UDP message saying "stopped breathing" if breathing is not detected for 15 seconds. Make sure you are running UDP_server.py on another device, and the and Ip addresses are matching. This can be used in tandem with graphical analysis to provide a more secure healthcare system.
