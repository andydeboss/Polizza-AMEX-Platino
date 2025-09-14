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
            ("Hai rispettato i tempi
