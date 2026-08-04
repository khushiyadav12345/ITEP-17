
# 26. Media Player

# Abstract:

# MediaPlayer

# Derived:

# AudioPlayer
# VideoPlayer

# Implement play functionality.

from abc import ABC, abstractmethod

class MediaPlayer(ABC):

    @abstractmethod
    def play(self):
        pass


class AudioPlayer(MediaPlayer):
    def play(self):
        print("Audio is playing")


class VideoPlayer(MediaPlayer):
    def play(self):
        print("Video is playing")


a = AudioPlayer()
a.play()

v = VideoPlayer()
v.play()