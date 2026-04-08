"""
Flask server for Emotion Detector application
"""

from flask import Flask, request, render_template
from emotion_detection import emotion_detector  # pylint: disable=import-error

app = Flask(__name__)


@app.route("/")
def home():
    """Render home page"""
    return render_template("index.html")


@app.route("/emotionDetector")
def emotion_detector_route():
    """Handle emotion detection request"""
    text = request.args.get('textToAnalyze')

    if not text:
        return "Invalid text! Please try again!"

    result = emotion_detector(text)

    if result is None:
        return "Error in processing"

    return str(result)


if __name__ == "__main__":
    app.run(debug=True)
