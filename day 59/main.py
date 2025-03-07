from flask import Flask, render_template
import requests

url = "https://api.npoint.io/6aad8970e877b4a17d9e"
response = requests.get(url).json()

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html", posts=response)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/post/<int:index>")
def post(index):
    requested_post = None
    for post in response:
        if post["id"] == index:
            requested_post = post
    return render_template("post.html", post=requested_post)

if __name__ == "__main__":
    app.run(debug=True)