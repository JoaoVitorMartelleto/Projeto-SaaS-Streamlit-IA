# 💭 Análise de Sentimento com IA

Este projeto é uma aplicação web simples de **análise de sentimento** de textos usando **IA generativa (Gemini)**, desenvolvida com **Streamlit**.

Você pode digitar um texto ou fazer upload de um arquivo `.txt`, e o modelo irá identificar se o sentimento é **Positivo**, **Negativo** ou **Neutro**.

---

## 🚀 Tecnologias usadas

- [Python 3.11](https://www.python.org/)
- [Streamlit](https://streamlit.io/)
- [Google Generative AI (Gemini)](https://ai.google.dev/)
- [python-dotenv](https://pypi.org/project/python-dotenv/)

---

## ⚙️ Como executar o projeto

## 1. Clone o repositório:

- git clone https://github.com/JoaoVitorMartelleto/Projeto-SaaS-Streamlit-IA.git
cd Projeto-SaaS-Streamlit-IA

## 2. Crie o ambiente virtual e ative:

- Linux/macOS:
python -m venv venv
source venv/bin/activate
- Windows:
python -m venv venv
.\venv\Scripts\activate

## 3. Instale as dependências:
-pip install -r requirements.txt

## 4. Crie um arquivo .env na raiz do projeto com sua chave da Gemini:
- GEMINI_API_KEY=sua-chave-aqui

## 5. Execute a aplicação:
- streamlit run main.py
