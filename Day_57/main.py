
from flask import Flask, render_template
from post import Post

app = Flask(__name__)

posts=Post()
all_posts=posts.posts_get()

@app.route('/')
def home():
    return render_template("index.html",posts=all_posts)

@app.route('/blog/<num>')
def get_blog(num):
    return render_template('post.html', num=int(num), posts=all_posts)

if __name__ == "__main__":
    app.run(debug=True)
