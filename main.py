from flask import Flask, send_from_directory

app = Flask(__name__, static_folder="cards")

# Route to serve card images
@app.route("/cards/<path:filename>")
def serve_card(filename):
    return send_from_directory(app.static_folder, filename)

@app.route("/")
def home():
    return "🎉 Invite Cards Server is Running 🎉"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

