# Callan M Keller
# Fall 2019
#
# Computer Organization
# Experimenting with Wav

import numpy as np
import wave
import file_io_wav as wavRW
import matplotlib.pyplot as plt

## NOTE: to visualize wav data:  plt.plot(data)


#read .wav file as numpy array
def readIn(file):
    x = wavRW.readWav(file)
    print(x)
    return x


# Reduce amplitude of sound in file by half
# test: halfV('Homestuck_Gold_Pilot.wav', file = 'gpTest.wav')
def halfV(fIn, file = 'test.wav'):
    w = readIn(fIn)
    d = w.data
    r = w.rate
    s = w.sampwidth
    y = np.floor_divide(d, 2)
    wavRW.writeWav(file, y, s, r)
    
    
# Makes a clip from middle of given wav file 1/10th the length of that wav file
# test: centerClip('Body_Blood.wav', file = 'BB_clip1.wav')
def centerClip(fIn, file = 'test.wav'):
    w = readIn(fIn)
    d = w.data
    r = w.rate
    s = w.sampwidth
    length = d.shape[0]
    tenth = length // 10
    startT = length // 2
    endT = startT + tenth
    y = d[startT:endT] 
    wavRW.writeWav(file, y, s, r)
    
