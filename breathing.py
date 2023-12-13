from sense_hat import SenseHat
from time import sleep

sense=SenseHat()


red = [255, 0, 0]
blue= [0, 0, 255]
#Will change the LED matrix depending on the relative time periods of the inhale/exhales
def show(inh, exh):
    hue = 0
    sense.clear()
    currTime=0
    for i in range(len(inh)):
        print(i)
        sense.set_pixels([red]*64)
        sleep(inh[i]-currTime)
        currTime=inh[i]
        sense.set_pixels([blue]*64)
        sleep(exh[i]-currTime)
        currTime=exh[i]
       



#####
# import required libraries
sense.clear()
import struct

import sys

import serial

import binascii

import time

import numpy as np

import math

 

import os

import datetime

import matplotlib.pyplot as plt

#/Users/djbautista/Desktop/437/radar/data_12_01_2023_17_52_47.npy

rawData = np.load("/home/pi/Downloads/data_12_01_2023_17_52_47.npy")

data = np.array([frame["adcSamples"][:, 128:] for frame in rawData])

data.shape # chirp* rx * samples per chirp

#########

rangeData = np.fft.fftn(data, axes=(2,))

closest=rangeData[:,:,1]

rangeDoppler = np.fft.fftn(closest, axes=(0,))

doppler=rangeDoppler[:,0]

angles = np.angle(doppler)

window_size=30

inhales = [1.5, 5.1, 9.8, 19.04, 28.4, 35.79]
exhales=[3.1, 9, 12.6, 23.9, 33.5, 37.2]
 

closest1 = rangeData[:,:,2]

rangeDoppler2 = np.fft.fftn(closest1, axes=(0,))

doppler2=rangeDoppler2[:,0]

angles2 = np.angle(doppler2)

cumsum2= np.cumsum(np.insert(angles2,0,0))

smoothed_data2=(cumsum2[window_size:]-cumsum2[:-window_size])/float(window_size)

 

cumsum= np.cumsum(np.insert(angles,0,0))

smoothed_data=(cumsum[window_size:]-cumsum[:-window_size])/float(window_size)

 


#############

import numpy as np

from scipy.signal import find_peaks

import matplotlib.pyplot as plt

 

def calculate_breathing_rate(inhale_peaks, time_per_sample):

    # Calculate time differences between consecutive inhales

    inhale_times = inhale_peaks * time_per_sample

    inhale_time_diff = np.diff(inhale_times)

 

    # Calculate breathing rate (breaths per minute)

    breathing_rate = 60 / np.mean(inhale_time_diff)

 

    return breathing_rate

 

def label_breathing_pattern(heights, prominence_threshold):

    # Find peaks (inhales)

    peaks, _ = find_peaks(heights, distance=10, prominence=prominence_threshold)

 

    # Find minima (exhales)

    minima, _ = find_peaks(-heights, distance=10, prominence=prominence_threshold)

 

    # Combine peaks and minima indices

    events = np.sort(np.concatenate([peaks, minima]))

 

    # Create a label array

    labels = np.zeros_like(heights, dtype=int)

 

    # Assign labels to inhales (1) and exhales (-1)

    labels[events] = np.where(np.isin(events, peaks), 1, -1)

 

    return labels, peaks, minima

# Example usage:

# Your array of points representing stomach compression heights

prominence_threshold = 0.8  # Adjust this threshold as needed

 

# Assuming each sample is separated by 0.0525 seconds

time_per_sample = 0.0525

 

breathing_labels, inhale_peaks, _ = label_breathing_pattern(smoothed_data, prominence_threshold)

 

# Calculate breathing rate

rate = calculate_breathing_rate(inhale_peaks, time_per_sample)

 

print(f"Breathing Rate: {rate:.2f} breaths per minute")

 

# Plot the heights with peaks and minima highlighted

import numpy as np

import matplotlib.pyplot as plt

from scipy.signal import find_peaks

 
time_ratio = 18.8
 

# Example usage:

prominence_threshold = 0.8  # Adjust this threshold as needed

 

breathing_labels, exhale_minima, inhale_peaks = label_breathing_pattern(smoothed_data, prominence_threshold)

inhale_peaks_c=inhale_peaks

exhale_minima_c=exhale_minima

# Plot the heights with peaks and minima highlighted

smoothed_data*=2.3

'''

for i in range(0, len(exhale_minima), 2):

    plt.axvspan(inhale_peaks[i], exhale_minima[i], color='red', alpha=0.3, label='Exhale Region')

'''

show(inhale_peaks_c/time_ratio, exhale_minima_c/time_ratio)
