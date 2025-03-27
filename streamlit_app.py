import streamlit as st
import openai
from PIL import Image
import io

st.set_page_config(page_title="SicurANCE", layout="centered")

st.title("SicurANCE")
st.subheader("L'intelligenza artificiale al servizio della sicurezza nei cantieri")

uploaded_file = st.file_uploader("Carica un'immagine del cantiere", type=["jpg", "jpeg", "png"])

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Immagine caricata", use_column_width=True)
    st.write("Analisi in corso...")

    # Integrazione futura: invia immagine all'AI e genera report
    st.info("Report automatico: (funzione in fase di sviluppo)")

    # Placeholder di output
    st.markdown("""
    - Rischio: Operai senza DPI (caschi o imbracature)
    - Articolo violato: Art. 115 D.Lgs. 81/2008
    - Misura correttiva: Utilizzo di DPI e installazione linee vita
    """)
