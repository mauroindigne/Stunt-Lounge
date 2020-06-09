import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'stunt_lounge'
app.config["MONGO_URI"] = os.getenv('MONGO_URI', 'mongodb+srv://Kincomoro5:Kincomoro5@cluster0-eyd41.mongodb.net/stunt_lounge?retryWrites=true&w=majority')

mongo = PyMongo(app)


@app.route('/')
@app.route('/home')
def home():
    return render_template("base.html")


@app.route('/add_video')
def add_video():
    return render_template('addvideo.html', 
        video=mongo.db.video.find(),
        brands=mongo.db.brand_names.find())


@app.route('/insert_video', methods=['POST'])
def insert_video():
    video = mongo.db.videos
    tasks.insert_one(request.form.to_dict())
    return redirect(url_for('get_tasks'))

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True)