from flask import Flask, render_template
from newsapi.newsapi_client import NewsApiClient

app = Flask(__name__)

# Initialize the NewsAPI client
newsapi = NewsApiClient(api_key='your_api_key')

@app.route("/")
def home():
  top_headlines = newsapi.get_top_headlines(country="in", language="en")
  all_headlines = top_headlines['articles']
  return render_template("index.html", all_headlines=all_headlines)

if __name__ == "__main__":
  app.run(debug=True)
