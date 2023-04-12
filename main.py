# pip
from dotenv import load_dotenv
from ulid import ULID

# system
import sys
import signal

# local module
from src.synthesis import synthesis
from src.play_voice import play_voice
from src.split_text import split_text
from src.implementation.chat_for_chatgpt import chat_for_chatgpt
from src.implementation.speech_recognition_class import speech_recognition_class

def signal_handler(sig, frame):
    print('中断されました')
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

def main():

    s = speech_recognition_class()
    c = chat_for_chatgpt()

    text = s.get_speech_text()

    # 何も応答がなかった際は後続処理を行わない
    if text == '': return 

    response = c.get_response_text(text)

    for t in split_text(response):
        ulid = ULID()
        synthesis(t, f"./voice/audio_{str(ulid)}.wav")
        play_voice(f"./voice/audio_{str(ulid)}.wav")
    
if __name__ == '__main__':
    load_dotenv()
    while True:
        main()
