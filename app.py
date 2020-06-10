import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'stunt_lounge'
app.config["MONGO_URI"] = os.getenv('MONGO_URI', 'mongodb+srv://Kincomoro5:Kincomoro5@cluster0-eyd41.mongodb.net/stunt_lounge?retryWrites=true&w=majority')

mongo = PyMongo(app)

#render home screen
@app.route('/')
@app.route('/home')
def home():
    return render_template("videos.html",
    videos=mongo.db.video.find(), brands=mongo.db.brand_names.find())


@app.route('/kawasaki')
def kawasaki():
    return render_template("kawasaki.html",
    videos=mongo.db.video.find()) 

# To add video
@app.route('/add_video')
def add_video():
    return render_template('addvideo.html', 
        brands=mongo.db.brand_names.find())

# edit video info
@app.route('/edit_video/<video_id>')
def edit_video(video_id):
    the_video = mongo.db.video.find_one({"_id": ObjectId(video_id)})
    return render_template('editvideo.html', video=the_video)

# delete video
@app.route('/delete_video/<video_id>')
def delete_video(video_id):
    videos=mongo.db.video.remove({'_id': ObjectId(video_id)})
    return redirect(url_for('home'))

# to insert video onto page
@app.route('/insert_video', methods=['POST'])
def insert_video():
    videos = mongo.db.video
    videos.insert_one(request.form.to_dict())
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True)
