import json
import os
import tkinter as tk
from tkinter import ttk

from .player import AudioPlayer


class PlayerWindow(tk.Tk):
    """Einfache GUI für den Audio-Player."""

    def __init__(self):
        super().__init__()
        self.title("Audio Player")
        self.player = AudioPlayer()
        self.length = 0

        self.create_widgets()
        self.load_playlist()

    def create_widgets(self):
        control = ttk.Frame(self)
        control.pack(fill=tk.X)

        self.play_btn = ttk.Button(control, text="Play", command=self.toggle)
        self.play_btn.pack(side=tk.LEFT, padx=5)

        self.stop_btn = ttk.Button(control, text="Stop", command=self.stop)
        self.stop_btn.pack(side=tk.LEFT)

        self.scale = ttk.Scale(self, from_=0, to=100, command=self.on_seek)
        self.scale.pack(fill=tk.X, padx=5, pady=5)

        self.label = ttk.Label(self, text="00:00/00:00")
        self.label.pack()

        self.listbox = tk.Listbox(self)
        self.listbox.pack(fill=tk.BOTH, expand=True)
        self.listbox.bind("<<ListboxSelect>>", self.on_select)

        self.after(500, self.update_ui)

    def load_playlist(self):
        path = os.path.join(os.path.dirname(__file__), "../../..", "library", "playlist.json")
        if os.path.exists(path):
            with open(path, "r", encoding="utf-8") as fh:
                data = json.load(fh)
                for item in data.get("tracks", []):
                    self.listbox.insert(tk.END, item)

    def on_select(self, event):
        if not self.listbox.curselection():
            return
        file = self.listbox.get(self.listbox.curselection()[0])
        self.player.load(file)
        self.length = len(self.player.segment)
        self.scale.configure(to=self.length / 1000)
        self.play()

    def toggle(self):
        if self.player.play_obj and not self.player.play_obj.is_playing():
            self.play()
        elif self.player.play_obj:
            self.pause()
        else:
            self.play()

    def play(self):
        self.player.play()
        self.play_btn.configure(text="Pause")

    def pause(self):
        self.player.pause()
        self.play_btn.configure(text="Play")

    def stop(self):
        self.player.stop()
        self.play_btn.configure(text="Play")
        self.scale.set(0)

    def on_seek(self, value):
        self.player.seek(float(value))

    def update_ui(self):
        if self.player.play_obj and self.player.play_obj.is_playing():
            pos_ms = self.player.position + int(self.player.play_obj.frames_played / self.player.play_obj.sample_rate * 1000)
        else:
            pos_ms = self.player.position
        if self.length:
            self.scale.set(pos_ms / 1000)
            label = f"{pos_ms // 1000:02d}:{(pos_ms//100)%60:02d}/{self.length//1000:02d}:{(self.length//100)%60:02d}"
            self.label.configure(text=label)
        self.after(500, self.update_ui)


def main():
    PlayerWindow().mainloop()


if __name__ == "__main__":
    main()
