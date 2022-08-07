from flask import Flask
from scrape_news import scrape_news

app = Flask(__name__)


@app.route("/")
def get_scrape_news():
    return scrape_news()


if __name__ == "__main__":
    app.run(debug=True)