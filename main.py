import streamlit as st
import pandas as pd

# Versión Grupal
from inc.basic import *

# Configuración de la página
md_presentation = "streamlit_sources/presentation.md"
st.set_page_config(page_title="DSB10RT Grupo A", layout="wide", initial_sidebar_state="collapsed")

# Título principal
col1, col2 = st.columns([3, 1])
with col1:
    st.title("Proyecto Final")
with col2:
    logo_path = "streamlit_sources/hab_logo.png"
    st.image(logo_path, width=100)

# Barra lateral con submenús
menu = st.sidebar.radio(
    "¿Qué quieres visitar?:",
    ("Presentación del Proyecto", "Presentación del Estudio", "Desarrollo del Estudio")
)

# 1. Presentación del Proyecto
if menu == "Presentación del Proyecto":
    st.header("Presentación del Proyecto")
    st.subheader("Proyecto de:")
    autores()

# 2. Presentación del Estudio
elif menu == "Presentación del Estudio":
    st.header("Presentación del Estudio")
    txt_presentation = read_markdown_file(md_presentation)
    st.markdown(txt_presentation)

# 3. Desarrollo del Estudio
elif menu == "Desarrollo del Estudio":
    st.header("Desarrollo del Estudio")
    st.write("""
        Prueba
    """)
    df = pd.read_csv("data/Yoga_figure_surya_namaskar_A - Hoja 1.csv")
    st.dataframe(df)
    # Aprox. = % continuo, Tonif. = Bien solo con +70%, Perf. = Bien solo con +90%
    difficulty = st.selectbox("Escoja la exigencia:", ["Aproximación", "Tonificación", "Perfección"])
    
    level = st.selectbox("Escoja el nivel de tu clase:", ["Básico", "Medio", "Experto"])

    duration = st.slider("¿De cuánto tiempo dispones?", 30, 90)

    # Buscar manera de Encontrar Vid / Name_Postura
    postura = "Tadasana"
    
    DEFAULT_WIDTH = 30
    VIDEO_DATA = "data/01_Tadasana/Figura1_Tadasana_Postura de equilibro.mov"
    width = st.sidebar.slider(
        label= "Tamaño del Video:",
        min_value=15,
        max_value=50,
        value=DEFAULT_WIDTH,
        format="%d%%")
    width = max(width, 0.01)
    side = max((100 - width) / 2, 0.01)
    # Creacion de 2 columnas side para centrar el Container del Vid
    _, container, _ = st.columns([side, width, side])
    container.subheader(f"Video ejemplo de la postura {postura}:")
    container.video(data=VIDEO_DATA)
    user_input = st.camera_input(f"Inicie la postura {postura}")