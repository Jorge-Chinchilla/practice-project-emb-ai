''' Executing this function initiates the application of sentiment
    analysis to be executed over the Flask channel and deployed on
    localhost:5000.
'''
from flask import Flask, render_template, request
from SentimentAnalysis.sentiment_analysis import sentiment_analyzer

app = Flask("Sentiment Analyzer")

@app.route("/sentimentAnalyzer")
def sent_analyzer():
    '''Send field data to analyzer
    '''
    text_to_analyze = request.args.get('textToAnalyze')

    response = sentiment_analyzer(text_to_analyze)

    label = response['label']
    score = response['score']

    if label is None:
        return "Invalid input."
    return f"The text is {label.split('_')[1]} with a score of {score}."

@app.route("/")
def render_index_page():
    '''Getting the homepage
    '''
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
