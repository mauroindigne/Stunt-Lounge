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


# search for kawasaki
@app.route('/kawasaki')
def kawasaki():
    return render_template("kawasaki.html",
    videos=mongo.db.video.find(), brands=mongo.db.brand_names.find()) 

# search for yamaha
@app.route('/yamaha')
def yamaha():
    return render_template("yamaha.html",
    videos=mongo.db.video.find(), brands=mongo.db.brand_names.find()) 

# search for honda
@app.route('/honda')
def honda():
    return render_template("honda.html",
    videos=mongo.db.video.find(), brands=mongo.db.brand_names.find()) 

# search for ktm
@app.route('/ktm')
def ktm():
    return render_template("ktm.html",
    videos=mongo.db.video.find(), brands=mongo.db.brand_names.find())


# Search for Mix of Brands
@app.route('/mix')
def mix():
    return render_template("mix.html",
    videos=mongo.db.video.find(), brands=mongo.db.brand_names.find())


@app.route('/about')
def about():
    return render_template("about.html",
    videos=mongo.db.video.find(), brands=mongo.db.brand_names.find())


# To add video
@app.route('/add_video')
def add_video():
    return render_template('addvideo.html', 
        brands=mongo.db.brand_names.find())


# to insert video onto page
@app.route('/insert_video', methods=['POST'])
def insert_video():
    videos = mongo.db.video
    videos.insert_one(request.form.to_dict())
    return redirect(url_for('home'))


# edit video info
@app.route('/edit_video/<video_id>')
def edit_video(video_id):
    the_video = mongo.db.video.find_one({"_id": ObjectId(video_id)})
    return render_template('editvideo.html', video=the_video, brands=mongo.db.brand_names.find())


# update video
@app.route('/update_video/<video_id>', methods=["POST"])
def update_video(video_id):
    videos=mongo.db.video
    videos.update({"_id": ObjectId(video_id)},
    {
        'video_title': request.form.get('video_title'),
        'video_url': request.form.get('video_url'),
        'brand': request.form.get('brand')
    })
    return redirect(url_for('home'))


# delete video
@app.route('/delete_video/<video_id>')
def delete_video(video_id):
    videos=mongo.db.video.remove({'_id': ObjectId(video_id)})
    return redirect(url_for('home'))



if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True)
