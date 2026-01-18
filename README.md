 # Projeto de Acessibilidade por Voz

Este projeto foi desenvolvido como parte de um curso, com foco em **acessibilidade para pessoas com deficiência visual**. 
O objetivo é permitir que o usuário faça perguntas por voz e receba respostas também em áudio, sem depender de interface visual.

---

## 🎯 Objetivo
- Gravar a voz do usuário.  
- Transcrever o áudio em texto.  
- Enviar a transcrição para um modelo de linguagem (OpenAI API).  
- Receber a resposta e convertê-la em áudio com **gTTS**.  
- Reproduzir a resposta em áudio no ambiente do notebook.  

---

## 📑 Estrutura do Código
O projeto está dividido em  blocos:

   **Instalação de dependências**: instala bibliotecas necessárias (`openai`, `gtts`, `sounddevice`, `scipy`).  
1. **Gravação de Áudio  Com Python e um pouco de JavaScript**: grava o áudio do usuário .
2. **Reconhecimento de Fala com Whisper (OpenAI):** Reconhece a voz do usuário e transcreve (simulado neste protótipo).
3. **Integração com API (com fallback)**: envia a transcrição para a API da OpenAI. Se não houver créditos ou chave válida, gera uma resposta simulada para manter o fluxo.  
4. **Conversão em Áudio (gTTS)**: transforma a resposta em áudio e exibe um player no Colab.  

---

## ⚙️ Como Executar
1. Clone este repositório ou copie o notebook para o Google Colab.  
2. Instale as dependências.  
3. Rode o Bloco 1 para gravar a voz do usuário.
4. Rode o Bloco 2 para reconhecimento da voz e transcrição do áudio (simulado neste protótipo)  
5. Configure sua chave da OpenAI no Bloco 3 (se tiver créditos ativos).  
6. Rode o Bloco 3 e 4 para obter a resposta em áudio.  

---

## 🔎 Observações Importantes
- Se a conta da OpenAI não tiver créditos, o sistema ainda funciona com **resposta simulada**, garantindo que o fluxo seja demonstrado.  
- Em produção, recomenda-se integrar com **Whisper** para transcrição real.  
- O modelo usado pode ser `gpt-4o-mini` ou `gpt-3.5-turbo`, dependendo do acesso da conta.  

---

## 💡 Impacto Social
Este projeto demonstra como tecnologias de IA podem ser aplicadas para **inclusão digital**. 
Pessoas com deficiência visual podem interagir com o sistema apenas por voz, recebendo respostas faladas, o que aumenta sua autonomia e acessibilidade.  

---

## 📜 Licença
Este projeto é de caráter educacional e pode ser adaptado para fins acadêmicos ou sociais.  

---

## 👨‍💻 Autor
- **Ericky**  
- Desenvolvido como parte de um curso de certificação, com foco em acessibilidade e inclusão.  
