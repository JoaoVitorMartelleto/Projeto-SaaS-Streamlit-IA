import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os
import json

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-2.0-flash")

st.set_page_config(page_title="Análise de Sentimento", page_icon="💭")

def analizar_texto(texto):
    prompt = f"""
    Analise os sentimentos no texto abaixo. Classifique cada trecho como Positivo, Negativo ou Neutro, baseando-se no tom emocional real transmitido (e não apenas em palavras isoladas).

    Critérios:
    - **Positivo**: trechos que expressam otimismo, esperança, superação ou motivação.
    - **Negativo**: tristeza, frustração, desânimo, pessimismo.
    - **Neutro**: fatos, conselhos, reflexões sem carga emocional forte.

    Formato da resposta (apenas JSON):
    {{
      "Positivo": ["..."],
      "Negativo": ["..."],
      "Neutro": ["..."]
    }}

    Texto: {texto}
    """
    try:
        response = model.generate_content(prompt)
        resposta_bruta = response.text.strip()


        if resposta_bruta.startswith("```"):
            resposta_bruta = resposta_bruta.strip("`")

            if resposta_bruta.startswith("json"):
                resposta_bruta = resposta_bruta[4:].strip()


        return json.loads(resposta_bruta)
    except Exception as e:
        return {
            "Erro": f"Erro ao analisar o texto: {str(e)}",
            "Resposta da IA": resposta_bruta
        }

def exibir_resultado(resultado):
    if isinstance(resultado, dict):
        if "Erro" in resultado:
            st.error(resultado["Erro"])
            st.code(resultado.get("Resposta da IA", ""), language="markdown")
        else:
            st.subheader("🧠 Sentimentos Detectados:")

            if resultado.get("Positivo"):
                st.markdown("### ✅ Positivo")
                for trecho in resultado["Positivo"]:
                    st.success(f"💚 {trecho}")

            if resultado.get("Negativo"):
                st.markdown("### ⚠️ Negativo")
                for trecho in resultado["Negativo"]:
                    st.error(f"💔 {trecho}")

            if resultado.get("Neutro"):
                st.markdown("### 📎 Neutro")
                for trecho in resultado["Neutro"]:
                    st.info(f"🌀 {trecho}")

st.title("💭 Análise de Sentimento de textos com IA")

texto_usuario = st.text_area("Digite o texto a ser analisado:")

st.write("OU")

uploaded_file = st.file_uploader("📂 Faça upload de um arquivo .txt", type=["txt"])

if st.button("Analisar Sentimento"):
    if texto_usuario.strip() == "":
        st.warning("Por favor, insira algum texto.")
    else:
        resultado = analizar_texto(texto_usuario)
        exibir_resultado(resultado)

if uploaded_file is not None:
    conteudo = uploaded_file.read().decode("utf-8")
    st.text_area("📄 Conteúdo do arquivo", value=conteudo, height=200)

    if st.button("Analisar Sentimento do Arquivo"):
        resultado = analizar_texto(conteudo)
        exibir_resultado(resultado)
