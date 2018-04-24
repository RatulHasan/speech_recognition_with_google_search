import pyaudio
import wave
import speech_recognition as sr
import subprocess
from commands import Commander

running = True

def say(text):
    subprocess.call("say "+ text, shell=True)

def play_audio(filename):
    chunk = 1024
    wf = wave.open(filename, 'rb')
    pa = pyaudio.PyAudio()

    stream = pa.open(
        format = pa.get_format_from_width(wf.getsampwidth()),
        channels = wf.getnchannels(),
        rate = wf.getframerate(),
        output = True
    )

    data_stream = wf.readframes(chunk)

    while data_stream:
        stream.write(data_stream)
        data_stream = wf.readframes(chunk)

    stream.close()
    pa.terminate()


# play_audio("audio/whistle-slide-down.wav")

  
r = sr.Recognizer()
r.energy_threshold=4000

cmd = Commander()

def init_speech():
    print("Listening...")

    play_audio("audio/beep.wav")

    with sr.Microphone() as source:
        print("Say something...")
        audio = r.listen(source)

    # write audio to a RAW file
    with open("./audio/write_audio/microphone-results.raw", "wb") as f:
        f.write(audio.get_raw_data())

    # write audio to a WAV file
    with open("./audio/write_audio/microphone-results.wav", "wb") as f:
        f.write(audio.get_wav_data())

    play_audio("./audio/Beep5.wav")

    command = ""

    try:
        command = r.recognize_google(audio)
    except:
        print("Couldn't understand you!")

    print("Your command: ")
    print(command)

    if command == "quit":
        global running
        running = False

    cmd.discover(command)

    # say("You said "+ command)

while running == True:
    init_speech()