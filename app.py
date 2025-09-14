import streamlit as st

# Database delle coperture Platino con sinonimi/keywords e checklist di domande in linguaggio naturale
database = [
    {
        "sinistro": "Spese mediche in viaggio",
        "keywords": [
            "malore", "mi sento male", "sto male", "ospedale", "ambulanza",
            "infortunio", "mi sono fatto male", "mi sono rotto", "pronto soccorso",
            "malattia", "sono ammalato", "ricovero", "incidentato"
        ],
        "domande": [
            "Il viaggio prevedeva almeno un volo o una notte in hotel prenotata?",
            "Hai pagato il viaggio con la Carta Platino?",
            "L'evento (malattia o infortunio) è avvenuto durante il viaggio e non prima della partenza?",
            "Si tratta di un evento improvviso e non di una condizione cronica già nota?",
            "Hai referti o documentazione medica che confermino l'accaduto?"
        ],
        "dettagli": "✅ Coperto fino a €5.000.000 per persona; cure dentistiche urgenti fino a €1.500."
    },
    {
        "sinistro": "Effetti personali, denaro e documenti in viaggio",
        "keywords": [
            "furto", "rubato", "scippo", "valigia", "bagaglio", "documenti",
            "portafoglio", "passaporto", "soldi", "bancomat", "borsa", "smarrito",
            "bagaglio perso", "bagaglio non arrivato", "valigia danneggiata"
        ],
        "domande": [
            "Il furto o la perdita è avvenuto durante il viaggio?",
            "Hai fatto denuncia alla polizia o al vettore?",
            "Gli oggetti erano custoditi in modo adeguato (non lasciati incustoditi)?",
            "Il valore rientra nei limiti di polizza (3.000 € totali, max 750 € per articolo/documenti/denaro)?",
            "Hai prove di possesso o acquisto degli oggetti (scontrini, foto, ricevute)?"
        ],
        "dettagli": "✅ Coperto fino a €3.000 totali; max €750 per articolo; max €750 per denaro/documenti."
    },
    {
        "sinistro": "Noleggio auto – danni o furto",
        "keywords": [
            "noleggio auto", "auto a noleggio", "macchina affittata",
            "ho graffiato l'auto", "graffiato la macchina", "danni auto",
            "furto auto", "rubato auto", "incidentato auto a noleggio",
            "danni alla macchina presa in vacanza"
        ],
        "domande": [
            "Era un’auto a noleggio (non di tua proprietà)?",
            "Il contratto era valido e intestato a te?",
            "Hai pagato il noleggio con la Carta Platino?",
            "Il sinistro è avvenuto durante il periodo di noleggio dichiarato?",
            "Stavi guidando nel rispetto delle regole (no ebbrezza, no uso improprio)?",
            "Hai denuncia o verbale del noleggiatore/autorità?"
        ],
        "dettagli": "✅ Coperto fino a €75.000 per evento."
    },
    {
        "sinistro": "Ritardo viaggio o mancata partenza",
        "keywords": [
            "ritardo volo", "volo cancellato", "aereo in ritardo", "mancata partenza",
            "ho perso la coincidenza", "treno in ritardo", "traghetto non partito",
            "partenza annullata", "hanno cancellato la mia partenza"
        ],
        "domande": [
            "Il viaggio era stato pagato con la Carta Platino?",
            "Il ritardo o la cancellazione è stato superiore alla soglia prevista (es. 4 ore)?",
            "Hai ricevuto conferma scritta del ritardo/cancellazione dalla compagnia?",
            "Hai sostenuto spese extra (pasti, hotel, trasferimenti) e le hai documentate?",
            "La causa del ritardo rientra tra quelle ammesse (non dolo, non sciopero selvaggio)?"
        ],
        "dettagli": "✅ Indennizzo per spese extra (pasti, pernottamenti) entro i limiti previsti."
    },
    {
        "sinistro": "Annullamento o interruzione viaggio",
        "keywords": [
            "annullamento", "cancellato viaggio", "non sono partito",
            "viaggio saltato", "interruzione viaggio", "rientrato prima",
            "ho dovuto annullare", "ho cancellato la vacanza", "non sono potuto partire"
        ],
        "domande": [
            "Hai pagato il viaggio con la Carta Platino?",
            "La causa dell’annullamento è tra quelle previste (malattia, infortunio, lutto, danni alla casa)?",
            "Hai certificato medico o altra documentazione che lo provi?",
            "Hai rispettato i tempi massimi di comunicazione alla compagnia?",
            "Le spese che chiedi erano non rimborsabili da altri fornitori?"
        ],
        "dettagli": "✅ Coperto fino a €10.000 per beneficiario per spese non rimborsabili."
    },
    {
        "sinistro": "Incidenti di viaggio",
        "keywords": [
            "incidente in vacanza", "mi sono fatto male", "infortunio in viaggio",
            "sono caduto", "invalidità in viaggio", "morte in viaggio",
            "incidentato in taxi", "incidente durante escursione", "caduto in hotel"
        ],
        "domande": [
            "L’incidente è avvenuto durante un viaggio coperto (con volo o notte prepagata)?",
            "Eri titolare della Carta Platino al momento dell’evento?",
            "Non si tratta di un’attività esclusa (es. sport estremi non previsti)?",
            "Hai referti medici o denuncia che provino l’incidente?",
            "L’evento è avvenuto entro i limiti temporali della polizza?"
        ],
        "dettagli": "✅ Indennizzi per morte o invalidità permanente da infortunio in viaggio, secondo i limiti di polizza."
    }
]

st.title("🤖 Assistente Coperture Amex Platino")
st.write("Scrivi in linguaggio naturale cosa ti è successo. Poi premi **Invia** per verificare se sei coperto. Ti farò alcune domande per controllare le condizioni della polizza.")

query = st.text_area("Descrivi cosa è successo", height=100)

if st.button("Invia"):
    if query:
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
