import tkinter as tk
from gtts import gTTS
import playsound
import os

def text_to_speech():
    text = entry.get()
    if text.strip():
        tts = gTTS(text=text, lang='en')
        audio_file = "speech.mp3"
        tts.save(audio_file)
        playsound.playsound(audio_file)
        os.remove(audio_file)

def clear_text():
    entry.delete(0, tk.END)

def exit_app():
    root.quit()

root = tk.Tk()
root.title("Text to Speech")
root.geometry("600x400")
root.config(bg="#f0f0f0")

label = tk.Label(root, text="Text to Speech", font=("Arial", 18, 'bold'), bg="#f0f0f0")
label.pack(pady=20)

frame = tk.Frame(root, bg="#f0f0f0")
frame.pack(pady=10)

label_instruction = tk.Label(frame, text="Enter your name", font=("Arial", 14), bg="#f0f0f0", anchor="w")
label_instruction.grid(row=0, column=0, padx=10)

entry = tk.Entry(frame, width=30, font=("Arial", 14), bd=2, relief="solid", justify="center")
entry.grid(row=0, column=1)

button_frame = tk.Frame(root, bg="#f0f0f0")
button_frame.pack(side=tk.BOTTOM, pady=30)

play_button = tk.Button(button_frame, text="Play", command=text_to_speech, bg="#4CAF50", fg="white", font=("Arial", 12), width=12, height=2, relief="raised")
play_button.grid(row=0, column=0, padx=20)

exit_button = tk.Button(button_frame, text="Exit", command=exit_app, bg="#f44336", fg="white", font=("Arial", 12), width=12, height=2, relief="raised")
exit_button.grid(row=0, column=1, padx=20)

clear_button = tk.Button(button_frame, text="Clear", command=clear_text, bg="#2196F3", fg="white", font=("Arial", 12), width=12, height=2, relief="raised")
clear_button.grid(row=0, column=2, padx=20)

root.mainloop()
