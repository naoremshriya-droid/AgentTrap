import json
from datetime import datetime, timezone
from pathlib import Path

AUDIT_FILE = Path(__file__).resolve().parent / "audit.log"


def log_event(event: dict) -> None:
    record = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        **event,
    }

    with AUDIT_FILE.open("a", encoding="utf-8") as file:
        file.write(json.dumps(record) + "\n")