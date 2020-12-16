# Callan M Keller
# Fall 2019
#
# Computer Organization
# Experimenting with Frequency Weighting

import numpy as np
import matplotlib.pyplot as plt

import cmk_wave_analyzer as wvA
#import CMK_wavIO_test as wt
#import cmk_meter as meter

"""
Currently testing how to use the much more comprehensible (and recent!) filtering design from 
endolith's waveform-analysis code, esp. ABC_weighting.
"""

# Prints full analysis per endolith's wave analysis functions
def analyzeFile(fIn):
    wvA.analyze(fIn)
    
# returns average of all channels' scaled, A-weighted RMS levels
# accesses function in cmk_wave_analyzer that calculates this
def avgLoudness(fIn):
    x = wvA.rmsA(fIn)
    return x

# compares relative loudness, by A-weighted RMS levels, of two given wav files.
def compareLoud(f1, f2):
    x = avgLoudness(f1)
    y = avgLoudness(f2)
    if x > y:
        print(f1, ' is louder than ', f2)
    elif y > x:
        print(f2, ' is louder than ', f1)
    elif y == x:
        print('files have same loudness')         
    return x, y


"""
meter, iirfilter, and audio_validate very lightly adapted from pyloudnorm package.
pyloudnorm required packages:
    future, numpy, textwrap, scipy


#test: howLoud('Homestuck_Gold_Pilot.wav')
def howLoud(file):
    x = wt.readIn(file) #load audio as ndarray
    d = x.data
    r = x.rate
    m = meter.Meter(r) # create BS.1770 meter
    loudness = m.integrated_loudness(d) # measure loudness
    return loudness

def compareLoud(f1, f2):
    x = howLoud(f1)
    y = howLoud(f2)
    if x > y:
        print(f1, ' is louder than ', f2)
    elif y > x:
        print(f2, ' is louder than ', f1)
    elif y == x:
        print('files have same loudness')         
    return x, y
"""