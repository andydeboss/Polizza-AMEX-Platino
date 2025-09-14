import streamlit as st

# Inizializzazione dello stato
if "categoria" not in st.session_state:
    st.session_state.categoria = None
if "step" not in st.session_state:
    st.session_state.step = 0
if "answers" not in st.session_state:
    st.session_state.answers = []
if "finished" not in st.session_state:
    st.session_state.finished = False

# Database delle coperture con domande e dettagli
coverages = {
    "Spese mediche in viaggio": {
        "domande": [
            ("Il viaggio prevedeva almeno un volo o una notte in hotel prepagata?", True),
            ("Hai pagato il viaggio con la Carta Platino?", True),
            ("L'evento è avvenuto durante il viaggio e non prima della partenza?", True),
            ("Non si tratta di una malattia cronica già nota?", True),
            ("Hai referti o documentazione medica?", False),
        ],
        "dettagli": "✅ Coperto fino a €5.000.000 per persona; cure dentistiche urgenti fino a €1.500."
    },
    "Furto o smarrimento effetti personali": {
        "domande": [
            ("Il furto o la perdita è avvenuto durante il viaggio?", True),
            ("Hai fatto denuncia alla polizia o al vettore?", True),
            ("Gli oggetti erano custoditi in modo adeguato?", True),
            ("Il valore rientra nei limiti (3.000 € totali, max 750 € per articolo/documenti/denaro)?", True),
            ("Hai prove di possesso o acquisto degli oggetti (scontrini, foto)?", False),
        ],
        "dettagli": "✅ Coperto fino a €3.000 totali; max €750 per articolo; max €750 per denaro/documenti."
    },
    "Noleggio auto – danni o furto": {
        "domande": [
            ("Era un’auto a noleggio (non tua)?", True),
            ("Il contratto era valido e intestato a te?", True),
            ("Hai pagato il noleggio con la Carta Platino?", True),
            ("Il sinistro è avvenuto durante il periodo di noleggio?", True),
            ("Stavi guidando nel rispetto delle regole (no ebbrezza, no uso improprio)?", True),
            ("Hai denuncia o verbale del noleggiatore/autorità?", False),
        ],
        "dettagli": "✅ Coperto fino a €75.000 per evento. Nota: non copre noleggi 'sotto casa', solo quelli parte di un viaggio."
    },
    "Ritardo viaggio o mancata partenza": {
        "domande": [
            ("Il viaggio era stato pagato con la Carta Platino?", True),
            ("Il ritardo o la cancellazione ha superato la soglia prevista (es. 4 ore)?", True),
            ("Hai ricevuto conferma scritta del ritardo/cancellazione dalla compagnia?", True),
            ("Hai sostenuto spese extra e conservato ricevute?", True),
            ("La causa rientra tra quelle ammesse (non dolo, non sciopero selvaggio)?", False),
        ],
        "dettagli": "✅ Indennizzo per spese extra (pasti, pernottamenti) entro i limiti previsti."
    },
    "Annullamento o interruzione viaggio": {
        "domande": [
            ("Hai pagato il viaggio con la Carta Platino?", True),
            ("La causa rientra tra quelle previste (malattia, lutto, infortunio, danni alla casa)?", True),
            ("Hai documentazione a supporto (es. certificato medico)?", True),
            ("Hai rispettato i tempi massimi di comunicazione?", True),
            ("Le spese che chiedi erano non rimborsabili da altri fornitori?", False),
        ],
        "dettagli": "✅ Coperto fino a €10.000 per beneficiario per spese non rimborsabili."
    },
    "Incidenti di viaggio": {
        "domande": [
            ("L’incidente è avvenuto durante un viaggio coperto (volo o notte prepagata)?", True),
            ("Eri titolare della Carta Platino al momento dell’evento?", True),
            ("Non si tratta di un’attività esclusa (es. sport estremi)?", True),
            ("Hai referti medici o denuncia che provino l’incidente?", True),
            ("L’evento è avvenuto entro i limiti temporali della polizza?", False),
        ],
        "dettagli": "✅ Previsti indennizzi per morte o invalidità permanente da infortunio in viaggio, entro i limiti di polizza."
    }
}

# Se non ha ancora scelto la categoria
if not st.session_state.categoria:
    st.header("Seleziona una tipologia di evento")
    categoria = st.selectbox("Che tipo di situazione vuoi verificare?", ["---"] + list(coverages.keys()))
    if categoria != "---":
        st.session_state.categoria = categoria
        st.session_state.step = 0
        st.session_state.answers = []
        st.session_state.finished = False

# Se categoria scelta, avvia wizard
else:
    categoria = st.session_state.categoria
    domande = coverages[categoria]["domande"]

    # Calcolo progress bar
    progress = st.session_state.step / len(domande)
    st.progress(progress)

    if not st.session_state.finished and st.session_state.step < len(domande):
        domanda, essenziale = domande[st.session_state.step]
        risposta = st.radio(domanda, ["Sì", "No"], key=f"q{st.session_state.step}")
        if st.button("Avanti", key=f"next{st.session_state.step}"):
            st.session_state.answers.append(risposta)
            if risposta == "No" and essenziale:
                st.error("❌ Non coperto: condizione fondamentale non rispettata.")
                st.session_state.finished = True
            else:
                st.session_state.step += 1

    elif not st.session_state.finished and st.session_state.step == len(domande):
        # Tutte le domande completate
        if all(ans == "Sì" for ans in st.session_state.answers):
            st.success(coverages[categoria]["dettagli"])
        else:
            st.error("❌ Non coperto: una o più condizioni non sono rispettate.")
        st.session_state.finished = True

    if st.session_state.finished:
        if st.button("🔄 Ricomincia"):
            st.session_state.categoria = None
            st.session_state.step = 0
            st.session_state.answers = []
            st.session_state.finished = False
