# LLM 活用のプロトタイピング用 Streamlit スタートキット

このリポジトリは、Streamlit を使った大規模言語モデルの活用のためのスタートキットです。デフォルトでは ChatGPT を使用して、会話をすることができます。

## 使い方

## 環境構築

```sh
poetry install
```

## 起動

以下のコマンドで、アプリを起動します。

```sh
poetry run streamlit run app.py
```

## 環境変数

OpenAI の API キーを .env ファイルに記述してください。

```python

OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

```

## 注意事項

.env ファイルに API キーを保存することによって、API キーが漏れる可能性があるため、.gitignore ファイルに .env ファイルを追加してください。
