import streamlit as st
import os

from embedchain import App

cj_bot = App()


# URLs to add
urls = [
"https://www.currimjee.com/",
"https://www.currimjee.com/fr",
"https://www.currimjee.com/about-us/group-structure",
"https://www.currimjee.com/about-us/our-team",
"https://www.currimjee.com/about-us/at-a-glance",
"https://www.currimjee.com/our-world/real-estate",
"https://www.currimjee.com/our-world/telecoms-media-it",
"https://www.currimjee.com/our-world/tourism-hospitality",
"https://www.currimjee.com/our-world/commerce-financial-services",
"https://www.currimjee.com/our-world/energy",
"https://www.currimjee.com/our-world/home-personal-care",
"https://www.currimjee.com/investors/governance",
"https://www.currimjee.com/our-world/food-beverages",
"https://www.currimjee.com/we-care",
"https://www.currimjee.com/our-people/life-at-currimjee",
"https://www.currimjee.com/mediaroom/gallery",
"https://www.currimjee.com/our-people/join-us",
"https://www.currimjee.com/news",
"https://www.currimjee.com/other/contact-us",
"https://www.currimjee.com/mediaroom/download",
"https://www.currimjee.com/news/le-groupe-currimjee-annonce-une-reorganisation-strategique-majeure",
"https://www.currimjee.com/news/canal-plug-play-now",
"https://www.currimjee.com/news/football-plug-play",
"https://www.currimjee.com/news/innovation-canal",
"https://www.currimjee.com/news/performance-financiere-positive-pour-compagnie-immobiliere-ltee",
"https://www.currimjee.com/news/cjnews-4u",
"https://www.currimjee.com/news/encore-plus-de-cinema-pour-tous",
"https://www.currimjee.com/news/cj-news-edition-speciale-we-care-we-do",
"https://www.currimjee.com/news/currimjee-jeewanjee-proudly-sponsors-the-mo-zar-back-on-the-road-tour",
"https://www.currimjee.com/news/coral-reef-restoration-launching-of-phase-2",
"https://www.currimjee.com/news/cil-analyst-meeting-08-june-2023",
"https://www.currimjee.com/news/aruba-fy22-africa-reseller-of-the-year-award",
"https://www.currimjee.com/news/vos-programmes-quand-vous-voulez-avec-canal",
"https://www.currimjee.com/news/cj-news-special-edition",
"https://www.currimjee.com/news/promoting-access-to-healthcare-for-all",
"https://www.currimjee.com/news/rainwater-harvesting-project",
"https://www.currimjee.com/news/the-currimjee-foundation-supports-dibout-ansam",
"https://www.currimjee.com/news/vine-pran-kont-to-la-sante",
"https://www.currimjee.com/news/l-eau-est-un-tresor-preservons-la",
"https://www.currimjee.com/news/la-fondation-currimjee-apporte-son-soutien-a-dibout-ansam",
"https://www.currimjee.com/news/les-employes-de-currimjee-jeewanjee-interpretent-natir-en-collaboration-avec-l-atelier-mo-zar",
"https://www.currimjee.com/news/entrepreneuriat-social-trampoline-by-currimjee-lance-un-appel-a-candidatures-pour-sa-2e-edition",
"https://www.currimjee.com/news/le-portefeuille-de-compagnie-immobiliere-limitee-passe-de-rs-400-millions-a-rs-1-7-milliard",
"https://www.currimjee.com/news/emtel-eoy-brochure-2022",
"https://www.currimjee.com/news/dividend-declaration-notice",
"https://www.currimjee.com/news/further-admission-document-of-compagnie-immobiliere-limitee",
"https://www.currimjee.com/news/update-regarding-the-acquisition-of-multi-channel-retail-limited-and-the-consideration-issue",
"https://www.currimjee.com/news/results-of-special-meeting-of-shareholders",
"https://www.currimjee.com/news/no-to-drug-project",
"https://www.currimjee.com/news/journee-internationale-des-droits-de-l-enfant",
"https://www.currimjee.com/news/blink-by-emtel",
"https://www.currimjee.com/news/abridged-unaudited-financial-statements-for-the-period-ended-30-september-2022",
"https://www.currimjee.com/news/the-currimjee-jeewanjee-video-newsletter-is-back",
"https://www.currimjee.com/news/notice-of-special-meeting-of-shareholders",
"https://www.currimjee.com/news/cil-shareholders-presentation",
"https://www.currimjee.com/news/lutte-contre-la-drogue-la-fondation-sensibilise-les-enfants",
"https://www.currimjee.com/news/compagnie-immobiliere-ltee-expansion-plan-to-grow-the-company-s-property-portfolio-1",
"https://www.currimjee.com/news/notice-abridged-unaudited-financial-statements-for-the-period-ended-30-september-2022",
"https://www.currimjee.com/news/ensemble-luttons-contre-la-pauvrete",
"https://www.currimjee.com/news/world-clean-up-day-currimjee-mobilise-ses-troupes-a-maurice-comme-dans-la-region",
"https://www.currimjee.com/news/abridged-unaudited-financial-statements-for-the-period-ended-30-june-2022-1",
"https://www.currimjee.com/news/abridged-unaudited-financial-statements-for-the-period-ended-30-june-2022",
"https://www.currimjee.com/news/airbox5g-by-emtel",
"https://www.currimjee.com/news/mycanal-une-app-tout-canal",
"https://www.currimjee.com/news/emtel-mega-blood-donation-2022",
"https://www.currimjee.com/news/blink-by-emtel-a-revolutionary-mobile-payment-app",
"https://www.currimjee.com/news/sustainable-development-new-modern-glass-bottling-line-of-quality-beverages-ltd",
"https://www.currimjee.com/news/world-health-day-2022",
"https://www.currimjee.com/news/new-luxurious-and-modern-quartz-collections-at-batimex-ltd",
"https://www.currimjee.com/news/emtel-quizmaster",
"https://www.currimjee.com/news/currimjee-wellness-event",
"https://www.currimjee.com/news/earth-hour-2022-let-s-shape-our-future",
"https://www.currimjee.com/news/compagnie-immobiliere-ltee-expansion-plan-to-grow-the-company-s-property-portfolio",
"https://www.currimjee.com/news/programme-d-etudes-pour-les-jeunes-footballeurs-de-la-mangalkhan-academy",
"https://www.currimjee.com/news/supporting-the-youth-s-education",
"https://www.currimjee.com/news/launch-of-friends-of-mauritian-wildlife",
"https://www.currimjee.com/news/trampoline-by-currimjee-les-gagnants-du-programme-d-acceleration-dedie-aux-projets-a-impact-positif-connus",
"https://www.currimjee.com/news/projet-pilote-l-universite-de-maurice-et-la-fondation-currimjee-oeuvrent-a-la-rehabilitation-du-recif-corallien-dans-le-sud-de-l-ile",
"https://www.currimjee.com/news/le-groupe-currimjee-lance-trampoline-un-accelerateur-d-entreprises-a-impact-positif",
"https://www.currimjee.com/news/world-clean-up-day-2021-becoming-part-of-the-solution",
"https://www.currimjee.com/news/third-integrated-report-of-currimjee-jeewanjee-and-company-limited",
"https://www.currimjee.com/news/currimjee-jeewanjee-celebrates-the-world-environment-day",
"https://www.currimjee.com/news/currimjee-jeewanjee-and-co-ltd-organise-la-distribution-de-100-packs-alimentaires-et-de-100-packs-scolaires-a-ti-rodrigues",
"https://www.currimjee.com/news/currimjee-jeewanjee-winner-at-the-pwc-corporate-reporting-awards-2020",
"https://www.currimjee.com/news/departure-of-teddy-bhullar-emtel-ceo-appointment-of-kresh-goomany-to-the-head-of-the-first-mobile-operator",
"https://www.currimjee.com/news/emtel-se-mobilise-pour-nettoyer-ebene",
"https://www.currimjee.com/news/emtel-s-associe-a-l-ong-codepa-pour-sa-campagne-de-nettoyage-annuelle-dans-la-cybercite-d-ebene",
"https://www.currimjee.com/news/53eme-journee-mondiale-de-la-terre-mc-vision-canal-maurice-de-plus-en-plus-ecoresponsable",
"https://www.currimjee.com/our-people",
"https://www.currimjee.com/fr/a-propos-de-nous/structure-du-groupe",
"https://www.currimjee.com/other/cookie-policy",
"https://www.currimjee.com/fr/a-propos-de-nous/en-bref",
"https://www.currimjee.com/fr/a-propos-de-nous/notre-equipe-de-direction",
"https://www.currimjee.com/fr/nos-activites/telecoms-media-ntic",
"https://www.currimjee.com/fr/nos-activites/immobilier",
"https://www.currimjee.com/fr/nos-activites/commerce-services-financiers",
"https://www.currimjee.com/fr/nos-activites/energie",
"https://www.currimjee.com/fr/nos-activites/produits-alimentaires-boissons",
"https://www.currimjee.com/fr/nos-activites/beaute-et-produits-menagers",
"https://www.currimjee.com/fr/investisseurs/gouvernance",
"https://www.currimjee.com/fr/nos-engagements",
"https://www.currimjee.com/fr/nos-equipes/la-vie-chez-currimjee",
"https://www.currimjee.com/fr/nos-equipes/rejoignez-nous",
"https://www.currimjee.com/fr/media/galerie",
"https://www.currimjee.com/fr/nos-activites/tourisme-hotellerie",
"https://www.currimjee.com/fr/media/publications",
"https://www.currimjee.com/fr/autre/contactez-nous",
"https://www.currimjee.com/fr/actualites/encore-plus-de-cinema-pour-tous",
"https://www.currimjee.com/fr/actualites/canal-plug-play-now",
"https://www.currimjee.com/fr/actualites",
"https://www.currimjee.com/fr/actualites/currimjee-jeewanjee-proudly-sponsors-the-mo-zar-back-on-the-road-tour",
"https://www.currimjee.com/fr/actualites/innovation-canal",
"https://www.currimjee.com/fr/actualites/performance-financiere-positive-pour-compagnie-immobiliere-ltee",
"https://www.currimjee.com/fr/actualites/cil-analyst-meeting-08-june-2023",
"https://www.currimjee.com/fr/actualites/cjnews-4u",
"https://www.currimjee.com/fr/actualites/cj-news-edition-speciale-we-care-we-do",
"https://www.currimjee.com/fr/actualites/coral-reef-restoration-launching-of-phase-2",
"https://www.currimjee.com/fr/actualites/aruba-fy22-africa-reseller-of-the-year-award",
"https://www.currimjee.com/fr/actualites/vos-programmes-quand-vous-voulez-avec-canal",
"https://www.currimjee.com/other/general-privacy-notice",
"https://www.currimjee.com/fr/actualites/cj-news-special-edition",
"https://www.currimjee.com/fr/actualites/les-employes-de-currimjee-jeewanjee-interpretent-natir-en-collaboration-avec-l-atelier-mo-zar",
"https://www.currimjee.com/fr/actualites/promoting-access-to-healthcare-for-all",
"https://www.currimjee.com/fr/actualites/the-currimjee-foundation-supports-dibout-ansam",
"https://www.currimjee.com/fr/actualites/l-eau-est-un-tresor-preservons-la",
"https://www.currimjee.com/fr/actualites/la-fondation-currimjee-apporte-son-soutien-a-dibout-ansam",
"https://www.currimjee.com/fr/actualites/entrepreneuriat-social-trampoline-by-currimjee-lance-un-appel-a-candidatures-pour-sa-2e-edition",
"https://www.currimjee.com/fr/actualites/rainwater-harvesting-project",
"https://www.currimjee.com/fr/actualites/le-portefeuille-de-compagnie-immobiliere-limitee-passe-de-rs-400-millions-a-rs-1-7-milliard",
"https://www.currimjee.com/fr/actualites/le-groupe-currimjee-annonce-une-reorganisation-strategique-majeure",
"https://www.currimjee.com/fr/actualites/emtel-eoy-brochure-2022",
"https://www.currimjee.com/fr/actualites/blink-by-emtel",
"https://www.currimjee.com/fr/actualites/dividend-declaration-notice",
"https://www.currimjee.com/fr/actualites/update-regarding-the-acquisition-of-multi-channel-retail-limited-and-the-consideration-issue",
"https://www.currimjee.com/fr/actualites/further-admission-document-of-compagnie-immobiliere-limitee",
"https://www.currimjee.com/fr/actualites/vine-pran-kont-to-la-sante",
"https://www.currimjee.com/fr/actualites/results-of-special-meeting-of-shareholders",
"https://www.currimjee.com/fr/actualites/journee-internationale-des-droits-de-l-enfant",
"https://www.currimjee.com/fr/actualites/notice-abridged-unaudited-financial-statements-for-the-period-ended-30-september-2022",
"https://www.currimjee.com/fr/actualites/abridged-unaudited-financial-statements-for-the-period-ended-30-september-2022",
"https://www.currimjee.com/fr/actualites/the-currimjee-jeewanjee-video-newsletter-is-back",
"https://www.currimjee.com/fr/actualites/no-to-drug-project",
"https://www.currimjee.com/fr/actualites/cil-shareholders-presentation",
"https://www.currimjee.com/fr/actualites/lutte-contre-la-drogue-la-fondation-sensibilise-les-enfants",
"https://www.currimjee.com/fr/actualites/compagnie-immobiliere-ltee-expansion-plan-to-grow-the-company-s-property-portfolio-1",
"https://www.currimjee.com/fr/actualites/ensemble-luttons-contre-la-pauvrete",
"https://www.currimjee.com/fr/actualites/incredibollywood",
"https://www.currimjee.com/fr/actualites/world-clean-up-day-currimjee-mobilise-ses-troupes-a-maurice-comme-dans-la-region",
"https://www.currimjee.com/fr/actualites/notice-of-special-meeting-of-shareholders",
"https://www.currimjee.com/fr/actualites/abridged-unaudited-financial-statements-for-the-period-ended-30-june-2022-1",
"https://www.currimjee.com/fr/actualites/abridged-unaudited-financial-statements-for-the-period-ended-30-june-2022",
"https://www.currimjee.com/fr/actualites/airbox5g-by-emtel",
"https://www.currimjee.com/fr/actualites/mycanal-une-app-tout-canal",
"https://www.currimjee.com/fr/actualites/pouvoir-de-tout-voir",
"https://www.currimjee.com/fr/actualites/canal-dans-la-langue-de-votre-choix",
"https://www.currimjee.com/fr/actualites/emtel-mega-blood-donation-2022",
"https://www.currimjee.com/fr/actualites/serie-limitee",
"https://www.currimjee.com/fr/actualites/sustainable-development-new-modern-glass-bottling-line-of-quality-beverages-ltd",
"https://www.currimjee.com/fr/actualites/world-health-day-2022",
"https://www.currimjee.com/fr/actualites/new-luxurious-and-modern-quartz-collections-at-batimex-ltd",
"https://www.currimjee.com/fr/actualites/emtel-quizmaster",
"https://www.currimjee.com/fr/actualites/currimjee-wellness-event",
"https://www.currimjee.com/fr/actualites/blink-by-emtel-a-revolutionary-mobile-payment-app",
"https://www.currimjee.com/fr/actualites/compagnie-immobiliere-ltee-expansion-plan-to-grow-the-company-s-property-portfolio",
"https://www.currimjee.com/fr/actualites/supporting-the-youth-s-education",
"https://www.currimjee.com/fr/actualites/programme-d-etudes-pour-les-jeunes-footballeurs-de-la-mangalkhan-academy",
"https://www.currimjee.com/fr/actualites/tous-les-programmes-un-seul-endroit",
"https://www.currimjee.com/fr/actualites/launch-of-friends-of-mauritian-wildlife",
"https://www.currimjee.com/fr/actualites/gagn-lagam-gete",
"https://www.currimjee.com/fr/actualites/earth-hour-2022-let-s-shape-our-future",
"https://www.currimjee.com/fr/actualites/vos-nouvelles-chaines-sont-la",
"https://www.currimjee.com/fr/actualites/trampoline-by-currimjee-les-gagnants-du-programme-d-acceleration-dedie-aux-projets-a-impact-positif-connus",
"https://www.currimjee.com/fr/actualites/projet-pilote-l-universite-de-maurice-et-la-fondation-currimjee-oeuvrent-a-la-rehabilitation-du-recif-corallien-dans-le-sud-de-l-ile",
"https://www.currimjee.com/fr/actualites/le-groupe-currimjee-lance-trampoline-un-accelerateur-d-entreprises-a-impact-positif",
"https://www.currimjee.com/fr/actualites/world-clean-up-day-2021-becoming-part-of-the-solution",
"https://www.currimjee.com/fr/actualites/third-integrated-report-of-currimjee-jeewanjee-and-company-limited",
"https://www.currimjee.com/fr/actualites/currimjee-jeewanjee-celebrates-the-world-environment-day",
"https://www.currimjee.com/fr/actualites/currimjee-jeewanjee-and-co-ltd-organise-la-distribution-de-100-packs-alimentaires-et-de-100-packs-scolaires-a-ti-rodrigues",
"https://www.currimjee.com/fr/actualites/currimjee-jeewanjee-winner-at-the-pwc-corporate-reporting-awards-2020",
"https://www.currimjee.com/fr/actualites/departure-of-teddy-bhullar-emtel-ceo-appointment-of-kresh-goomany-to-the-head-of-the-first-mobile-operator",
"https://www.currimjee.com/fr/actualites/emtel-se-mobilise-pour-nettoyer-ebene",
"https://www.currimjee.com/fr/actualites/emtel-s-associe-a-l-ong-codepa-pour-sa-campagne-de-nettoyage-annuelle-dans-la-cybercite-d-ebene",
"https://www.currimjee.com/fr/actualites/53eme-journee-mondiale-de-la-terre-mc-vision-canal-maurice-de-plus-en-plus-ecoresponsable",
"https://www.currimjee.com/fr/nos-equipes",
"https://www.currimjee.com/fr/autre/politique-de-cookies",
"https://www.currimjee.com/fr/autre/politique-generale-de-confidentialite",
"https://www.currimjee.com/our-world/telecoms-media-it/emtel",
"https://www.currimjee.com/our-world/telecoms-media-it/screenage",
"https://www.currimjee.com/our-world/telecoms-media-it/seejay-cellular-ltd",
"https://www.currimjee.com/our-world/telecoms-media-it/cinf",
"https://www.currimjee.com/our-world/real-estate/cre",
"https://www.currimjee.com/our-world/real-estate/multi-channel-retail-limited-mcr",
"https://www.currimjee.com/our-world/real-estate/plaisance-aeroville-limited",
"https://www.currimjee.com/our-world/telecoms-media-it/mc-vision",
"https://www.currimjee.com/our-world/real-estate/compagnie-immobiliere-limitee-cil",
"https://www.currimjee.com/our-world/tourism-hospitality/iko-mauritius-resort-village-ltd",
"https://www.currimjee.com/our-world/tourism-hospitality/anantara-iko-mauritius-resort-villas",
"https://www.currimjee.com/our-world/commerce-financial-services/batimex-ltd",
"https://www.currimjee.com/our-world/commerce-financial-services/island-life-assurance-co-ltd-ila",
"https://www.currimjee.com/our-world/tourism-hospitality/silver-wings",
"https://www.currimjee.com/our-world/energy/totalenergies",
"https://www.currimjee.com/our-world/home-personal-care/soap-allied-industries-limited-sail",
"https://www.currimjee.com/our-world/food-beverages/creative-advertising-bureau-ltd",
"https://www.currimjee.com/our-world/food-beverages/quality-beverage",
"https://www.currimjee.com/our-world/tourism-hospitality/singapore-airlines-gsa",
"https://www.currimjee.com/our-world/energy/ceejay-gas-ltd",
"https://www.currimjee.com/our-people/life-at-currimjee/network-engineer",
"https://www.currimjee.com/our-people/life-at-currimjee/accounting-associates-1",
"https://www.currimjee.com/our-people/life-at-currimjee/credit-administration-specialist",
"https://www.currimjee.com/our-people/life-at-currimjee/customer-experience-officer",
"https://www.currimjee.com/fr/nos-activites/telecoms-media-ntic/mc-vision",
"https://www.currimjee.com/fr/nos-activites/telecoms-media-ntic/seejay-cellular-ltd",
"https://www.currimjee.com/fr/nos-activites/telecoms-media-ntic/screenage",
"https://www.currimjee.com/fr/nos-activites/immobilier/currimjee-real-estate",
"https://www.currimjee.com/fr/nos-activites/telecoms-media-ntic/emtel",
"https://www.currimjee.com/fr/nos-activites/immobilier/multi-channel-retail-limited-mcr",
"https://www.currimjee.com/fr/nos-activites/immobilier/plaisance-aeroville-limited",
"https://www.currimjee.com/fr/nos-activites/telecoms-media-ntic/cinf",
"https://www.currimjee.com/fr/nos-activites/commerce-services-financiers/island-life-assurance-co-ltd-ila",
"https://www.currimjee.com/fr/nos-activites/immobilier/compagnie-immobiliere-limitee-cil",
"https://www.currimjee.com/fr/nos-activites/energie/total-mauritius-limited",
"https://www.currimjee.com/fr/nos-activites/produits-alimentaires-boissons/quality-beverages",
"https://www.currimjee.com/fr/nos-activites/produits-alimentaires-boissons/central-distributors-company-limited-cdco",
"https://www.currimjee.com/fr/nos-activites/commerce-services-financiers/batimex-ltd",
"https://www.currimjee.com/fr/nos-activites/energie/ceejay-gas-ltd",
"https://www.currimjee.com/fr/nos-activites/produits-alimentaires-boissons/creative-advertising-bureau-ltd",
"https://www.currimjee.com/fr/nos-activites/beaute-et-produits-menagers/soap-allied-industries-limited-sail",
"https://www.currimjee.com/fr/nos-activites/tourisme-hotellerie/singapore-airlines",
"https://www.currimjee.com/fr/nos-activites/tourisme-hotellerie/iko-mauritius-resort-village-ltd",
"https://www.currimjee.com/fr/nos-activites/tourisme-hotellerie/anantara-iko-mauritius-resort-villas",
"https://www.currimjee.com/fr/nos-activites/tourisme-hotellerie/silver-wings"
]


if 'cj_bot' not in st.session_state:
    st.session_state.cj_bot = App()
    for url in urls:
        st.session_state.cj_bot.add(url)

# Streamlit UI
st.title("MC Vision CHATBOT")

# Get user input
query = st.text_input("Enter your query:")

# If there's a query and the user presses the button
if query and st.button("Query"):
    response = cj_bot.query(query)
    st.write(response)