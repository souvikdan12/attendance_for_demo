# backend/app/auth/utils.py

import uuid


def generate_demo_token(user_id: str) -> str:
    """
    Generate a simple demo token.
    (In production this will be JWT)
    """
    return f"demo-{user_id}-{uuid.uuid4()}"
