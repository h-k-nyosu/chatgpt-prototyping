import openai
import time

class ChatGPT:
    def __init__(self, api_key, model_engine="gpt-3.5-turbo", messages=[], temperature=0.5):
        self.api_key = api_key
        self.model_engine = model_engine
        self.temperature = temperature
        self.messages = messages
        openai.api_key = api_key
        self.chat_log = []

    def send_message(self, user_message):
        self.chat_log.append(('user', user_message))
        response = self._request(user_message)
        self.chat_log.append(('chatbot', response))
        print(f"log after send: {self.chat_log}")
        return response

    def _request(self, message):
        print(f"message: {message}")
        print(f"messages: {self.messages}")
        chat_messages = [
            *self.messages,
            {"role": "user", "content": message},
        ]
        print(f"chat_messages: {chat_messages}")
        response = openai.ChatCompletion.create(
            model=self.model_engine,
            max_tokens=1024,
            temperature=self.temperature,
            messages=chat_messages
        )
        message = response.choices[0].message.content
        return message.strip()

    def get_chat_log(self):
        print(f"log: {self.chat_log}")
        return self.chat_log

    def clear_chat_log(self):
        self.chat_log = []
