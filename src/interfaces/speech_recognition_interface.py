from abc import ABC, abstractmethod

class speech_recognition_interface(ABC):
    """音声認識クラス
    """
    @abstractmethod
    def get_speech_text(self) -> str:
        """マイクの音声からテキストを取得する
        """
        pass