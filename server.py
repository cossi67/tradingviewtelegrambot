from flask import Flask, request
import requests
import json

app = Flask(__name__)

TELEGRAM_TOKEN = "8387106902:AAG4WqC8txKTQxqFg36GcdeTyev7hBW294s"
TELEGRAM_CHAT_ID = "7038986266"

def send_telegram(msg):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    data = {"chat_id": TELEGRAM_CHAT_ID, "text": msg, "parse_mode": "HTML"}
    requests.post(url, json=data)

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json
    try:
        message = data.get("message", str(data))
        send_telegram(f"📡 Nouveau signal :\n{message}")
        return {"status":"success"}, 200
    except Exception as e:
        return {"status":"error", "error": str(e)}, 500

if __name__=="__main__":
    app.run(host="0.0.0.0", port=5000)
