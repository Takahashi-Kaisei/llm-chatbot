import openai
from openai import OpenAI
import os
import gradio as gr
from dotenv import load_dotenv
# %%

load_dotenv()
client = OpenAI()

openai.api_key = os.getenv("OPENAI_API_KEY")

def chatbot(prompt):
    response = client.chat.completions.create(
        model="gpt-4.1",  # 必要に応じてモデルを変更
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content

iface = gr.Interface(
    fn=chatbot,
    inputs=gr.Textbox(lines=2, label="あなたのメッセージ"),
    outputs=gr.Textbox(label="Botの応答"),
    title="OpenAI Chatbot",
    description="OpenAI APIを使ったシンプルなチャットボット"
)

if __name__ == "__main__":
    iface.launch()

# %%
import chromadb

chroma_client = chromadb.Client()

collection = chroma_client.create_collection(name="my_collection")

import json

data_path = "aozorabunko-dedupe-clean.jsonl"

with open(data_path, "r") as f:
    data = f.readlines()
data = [json.loads(x) for x in data]
# data = [x["text"] for x in data]

len(data)

# %%
collection.add(
    documents=[x["text"] for x in data],
    ids=[x["meta"]["作品ID"] for x in data]
)

# dirコマンドは大事，メソッドの一覧がわかる．jsonで言うと，jsonの構造が一目でわかるわけ．

# 来週はlangchainを使った．チャンキング
# %%
