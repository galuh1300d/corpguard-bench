from fastapi import HTTPException

def elicitation_check(operation: str):
    op = operation.lower()

    if "delete" in op or "drop" in op:
        raise HTTPException(status_code=409, detail="Elicitation Required: Confirm destructive action.")

    return operation
