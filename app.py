from flask import Flask
from config import Configuration
from posts.blueprint import posts, poster

app = Flask(__name__)
app.config.from_object(Configuration)
app.register_blueprint(posts, url_prefix='/blog')
app.register_blueprint(poster, url_prefix='/about')
