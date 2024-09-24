from flask import Flask, request, jsonify
from textblob import TextBlob

app = Flask(__name__)


@app.route('/sentiment', methods=['POST'])
def sentiment_analysis():
    data = request.json  # Expecting JSON data with a "phrase" key
    phrase = data.get('phrase')

    if phrase:
        blob = TextBlob(phrase)
        sentiment = blob.sentiment.polarity  # Returns a float from -1 (negative) to 1 (positive)
        return jsonify({'phrase': phrase, 'sentiment': sentiment})
    else:
        return jsonify({'error': 'No phrase provided'}), 400

#
# @app.route('/getById', methods=['GET'])
# def return_get_id():
#
# @app.route('/getByName', methods=['PUT'])
# def return_get_id():


if __name__ == '__main__':
    app.run(debug=True)
