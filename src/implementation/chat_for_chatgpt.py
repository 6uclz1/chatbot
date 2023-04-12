# pip
import openai

# system
import os

# local module
from src.interfaces.chat_interface import chat_interface

class chat_for_chatgpt(chat_interface):
    """チャットクラス
    """

    def get_response_text(self, text: str) -> str:
        """応答の結果をテキストで受け取る

        Arguments:
            text: チャットに投げるメッセージ
        """

        openai.api_key = os.environ.get('OPENAI_SECRET_KEY')

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "会話を行ってください"},
                {"role": "user", "content": text}
            ]   
        )
        print(response)
        return response.choices[0]["message"]["content"].strip()
