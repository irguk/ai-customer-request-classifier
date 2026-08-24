"""
classifier.py: LLM-basierte Klassifizierung und strukturierte Extraktion von Support-Tickets.
"""

import os
from enum import Enum
from typing import Optional
from dotenv import load_dotenv
from google import genai
from google.genai import types
from pydantic import BaseModel, Field

load_dotenv()


class TicketIntent(str, Enum):
    ORDER_REQUEST = "Bestellanfrage"
    COMPLAINT = "Reklamation"
    DELIVERY_STATUS = "Lieferstatus"
    GENERAL_INQUIRY = "Allgemeine Anfrage"


class TicketPriority(str, Enum):
    LOW = "Niedrig"
    MEDIUM = "Mittel"
    HIGH = "Hoch"
    CRITICAL = "Kritisch"


class ExtractedEntities(BaseModel):
    order_number: Optional[str] = Field(
        None, description="Bestellnummer, falls vorhanden (z. B. #DE-1234)"
    )
    product_type: Optional[str] = Field(
        None, description="Erwähnte Artikel- oder Produkttypen"
    )
    quantity: Optional[int] = Field(
        None, description="Angefragte oder reklamierte Menge"
    )
    delivery_deadline: Optional[str] = Field(
        None, description="Genannte Fristen oder Lieferdaten"
    )


class TicketAnalysis(BaseModel):
    intent: TicketIntent = Field(description="Hauptabsicht des Kunden")
    priority: TicketPriority = Field(description="Dringlichkeitsstufe")
    sentiment: str = Field(description="Stimmung des Kunden: Positiv, Neutral, Verärgert")
    entities: ExtractedEntities = Field(description="Extrahierte Entitäten")
    summary: str = Field(description="Prägnante 1-Satz-Zusammenfassung des Anliegens auf Deutsch")
    suggested_response: str = Field(
        description="Höflicher, professioneller Antwortentwurf auf Deutsch"
    )


class TicketClassifier:
    def __init__(self):
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            raise ValueError("GEMINI_API_KEY wurde nicht in den Umgebungsvariablen gefunden.")
        self.client = genai.Client(api_key=api_key)

    def analyze_ticket(self, ticket_text: str) -> TicketAnalysis:
        prompt = f"""
        Du bist ein KI-Assistent für Customer Support & Lead Automation im E-Commerce.
        Analysiere die folgende Kundenanfrage präzise und extrahiere alle relevanten Daten als JSON.

        Kundenanfrage:
        \"\"\"{ticket_text}\"\"\"
        """

        response = self.client.models.generate_content(
            model="gemini-3.6-flash",
            contents=prompt,
            config=types.GenerateContentConfig(
                response_mime_type="application/json",
                response_schema=TicketAnalysis,
                temperature=0.1,
            ),
        )

        return TicketAnalysis.model_validate_json(response.text)