from fastapi import HTTPException

def elicitation_check(operation: str):
    op = operation.lower()
    
    # Daftar operasi yang HARUS minta izin manusia (Destructive/Administrative)
    sensitive_ops = [
        # SQL Destructive
        "delete", "drop", "truncate", "alter table", "drop table",
        # User Management
        "grant", "revoke", "create user", "change password",
        # System
        "shutdown", "restart", "rm -rf", "format"
    ]

    if any(action in op for action in sensitive_ops):
        raise HTTPException(
            status_code=409, 
            detail=f"Elicitation Required: Operation '{op}' is destructive/sensitive. Human confirmation needed."
        )

    return operation
