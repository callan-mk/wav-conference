Callan M Keller
Fall 2019
Computer Organization

Required packages for the enclosed code to run correctly:
numpy, wave, matplotlib, scipy, waveform_analysis
	waveform_analysis can be installed using: pip install git+https://github.com/endolith/waveform_analysis.git@master


The main high-level files are cmk_wavMain, and test_wav_loudness. Other files include functions which are called in those two functions,
	or are included for reference purposes.


Primary functions:

cmk_wavMain:
readIn reads a given .wav file, returns data from that file as a numpy array that can be manipulated from there.
halfV shows a basic use case for the read and write functions I created in file_io_wav, by reducing the amplitude of sound in a given file by half.
centerClip is mostly a utility function. It makes a clip from the center of the data in a given wav file to 1/10th the length of that wav file 
	after the center point.

test_wav_loudness:
analyzeFile prints the full analysis of data in a given .wav file, per endolith's wave analysis functions.
avgLoudness for a given .wav file, returns the average of all channels' scaled, A-weighted RMS levels.
compareLoud prints the results of a comparison of relative loudness of two given .wav files, by A-weighted RMS levels.



Notes:
I included a function to make shorter clips, as discussed. I decided that it would be most productive to focus on getting a working scaled loudness comparison function operational, as 	demonstrated in test_wav_loudness. 
The folder waveform_analysis_master is not mine, but is included as I used this package both for helper functions and as reference material.
