"""
process_tickets.py: Batch-Processing-Pipeline für eingehende Kundentickets.
"""

import json
from pathlib import Path
from classifier import TicketClassifier


def run_pipeline():
    base_dir = Path(__file__).resolve().parent.parent
    input_file = base_dir / "data" / "sample_tickets.json"
    output_file = base_dir / "data" / "results.json"

    print("🚀 Starte AI Ticket Processing Pipeline...")

    with open(input_file, "r", encoding="utf-8") as f:
        tickets = json.load(f)

    classifier = TicketClassifier()
    processed_results = []

    for ticket in tickets:
        ticket_id = ticket.get("ticket_id")
        print(f"⏳ Verarbeite Ticket {ticket_id}...")

        analysis = classifier.analyze_ticket(ticket.get("message", ""))

        processed_item = {
            "ticket_id": ticket_id,
            "sender_email": ticket.get("sender_email"),
            "received_at": ticket.get("received_at"),
            "raw_message": ticket.get("message"),
            "ai_analysis": analysis.model_dump(),
        }
        processed_results.append(processed_item)

    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(processed_results, f, ensure_ascii=False, indent=2)

    print(f"✅ Pipeline abgeschlossen! {len(processed_results)} Tickets gespeichert in: {output_file}")


if __name__ == "__main__":
    run_pipeline()
    