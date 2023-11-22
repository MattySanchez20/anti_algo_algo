from flask import Flask, render_template

from get_random_videos import YoutubeVideoRandomiser

yt = YoutubeVideoRandomiser(favourite_youtubers=["KitchenNightmares"], num_of_videos=1)

app = Flask(__name__)

@app.route('/')
def home():
    video_urls = yt.f_mark_z()
    return render_template('index.html', videos=video_urls)

if __name__ == '__main__':
    app.run(debug=True)
