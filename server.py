"""This module is for the server code for emotion detector"""
from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector


# initialize the flask app
app = Flask('Emotion Detecotor')


@app.route('/emotionDetector')
def detect_emotion():
    text_to_analyze = request.args.get('textToAnalyze')

    response = emotion_detector(text_to_analyze)

    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    output_string = f'For the given statement, the system response is ' \
    f"'anger': {response['anger']}, 'disgust': {response['disgust']}, " \
    f"'fear': {response['fear']}, 'joy': {response['joy']} and 'sadness': " \
    f"{response['sadness']}. The dominant emotion is {response['dominant_emotion']}."

    return output_string


@app.route("/")
def render_index_page():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)
