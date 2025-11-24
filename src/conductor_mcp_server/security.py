from fastapi import HTTPException

def security_check(operation: str):
    op = operation.lower()

    if "ignore safety" in op or "bypass" in op:
        raise HTTPException(status_code=400, detail="Security Violation: Context Poisoning Detected")

    return operation
