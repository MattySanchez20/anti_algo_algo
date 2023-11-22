from get_random_videos import YoutubeVideoRandomiser
from db_connection import move_videos_to_db

yt = YoutubeVideoRandomiser(num_of_videos=1)

videos = yt.f_mark_z()

print(videos)

print("Moving videos to back end... \n")

move_videos_to_db(videos)

print("Videos successfully moved to back end.")

