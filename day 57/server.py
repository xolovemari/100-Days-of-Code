from flask import Flask, render_template
from datetime import datetime
import requests
app = Flask(__name__)

@app.route("/")
def home():
    CURRENT_YEAR = datetime.now().year
    YOUR_NAME = "Mariana"
    return render_template("index.html", year=CURRENT_YEAR, name=YOUR_NAME)

@app.route("/guess/<some_name>")
def guessing(some_name):
    response_age_api = requests.get(f"https://api.agify.io?name={some_name}")
    data_age = response_age_api.json()
    estimated_age = data_age["age"]

    response_gender_api = requests.get(f"https://api.genderize.io?name={some_name}")
    data_gender = response_gender_api.json()
    estimated_gender = data_gender["gender"]

    return render_template("guess.html", name=some_name.title(), age=estimated_age, gender=estimated_gender)

@app.route("/blog/<num>")
def get_blog(num):
    print(num)
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(blog_url)
    all_posts = response.json()
    return render_template("blog.html", posts=all_posts)

if __name__ == "__main__":
    app.run(debug=True)