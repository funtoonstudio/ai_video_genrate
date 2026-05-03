# ai_video_genrate
AI Video Generator Backend API using Flask and Replicate. This service takes a text prompt and generates videos using AI.
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
            "anotherjesse/zeroscope-v2-xl",
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
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
