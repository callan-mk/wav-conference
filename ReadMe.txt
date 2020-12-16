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
I included a function to make shorter clips, as we discussed. However, I did not end up creating functions to remove sound withing a specific
	frequency range from given .wav file, or to calculate the rms for a specific frequency range as, upon further investigation, I realized
	that doing so would require a much deeper understanding of fourier transforms than I currently possess. (I've never been all that great
	at trigonometry to be entirely honest.) Given this very significant roadblock, I decided that it would be more productive to focus on
	getting a working scaled loudness comparison function operational, as demonstrated in test_wav_loudness. I hope this is a reasonable 
	substitution on my part.
I ran into a lot of dead ends in my research on this project as, unsurprisingly, audio encoding is very complex! I hope my results enclosed herein
	are satisfactory, at least in showing what I've learned throughout the process of researching this topic.
My zip file includes 5 .wav files: the three full-length songs I used to test various functions throughout this project, and two sample clips
	created from two of those songs using centerClip.
The folder waveform_analysis_master is included for reference purposes, as I used this package both for helper functions and as reference material,
	and so I thought it might be useful to include the code from the package in my submission.
