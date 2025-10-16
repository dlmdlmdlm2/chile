# elecciones_chile_app.py
import streamlit as st

st.set_page_config(page_title="Elecciones Chile", page_icon="🇨🇱", layout="centered")

st.title("📊 Elecciones en Chile — Datos Reales")
st.write("Este panel muestra datos reales de elecciones municipales/regionales 2024 y primarias presidenciales 2025 en Chile.")

st.header("Elecciones Municipales y Regionales 2024")

col1, col2 = st.columns(2)
with col1:
    st.subheader("Fecha")
    st.write("26 y 27 de octubre de 2024")  # según fuentes wikipedia / resultados electorales
with col2:
    st.subheader("Participación")
    st.write("≈ 84,87 % del padrón electoral")  # cifra reportada para las municipales/regionales 2024 :contentReference[oaicite:0]{index=0}

st.markdown("---")

st.header("Primarias Presidenciales 2025 (Pacto Unidad por Chile)")

st.subheader("Fecha")
st.write("29 de junio de 2025")  # fecha primarias presidenciales :contentReference[oaicite:1]{index=1}

st.subheader("Resultados preliminares (93,73 % de mesas escrutadas)")  
# Datos del SERVEL preliminares :contentReference[oaicite:2]{index=2}
st.write("- Jeannette Jara: 760,295 votos (~60,48 %)")  
st.write("- Carolina Tohá: 348,473 votos (~27,72 %)")  
st.write("- Gonzalo Winter: 113,340 votos (~9,02 %)")  
st.write("- Jaime Mulet: 34,960 votos (~2,78 %)")  
st.write("- Votos nulos: 31,690 (~2,43 %)")  
st.write("- Votos en blanco: 13,186 (~1,01 %)")  
st.write("- Total de sufragios: 1,301,944 votos válidos + nulos + blancos")  

st.markdown("---")

st.header("Elección Presidencial Chile 2025")

st.subheader("Fecha oficial")
st.write("16 de noviembre de 2025")  # fecha de la elección presidencial chilena 2025 :contentReference[oaicite:3]{index=3}

st.subheader("Segunda vuelta")
st.write("14 de diciembre de 2025 (si ningún candidato obtiene más del 50 % en primera vuelta)") :contentReference[oaicite:4]{index=4}

st.subheader("Condiciones legales y requisitos")
st.write("""
- El sufragio es obligatorio para la mayoría de las elecciones (no para primarias)  
- Para candidaturas independientes se exige recolectar patrocinios (aproximadamente 35,361 firmas) :contentReference[oaicite:5]{index=5}  
- Los partidos también tienen umbrales mínimos de afiliación para postular sus candidatos oficiales :contentReference[oaicite:6]{index=6}  
""")

st.markdown("---")

st.caption("Fuentes: SERVEL, Wikipedia, medios chilenos sobre elecciones 2024–2025")
