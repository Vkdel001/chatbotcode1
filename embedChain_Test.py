import streamlit as st
import os

from embedchain import App

canal_bot = App()


# URLs to add
urls = [
"https://www.canalplus-maurice.com/",
"https://www.canalplus-maurice.com/mycanal",
"https://www.canalplus-maurice.com/offres-tv",
"https://www.canalplus-maurice.com/programmes-tv",
"https://www.canalplus-maurice.com/faq",
"https://www.canalplus-maurice.com/offres-internet",
"https://www.canalplus-maurice.com/contacts",
"https://www.canalplus-maurice.com/offres-tv/disney",
"https://www.canalplus-maurice.com/offres-tv/netflix",
"https://www.canalplus-maurice.com/cookies",
"https://www.canalplus-maurice.com/faq/mon-abonnement?thematic=Disney%2B",
"https://www.canalplus-maurice.com/offres/pack-cine-series-449",
"https://www.canalplus-maurice.com/offres/pack-famille-767",
"https://www.canalplus-maurice.com/contacts/formulaire/prive/store",
"https://www.canalplus-maurice.com/offres/pack-foot-sport-452",
"https://www.canalplus-maurice.com/services",
"https://www.canalplus-maurice.com/offres/pack-bollywood-455",
"https://www.canalplus-maurice.com/offres-tv/tout-canal",
"https://www.canalplus-maurice.com/offres/pack-decouverte-454",
"https://www.canalplus-maurice.com/programmes/program/264396908",
"https://www.canalplus-maurice.com/faq/l-assistance-technique",
"https://www.canalplus-maurice.com/faq/les-programmes",
"https://www.canalplus-maurice.com/faq/mycanal",
"https://www.canalplus-maurice.com/faq/nouveaux-abonnes",
"https://www.canalplus-maurice.com/faq/programme-fidelite",
"https://www.canalplus-maurice.com/faq/s-inscrire-et-naviguer",
"https://www.canalplus-maurice.com/contacts/formulaire/prive",
"https://www.canalplus-maurice.com/services/decodeur-4k-ultra-hd",
"https://drive.google.com/file/d/1Nf_3enLYHm4wtxGA7ImF7yL7J_Fp2cG-/view?usp=sharing"
]


if 'canal_bot' not in st.session_state:
    st.session_state.canal_bot = App()
    for url in urls:
        st.session_state.canal_bot.add(url)

# Streamlit UI
st.title("MC Vision CHATBOT")

# Get user input
query = st.text_input("Enter your query:")

# If there's a query and the user presses the button
if query and st.button("Query"):
    response = canal_bot.query(query)
    st.write(response)
