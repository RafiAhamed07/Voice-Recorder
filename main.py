from tkinter import *
from tkinter.filedialog import askdirectory
from tkinter.messagebox import showinfo, showwarning

import sounddevice as sd
from scipy.io.wavfile import write

add = ""


def path():
    global add
    add = askdirectory()


def record():
    global add
    try:
        time = int(sec.get())
        filename = fname.get()
        saveas = add + "/" + f"{filename}"
        showinfo(title="Start", message="Recording started")
        r = sd.rec(frames=(time * 44100), samplerate=44100, channels=2)
        sd.wait()
        write(f"{saveas}.mp3", 44100, r)
        showinfo(title="End", message="Recording ended")
    except ValueError:
        showwarning(title="Time", message="Please enter a valid time")


def main_window():
    global sec
    global fname
    root = Tk()
    root.geometry("500x300")
    root.title("Voice Recorder")
    root.iconbitmap("voice-recorder.ico")
    root.resizable(False, False)
    root.config(bg="#424a57")

    # Header Label
    header_label = Label(root, text="Voice Recorder", bg="#424a57", fg="white", font=("Helvetica", 16, "bold"))
    header_label.pack(pady=10)

    # Time Entry
    time_label = Label(root, text="Recording Time (seconds):", font=("Helvetica", 12), bg="#424a57", fg="white")
    time_label.pack(pady=5)
    sec = Entry(root, font=("Helvetica", 12))
    sec.pack(pady=5)

    # Filename Entry
    filename_label = Label(root, text="Filename:", font=("Helvetica", 12), bg="#424a57", fg="white")
    filename_label.pack(pady=5)
    fname = Entry(root, font=("Helvetica", 12))
    fname.pack(pady=5)

    # Path Button
    path_button = Button(root, text="Select Path", bg="#346137", font=("Helvetica", 12), command=path)
    path_button.pack(pady=10)

    # Start Button
    sb = Button(root, text="Start Recording", bg="#8a3437", font=("Helvetica", 12), command=record)
    sb.pack(pady=10)

    root.mainloop()


main_window()
