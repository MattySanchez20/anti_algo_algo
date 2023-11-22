from pymongo import MongoClient
from typing import List
from datetime import datetime

def move_videos_to_db(videos_list: List[str]) -> None:
    
    client = MongoClient("mongodb://mongo_backend:27017/")
    
    db = client["video_database"]
    
    collection = db["video_collection"]
    
    time_stamp = datetime.now().date().strftime('%Y-%m-%d')
    
    item_to_insert = [
        {
            "time_stamp": time_stamp,
            "videos": videos_list
        }
    ]
    
    collection.insert_many(item_to_insert)