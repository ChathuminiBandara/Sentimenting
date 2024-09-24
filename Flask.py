from flask import Flask, render_template, request
from textblob import TextBlob

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/submit', methods=['POST'])
def submit():
    # Get the phrase from the form input
    phrase = request.form['phrase']

    # Create a TextBlob object and calculate sentiment
    blob = TextBlob(phrase)
    sentiment = blob.sentiment  # Contains polarity and subjectivity

    # Prepare sentiment response
    sentiment_response = f"Sentiment Analysis of '{phrase}':\n"
    sentiment_response += f"Polarity: {sentiment.polarity:.2f}\n"
    sentiment_response += f"Subjectivity: {sentiment.subjectivity:.2f}"

    # Render the template with the sentiment response
    return render_template('index.html', sentiment=sentiment_response)


if __name__ == '__main__':
    app.run(debug=True)
