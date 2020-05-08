from flask import Blueprint
from flask import render_template

posts = Blueprint('blog', __name__, template_folder='templates')

@posts.route('/')
def index():
    return render_template('posts/index.html')

@posts.route('/')
def about():
    return render_template('posts/about.html')