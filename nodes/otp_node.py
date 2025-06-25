from langgraph.graph import tool
import random

# Simulación básica (en producción usarías Twilio, WhatsApp API o correo)
# Aquí simulamos OTP fijo para pruebas
OTP_CODE = "123456"


@tool
def otp_verification(user_id: str, otp_input: str = "") -> dict:
    """
    Verifica el código OTP para el usuario. En producción enviaría y luego validaría.
    """
    if otp_input == "":
        # Simula envío del código al usuario (esto se integraría con Twilio/WhatsApp)
        print(f"🔐 Enviando código OTP a usuario {user_id}...")
        print(f"(Para pruebas, el código es: {OTP_CODE})")
        return {"user_id": user_id, "awaiting_otp": True}

    if otp_input == OTP_CODE:
        return {"user_id": user_id, "otp_valid": True}

    return {"user_id": user_id, "otp_valid": False, "awaiting_otp": False}
