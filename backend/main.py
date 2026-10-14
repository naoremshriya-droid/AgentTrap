from fastapi import FastAPI
from pydantic import BaseModel, Field

from security import evaluate_payment
from audit import log_event

app = FastAPI(
    title="AgentTrap",
    description="AI Agent Security Gateway",
    version="1.0.0",
)


class PaymentProposal(BaseModel):
    agent_id: str
    vendor_id: str
    amount: float = Field(gt=0, allow_inf_nan=False)


@app.get("/")
def home():
    return {
        "project": "AgentTrap",
        "status": "running",
        "message": "AI Security Gateway is online!",
    }


@app.get("/health")
def health():
    return {"status": "healthy"}


@app.post("/api/payments/evaluate")
def evaluate(proposal: PaymentProposal):
    payment_data = proposal.model_dump()
    result = evaluate_payment(payment_data)

    log_event({
        "event": "PAYMENT_EVALUATED",
        "payment": payment_data,
        "decision": result["decision"],
        "reasons": result["reasons"],
    })

    return {
        **result,
        "payment": None,
    }