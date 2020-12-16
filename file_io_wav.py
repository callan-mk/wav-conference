# Callan M Keller
# Fall 2019
#
# Computer Organization
# Wav file I/O

import numpy as np
import wave as w

## Functions (where marked) copied from Wavio source code:
    # https://github.com/WarrenWeckesser/wavio/blob/master/wavio.py

## Wav data interpretation notes:
    # nchannels indicates number of audio channels (1 for mono, 2 for stereo).
    # framerate = sampling frequency
    # nframes = total number of audio frames

# -------------------------------------------------------------------------------------------------
# Read wav files.

#opens .wav file in base python read-only mode
def toRead(file):
    x = w.open(file, mode='rb')
    return x

def readFrames(wavObj, params):
    frames = params[3]
    data = wavObj.readframes(frames)
    return data

# wav2array copied from wavio
def wav2array(nchannels, sampwidth, data):
    """data must be the string containing the bytes from the wav file."""
    num_samples, remainder = divmod(len(data), sampwidth * nchannels)
    if remainder > 0:
        raise ValueError('The length of data is not a multiple of '
                         'sampwidth * num_channels.')
    if sampwidth > 4:
        raise ValueError("sampwidth must not be greater than 4.")

    if sampwidth == 3:
        a = np.empty((num_samples, nchannels, 4), dtype=np.uint8)
        raw_bytes = np.frombuffer(data, dtype=np.uint8)
        a[:, :, :sampwidth] = raw_bytes.reshape(-1, nchannels, sampwidth)
        a[:, :, sampwidth:] = (a[:, :, sampwidth - 1:sampwidth] >> 7) * 255
        result = a.view('<i4').reshape(a.shape[:-1])
    else:
        # 8 bit samples are stored as unsigned ints; others as signed ints.
        dt_char = 'u' if sampwidth == 1 else 'i'
        a = np.frombuffer(data, dtype='<%s%d' % (dt_char, sampwidth))
        result = a.reshape(-1, nchannels)
    return result

# user-end function
def readWav(file):
    wavObj = toRead(file)
    params = wavObj.getparams()
    data = readFrames(wavObj, params)
    wavObj.close()

    array = wav2array(params[0], params[1], data)
    out = Wav(data=array, rate=params[2], sampwidth=params[1])
    return out
    
    
# ---------------------------------------------------------------------------------------------------
# Write wav files.

#opens .wav file in base python write-only mode
def toWrite(file='test.wav'):
    x = w.open(file, mode = 'wb')
    return x

# array2wav copied from wavio
def array2wav(a, sampwidth):
    """
    Convert the input array `a` to a string of WAV data.
    a.dtype must be one of uint8, int16 or int32.  Allowed sampwidth
    values are:
        dtype    sampwidth
        uint8        1
        int16        2
        int32      3 or 4
    When sampwidth is 3, the *low* bytes of `a` are assumed to contain
    the values to include in the string.
    """
    if sampwidth == 3:
        # `a` must have dtype int32
        if a.ndim == 1:
            # Convert to a 2D array with a single column.
            a = a.reshape(-1, 1)
        # By shifting first 0 bits, then 8, then 16, the resulting output
        # is 24 bit little-endian.
        a8 = (a.reshape(a.shape + (1,)) >> np.array([0, 8, 16])) & 255
        wavdata = a8.astype(np.uint8).tostring()
    else:
        # Make sure the array is little-endian, and then convert using
        # tostring()
        a = a.astype('<' + a.dtype.str[1:], copy=False)
        wavdata = a.tostring()
    return wavdata

# user-end function
def writeWav(file, npData, sampwidth, framerate):
    wavObj = toWrite(file)
    wavdata = array2wav(npData, sampwidth)
    wavObj.setnchannels(npData.shape[1])
    wavObj.setsampwidth(sampwidth)
    wavObj.setframerate(framerate)
    wavObj.setnframes(npData.shape[0])
    #wavObj.setparams(channels, sampwidth, framerate, frames, 'NONE', 'not compressed')
    wavObj.writeframes(wavdata)
    wavObj.close()
    
# ---------------------------------------------------------------------------------------------------
# Wav data storage type,pretty much copied from wavio.
class Wav(object):
    """
    Object returned by `readWav`.  Attributes are:
    data : numpy array
        The array of data read from the WAV file. The shape of the array is 
        (nframes, nchannels).
        The data type of the array (i.e. data.dtype) is determined by `sampwidth`::
                sampwidth      dtype
                    1          numpy.uint8
                    2          numpy.int16
                    3          numpy.int32
                    4          numpy.int32
    rate : float
        Framerate of file.
    sampwidth : int
        The sample width (i.e. number of bytes per sample) of the WAV file.
        For example, `sampwidth == 3` is a 24 bit WAV file.
    """

    def __init__(self, data, rate, sampwidth):
        self.data = data
        self.rate = rate
        self.sampwidth = sampwidth

    def __repr__(self):
        s = ("Wav(data.shape=%s, data.dtype=%s, framerate=%r, sampwidth=%r)" %
             (self.data.shape, self.data.dtype, self.rate, self.sampwidth))
        return s