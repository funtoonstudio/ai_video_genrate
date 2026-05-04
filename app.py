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
