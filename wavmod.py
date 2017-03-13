# Sound Processing using .wav files
# Adapted from http://www.eg.bucknell.edu/~csci203/2012-fall/hw/hw03/hw3pr4.html
#

import math
from csaudio import *
#csaudio contains functions like play(), readWav(), and writeWav()

class WavMod:
    """WavMod constructor takes:
        fileName, a string indicating the sound you wish to use.
        outputFile, an OPTIONAL string indicating the name to which
                     you wish to save the modified sound.
                     If you don't specify a second input,
                     the new sound will be saved as "out.wav"
    """
    def __init__(self,fileName, outputFile = "out.wav"):
        self.wavFile = fileName
        self.newFile = outputFile
    
    # a function to make sure everything is working
    def test(self):
        """ a test function that plays the wav file.
        """
        play(self.wavFile)    

    def changeSpeed(self,newSampleRate):
        """ changeSpeed takes in             

              newSampleRate, an integer representing the new sample rate you want,
                     in units of samples per second.
    
            changeSpeed creates a new file (using the name in newFile)
              that uses the same sound data as self.wavFile, but runs it at the
              samplerate of newSampleRate samples per second.
              It plays the new sound and then does not return anything...
        """
        # This next function call returns TWO values:
        #   samples is a LIST of the raw sound data
        #   oldSampleRate is the old sample rate, in samples per second
        #
        # This will be the standard way to get sound data from a file.
        samples, oldSampleRate = readWav(self.wavFile)

        # This next function call does not return any value, but
        #   it does write the sound data in the list "samples" into
        #   a file whose name is the string in the newFile variable
        #   It uses the new sample rate instead of the old.
        writeWav(samples, newSampleRate, self.newFile)

        # This next call to play also does not return a value,
        #   but it plays the sound in the file named newFile.
        play(self.newFile)

        # Now, we return the list of the sound data - it won't always
        #   be needed, we return it just in case it is.
        # actually, let's comment this out for now...
        #return samples

    def flipflop(self):
        """ flipflop creates a new file (using the name in self.newFile)
              that uses the same sound data as self.wavFile, but with the first and second
              halves of the sound interchanged.

            flipflop plays the new sound that it creates (no return value)
        """
        samples, sampleRate = readWav(self.wavFile)

        length = len(samples)
        newSamples = samples[length // 2:] + samples[:length // 2] # flip flop

        writeWav(newSamples, sampleRate, self.newFile)

        play(self.newFile)
        
    def reverse(self):

        samples, sampleRate = readWav(self.wavFile)

        length = len(samples) - 1
        
        samples = samples[::-1]
            
        writeWav(samples, sampleRate, self.newFile)
        play(self.newFile)
