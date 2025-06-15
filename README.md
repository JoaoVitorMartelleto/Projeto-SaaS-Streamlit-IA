# 💭 Análise de Sentimento com IA

Este projeto é uma aplicação web simples de **análise de sentimento** de textos usando **IA generativa (Gemini)**, desenvolvida com **Streamlit**.

Você pode digitar um texto ou fazer upload de um arquivo `.txt`, e o modelo irá identificar se o sentimento é **Positivo**, **Negativo** ou **Neutro**.

---

## 🚀 Tecnologias usadas

- [Python 3.11](https://www.python.org/)
- [Streamlit](https://streamlit.io/)
- [Google Generative AI (Gemini)](https://ai.google.dev/)
- [dotenv](https://pypi.org/project/python-dotenv/)

## 🚀 Como executar o projeto

1. Clone o repositório:
```bash
git clone https://github.com/JoaoVitorMartelleto/Projeto-SaaS-Streamlit-IA.git
cd Projeto-SaaS-Streamlit-IA
python -m venv venv
source venv/bin/activate  # Linux/macOS
.\venv\Scripts\activate    # Windows
pip install -r requirements.txt
GEMINI_API_KEY=sua-chave-aqui
streamlit run main.py
