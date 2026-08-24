import streamlit as st
from src.classifier import TicketClassifier

st.set_page_config(page_title="AI Ticket Classifier", page_icon="📩", layout="wide")
st.title("📩 AI Customer Support Ticket Classifier")

classifier = TicketClassifier()

ticket_input = st.text_area(
    "Fügen Sie hier die Kundenanfrage ein:",
    height=150,
    placeholder="Guten Tag, wo bleibt meine Bestellung #DE-9988?..."
)

if st.button("Anfrage analysieren", type="primary"):
    if ticket_input.strip():
        with st.spinner("Analysiere Ticket mit Gemini..."):
            res = classifier.analyze_ticket(ticket_input)

            col1, col2, col3 = st.columns(3)
            col1.metric("Intent", res.intent.value)
            col2.metric("Priorität", res.priority.value)
            col3.metric("Stimmung", res.sentiment)

            st.subheader("📋 Zusammenfassung")
            st.info(res.summary)

            st.subheader("🔍 Extrahierte Entitäten")
            st.json(res.entities.model_dump())

            st.subheader("✉️ Antwortentwurf")
            st.success(res.suggested_response)
    else:
        st.warning("Bitte geben Sie einen Text ein.")