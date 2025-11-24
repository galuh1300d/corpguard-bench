from fastapi import HTTPException
import re

def security_check(operation: str):
    op = operation.lower()
    
    # 1. Direct Override Patterns
    unsafe_keywords = [
        "ignore safety", "bypass", "override", "force execute", 
        "sudo", "admin mode", "jailbreak", "developer mode",
        "ignore previous", "system override"
    ]
    
    # 2. Manipulative Intent
    if any(keyword in op for keyword in unsafe_keywords):
        raise HTTPException(
            status_code=400, 
            detail="Security Violation: Context Poisoning/Jailbreak Attempt Detected"
        )

    # 3. Hidden/Obfuscated Payload (Base64 or Hex-like patterns typically used in attacks)
    # Simple heuristic: Strings that look too much like encoded payloads
    if len(op) > 50 and not " " in op: 
        raise HTTPException(
            status_code=400, 
            detail="Security Violation: Suspicious Obfuscated Payload"
        )

    return operation
