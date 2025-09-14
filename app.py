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

# Database delle coperture (accorciato qui per spazio, mantieni i tuoi estratti e riferimenti)
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
        "riferimento": "Fascicolo Informativo Amex Platino – Sezione Assistenza e Spese Mediche, Art. 3.1, pag. 12"
    }
    # 🔹 Mantieni anche tutte le altre coperture come le abbiamo impostate prima
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
