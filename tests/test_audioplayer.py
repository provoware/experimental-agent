import os
import sys

import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
from modules.audioplayer import player


class FakeSegment:
    frame_rate = 44100

    def __init__(self, duration_ms=1000):
        self.duration_ms = duration_ms

    def __len__(self):
        return self.duration_ms

    def __getitem__(self, _):
        return self


class DummyPlay:
    def __init__(self):
        self.stopped = False
        self.frames_played = 0
        self.sample_rate = 44100

    def stop(self):
        self.stopped = True

    def is_playing(self):
        return not self.stopped


def test_player_load_play_pause_seek(monkeypatch):
    dummy_segment = FakeSegment()
    monkeypatch.setattr(player.AudioSegment, "from_file", lambda f: dummy_segment)
    play_obj = DummyPlay()
    monkeypatch.setattr(player, "_play_with_simpleaudio", lambda seg: play_obj)

    p = player.AudioPlayer()
    p.load("foo.mp3")
    assert p.segment is dummy_segment

    p.play()
    assert not play_obj.stopped

    play_obj.frames_played = 44100  # 1 Sekunde
    p.pause()
    assert play_obj.stopped
    assert p.position >= 1000

    p.seek(0)
    assert p.position == 0
    assert play_obj.stopped


def test_stop_resets_position(monkeypatch):
    dummy_segment = FakeSegment()
    monkeypatch.setattr(player.AudioSegment, "from_file", lambda f: dummy_segment)
    play_obj = DummyPlay()
    monkeypatch.setattr(player, "_play_with_simpleaudio", lambda seg: play_obj)

    p = player.AudioPlayer()
    p.load("foo.wav")
    p.play()
    play_obj.frames_played = 22050
    p.stop()
    assert p.position == 0
    assert play_obj.stopped
