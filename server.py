import os
import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN", "")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID", "")

TELEGRAM_API = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}"

def send_to_telegram(chat_id, text, parse_mode=None):
    url = f"{TELEGRAM_API}/sendMessage"
    payload = {"chat_id": chat_id, "text": text}
    if parse_mode:
        payload["parse_mode"] = parse_mode
    try:
        r = requests.post(url, json=payload, timeout=10)
        r.raise_for_status()
        return True
    except Exception as e:
        app.logger.error(f"[Telegram send error] {e}")
        return False

@app.route("/alert", methods=["POST"])
def alert():
    data = request.get_json(force=True, silent=True) or {}
    message = data.get("message") or data.get("text") or str(data)
    preview = (message[:400] + "...") if isinstance(message, str) and len(message) > 400 else message
    ok = send_to_telegram(TELEGRAM_CHAT_ID, f"📡 Signal reçu :\n{preview}")
    return jsonify({"status": "ok" if ok else "error", "sent": ok}), (200 if ok else 500)

@app.route("/telegram_webhook", methods=["POST"])
def telegram_webhook():
    update = request.get_json(force=True, silent=True) or {}
    app.logger.info(f"Telegram update: {update}")

    if "message" in update:
        msg = update["message"]
        chat = msg.get("chat", {})
        chat_id = chat.get("id")
        text = msg.get("text", "")

        if text:
            t = text.strip().lower()
            if t == "/start":
                send_to_telegram(chat_id, "Salut 👋 Je suis ton bot. J'envoie les alertes TradingView ici.")
            elif t == "/help":
                send_to_telegram(chat_id, "Commandes: /start /help /status")
            elif t == "/status":
                send_to_telegram(chat_id, "✅ Bot actif. Webhook opérationnel.")
            else:
                send_to_telegram(chat_id, f"Reçu : {text}")

    return jsonify({"ok": True}), 200

@app.route("/")
def home():
    return "Bot actif — endpoints: /alert et /telegram_webhook"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
