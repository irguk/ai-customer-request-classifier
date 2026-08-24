# AI Customer Request Classifier & Support Automation

Ein automatisiertes System zur semantischen Klassifizierung von Support-Tickets, strukturierter Entitätsextraktion und Generierung von Antwortentwürfen auf Basis des **Gemini 3.6 Flash** Modells.

## 🚀 Funktionen

* **Klassifizierung nach Intent**: Automatische Erkennung von *Bestellanfragen*, *Reklamationen*, *Lieferstatus* und *Allgemeinen Anfragen*.
* **Priorisierung & Sentiment-Analyse**: Dynamische Einstufung der Dringlichkeit (*Niedrig*, *Mittel*, *Hoch*, *Kritisch*) sowie Erkennung der Kundenstimmung.
* **Entitätsextraktion**: Zuverlässiges Auslesen von Bestellnummern, Produkttypen, Mengenangaben und Fristen.
* **Strukturierte JSON-Ausgabe**: Typensichere Validierung der LLM-Ausgaben über **Pydantic**-Schemas (`Structured Outputs`).
* **Automatisierte Antwortentwürfe**: Generierung kontextbezogener, professioneller E-Mail-Vorlagen auf Deutsch.

## 🛠️ Tech-Stack

* **Sprache**: Python 3.11
* **LLM / API**: Google GenAI SDK (`gemini-3.6-flash`)
* **Datenvalidierung**: Pydantic v2
* **Konfiguration**: python-dotenv

## 📂 Projektstruktur

```text
ai-customer-request-classifier/
├── data/
│   ├── sample_tickets.json    # Eingabe: Unstrukturierte Support-Tickets
│   └── results.json           # Ausgabe: Strukturierte Analyse & Antworten
├── src/
│   ├── classifier.py          # Pydantic-Modelle & Gemini API-Integration
│   └── process_tickets.py     # Pipeline zur Batch-Verarbeitung
├── .env.example               # Vorlage für Umgebungsvariablen
├── .gitignore                 # Ausschluss von venv, .env und Caches
├── requirements.txt           # Projektabhängigkeiten
└── README.md                  # Projektdokumentation
