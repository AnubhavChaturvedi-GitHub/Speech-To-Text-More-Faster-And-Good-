import speech_recognition as sr
import os
import threading
from mtranslate import translate
from colorama import Fore, Style, init

init(autoreset=True)  # Automatically reset styles after each print

# Function to listen for speech
def print_loop():
    while True:
        print(Fore.GREEN + "Listening....", end='', flush=True)
        print(Style.RESET_ALL, end='', flush=True)
        print("", end='', flush=True)

def translation_hin_to_eng(text):
    english_translation = translate(text, 'en-in')
    return english_translation

def listen():
    recognizer = sr.Recognizer()
    recognizer.dynamic_energy_threshold = False
    recognizer.energy_threshold = 35000
    recognizer.dynamic_energy_adjustment_damping = 0.03
    recognizer.dynamic_energy_ratio = 1.9
    recognizer.pause_threshold = 0.4
    recognizer.operation_timeout = None
    recognizer.phrase_threshold = 0.2
    recognizer.non_speaking_duration = 0.3

    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)

        while True:
            print(Fore.GREEN + "Listening....", end='', flush=True)
            try:
                audio = recognizer.listen(source, timeout=None)
                print("\r" + Fore.YELLOW + "Recognizing...   ", end='', flush=True)
                recognized_text = recognizer.recognize_google(audio).lower()
                if recognized_text:
                    translated_text = translation_hin_to_eng(recognized_text)
                    print("\r" + Fore.CYAN + "Mr.Stank: " + translated_text)
                    return translated_text
                else:
                    return ""
            except sr.UnknownValueError:
                recognized_text = ""
            finally:
                print("\r", end='', flush=True)
                os.system('cls' if os.name == 'nt' else 'clear')
            listen_thread = threading.Thread(target=listen)
            listen_thread.start()
            print_thread = threading.Thread(target=print_loop)
            print_thread.start()

            listen_thread.join()
            print_thread.join()

listen()

