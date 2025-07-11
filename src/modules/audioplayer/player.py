from pydub import AudioSegment
from pydub.playback import _play_with_simpleaudio


class AudioPlayer:
    """Einfacher Audio-Player."""

    def __init__(self):
        self.segment = None
        self.play_obj = None
        self.position = 0  # Millisekunden

    def load(self, file):
        """Audio-Datei laden."""
        self.segment = AudioSegment.from_file(file)
        self.position = 0

    def play(self):
        """Abspielen ab aktueller Position."""
        if self.segment is None:
            return
        seg = self.segment[self.position:]
        self.play_obj = _play_with_simpleaudio(seg)

    def pause(self):
        """Wiedergabe pausieren."""
        if self.play_obj:
            # gespielte Zeit berechnen
            played_ms = int(self.play_obj.frames_played / self.play_obj.sample_rate * 1000)
            self.position += played_ms
            self.play_obj.stop()

    def stop(self):
        """Wiedergabe stoppen."""
        if self.play_obj:
            self.play_obj.stop()
        self.position = 0

    def seek(self, seconds):
        """Zur Position springen."""
        self.position = int(seconds * 1000)
        if self.play_obj:
            self.play_obj.stop()
            self.play()
