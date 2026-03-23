import pygame
import numpy
import math
import time
import threading

pygame.init()
bits = 16
sample_rate = 44100
pygame.mixer.pre_init(sample_rate, bits)

def sine_x (amp, freq, time):
    return int (round (amp* math.sin(2 *math.pi *freq * time)))

class Tone: 
    def sine(freq, durr = 1, speaker = None):
        num_sampels = int(round(durr*sample_rate))

        sound_buffer = numpy.zeros((num_sampels,2), dtype= numpy.int16)
        amplitude = 2 ** (bits-1) -1

        for sample_num in range(num_sampels):
            t = float(sample_num) / sample_rate

            sine = sine_x (amplitude, freq, t)
            if speaker == 'r':
                sound_buffer[sample_num][1] = sine
            if speaker == 'l':
                sound_buffer[sample_num][0] = sine
            else:
                sound_buffer[sample_num][0] = sine
                sound_buffer[sample_num][1] = sine
        
        sound = pygame.sndarray.make_sound(sound_buffer)
        sound.play(loops =1, maxtime= int (durr *1000 ))
        time.sleep(durr)
    
    @staticmethod
    def create_tone_from_list(freq_list,durr =1, speaker = None):
        tone_threads = []
        for freq in freq_list:
            freq_thread = threading.Thread(target = Tone.sine, args = [freq, durr, speaker])
            tone_threads.append(freq_thread)

        for tone_thread in tone_threads:
            tone_thread.start()

        for tone_thread in tone_threads:
            tone_thread.join

