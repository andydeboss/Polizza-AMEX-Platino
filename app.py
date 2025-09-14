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

# Funzione per domanda sul pagamento con Platino
def domanda_pagamento(label):
    return st.radio(
        label,
        [
            "Ho pagato con Carta Platino",
            "Ho pagato con un’altra carta perché Platino non era accettata",
            "Ho pagato con un’altra carta anche se Platino era accettata"
        ],
        key=f"pay_{st.session_state.step}"
    )

# Database completo delle coperture
coverages = {
    "Spese mediche in viaggio": {
        "domande": [
            ("Il viaggio prevedeva almeno un volo o una notte in hotel prepagata?", True),
            ("PAGAMENTO", True),
            ("L'evento è avvenuto durante il viaggio e non prima della partenza?", True),
            ("Non si tratta di una malattia cronica già nota?", True),
            ("Hai referti o documentazione medica?", False),
        ],
        "dettagli": "✅ Coperto fino a €5.000.000 per persona; cure dentistiche urgenti fino a €1.500.",
        "estratto": """
**Estratto di polizza – Assistenza e Spese Mediche**  
Per godere di queste coperture è necessario che le spese per l’acquisto del Viaggio (trasporto e/o alloggio) siano effettuate attraverso una delle modalità di utilizzo della Carta.  
La copertura include le spese mediche d’emergenza sostenute all’estero fino a €5.000.000 per assicurato.  
Sono incluse cure dentistiche urgenti fino a €1.500 e rimpatrio sanitario se necessario.  
        """,
        "riferimento": "Sezione Assistenza e Spese Mediche, Art. 3.1, pag. 12"
    },
    "Furto o smarrimento effetti personali": {
        "domande": [
            ("Il furto o la perdita è avvenuto durante il viaggio?", True),
            ("Hai fatto denuncia alla polizia o al vettore?", True),
            ("Gli oggetti erano custoditi in modo adeguato?", True),
            ("Il valore rientra nei limiti (3.000 € totali, max 750 € per articolo/documenti/denaro)?", True),
            ("Hai prove di possesso o acquisto degli oggetti (scontrini, foto)?", False),
        ],
        "dettagli": "✅ Coperto fino a €3.000 totali; max €750 per articolo; max €750 per denaro/documenti.",
        "estratto": """
**Estratto di polizza – Bagagli ed effetti personali**  
La copertura prevede un indennizzo fino a €3.000 per assicurato, con limite di €750 per singolo articolo, documenti o denaro.  
È obbligatoria la denuncia alle autorità o al vettore entro 24 ore.  
Sono esclusi oggetti lasciati incustoditi o senza adeguata sorveglianza.  
        """,
        "riferimento": "Sezione Bagaglio, Art. 5.2, pag. 18"
    },
    "Noleggio auto – danni o furto": {
        "domande": [
            ("Era un’auto a noleggio (non tua)?", True),
            ("Il contratto era valido e intestato a te?", True),
            ("PAGAMENTO", True),
            ("Il sinistro è avvenuto durante il periodo di noleggio?", True),
            ("Stavi guidando nel rispetto delle regole (no ebbrezza, no uso improprio)?", True),
            ("Hai denuncia o verbale del noleggiatore/autorità?", False),
        ],
        "dettagli": "✅ Coperto fino a €75.000 per evento.",
        "estratto": """
**Estratto di polizza – Noleggio auto**  
La copertura prevede rimborso fino a €75.000 per danni o furto di auto a noleggio intestata al Titolare, se pagata con Carta Platino (o altra carta se Platino non accettata).  
Sono esclusi i noleggi a lungo termine e quelli effettuati nella città di residenza senza collegamento con un viaggio.  
        """,
        "riferimento": "Sezione Noleggio Auto, Art. 6.1, pag. 22"
    },
    "Ritardo viaggio o mancata partenza": {
        "domande": [
            ("PAGAMENTO", True),
            ("Il ritardo o la cancellazione ha superato la soglia prevista (es. 4 ore)?", True),
            ("Hai ricevuto conferma scritta del ritardo/cancellazione dalla compagnia?", True),
            ("Hai sostenuto spese extra e conservato ricevute?", True),
            ("La causa rientra tra quelle ammesse (non dolo, non sciopero selvaggio)?", False),
        ],
        "dettagli": "✅ Copertura per spese extra (pasti, pernottamenti) in caso di ritardo oltre 4 ore.",
        "estratto": """
**Estratto di polizza – Ritardo viaggio e mancata partenza**  
Sono coperte le spese ragionevoli per pasti, pernottamenti e trasferimenti sostenute a seguito di ritardo superiore a 4 ore o cancellazione del viaggio, se pagato con Carta Platino (o altra carta se Platino non accettata).  
È necessario presentare documentazione del vettore che certifichi il ritardo/cancellazione.  
        """,
        "riferimento": "Sezione Ritardo Viaggio, Art. 4.2, pag. 15"
    },
    "Annullamento o interruzione viaggio": {
        "domande": [
            ("PAGAMENTO", True),
            ("La causa rientra tra quelle previste (malattia, lutto, infortunio, danni alla casa)?", True),
            ("Hai documentazione a supporto (es. certificato medico)?", True),
            ("Hai rispettato i tempi massimi di comunicazione?", True),
            ("Le spese che chiedi erano non rimborsabili da altri fornitori?", False),
        ],
        "dettagli": "✅ Coperto fino a €10.000 per beneficiario.",
        "estratto": """
**Estratto di polizza – Annullamento o interruzione viaggio**  
Sono coperte le spese non rimborsabili fino a €10.000 per assicurato se il viaggio (pagato con Carta Platino o altra carta se Platino non accettata) è annullato o interrotto per malattia, infortunio, lutto o danni rilevanti alla casa.  
È richiesta documentazione medica o denuncia, e la comunicazione tempestiva all’assicuratore.  
        """,
        "riferimento": "Sezione Annullamento Viaggio, Art. 4.1, pag. 14"
    },
    "Incidenti di viaggio": {
        "domande": [
            ("L’incidente è avvenuto durante un viaggio coperto (volo o notte prepagata)?", True),
            ("Eri titolare della Carta Platino al momento dell’evento?", True),
            ("Non si tratta di un’attività esclusa (es. sport estremi)?", True),
            ("Hai referti medici o denuncia che provino l’incidente?", True),
            ("L’evento è avvenuto entro i limiti temporali della polizza?", False),
        ],
        "dettagli": "✅ Previsti indennizzi per morte o invalidità permanente.",
        "estratto": """
**Estratto di polizza – Infortuni di viaggio**  
La copertura prevede indennizzi per morte o invalidità permanente derivanti da infortunio durante un viaggio, entro i massimali previsti dalla polizza.  
Sono esclusi gli incidenti dovuti a sport pericolosi o comportamenti non conformi alla legge.  
        """,
        "riferimento": "Sezione Infortuni di Viaggio, Art. 7.1, pag. 25"
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
        st.rerun()

# Se categoria scelta, avvia wizard
else:
    categoria = st.session_state.categoria
    domande = coverages[categoria]["domande"]
    totale = len(domande)

    # Barra numerica + progress bar
    if not st.session_state.finished and st.session_state.step < totale:
        numero_domanda = st.session_state.step + 1
        percentuale = int((numero_domanda - 1) / totale * 100)
        st.markdown(f"**Domanda {numero_domanda}/{totale} – {percentuale}% completato**")

    progress = st.session_state.step / totale
    st.progress(progress)

    if not st.session_state.finished and st.session_state.step < totale:
        domanda, essenziale = domande[st.session_state.step]

        if domanda == "PAGAMENTO":
            risposta = domanda_pagamento("Hai pagato il viaggio/noleggio con Carta Platino?")
        else:
            risposta = st.radio(domanda, ["Sì", "No"], key=f"q{st.session_state.step}")

        col1, col2 = st.columns([1, 1])

        with col1:
            if st.button("⬅️ Indietro") and st.session_state.step > 0:
                st.session_state.step -= 1
                st.session_state.answers.pop()
                st.rerun()

        with col2:
            if st.button("Avanti", key=f"next{st.session_state.step}"):
                st.session_state.answers.append(risposta)
                if domanda == "PAGAMENTO" and risposta == "Ho pagato con un’altra carta anche se Platino era accettata":
                    st.error("❌ Non coperto: il viaggio/noleggio non è stato pagato con Carta Platino pur essendo accettata.")
                    st.session_state.finished = True
                elif risposta == "No" and essenziale:
                    st.error("❌ Non coperto: condizione fondamentale non rispettata.")
                    st.session_state.finished = True
                else:
                    st.session_state.step += 1
                    st.rerun()

    elif not st.session_state.finished and st.session_state.step == totale:
        if all(("No" not in ans and "altra carta anche se" not in ans) for ans in st.session_state.answers):
            st.success(coverages[categoria]["dettagli"])
            st.markdown(coverages[categoria]["estratto"])
            st.caption(coverages[categoria]["riferimento"])
        else:
            st.error("❌ Non coperto: una o più condizioni non sono rispettate.")
        st.session_state.finished = True

    if st.session_state.finished:
        if st.button("🔄 Ricomincia"):
            st.session_state.categoria = None
            st.session_state.step = 0
            st.session_state.answers = []
            st.session_state.finished = False
            st.rerun()
