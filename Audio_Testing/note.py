from utils import NOTE_MAP
from AudioTest import Tone
import threading
import time

class Note:
    def __init__(self, note_str, durr = 1):
        main_note = note_str[0].upper()
        self.note_str= main_note +note_str[1:]
        self.durr = durr
        self.freq = NOTE_MAP[self.note_str]

    def play(self, speaker = None):
        Tone.sine(self.freq, self.durr, speaker= speaker)
    
    @staticmethod
    def rest(durr = 1):
        time.sleep(durr)




    @staticmethod
    def play_cord(note_list):
        note_threads = []

        for note in note_list:
            thread = threading.Thread(target=note.play)
            note_threads.append(thread)

        for note_thread in note_threads:
            note_thread.start()

        for note_thread in note_threads:
            note_thread.join()


