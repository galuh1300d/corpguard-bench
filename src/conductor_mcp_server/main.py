from fastapi import FastAPI, Depends, Body
from .models import TaskRequest, RoutingResponse, OperationRequest, SafetyResponse
from .security import security_check
from .elicitation import elicitation_check

app = FastAPI()

@app.post("/route", response_model=RoutingResponse)
async def route_task(task: TaskRequest):
    desc = task.description.lower()
    
    if "technical" in desc or "architecture" in desc or "microservice" in desc:
        return {"target_orchestrator": "CTO_Orchestrator", "confidence": 0.95}
    elif "budget" in desc or "finance" in desc:
        return {"target_orchestrator": "FinancialAgent", "confidence": 0.9}
    else:
        return {"target_orchestrator": "CEO_Orchestrator", "confidence": 0.5}

@app.post("/validate_safety", response_model=SafetyResponse)
async def validate_safety(req: OperationRequest):
    op = req.operation.lower()
    
    if "ignore safety" in op:
        return {"is_safe": False, "requires_elicitation": False}

    if "delete" in op or "drop" in op:
        return {"is_safe": True, "requires_elicitation": True}

    return {"is_safe": True, "requires_elicitation": False}

@app.post("/execute")
async def execute(req: OperationRequest):
    security_check(req.operation)
    elicitation_check(req.operation)

    return {"status": "executed", "operation": req.operation}
