from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Status": "AI-Krishidoot is running"}

@app.post("/api/whatsapp")
async def handle_whatsapp_message(data: dict):
    # This is where the message from WhatsApp will be processed
    user_message = data.get("message", "No message received")
    print(f"Received message: {user_message}")

    # TODO: Add CrewAI logic here
    response_message = f"AI Krishidoot received your message: '{user_message}'"

    return {"reply": response_message}