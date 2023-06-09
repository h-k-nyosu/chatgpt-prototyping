import streamlit as st
import os
from dotenv import load_dotenv
from src.api.chatgpt import ChatGPT


# .envファイルから環境変数をロードする
load_dotenv()

# APIキーの設定
API_KEY = os.environ.get("OPENAI_API_KEY")
MODEL_ENGINE = "gpt-3.5-turbo"

# ページのタイトルを設定する
st.set_page_config(page_title="Chatbot App")


#
# SessionStateを使用して状態を管理する
#

messages = []

if 'message_count' not in st.session_state:
    st.session_state.message_count = 1
if 'messages' not in st.session_state:
    st.session_state.messages = []

st.title("事前入力プロンプト")
btn_col1, btn_col2 = st.columns(2)
with btn_col1:
    if st.button('プロンプトの追加'):
        st.session_state.message_count += 1
with btn_col2:
    if st.session_state.message_count > 1 and st.button('プロンプトの削除'):
        st.session_state.message_count -= 1
        st.session_state.messages.pop()
st.caption("---")

for i in range(st.session_state.message_count):
    col1, col2 = st.columns(2)
    with col1:
        role = st.selectbox("", ["system", "user", "assistant"], key=f"role_{i}")
        st.caption("Role")
    with col2:
        if role == "system":
            message = st.text_input("", "あなたは親身に回答してくれるチャットボットです。", key=f"message_{i}")
        else:
            message = st.text_input("", "", key=f"message_{i}")
        st.caption("Message")
    messages.append({'role': role, 'content': message})

# プログラム側で初期値を規定する場合は、以下のコメントアウトを外す
# messages = [{'role': 'system', 'content': 'あなたは親身に回答してくれるチャットボットです。'}]

st.session_state.messages = messages
st.write(messages)




# Chat GPT インスタンスの作成
chatbot = ChatGPT(api_key=API_KEY, model_engine=MODEL_ENGINE, messages=messages)

# SessionStateを使用して状態を管理する
session_state = st.session_state
session_state.response = "ここにChatGPTからの出力結果が表示されます。"
if "chat_log_list" not in session_state:
    session_state.chat_log_list = []

st.title('ユーザー入力文')

# ユーザーのメッセージを入力するテキストボックス
user_input = st.text_input("Enter your message")

# ボタンがクリックされたときに実行される関数
def get_response(user_input):
    return chatbot.send_message(user_input)

def on_button_click():
    # ユーザーのメッセージを送信し、チャットのログを更新する
    response = get_response(user_input)
    
    # レスポンスを上書きする
    session_state.response = response
    
    # チャットログをリストの先頭に追加する
    session_state.chat_log_list.insert(0, ("You: " + user_input, "Chatbot: " + response))
    
    return response


# ボタンの作成とクリックイベントの設定
if st.button("Send", key="send"):
    on_button_click()


# 出力結果を表示する
st.title('出力結果')

session_state.response

st.caption("---")

if st.checkbox("チャットログを表示する", value=False):

    with st.container():
        for you_ms, chatbot_ms in session_state.chat_log_list:
            st.write(f"{you_ms}", key=f"{you_ms}")
            st.write(f"{chatbot_ms}", key=f"{chatbot_ms}")
            st.caption("---")
