from flask import Flask, request

app = Flask(__name__)

VERIFY_TOKEN = "movego_verify_2026"

@app.route("/", methods=["GET"])
def home():
    return "MoveGo server is running", 200

@app.route("/webhook", methods=["GET"])
def verify_webhook():
    mode = request.args.get("hub.mode")
    token = request.args.get("hub.verify_token")
    challenge = request.args.get("hub.challenge")

    if mode == "subscribe" and token == VERIFY_TOKEN:
        return challenge, 200

    return "Verification failed", 403


@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.get_json(silent=True)
    print(data)
    return "EVENT_RECEIVED", 200
