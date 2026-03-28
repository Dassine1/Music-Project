import time

from music21 import duration
notes = {
    "A3": 440.00,
    "G2": 195.998,
    "C5": 1046.50,
    "F1": 87.3071,
    "Bb4": 932.328
}

class MusicMaker:
    def __init__(self, notes, duration):
        self.notes = notes
        self.duration = duration


    def get(self):
        return self.notes and self.duration
    
    
    def set(self, notes, duration):
        if notes != notes:
            print("Enter a valid note from the dictionary")
        else:
            return self.notes and self.duration



MusicMaker(notes)


first_pause = time.sleep(0.75)
second_pause = time.sleep(0.75)
third_pause = time.sleep(0.25)
fourth_pause = time.sleep(0.25)
fifth_pause = time.sleep(1)
