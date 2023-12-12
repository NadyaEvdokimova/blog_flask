from flask import Flask, render_template
import requests

app = Flask(__name__)
response = requests.get('https://api.npoint.io/4a701b1f2e6bf3d34034')
all_posts = response.json()


@app.route('/')
def home():
    return render_template("index.html", posts=all_posts)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/post/<id_num>')
def get_post(id_num):
    post_num = len(all_posts)
    num = int(id_num)
    return render_template("post.html", posts=all_posts, length=post_num, num=num)


if __name__ == "__main__":
    app.run(debug=True)
