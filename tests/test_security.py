from backend.security import evaluate_payment


def test_trusted_payment_is_approved():
    payment = {
        "agent_id": "finance-agent",
        "vendor_id": "VENDOR001",
        "amount": 5000,
    }

    result = evaluate_payment(payment)

    assert result["decision"] == "APPROVED"


def test_unknown_vendor_is_blocked():
    payment = {
        "agent_id": "finance-agent",
        "vendor_id": "UNKNOWN999",
        "amount": 5000,
    }

    result = evaluate_payment(payment)

    assert result["decision"] == "BLOCKED"
    assert "Vendor is not trusted" in result["reasons"]


def test_unauthorized_agent_is_blocked():
    payment = {
        "agent_id": "random-agent",
        "vendor_id": "VENDOR001",
        "amount": 5000,
    }

    result = evaluate_payment(payment)

    assert result["decision"] == "BLOCKED"


def test_payment_above_limit_is_blocked():
    payment = {
        "agent_id": "finance-agent",
        "vendor_id": "VENDOR001",
        "amount": 60000,
    }

    result = evaluate_payment(payment)

    assert result["decision"] == "BLOCKED"


def test_negative_payment_is_blocked():
    payment = {
        "agent_id": "finance-agent",
        "vendor_id": "VENDOR001",
        "amount": -100,
    }

    result = evaluate_payment(payment)

    assert result["decision"] == "BLOCKED"