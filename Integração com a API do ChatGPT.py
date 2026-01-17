#Integração com a API do ChatGPT

!pip install openai

 Looking in indexes: https://pypi.org/simple, https://us-python.pkg.dev/colab-wheels/public/simple/
 Requirement already satisfied: openai in /usr/local/lib/python3.10/dist-packages (0.27.6)
 Requirement already satisfied: tqdm in /usr/local/lib/python3.10/dist-packages (from openai) (4.65.0)
 Requirement already satisfied: requests>=2.20 in /usr/local/lib/python3.10/dist-packages (from openai) (2.27.1)
 Requirement already satisfied: aiohttp in /usr/local/lib/python3.10/dist-packages (from openai) (3.8.4)
 Requirement already satisfied: certifi>=2017.4.17 in /usr/local/lib/python3.10/dist-packages (from requests>=2.20->openai) (2022.12.7)
 Requirement already satisfied: idna<4,>=2.5 in /usr/local/lib/python3.10/dist-packages (from requests>=2.20->openai) (3.4)
 Requirement already satisfied: urllib3<1.27,>=1.21.1 in /usr/local/lib/python3.10/dist-packages (from requests>=2.20->openai) (1.26.15)
 Requirement already satisfied: charset-normalizer~=2.0.0 in /usr/local/lib/python3.10/dist-packages (from requests>=2.20->openai) (2.0.12)
 Requirement already satisfied: aiosignal>=1.1.2 in /usr/local/lib/python3.10/dist-packages (from aiohttp->openai) (1.3.1)
 Requirement already satisfied: yarl<2.0,>=1.0 in /usr/local/lib/python3.10/dist-packages (from aiohttp->openai) (1.9.2)
 Requirement already satisfied: frozenlist>=1.1.1 in /usr/local/lib/python3.10/dist-packages (from aiohttp->openai) (1.3.3)
 Requirement already satisfied: attrs>=17.3.0 in /usr/local/lib/python3.10/dist-packages (from aiohttp->openai) (23.1.0)
 Requirement already satisfied: async-timeout<5.0,>=4.0.0a3 in /usr/local/lib/python3.10/dist-packages (from aiohttp->openai) (4.0.2)
 Requirement already satisfied: multidict<7.0,>=4.5 in /usr/local/lib/python3.10/dist-packages (from aiohttp->openai) (6.0.4)

import os

os.environ['OPENAI_API_KEY'] = ''
import openai

# Configura a chave de API da OpenAI usando a variável de ambiente 'OPENAI_API_KEY'
openai.api_key = os.environ.get('OPENAI_API_KEY')

# Envia uma requisição à API do ChatCompletion usando o modelo GPT-3.5 Turbo
# Lembrando que, a variável 'transcription' contém a transcrição do nosso áudio.
response = openai.ChatCompletion.create(
    model="gpt-4",
    messages=[ { "role": "user", "content": transcription } ]
)

# Obtém a resposta gerada pelo ChatGPT
chatgpt_response = response.choices[0].message.content

print(chatgpt_response)
