from flask import Flask
from views import views

spath = Flask(__name__)
spath.register_blueprint(views, url_prefix="/views")

if __name__ == '__main__':
    spath.run(debug=True, port=8000)