#Sintetizando a Resposta do ChatGPT Como Voz (gTTS)

 !pip install gTTS

 Looking in indexes: https://pypi.org/simple, https://us-python.pkg.dev/colab-wheels/public/simple/
 Collecting gTTS

 Downloading gTTS-2.3.2-py3-none-any.whl (28 kB)
 Requirement already satisfied: click<8.2,>=7.1 in /usr/local/lib/python3.10/dist-packages (from gTTS) (8.1.3)
 Requirement already satisfied: requests<3,>=2.27 in /usr/local/lib/python3.10/dist-packages (from gTTS) (2.27.1)
 Requirement already satisfied: certifi>=2017.4.17 in /usr/local/lib/python3.10/dist-packages (from requests<3,>=2.27->gTTS) (2022.12.7)
 Requirement already satisfied: idna<4,>=2.5 in /usr/local/lib/python3.10/dist-packages (from requests<3,>=2.27->gTTS) (3.4)
 Requirement already satisfied: charset-normalizer~=2.0.0 in /usr/local/lib/python3.10/dist-packages (from requests<3,>=2.27->gTTS) (2.0.12)
 Requirement already satisfied: urllib3<1.27,>=1.21.1 in /usr/local/lib/python3.10/dist-packages (from requests<3,>=2.27->gTTS) (1.26.15)
 Installing collected packages: gTTS
 Successfully installed gTTS-2.3.2

from gtts import  gTTS

# Cria um objeto gTTS com a resposta gerada pelo ChatGPT e a língua que será sintetizada em voz (variável "language").
gtts_object = gTTS(text=chatgpt_response, lang=language, slow=False)

# Salva o áudio da resposta no arquivo especificado (pasta padrão do Google Colab)
response_audio = "/content/response_audio.wav"
gtts_object.save(response_audio)

# Reproduz o áudio da resposta salvo no arquivo

display(Audio(response_audio, autoplay=True))

