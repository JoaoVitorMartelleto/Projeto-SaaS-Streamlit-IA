# 💭 Análise de Sentimento com IA

Esta aplicação web realiza **análise de sentimentos** em textos com o uso de **IA generativa (Gemini)**, construída com **Streamlit**.

O usuário pode inserir manualmente um texto ou fazer upload de um arquivo `.txt`. A inteligência artificial analisará o conteúdo e classificará os trechos como **Positivo**, **Negativo** ou **Neutro**, com base no tom emocional transmitido.

Além disso, os resultados são apresentados de forma visual por meio de **gráficos interativos** e podem ser exportados em formato **CSV**.


---

## 🚀 Tecnologias usadas

- [Python 3.11](https://www.python.org/)
- [Streamlit](https://streamlit.io/)
- [Google Generative AI (Gemini)](https://ai.google.dev/)
- [python-dotenv](https://pypi.org/project/python-dotenv/)
- [pandas](https://pandas.pydata.org/)
- [plotly](https://plotly.com/python/)

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
