import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os
import json
import pandas as pd
import plotly.express as px

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-2.0-flash")

st.set_page_config(page_title="Análise de Sentimento", page_icon="💭")

def analisar_texto(texto):
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
    resposta_bruta = ""  # Inicializa para evitar UnboundLocalError
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

def contar_sentimentos(resultado):
    return {
        "Positivo": len(resultado.get("Positivo", [])),
        "Negativo": len(resultado.get("Negativo", [])),
        "Neutro": len(resultado.get("Neutro", []))
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

            dados = contar_sentimentos(resultado)
            total = sum(dados.values())
            df = pd.DataFrame([
                {
                    "Sentimento": k,
                    "Quantidade": v,
                    "Percentual": (v / total * 100) if total > 0 else 0
                } for k, v in dados.items()
            ])
            fig = px.bar(
                df,
                y="Sentimento",
                x="Quantidade",
                orientation="h",
                color="Sentimento",
                color_discrete_map={"Positivo": "#21c55d", "Negativo": "#ef4444", "Neutro": "#9ca3af"},
                text="Quantidade",
                title="Distribuição de Sentimentos no Texto",
            )
            fig.update_traces(
                texttemplate='%{x} (%{customdata[0]:.1f}%)',
                customdata=df[["Percentual"]],
                textposition='outside'
            )
            fig.update_layout(
                xaxis_title="Quantidade",
                yaxis_title="Sentimento",
                yaxis=dict(categoryorder='total ascending'),
                plot_bgcolor="#18181b",
                paper_bgcolor="#18181b",
                font=dict(color="#f1f5f9"),
                title_x=0.5,
                margin=dict(l=50, r=30, t=50, b=30),
                height=400
            )
            st.plotly_chart(fig, use_container_width=True)

st.title("💭 Análise de Sentimento de textos com IA")

texto_usuario = st.text_area("Digite o texto a ser analisado:")

st.write("OU")

uploaded_file = st.file_uploader("📂 Faça upload de um arquivo .txt", type=["txt"])

if st.button("Analisar Sentimento"):
    if texto_usuario.strip() == "":
        st.warning("Por favor, insira algum texto.")
    else:
        resultado = analisar_texto(texto_usuario)
        exibir_resultado(resultado)

if uploaded_file is not None:
    conteudo = uploaded_file.read().decode("utf-8")
    st.text_area("📄 Conteúdo do arquivo", value=conteudo, height=200)

    if st.button("Analisar Sentimento do Arquivo"):
        resultado = analisar_texto(conteudo)
        exibir_resultado(resultado)
