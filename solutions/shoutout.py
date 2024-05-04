# Python program to convert text to speech
import win32com.client

# Calling the Dispatch method of the module which
# interact with Microsoft Speech SDK to speak
# the given input from the keyboard

speaker = win32com.client.Dispatch("SAPI.SpVoice")
names = ["Rahul", "Nishant", "Harry"]

for name in names:
    print(f"Shoutout to {name}.\n")
    speaker.Speak(f"Shoutout to {name}")

# To stop the program press CTRL + Z
