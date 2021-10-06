from flask import Flask, render_template
from datetime import date
import random
import requests

# Jinja for python expressions
app = Flask(__name__)
CURRENT_YEAR = date.today().year


@app.route('/')
def home():
    random_number = random.randint(1, 10)
    return render_template(
        'index.html', num=random_number, year=CURRENT_YEAR
    )


@app.route('/guess/<name>')
def guess(name):
    response = requests.get(url="https://api.genderize.io?", params={"name": name})
    gender = response.json()['gender']

    response = requests.get(url="https://api.agify.io", params={"name": name})
    age = response.json()['age']

    return render_template(
        "guess.html",
        name=name,
        age=age,
        gender=gender,
        year=CURRENT_YEAR
    )


@app.route('/blog/<num>')
def blog(num):
    print(num)
    blog_url = "https://api.npoint.io/ed99320662742443cc5b"
    response = requests.get(blog_url)
    all_posts = response.json()
    return render_template("blog.html", posts=all_posts)


if __name__ == '__main__':
    app.run(debug=True)
