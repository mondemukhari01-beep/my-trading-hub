from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

bot_running = False
balance = 1000

# YOUR STRATEGY - You can edit this later
def trading_logic():
    # This is where your buy/sell logic will go
    return "Waiting for signal..."

@app.route("/")
def dashboard():
    return render_template("dashboard.html")

@app.route("/start", methods=["POST"])
def start_bot():
    global bot_running
    bot_running = True
    return jsonify({"status": "Bot Started - Running"})

@app.route("/stop", methods=["POST"])
def stop_bot():
    global bot_running
    bot_running = False
    return jsonify({"status": "Bot Stopped"})

@app.route("/status")
def status():
    return jsonify({
        "running": bot_running,
        "balance": balance,
        "last_signal": trading_logic() if bot_running else "Bot stopped"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
