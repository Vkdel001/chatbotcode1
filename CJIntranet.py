import streamlit as st
import os

from embedchain import App

cj_bot = App()


# URLs to add
urls = [
"https://www.emtel.com/",
"https://www.emtel.com/5g",
"https://www.emtel.com/about-us/careers",
"https://www.emtel.com/about-us/company-profile",
"https://www.emtel.com/airbox/buy-airbox",
"https://www.emtel.com/airbox/home-fixed-voice-plans",
"https://www.emtel.com/airbox/postpaid-airbox",
"https://www.emtel.com/airbox/prepaid-airbox",
"https://www.emtel.com/airbox/user-guide",
"https://www.emtel.com/airbox5g",
"https://www.emtel.com/airbox-5g-plans",
"https://www.emtel.com/airtime-recharge",
"https://www.emtel.com/bangla-pack",
"https://www.emtel.com/bizconnect",
"https://www.emtel.com/business",
"https://www.emtel.com/contact/our-showrooms/locate-us",
"https://www.emtel.com/cookie-notice",
"https://www.emtel.com/corporate-social-responsibility",
"https://www.emtel.com/devices",
"https://www.emtel.com/emtel-app",
"https://www.emtel.com/emtel-welcome-pack",
"https://www.emtel.com/e-sim",
"https://www.emtel.com/friends-family",
"https://www.emtel.com/general-terms-and-conditions",
"https://www.emtel.com/international-calling",
"https://www.emtel.com/lite%26familyplans",
"https://www.emtel.com/media-centre",
"https://www.emtel.com/mobile-services/postpaid/get-new-connection",
"https://www.emtel.com/mobile-services/postpaid/illimite-data-packs",
"https://www.emtel.com/mobile-services/postpaid/voice-sms",
"https://www.emtel.com/mobile-services/prepaid/get-new-connection",
"https://www.emtel.com/mobile-services/prepaid/unlimited-data-packs",
"https://www.emtel.com/mobile-services/prepaid/unlimited-data-packs-old",
"https://www.emtel.com/mobile-services/prepaid/unlimited-voice-data-combo",
"https://www.emtel.com/mobile-services/prepaid/voice-sms-packs",
"https://www.emtel.com/online-frequently-asked-questions",
"https://www.emtel.com/pay-bill/postpaid/available-modes-of-payment",
"https://www.emtel.com/pay-recharge/pay-bill/postpaid-airbox",
"https://www.emtel.com/pay-recharge/pay-bill/postpaid-mobile",
"https://www.emtel.com/pay-recharge/prepaid-airbox",
"https://www.emtel.com/pay-recharge/prepaid-mobile",
"https://www.emtel.com/postpaidbundles",
"https://www.emtel.com/privacy-notice",
"https://www.emtel.com/puk",
"https://www.emtel.com/roaming-packs",
"https://www.emtel.com/services/international-postpaid-roaming",
"https://www.emtel.com/services/international-prepaid-roaming",
"https://www.emtel.com/services/value-added-services",
"https://www.emtel.com/services/value-added-services/caller-tunes",
"https://www.emtel.com/services/value-added-services/emtel-sos",
"https://www.emtel.com/services/value-added-services/fun-sms",
https://www.emtel.com/service-termshttps://www.emtel.com/tourist-pack
]


if 'cj_bot' not in st.session_state:
    st.session_state.cj_bot = App()
    for url in urls:
        st.session_state.cj_bot.add(url)

# Streamlit UI
st.title("EMTEL CHATBOT")

# Get user input
query = st.text_input("Enter your query:")

# If there's a query and the user presses the button
if query and st.button("Query"):
    response = cj_bot.query(query)
    st.write(response)
