from pydantic import BaseModel
from typing import Optional

class TaskRequest(BaseModel):
    description: str
    context_id: Optional[str] = None

class RoutingResponse(BaseModel):
    target_orchestrator: str
    confidence: float

class OperationRequest(BaseModel):
    operation: str

class SafetyResponse(BaseModel):
    is_safe: bool
    requires_elicitation: bool
