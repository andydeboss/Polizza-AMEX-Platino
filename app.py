import streamlit as st

st.title("🤖 Assistente Coperture Amex Platino")
st.write("Scrivi liberamente la tua domanda o cosa ti è successo. L'assistente verificherà se sei coperto, ponendoti domande di chiarimento oppure rispondendo ai tuoi dubbi.")

# Definizione coperture con logica eventi + dubbi
coverages = [
    {
        "nome": "Spese mediche in viaggio",
        "keywords_evento": [
            "mi sento male", "malore", "malattia", "ospedale", "ambulanza",
            "infortunio", "mi sono fatto male", "mi sono rotto", "ricovero",
            "pronto soccorso"
        ],
        "keywords_dubbio": [
            "sono coperto se mi ammalo", "vale se sto male",
            "sono coperto per spese mediche", "copre ospedale", "cure all'estero"
        ],
        "domande": [
            "Il viaggio prevedeva almeno un volo o una notte in hotel prepagata?",
            "Hai pagato il viaggio con la Carta Platino?",
            "L'evento è avvenuto durante il viaggio e non prima della partenza?",
            "Non si tratta di una malattia cronica già nota?",
            "Hai referti o documentazione medica?"
        ],
        "risposta_dubbio": "✅ Le spese mediche sono coperte fino a €5.000.000 per persona, ma solo se il viaggio include un volo o una notte di hotel prepagata e se hai pagato con la Carta Platino. Sono escluse malattie croniche già note."
    },
    {
        "nome": "Annullamento o interruzione viaggio",
        "keywords_evento": [
            "ho annullato il viaggio", "ho cancellato la vacanza", "non sono partito",
            "viaggio saltato", "interruzione viaggio", "rientrato prima"
        ],
        "keywords_dubbio": [
            "sono coperto se annullo", "vale se devo annullare",
            "posso annullare", "copre se rientro prima"
        ],
        "domande": [
            "Hai pagato il viaggio con la Carta Platino?",
            "La causa dell’annullamento rientra tra quelle previste (malattia, lutto, infortunio, danni alla casa)?",
            "Hai documentazione a supporto (es. certificato medico)?",
            "Hai rispettato i tempi massimi di comunicazione?",
            "Le spese che chiedi erano non rimborsabili da altri fornitori?"
        ],
        "risposta_dubbio": "✅ L'annullamento è coperto fino a €10.000 per beneficiario, ma solo se il viaggio è stato pagato con Carta Platino e la causa rientra tra quelle previste (malattia, lutto, infortunio, danni alla casa)."
    },
    {
        "nome": "Effetti personali, denaro e documenti",
        "keywords_evento": [
            "furto bagagli", "rubato portafoglio", "scippo", "valigia sparita",
            "smarrito passaporto", "bagaglio non arrivato", "bagaglio perso"
        ],
        "keywords_dubbio": [
            "sono coperto se mi rubano", "vale per il furto", "copre documenti",
            "copre soldi", "copre valigia"
        ],
        "domande": [
            "Il furto o la perdita è avvenuto durante il viaggio?",
            "Hai fatto denuncia alla polizia o al vettore?",
            "Gli oggetti erano custoditi in modo adeguato?",
            "Il valore rientra nei limiti (3.000 € totali, 750 € max per articolo/documenti/denaro)?",
            "Hai prove di possesso o acquisto (scontrini, foto)?"
        ],
        "risposta_dubbio": "✅ Coperti furti o smarrimenti fino a €3.000 totali, con limite di €750 per articolo/documenti/denaro. Serve denuncia alle autorità e prova di possesso."
    },
    {
        "nome": "Noleggio auto",
        "keywords_evento": [
            "ho graffiato l'auto a noleggio", "danni auto a noleggio",
            "furto auto a noleggio", "incidentato macchina presa in vacanza"
        ],
        "keywords_dubbio": [
            "sono coperto se noleggio un'auto", "vale per auto a noleggio",
            "copre il noleggio auto", "copre danni auto affittata"
        ],
        "domande": [
            "Era un’auto a noleggio (non tua)?",
            "Il contratto era valido e intestato a te?",
            "Hai pagato il noleggio con la Carta Platino?",
            "Il sinistro è avvenuto durante il periodo di noleggio?",
            "Stavi guidando nel rispetto delle regole (no ebbrezza)?",
            "Hai denuncia o verbale del noleggiatore/autorità?"
        ],
        "risposta_dubbio": "✅ Coperti danni o furto fino a €75.000, ma solo per auto a noleggio legate a un viaggio con almeno un volo o una notte di hotel. Non copre noleggi usati 'sotto casa'."
    },
    {
        "nome": "Ritardo viaggio o mancata partenza",
        "keywords_evento": [
            "volo cancellato", "aereo in ritardo", "ritardo volo",
            "ho perso la coincidenza", "partenza annullata"
        ],
        "keywords_dubbio": [
            "sono coperto se il volo è in ritardo", "vale per ritardi",
            "copre se cancellano il volo"
        ],
        "domande": [
            "Il viaggio era stato pagato con la Carta Platino?",
            "Il ritardo o la cancellazione ha superato la soglia prevista (es. 4 ore)?",
            "Hai ricevuto conferma scritta del ritardo/cancellazione?",
            "Hai sostenuto spese extra e conservato ricevute?",
            "La causa rientra tra quelle ammesse (non dolo, non sciopero selvaggio)?"
        ],
        "risposta_dubbio": "✅ Coperti ritardi o cancellazioni con rimborso spese extra (pasti, hotel, trasferimenti) se superiori a 4 ore e se documentati."
    },
    {
        "nome": "Incidenti di viaggio",
        "keywords_evento": [
            "incidente in vacanza", "mi sono fatto male", "infortunio in viaggio",
            "sono caduto", "invalidità in viaggio", "morte in viaggio"
        ],
        "keywords_dubbio": [
            "sono coperto se ho un incidente", "copre invalidità", "copre morte",
            "vale per infortuni in viaggio"
        ],
        "domande": [
            "L’incidente è avvenuto durante un viaggio coperto (volo o notte prepagata)?",
            "Eri titolare della Carta Platino?",
            "Non si tratta di un’attività esclusa (es. sport estremi)?",
            "Hai referti medici o denuncia che provino l’incidente?",
            "L’evento è avvenuto entro i limiti temporali della polizza?"
        ],
        "risposta_dubbio": "✅ Previsti indennizzi per morte o invalidità permanente da infortunio in viaggio, entro i limiti di polizza e con esclusioni per attività rischiose."
    }
]

query = st.text_area("✍️ Scrivi qui la tua domanda o descrivi cosa è successo", height=100)

if st.button("Invia"):
    risposta = None

    for cov in coverages:
        if any(k in query.lower() for k in cov["keywords_dubbio"]):
            risposta = cov["risposta_dubbio"]
            st.info(f"ℹ️ {cov['nome']}: {risposta}")
            break
        elif any(k in query.lower() for k in cov["keywords_evento"]):
            st.subheader(f"Possibile copertura: {cov['nome']}")
            answers = []
            with st.form(key=f"form_{cov['nome']}"):
                for q in cov["domande"]:
                    answers.append(st.radio(q, ["Sì", "No"], index=0))
                submitted = st.form_submit_button("Verifica copertura")

            if submitted:
                if all(a == "Sì" for a in answers):
                    st.success(f"✅ {cov['dettagli']}")
                else:
                    st.error("❌ Non coperto: una o più condizioni non sono rispettate.")
            break

    if not risposta and not any(any(k in query.lower() for k in c["keywords_evento"]+c["keywords_dubbio"]) for c in coverages):
        st.warning("Non ho trovato una copertura corrispondente. Prova a riformulare la domanda.")
