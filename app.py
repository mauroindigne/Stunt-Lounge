import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

if os.path.exists("env.py"):
    import env

app = Flask(__name__)

app.config["MONGO_URI"] = os.environ = 'SECRET_KEY'


mongo = PyMongo(app)


@app.route('/base.html')

@app.route('/home')
def get_tasks():
    return render_template("base.html", 
                           tasks=mongo.db.tasks.find())

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)