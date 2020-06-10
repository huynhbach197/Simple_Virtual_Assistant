import speech_recognition
from datetime import date, datetime
import os

today = date.today().strftime("%B %d, %Y")
import pyttsx3
engine = pyttsx3.init()
robot_ear = speech_recognition.Recognizer()
while True:
    with speech_recognition.Microphone() as mic:
        print("Robot: I'm listening")
        audio = robot_ear.listen(mic)
    print("...")
    try:
        you = robot_ear.recognize_google(audio)
    except:
        you = ""
    print("You: " + you)


    if you == "":
        robot_brain = "I can't understand you, try again"
        print("Robot: " + robot_brain)
        engine.say(robot_brain)
        engine.runAndWait()
    elif "hello" in you:
        robot_brain = "Hello Merlin"
        print("Robot: " + robot_brain)
        engine.say(robot_brain)
        engine.runAndWait()
    elif "today" in you:
        robot_brain = today
        print("Robot: " + robot_brain)
        engine.say(robot_brain)
        engine.runAndWait()
    elif "weather"in you:
        robot_brain = "nang"
        print("Robot: " + robot_brain)
        engine.say(robot_brain)
        engine.runAndWait()
    elif ("mail"in you) or ("email" in you):
        robot_brain = "Opening Outlook mail"
        print("Robot: " + robot_brain)
        engine.say(robot_brain)
        engine.runAndWait()
        os.system("c:\Python36\python.exe openmail.py")
    elif ("cctv"in you) or ("CCTV" in you):
        robot_brain = "Opening CCTV"
        print("Robot: " + robot_brain)
        engine.say(robot_brain)
        engine.runAndWait()
        os.system("c:\Python36\python.exe opencctv.py")
    elif "time" in you:
        robot_brain = datetime.now().strftime("%H hours %M minutes %S seconds")
        print("Robot: " + robot_brain)
        engine.say(robot_brain)
        engine.runAndWait()
    elif "pi" in you:
        robot_brain = "Connecting to Raspberry Pi 4"
        print("Robot: " + robot_brain)
        engine.say(robot_brain)
        engine.runAndWait()
        # os.system("ssh pi@192.168.5.178")
        os.system("start /B start cmd.exe @cmd /k ssh pi@192.168.5.178")
    elif "bye" in you:
        robot_brain = "Goodbye my master"
        print("Robot: " + robot_brain)
        engine.say(robot_brain)
        engine.runAndWait()
        break
    else:
        robot_brain = "I dont understand what you're saying"
        print("Robot: " + robot_brain)
        engine.say(robot_brain)
        engine.runAndWait()


    
    
    

# robot_brain = "Hello Merlin"

# en_voice_id = "HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Speech\\Voices\\Tokens\\TTS_MS_EN-US_ZIRA_11.0"


# engine.setProperty('voice', en_voice_id)
# engine.setProperty('rate', 150)    # Speed percent (can go over 100)
# engine.setProperty('volume', 1)  # Volume 0-1
