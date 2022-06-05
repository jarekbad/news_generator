from flask import Flask, render_template, request, url_for
from request_news import polish_news, world_news, hacker_news, find_article_from_Hacker_News


app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/polish_news")
def go_to_page_polish_news():
    all_polish_news = polish_news()
    return render_template("polish_news.html", answers=all_polish_news)

@app.route("/world_news")
def go_to_page_world_news_input():
    return render_template("world_news.html")

@app.route("/world_news", methods=['POST'])
def get_input():
    variable = request.form['variable']
    all_world_news = world_news(variable)
    return render_template("world_news_answer.html", answers=all_world_news)

@app.route("/hacker_news")
def go_to_page_hacker_news():
    all_hacker_news = hacker_news()
    return render_template("hacker_news.html", answers=all_hacker_news)

@app.route("/hacker_news_plus")
def hacker_news_plus_input():
    return render_template("hacker_news_plus.html")

@app.route("/hacker_news_plus", methods=['POST'])
def get_input_hacker_news_plus():
    variable = int(request.form['variable'])
    variable2 = int(request.form['variable2'])
    answers = find_article_from_Hacker_News(variable, variable2)
    return render_template("hacker_news_plus_answer.html", answers=answers)


if __name__ == "__main__":
    app.run(debug=True)

