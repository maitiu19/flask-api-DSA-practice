from sqlite3 import Connection as SQLite3Connection
from flask import Flask, request,jsonify
from datetime import datetime
from sqlalchemy import event
from sqlalchemy.engine import Engine
from flask_sqlalchemy import SQLAlchemy
import os

#define the app
basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)

#configure the app
app.config["SQLALCHEMY_DATABASE_URI"] = \
    "sqlite:///" + os.path.join(basedir,"data.sqlite")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
now = datetime.now()

#setup some basic models
class User(db.Model):
    __tblename__ = "users"
    id = db.Column(db.Integer(),primary_key=True)
    name = db.Column(db.String(64))
    email = db.Column(db.String(64))
    address = db.Column(db.String(200))
    phone = db.Column(db.String(64))
    posts = db.relationship("BlogPost")

    def __repr__(self):
        return '<User %r>' % self.name

class BlogPost(db.Model):
    __tablename__ = "blog_posts"
    id = db.Column(db.Integer(),primary_key=True)
    title = db.Column(db.String(64))
    body = db.Column(db.String(500))
    date = db.Column(db.Date)
    user_id = db.Column(db.Integer(),db.ForeignKey("user.id"),nullable=False)

    def __repr__(self):
        return '<BlogPost %r>' % self.title

#create routes
@app.route("/user", methods=['POST'])
def create_user():
    pass

@app.route("/user/ascending_id", methods=['GET'])
def get_all_users_asc():
    pass

@app.route("/user/descending_id", methods=['GET'])
def get_all_users_desc():
    pass

@app.route("/user/<user_id>", methods=['GET'])
def get_user(user_id):
    pass

@app.route("/user/<user_id>", methods=['DELETE'])
def delete_user(user_id):
    pass

@app.route("/blog_post/<user_id>", methods=['POST'])
def create_blog_post(user_id):
    pass

@app.route("/blog_post/<blog_post_id>", methods=['GET'])
def get_blog_post(blog_post_id):
    pass

@app.route("/blog_post/<user_id>", methods=['GET'])
def get_all_blog_posts(user_id):
    pass

@app.route("/blog_post/<blog_post_id>", methods=['GET'])
def delete_blog_posts(blog_post_id):
    pass

if __name__ == "__main__":
    app.run(debug=True)