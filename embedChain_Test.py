import streamlit as st
from embedchain import App

elon_bot = App()

# URLs to add
urls = [
    "https://www.canalplus-maurice.com/offres/pack-famille-767",
    "https://www.canalplus-maurice.com/offres-tv/tout-canal",
    "https://www.canalplus-maurice.com/offres/pack-decouverte-454",
    "https://www.canalplus-maurice.com/offres/pack-bollywood-455"
]

for url in urls:
    elon_bot.add(url)

# Streamlit UI
st.title("Elon Bot Query Interface")

# Get user input
query = st.text_input("Enter your query:")

# If there's a query and the user presses the button
if query and st.button("Query"):
    response = elon_bot.query(query)
    st.write(response)
