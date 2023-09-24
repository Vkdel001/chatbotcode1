import streamlit as st
import os

from embedchain import App

canal_bot = App()


# URLs to add
urls = [
"https://www.canalplus-maurice.com/",
"https://www.canalplus-maurice.com/mycanal",
"https://www.canalplus-maurice.com/offres-tv",
"https://www.canalplus-maurice.com/programmes-tv"
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
