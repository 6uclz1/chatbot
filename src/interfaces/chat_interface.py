from abc import ABC, abstractmethod


class chat_interface(ABC):
    """チャットインターフェース
    """
    @abstractmethod
    def get_response_text(self, text: str) -> str:
        """応答の結果をテキストで受け取る

        Arguments:
            text: チャットに投げるメッセージ
        """
        pass