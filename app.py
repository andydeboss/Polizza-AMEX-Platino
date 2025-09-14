import streamlit as st

# Database delle coperture Platino con parole chiave, checklist condizioni e dettagli
database = [
    {
        "sinistro": "Spese mediche in viaggio",
        "keywords": ["mediche", "ospedale", "infortunio", "malattia"],
        "domande": [
            "Il viaggio era all'estero?",
            "Le spese mediche derivano da un evento improvviso e imprevisto?",
            "Hai usato la Carta Platino per pagare il viaggio?"
        ],
        "dettagli": "Coperto fino a €5.000.000 per persona; cure dentistiche urgenti fino a €1.500."
    },
    {
        "sinistro": "Annullamento o interruzione viaggio",
        "keywords": ["annullamento", "interruzione", "cancellazione", "partenza"],
        "domande": [
            "Il viaggio era stato prenotato con la Carta Platino?",
            "La causa dell'annullamento rientra tra quelle previste (malattia, infortunio, danni alla casa, ecc.)?",
            "Hai rispettato le tempistiche di comunicazione richieste dalla polizza?"
        ],
        "dettagli": "Coperto fino a €10.000 per beneficiario per spese non rimborsabili."
    },
    {
        "sinistro": "Effetti personali, denaro e documenti in viaggio",
        "keywords": ["furto", "bagaglio", "documenti", "denaro", "valigia"],
        "domande": [
            "Il furto o smarrimento è avvenuto durante il viaggio?",
            "Hai denunciato l'accaduto alle autorità competenti?",
            "Gli effetti personali erano sotto la tua custodia o in un luogo sicuro?"
        ],
        "dettagli": "Coperto fino a €3.000 totali; max €750 per articolo; max €750 per denaro/documenti."
    },
    {
        "sinistro": "Noleggio auto – danni o furto",
        "keywords": ["auto", "noleggio", "furto auto", "danno auto", "veicolo"],
        "domande": [
            "Il veicolo era noleggiato con contratto valido a tuo nome?",
            "Hai usato la Carta Platino per pagare il noleggio?",
            "Il sinistro è avvenuto durante il periodo di noleggio dichiarato?"
        ],
        "dettagli": "Coperto fino a €75.000 per evento."
    },
    {
        "sinistro": "Ritardo viaggio o mancata partenza",
        "keywords": ["ritardo", "mancata partenza", "volo in ritardo", "perdita coincidenza"],
        "domande": [
            "Il viaggio era stato acquistato con la Carta Platino?",
            "Il ritardo supera le ore minime previste dal contratto (es. 4 ore)?",
            "Hai conservato ricevute delle spese extra sostenute?"
        ],
        "dettagli": "Indennizzo per spese extra (pasti, pernottamenti) entro i limiti previsti."
    },
    {
        "sinistro": "Incidenti di viaggio",
        "keywords": ["incidente", "morte", "invalidità", "infortunio viaggio"],
        "domande": [
            "L'incidente è avvenuto durante un viaggio coperto?",
            "Eri titolare di Carta Platino al momento dell'evento?",
            "L'incidente non rientra tra le esclusioni (es. sport estremi)?"
        ],
        "dettagli": "Indennizzi per morte o invalidità permanente da infortunio durante il viaggio, secondo i limiti di polizza."
    }
]

st.title("🤖 Assistente Coperture Amex Platino")
st.write("Scrivi in linguaggio naturale cosa ti è successo e l'app verificherà se sei coperto.")

query = st.text_input("Descrivi il sinistro")

if query:
    # ricerca corrispondenza con parole chiave
    match = None
    for item in database:
        if any(k in query.lower() for k in item["keywords"]):
            match = item
            break

    if match:
        st.subheader(f"Possibile copertura: {match['sinistro']}")

        answers = []
        with st.form(key="checklist"):
            for q in match["domande"]:
                answers.append(st.radio(q, ["Sì", "No"], index=0))
            submitted = st.form_submit_button("Verifica copertura")

        if submitted:
            if all(a == "Sì" for a in answers):
                st.success("✅ Coperto")
                st.write(match["dettagli"])
            else:
                st.error("❌ Non coperto")
                st.write("Una o più condizioni richieste dalla polizza non sono rispettate.")
    else:
        st.warning("Non ho trovato una copertura corrispondente. Prova a descrivere diversamente il sinistro.")
