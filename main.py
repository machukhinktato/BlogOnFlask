from app import app
from app import db
from posts.blueprint import posts, poster
import view


app.register_blueprint(posts, url_prefix='/blog')
app.register_blueprint(poster, url_prefix='/about')

if __name__ == '__main__':
    app.run()

