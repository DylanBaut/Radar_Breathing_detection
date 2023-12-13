# Radar_Breathing_detection
Radar Breathing Detection: CS 437

This system is designed to detect breathing using radar to measure stomach micro-movements using the phase obtained from the phase Doppler profile. To operate the system, either collect raw ADC data or use one of the four preexisting files within this repository. To collect data, use the attached .cfg file inside the Industrial Visualizer and then pass the pathname of the corresponding bin into the parse_bin_data.py file inside the quotes. In BreathSensing.ipynb, you can graphically display the processed phase information, get the breathing rate, and identify inhale/exhale peaks. Simply run the cells in order and the paths must be changed accordingly to the correct path throughout the code. Additionally, multiple data files and their ground truth breathing rates can be compared in the last cell of this notebook. Comparisons of measurements from varying distances and between different people are already shown.

breathing.py and not_breathing.py are files run in a Raspberry Pi environment. breathing is used to simply play back the inhale-exhale periods in red/blue increments on the LED matrix while not_breathing also will send a UDP message saying "stopped breathing" if breathing is not detected for 15 seconds. Make sure you are running UDP_server.py on another device, and that the UDP port numbers and IP addresses are matching. This can be used in tandem with graphical analysis to provide a more secure healthcare system.

(.npy files ending with 47, 36, 20, and 02 are at distances of 4 cm, 8cm, 12cm, and 16cm respectively)
(.npy files ending with 47, 55, 17, and 07 are with four separate people)
