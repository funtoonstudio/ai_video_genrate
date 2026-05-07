from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/generate", methods=["POST"])
def generate():
    data = request.json
    
    prompt = data.get("prompt")
    resolution = data.get("resolution")
    duration = data.get("duration")

    print(prompt, resolution, duration)

    return jsonify({
        "video_url": "https://sample-videos.com/video123/mp4/720/big_buck_bunny_720p_1mb.mp4"
    })

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
