TRUSTED_VENDORS = {
    "VENDOR001": "Lumiere Supplies",
    "VENDOR002": "Cloud Services Ltd",
}

MAX_PAYMENT = 50_000


def evaluate_payment(payment: dict) -> dict:
    amount = payment.get("amount")
    vendor_id = payment.get("vendor_id")
    agent_id = payment.get("agent_id")

    reasons = []

    # Check 1: Is the amount valid?
    if not isinstance(amount, (int, float)) or isinstance(amount, bool):
        return {
            "decision": "BLOCKED",
            "risk_score": 100,
            "reasons": ["Invalid payment amount"],
        }

    if amount <= 0:
        reasons.append("Payment amount must be positive")

    # Check 2: Is the vendor trusted?
    if not isinstance(vendor_id, str) or vendor_id not in TRUSTED_VENDORS:
        reasons.append("Vendor is not trusted")

    # Check 3: Is this agent allowed to propose payments?
    if agent_id != "finance-agent":
        reasons.append("Agent does not have permission to propose payments")

    # Check 4: Is the payment within the limit?
    if amount > MAX_PAYMENT:
        reasons.append(
            f"Payment exceeds the ₹{MAX_PAYMENT:,} limit"
        )

    if reasons:
        return {
            "decision": "BLOCKED",
            "risk_score": 100,
            "reasons": reasons,
        }

    return {
        "decision": "APPROVED",
        "risk_score": 0,
        "reasons": [
            "Payment passed the configured security checks"
        ],
    }