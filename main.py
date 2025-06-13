import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-2.0-flash")

st.set_page_config(page_title="Análise de Sentimento", page_icon="💭")

def analizar_texto(texto):
    prompt = f"""
       Analise o sentimento do texto a seguir. 
       Responda apenas com: Positivo, Negativo ou Neutro.

       Texto: {texto}
       """
    try:
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        return f"Erro ao analisar o texto: {str(e)}"

st.title("💭 Análise de Sentimento de textos com IA")


texto_usuario = st.text_area("Digite o texto a ser analizado:")

st.write("OU")

uploaded_file = st.file_uploader("📂 Faça upload de um arquivo .txt", type=["txt"])

if uploaded_file is not None:
    conteudo = uploaded_file.read().decode("utf-8")
    st.text_area("📄 Conteúdo do arquivo", value=conteudo, height=200)

    if st.button("Analisar Sentimento do Arquivo"):
        resultado = analizar_texto(conteudo)
        st.success(f"🧠 Sentimento detectado: **{resultado}**")

if st.button("Analisar Sentimento"):
    if texto_usuario.strip() == "":
        st.warning("Por favor, insira algum texto.")
    else:
        resultado = analizar_texto(texto_usuario)
        st.success(f"🧠 Sentimento detectado: **{resultado}**")
