#Reconhecimento de Fala com Whisper(OpenAI)

   !pip install git+https://github.com/openai/whisper.git -q
  
  #Instalar as Dependências
  # Installing build dependencies 
  # Getting requirements to build wheel 
  # Preparing metadata (pyproject.toml) 

  import whisper

# Selecione o modelo do Whisper que melhor atenda às suas necessidades:
# https://github.com/openai/whisper#available-models-and-languages
model = whisper.load_model("small")

# Transcreve o audio gravado anteriormente.
result = model.transcribe(record_file, fp16=False, language=language)
transcription = result["text"]

print(transcription)
