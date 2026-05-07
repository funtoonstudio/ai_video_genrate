from flask import Flask, request, jsonify
import os
import replicate

app = Flask(__name__)

@app.route("/")
def home():
    return "AI Video Generator API is running!"

@app.route("/generate", methods=["POST"])
def generate_video():
    try:
        data = request.get_json()
        prompt = data.get("prompt")

        if not prompt:
            return jsonify({"error": "Prompt is required"}), 400

        output = replicate.run(
            "cerspense/zeroscope_v2_576w",
            input={
                "prompt": prompt
            }
        )

        video_url = output[-1] if isinstance(output, list) else output

        return jsonify({
            "status": "success",
            "video_url": video_url
        })

    except Exception as e:
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
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
