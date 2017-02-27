from flask import Flask
from admin.views import admin
from website.views import site
from api.api import api
from db.models import db, create_tables

app = Flask(__name__)
app.register_blueprint(admin)
app.register_blueprint(site)
app.register_blueprint(api)


@app.route("/")
def index():
    return "Hello World!"


@app.before_request
def before_request():
    db.connect()


@app.after_request
def after_request(response):
    db.close()
    return response


if __name__ == "__main__":
    create_tables()
    app.run(debug=True)