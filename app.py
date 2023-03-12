import streamlit as st
import os
from dotenv import load_dotenv
from src.api.chatgpt import ChatGPT

# .envファイルから環境変数をロードする
load_dotenv()

# APIキーの設定
API_KEY = os.environ.get("OPENAI_API_KEY")
MODEL_ENGINE = "gpt-3.5-turbo"

# Chat GPT インスタンスの作成
chatbot = ChatGPT(api_key=API_KEY, model_engine=MODEL_ENGINE)

# ページのタイトルを設定する
st.set_page_config(page_title="Chatbot App")

# SessionStateを使用して状態を管理する
session_state = st.session_state
if "chat_log_list" not in session_state:
    session_state.chat_log_list = []

st.title('Chatbot App')

# ユーザーのメッセージを入力するテキストボックス
user_input = st.text_input("Enter your message")

# ボタンがクリックされたときに実行される関数
@st.cache_data
def get_response(user_input):
    return chatbot.send_message(user_input)

def on_button_click():
    # ユーザーのメッセージを送信し、チャットのログを更新する
    response = get_response(user_input)
    
    # チャットログをリストの先頭に追加する
    session_state.chat_log_list.insert(0, ("You: " + user_input, "Chatbot: " + response))

# ボタンの作成とクリックイベントの設定
button = st.button("Send")
if button:
    on_button_click()

# 過去のチャットログを表示する
st.title('Chat Log')

with st.container():
    for you_ms, chatbot_ms in session_state.chat_log_list:
        st.caption("---")
        st.write(f"{you_ms}", key=f"{you_ms}")
        st.write(f"{chatbot_ms}", key=f"{chatbot_ms}")
