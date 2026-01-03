# backend/app/config/demo.py

class Settings:
    MODE = "demo"

    # Allowed origins for CORS (dashboard + mobile)
    ALLOWED_ORIGINS = [
        "http://localhost",
        "http://localhost:8501",   # Streamlit
        "http://127.0.0.1:8501",
        "http://localhost:3000",
        "*",  # allow all for demo
    ]

    # Demo attendance settings
    MIN_PRESENCE_MINUTES = 1
    RSSI_THRESHOLD = -90  # relaxed for demo
    ENABLE_HYBRID_VERIFICATION = True


# THIS is what main.py is importing
settings = Settings()
