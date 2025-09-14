import streamlit as st

st.title("🤖 Assistente Coperture Amex Platino")
st.write("Rispondi ad alcune domande per capire se sei coperto dalla polizza Amex Platino.")

# Scelta macro-categoria
categoria = st.selectbox(
    "Quale situazione vuoi verificare?",
    [
        "---",
        "Spese mediche in viaggio",
        "Furto o smarrimento effetti personali",
        "Noleggio auto – danni o furto",
        "Ritardo viaggio o mancata partenza",
        "Annullamento o interruzione viaggio",
        "Incidenti di viaggio"
    ]
)

if categoria == "Spese mediche in viaggio":
    st.subheader("🏥 Spese mediche in viaggio")
    q1 = st.radio("Il viaggio prevedeva almeno un volo o una notte in hotel prepagata?", ["Sì", "No"])
    q2 = st.radio("Hai pagato il viaggio con la Carta Platino?", ["Sì", "No"])
    q3 = st.radio("L'evento è avvenuto durante il viaggio e non prima della partenza?", ["Sì", "No"])
    q4 = st.radio("Non si tratta di una malattia cronica già nota?", ["Sì", "No"])
    q5 = st.radio("Hai referti o documentazione medica?", ["Sì", "No"])

    if st.button("Verifica copertura"):
        if all(ans == "Sì" for ans in [q1, q2, q3, q4, q5]):
            st.success("✅ Coperto fino a €5.000.000 per persona; cure dentistiche urgenti fino a €1.500.")
        else:
            st.error("❌ Non coperto: una o più condizioni richieste non sono rispettate.")

elif categoria == "Furto o smarrimento effetti personali":
    st.subheader("🧳 Furto o smarrimento effetti personali")
    q1 = st.radio("Il furto o la perdita è avvenuto durante il viaggio?", ["Sì", "No"])
    q2 = st.radio("Hai fatto denuncia alla polizia o al vettore?", ["Sì", "No"])
    q3 = st.radio("Gli oggetti erano custoditi in modo adeguato?", ["Sì", "No"])
    q4 = st.radio("Il valore rientra nei limiti di polizza (3.000 € totali, max 750 € per articolo/documenti/denaro)?", ["Sì", "No"])
    q5 = st.radio("Hai prove di possesso o acquisto degli oggetti (scontrini, foto)?", ["Sì", "No"])

    if st.button("Verifica copertura"):
        if all(ans == "Sì" for ans in [q1, q2, q3, q4, q5]):
            st.success("✅ Coperto fino a €3.000 totali; max €750 per articolo; max €750 per denaro/documenti.")
        else:
            st.error("❌ Non coperto: una o più condizioni non sono rispettate.")

elif categoria == "Noleggio auto – danni o furto":
    st.subheader("🚗 Noleggio auto – danni o furto")
    q1 = st.radio("Era un’auto a noleggio (non tua)?", ["Sì", "No"])
    q2 = st.radio("Il contratto era valido e intestato a te?", ["Sì", "No"])
    q3 = st.radio("Hai pagato il noleggio con la Carta Platino?", ["Sì", "No"])
    q4 = st.radio("Il sinistro è avvenuto durante il periodo di noleggio?", ["Sì", "No"])
    q5 = st.radio("Stavi guidando nel rispetto delle regole (no ebbrezza, no uso improprio)?", ["Sì", "No"])
    q6 = st.radio("Hai denuncia o verbale del noleggiatore/autorità?", ["Sì", "No"])

    if st.button("Verifica copertura"):
        if all(ans == "Sì" for ans in [q1, q2, q3, q4, q5, q6]):
            st.success("✅ Coperto fino a €75.000 per evento. Nota: non copre noleggi 'sotto casa', solo quelli parte di un viaggio.")
        else:
            st.error("❌ Non coperto: una o più condizioni non sono rispettate.")

elif categoria == "Ritardo viaggio o mancata partenza":
    st.subheader("✈️ Ritardo viaggio o mancata partenza")
    q1 = st.radio("Il viaggio era stato pagato con la Carta Platino?", ["Sì", "No"])
    q2 = st.radio("Il ritardo o la cancellazione ha superato la soglia prevista (es. 4 ore)?", ["Sì", "No"])
    q3 = st.radio("Hai ricevuto conferma scritta del ritardo/cancellazione dalla compagnia?", ["Sì", "No"])
    q4 = st.radio("Hai sostenuto spese extra e conservato ricevute?", ["Sì", "No"])
    q5 = st.radio("La causa rientra tra quelle ammesse (non dolo, non sciopero selvaggio)?", ["Sì", "No"])

    if st.button("Verifica copertura"):
        if all(ans == "Sì" for ans in [q1, q2, q3, q4, q5]):
            st.success("✅ Indennizzo per spese extra (pasti, pernottamenti) entro i limiti previsti.")
        else:
            st.error("❌ Non coperto: una o più condizioni non sono rispettate.")

elif categoria == "Annullamento o interruzione viaggio":
    st.subheader("🛑 Annullamento o interruzione viaggio")
    q1 = st.radio("Hai pagato il viaggio con la Carta Platino?", ["Sì", "No"])
    q2 = st.radio("La causa rientra tra quelle previste (malattia, lutto, infortunio, danni alla casa)?", ["Sì", "No"])
    q3 = st.radio("Hai documentazione a supporto (es. certificato medico)?", ["Sì", "No"])
    q4 = st.radio("Hai rispettato i tempi massimi di comunicazione?", ["Sì", "No"])
    q5 = st.radio("Le spese che chiedi erano non rimborsabili da altri fornitori?", ["Sì", "No"])

    if st.button("Verifica copertura"):
        if all(ans == "Sì" for ans in [q1, q2, q3, q4, q5]):
            st.success("✅ Coperto fino a €10.000 per beneficiario per spese non rimborsabili.")
        else:
            st.error("❌ Non coperto: una o più condizioni non sono rispettate.")

elif categoria == "Incidenti di viaggio":
    st.subheader("🚑 Incidenti di viaggio")
    q1 = st.radio("L’incidente è avvenuto durante un viaggio coperto (volo o notte prepagata)?", ["Sì", "No"])
    q2 = st.radio("Eri titolare della Carta Platino al momento dell’evento?", ["Sì", "No"])
    q3 = st.radio("Non si tratta di un’attività esclusa (es. sport estremi)?", ["Sì", "No"])
    q4 = st.radio("Hai referti medici o denuncia che provino l’incidente?", ["Sì", "No"])
    q5 = st.radio("L’evento è avvenuto entro i limiti temporali della polizza?", ["Sì", "No"])

    if st.button("Verifica copertura"):
        if all(ans == "Sì" for ans in [q1, q2, q3, q4, q5]):
            st.success("✅ Previsti indennizzi per morte o invalidità permanente da infortunio in viaggio, entro i limiti di polizza.")
        else:
            st.error("❌ Non coperto: una o più condizioni non sono rispettate.")
