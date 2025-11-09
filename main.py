# from flask import Flask, send_from_directory
#
# app = Flask(__name__, static_folder="cards")
#
# # Route to serve card images
# @app.route("/cards/<path:filename>")
# def serve_card(filename):
#     return send_from_directory(app.static_folder, filename)
#
# @app.route("/")
# def home():
#     return "🎉 Invite Cards Server is Running 🎉"
#
# if __name__ == "__main__":
#     app.run(host="0.0.0.0", port=5000)


from flask import Flask, send_from_directory, render_template_string, url_for

app = Flask(__name__, static_folder="cards")

# Route to download the image
@app.route("/download/<path:filename>")
def download_card(filename):
    return send_from_directory(app.static_folder, filename, as_attachment=True)

# Route to view the image with animation & Swahili instruction
@app.route("/view/<path:filename>")
def view_card(filename):
    image_url = url_for('static', filename=filename)
    download_url = url_for('download_card', filename=filename)

    html = f"""
    <!DOCTYPE html>
    <html lang="sw">
    <head>
        <meta charset="UTF-8" />
        <title>Kadi Yako</title>
        <style>
            body {{
                font-family: 'Poppins', sans-serif;
                background: linear-gradient(135deg, #f0f7ff, #e0ecff);
                display: flex;
                flex-direction: column;
                align-items: center;
                justify-content: center;
                height: 100vh;
                margin: 0;
            }}
            .card-container {{
                background: white;
                border-radius: 20px;
                box-shadow: 0 6px 20px rgba(0, 0, 0, 0.1);
                padding: 20px;
                text-align: center;
                max-width: 400px;
                width: 90%;
                animation: fadeIn 1s ease-in;
            }}
            img {{
                width: 100%;
                border-radius: 15px;
                margin-bottom: 20px;
            }}
            .download-btn {{
                display: inline-block;
                padding: 15px 25px;
                background: #007bff;
                color: white;
                border-radius: 12px;
                font-size: 1.1em;
                font-weight: 600;
                text-decoration: none;
                transition: background 0.3s, transform 0.2s;
            }}
            .download-btn:hover {{
                background: #0056b3;
                transform: scale(1.05);
            }}
            .instruction {{
                font-size: 1.2em;
                color: #333;
                margin-top: 10px;
                font-weight: 500;
            }}
            .hand {{
                font-size: 2em;
                display: inline-block;
                animation: bounce 1.2s infinite;
                margin-left: 10px;
            }}
            @keyframes bounce {{
                0%, 100% {{ transform: translateY(0); }}
                50% {{ transform: translateY(-10px); }}
            }}
            @keyframes fadeIn {{
                from {{ opacity: 0; transform: translateY(20px); }}
                to {{ opacity: 1; transform: translateY(0); }}
            }}
        </style>
    </head>
    <body>
        <div class="card-container">
            <img src="{image_url}" alt="Kadi yako" />
            <a class="download-btn" href="{download_url}" download>
                ⬇️ Bonyeza hapa kubaki na kadi yako
            </a>
            <div class="instruction">
                👇 Bonyeza hapa <span class="hand">🤚</span>
            </div>
        </div>
    </body>
    </html>
    """
    return render_template_string(html)

@app.route("/")
def home():
    return "🎉 Invite Cards Server is Running 🎉"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)



# from flask import Flask, send_from_directory, render_template_string, url_for
#
# app = Flask(__name__, static_folder="cards")
#
# # Direct download route
# @app.route("/download/<path:filename>")
# def download_card(filename):
#     return send_from_directory(app.static_folder, filename, as_attachment=True)
#
# # View route (shows the image + download button)
# @app.route("/view/<path:filename>")
# def view_card(filename):
#     image_url = url_for('static', filename=filename)
#     download_url = url_for('download_card', filename=filename)
#
#     html = f"""
#     <html>
#     <head>
#         <title>Card Viewer</title>
#         <style>
#             body {{
#                 font-family: sans-serif;
#                 text-align: center;
#                 background: #f5f5f5;
#                 margin-top: 50px;
#             }}
#             img {{
#                 max-width: 90%;
#                 border-radius: 12px;
#                 box-shadow: 0 4px 10px rgba(0,0,0,0.2);
#             }}
#             .download-btn {{
#                 display: inline-block;
#                 margin-top: 20px;
#                 padding: 10px 18px;
#                 background: #007bff;
#                 color: white;
#                 border-radius: 8px;
#                 text-decoration: none;
#                 font-weight: bold;
#                 transition: background 0.3s;
#             }}
#             .download-btn:hover {{
#                 background: #0056b3;
#             }}
#         </style>
#     </head>
#     <body>
#         <h2>🎨 Card Preview</h2>
#         <img src="{image_url}" alt="Card" />
#         <br>
#         <a class="download-btn" href="{download_url}" download>
#             ⬇️ Download Image
#         </a>
#     </body>
#     </html>
#     """
#     return render_template_string(html)
#
# @app.route("/")
# def home():
#     return "🎉 Invite Cards Server is Running 🎉"
#
# if __name__ == "__main__":
#     app.run(host="0.0.0.0", port=5000)

