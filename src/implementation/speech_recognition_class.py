from src.interfaces.speech_recognition_interface import speech_recognition_interface
import speech_recognition as sr

class speech_recognition_class(speech_recognition_interface):
    """音声認識クラス
    """

    def get_speech_text(self) -> str:
        """マイクの音声からテキストを取得する
        """

        # マイクから音声を取得する
        r = sr.Recognizer()
    
        with sr.Microphone() as source:
            print("何か話しかけてください...")
            audio = r.listen(source)

            # 音声をテキストに変換する
            try:
                text = r.recognize_google(audio, language='ja-JP')
                print("音声認識結果: " + text)
                return text
            except sr.UnknownValueError:
                print("音声が認識できませんでした。")
                return ''
            except sr.RequestError as e:
                print("Google Speech Recognition API への接続が失敗しました。 {0}".format(e))
                return ''
