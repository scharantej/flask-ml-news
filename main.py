 
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Create a list of ML-related news articles
articles = [
    {
        "title": "What is Machine Learning?",
        "url": "https://www.tensorflow.org/tutorials/machine_learning/overview",
    },
    {
        "title": "How to Build a Machine Learning Model",
        "url": "https://www.coursera.org/specializations/machine-learning",
    },
    {
        "title": "The Future of Machine Learning",
        "url": "https://www.forbes.com/sites/forbestechcouncil/2022/01/18/the-future-of-machine-learning/?sh=6606007a1e28",
    },
]

# Route for the main page of the application
@app.route("/")
def index():
    return render_template("index.html", articles=articles)

# Route for a page that displays the full text of a single article
@app.route("/article/<int:article_id>")
def article(article_id):
    article = articles[article_id]
    return render_template("article.html", article=article)

# Route for a page that displays a list of the user's saved articles
@app.route("/saved")
def saved():
    saved_articles = [article for article in articles if article in user.saved_articles]
    return render_template("saved.html", saved_articles=saved_articles)

# Route for a page that displays a list of the articles that the user has shared with other users
@app.route("/shared")
def shared():
    shared_articles = [article for article in articles if article in user.shared_articles]
    return render_template("shared.html", shared_articles=shared_articles)

if __name__ == "__main__":
    app.run()
